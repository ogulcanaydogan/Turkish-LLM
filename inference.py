"""
Turkish-LLM inference example.
Usage: python inference.py --model 14b --prompt "Turkiye'nin baskenti neresidir?"
"""

import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODELS = {
    "7b": "ogulcanaydogan/Turkish-LLM-7B-Instruct",
    "14b": "ogulcanaydogan/Turkish-LLM-14B-Instruct",
}

SYSTEM_PROMPT = "Sen yardimci bir Turkce yapay zeka asistanisin."


def generate(model_size: str, prompt: str, max_tokens: int = 512) -> str:
    model_id = MODELS[model_size]
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.15,
        do_sample=True,
    )
    return tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1] :], skip_special_tokens=True
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Turkish-LLM Inference")
    parser.add_argument(
        "--model", choices=["7b", "14b"], default="14b", help="Model size"
    )
    parser.add_argument("--prompt", required=True, help="Input prompt in Turkish")
    parser.add_argument(
        "--max-tokens", type=int, default=512, help="Maximum tokens to generate"
    )
    args = parser.parse_args()

    response = generate(args.model, args.prompt, args.max_tokens)
    print(response)
