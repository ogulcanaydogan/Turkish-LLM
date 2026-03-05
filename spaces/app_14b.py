import gradio as gr
import spaces
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re

model = None
tokenizer = None

SYSTEM_PROMPT = "Sen Turkce konusan bir yapay zeka asistanisin. Her zaman Turkce yanit ver. Baska bir dilde yanit verme."

def load_model():
    global model, tokenizer
    if model is None:
        model_id = "ogulcanaydogan/Turkish-LLM-14B-Instruct"
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            device_map="auto"
        )
    return model, tokenizer

def clean_response(text):
    # Cut off at first Chinese/Japanese/Korean character
    cjk_match = re.search(r'[\u4e00-\u9fff\u3400-\u4dbf\u3040-\u309f\u30a0-\u30ff]', text)
    if cjk_match:
        text = text[:cjk_match.start()]
    # Remove trailing incomplete sentences
    text = text.rstrip()
    if text and text[-1] not in '.!?:;)]\'"':
        last_sentence = max(text.rfind('.'), text.rfind('!'), text.rfind('?'), text.rfind('\n'))
        if last_sentence > len(text) // 2:
            text = text[:last_sentence + 1]
    return text.strip()

@spaces.GPU(duration=120)
def chat(message, history):
    model, tokenizer = load_model()
    prompt = f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
    if history:
        for user_msg, assistant_msg in history:
            prompt += f"<|im_start|>user\n{user_msg}<|im_end|>\n"
            prompt += f"<|im_start|>assistant\n{assistant_msg}<|im_end|>\n"
    prompt += f"<|im_start|>user\n{message}<|im_end|>\n<|im_start|>assistant\n"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=512,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=False)

    if "<|im_end|>" in response:
        response = response.split("<|im_end|>")[0]
    if "\nuser" in response.lower():
        response = response.split("\nuser")[0]

    response = clean_response(response)
    return response.strip()

demo = gr.ChatInterface(
    fn=chat,
    title="Turkish-LLM-14B-Instruct",
    description="Turkce 14 milyar parametreli dil modeli ile sohbet edin. (ZeroGPU)",
    examples=[
        "Turkiye'nin baskenti neresidir?",
        "Yapay zeka nedir kisaca aciklar misin?",
        "Bana kisa bir hikaye yaz.",
        "Python ile fibonacci dizisi nasil yazilir?"
    ],
    cache_examples=False
)

if __name__ == "__main__":
    demo.launch(ssr_mode=False)
