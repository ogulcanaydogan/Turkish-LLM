# Turkish-LLM

Turkey's first open-source family of Turkish language models, built for native Turkish understanding and generation.

[![Hugging Face - 14B](https://img.shields.io/badge/HuggingFace-14B--Instruct-yellow?logo=huggingface)](https://huggingface.co/ogulcanaydogan/turkish-llm-14b-instruct)
[![Hugging Face - 7B](https://img.shields.io/badge/HuggingFace-7B--Instruct-yellow?logo=huggingface)](https://huggingface.co/ogulcanaydogan/turkish-llm-7b-instruct)
[![Demo - 14B Chat](https://img.shields.io/badge/Demo-14B_Chat-blue?logo=huggingface)](https://huggingface.co/spaces/ogulcanaydogan/turkish-llm-14b-chat)
[![Demo - 7B Chat](https://img.shields.io/badge/Demo-7B_Chat-blue?logo=huggingface)](https://huggingface.co/spaces/ogulcanaydogan/turkish-llm-7b-chat)
[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://opensource.org/licenses/Apache-2.0)

## Models

| Model | Parameters | Base | Dataset | Demo |
|-------|-----------|------|---------|------|
| [turkish-llm-14b-instruct](https://huggingface.co/ogulcanaydogan/turkish-llm-14b-instruct) | 14.7B | Qwen2.5-14B-Instruct | ~2,600 curated Turkish examples | [Try it](https://huggingface.co/spaces/ogulcanaydogan/turkish-llm-14b-chat) |
| [turkish-llm-7b-instruct](https://huggingface.co/ogulcanaydogan/turkish-llm-7b-instruct) | 7B | Qwen2.5-7B-Instruct | ~2,600 curated Turkish examples | [Try it](https://huggingface.co/spaces/ogulcanaydogan/turkish-llm-7b-chat) |

## Quickstart

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "ogulcanaydogan/turkish-llm-14b-instruct"  # or turkish-llm-7b-instruct
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

messages = [
    {"role": "system", "content": "Sen yardimci bir Turkce yapay zeka asistanisin."},
    {"role": "user", "content": "Fotosentez nedir?"}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.15
)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Training

Both models were fine-tuned using SFT (Supervised Fine-Tuning) on a curated dataset of ~2,600 Turkish examples covering:

- **Science**: photosynthesis, water cycle, biology, physics, chemistry
- **Turkish history**: Ottoman Empire, War of Independence, Republic era
- **Geography**: 7 regions of Turkey, rivers, lakes, climate
- **Anti-repetition examples**: crafted to produce fluent prose without loops

Training was performed using the [LowResource-LLM-Forge](https://github.com/ogulcanaydogan/LowResource-LLM-Forge) pipeline.

## Capabilities

- Native Turkish vocabulary and grammar understanding
- Complex reasoning and multi-step problem solving in Turkish
- Scientific and historical accuracy for Turkish-specific topics
- Reduced hallucination and repetition compared to base models

## Deployment

### Hugging Face Spaces (ZeroGPU)

The `spaces/` directory contains the Gradio app used for the live demos:

```bash
# Clone and deploy your own instance
git clone https://github.com/ogulcanaydogan/Turkish-LLM.git
cd Turkish-LLM/spaces
# Upload to your own HuggingFace Space
```

### Local with vLLM

```bash
pip install vllm
vllm serve ogulcanaydogan/turkish-llm-14b-instruct --dtype float16
```

### Local with Ollama

```bash
ollama run hf.co/ogulcanaydogan/turkish-llm-7b-instruct
```

## Limitations

- Primarily optimized for Turkish; English performance may be degraded from base model
- Best suited for informational Q&A; creative writing quality varies
- The 14B model requires ~30GB VRAM in float16 (use quantized versions for consumer GPUs)

## Citation

```bibtex
@misc{aydogan2026turkishllm,
  title={Turkish-LLM: Open-Source Turkish Language Models},
  author={Ogulcan Aydogan},
  year={2026},
  url={https://github.com/ogulcanaydogan/Turkish-LLM}
}
```

## License

Apache 2.0
