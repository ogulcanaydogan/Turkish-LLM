<p align="center">
  <h1 align="center">Turkish-LLM</h1>
  <p align="center">
    An open-source family of large language models purpose-built for the Turkish language
    <br />
    <a href="https://huggingface.co/spaces/ogulcanaydogan/Turkish-LLM-14B-Chat"><strong>Try the 14B Demo</strong></a>
    &middot;
    <a href="https://huggingface.co/spaces/ogulcanaydogan/Turkish-LLM-7B-Chat"><strong>Try the 7B Demo</strong></a>
    &middot;
    <a href="https://huggingface.co/datasets/ogulcanaydogan/Turkish-LLM-v10-Training"><strong>Training Dataset</strong></a>
  </p>
</p>

<p align="center">
  <a href="https://huggingface.co/ogulcanaydogan/Turkish-LLM-14B-Instruct"><img src="https://img.shields.io/badge/HuggingFace-14B_Instruct-yellow?style=for-the-badge&logo=huggingface" alt="14B Model"></a>
  <a href="https://huggingface.co/ogulcanaydogan/Turkish-LLM-7B-Instruct"><img src="https://img.shields.io/badge/HuggingFace-7B_Instruct-yellow?style=for-the-badge&logo=huggingface" alt="7B Model"></a>
  <a href="https://huggingface.co/ogulcanaydogan/Turkish-LLM-14B-Instruct-GGUF"><img src="https://img.shields.io/badge/GGUF-Quantized-orange?style=for-the-badge&logo=huggingface" alt="GGUF"></a>
  <a href="https://huggingface.co/datasets/ogulcanaydogan/Turkish-LLM-v10-Training"><img src="https://img.shields.io/badge/Dataset-144K_samples-blue?style=for-the-badge&logo=huggingface" alt="Dataset"></a>
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache_2.0-green?style=for-the-badge" alt="License"></a>
</p>

---

## Overview

Turkish is spoken by over 80 million native speakers, yet remains significantly underrepresented in the LLM landscape. Most existing multilingual models treat Turkish as a secondary language, resulting in poor grammar, hallucinated content, and lack of cultural context.

**Turkish-LLM** addresses this gap by providing a family of open-source language models specifically fine-tuned for native Turkish understanding and generation. The project includes the full training pipeline, curated datasets, and ready-to-deploy inference applications.

### Key Contributions

- **First open-source Turkish LLM family** spanning 7B and 14B parameters
- **144,000 curated Turkish instruction-response pairs** released as an open dataset
- **End-to-end training pipeline** for low-resource language model development
- **Live interactive demos** running on Hugging Face Spaces with ZeroGPU
- **GGUF quantized models** for local deployment via llama.cpp, Ollama, and LM Studio

## Model Family

| Model | Parameters | Base Architecture | Training Method | Hardware | Demo |
|-------|-----------|-------------------|-----------------|----------|------|
| [turkish-llm-14b-instruct](https://huggingface.co/ogulcanaydogan/Turkish-LLM-14B-Instruct) | 14.7B | Qwen2.5-14B-Instruct | SFT | A100 80GB | [Chat](https://huggingface.co/spaces/ogulcanaydogan/Turkish-LLM-14B-Chat) |
| [turkish-llm-7b-instruct](https://huggingface.co/ogulcanaydogan/Turkish-LLM-7B-Instruct) | 7B | Turkcell-LLM-7b-v1 | LoRA (r=64, α=128) | A100 80GB | [Chat](https://huggingface.co/spaces/ogulcanaydogan/Turkish-LLM-7B-Chat) |

## GGUF Quantizations

Pre-quantized GGUF models are available for local inference with llama.cpp, Ollama, and LM Studio.

| File | Quant | Size | RAM Needed | Best For |
|------|-------|------|------------|----------|
| [Turkish-LLM-14B-Instruct-F16.gguf](https://huggingface.co/ogulcanaydogan/Turkish-LLM-14B-Instruct-GGUF/blob/main/Turkish-LLM-14B-Instruct-F16.gguf) | F16 | 28 GB | 32-35 GB | Full precision, A100/H100 |
| [Turkish-LLM-14B-Instruct-Q8_0.gguf](https://huggingface.co/ogulcanaydogan/Turkish-LLM-14B-Instruct-GGUF/blob/main/Turkish-LLM-14B-Instruct-Q8_0.gguf) | Q8_0 | 15 GB | 18-20 GB | RTX 3090/4090 |
| [Turkish-LLM-14B-Instruct-Q5_K_M.gguf](https://huggingface.co/ogulcanaydogan/Turkish-LLM-14B-Instruct-GGUF/blob/main/Turkish-LLM-14B-Instruct-Q5_K_M.gguf) | Q5_K_M | 9.8 GB | 13-14 GB | M2/M3 Mac |
| [Turkish-LLM-14B-Instruct-Q4_K_M.gguf](https://huggingface.co/ogulcanaydogan/Turkish-LLM-14B-Instruct-GGUF/blob/main/Turkish-LLM-14B-Instruct-Q4_K_M.gguf) | Q4_K_M | 8.4 GB | 11-12 GB | M1/M2 Mac, 16GB laptop |

> **Recommendation:** Q4_K_M offers the best size-to-quality ratio for most consumer hardware.

Full details: [Turkish-LLM-14B-Instruct-GGUF](https://huggingface.co/ogulcanaydogan/Turkish-LLM-14B-Instruct-GGUF)

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Turkish-LLM Pipeline                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐    ┌──────────────┐    ┌───────────┐  │
│  │  Data Coll.  │───▶│  Training    │───▶│  Serving  │  │
│  │              │    │              │    │           │  │
│  │ 144K Turkish │    │ SFT / LoRA   │    │ Gradio    │  │
│  │ pairs from   │    │ on A100 80GB │    │ on Zero-  │  │
│  │ curated      │    │              │    │ GPU       │  │
│  │ sources      │    │ bf16 mixed   │    │           │  │
│  │              │    │ precision    │    │ vLLM /    │  │
│  │              │    │              │    │ Ollama    │  │
│  └──────────────┘    └──────────────┘    └───────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Training Methodology

### Dataset

The training data consists of **144,000 Turkish instruction-response pairs** covering diverse domains:

| Domain | Description | Purpose |
|--------|-------------|---------|
| Science | Photosynthesis, water cycle, biology, physics, chemistry | Factual accuracy in Turkish scientific discourse |
| History | Ottoman Empire, War of Independence, Republic era | Culturally grounded historical knowledge |
| Geography | 7 regions of Turkey, rivers, lakes, climate systems | Location-aware Turkish responses |
| General Knowledge | Education, culture, daily life | Broad conversational ability |
| Anti-Repetition | Specially crafted examples | Fluent prose generation without loops |

The full dataset is publicly available: [`ogulcanaydogan/Turkish-LLM-v10-Training`](https://huggingface.co/datasets/ogulcanaydogan/Turkish-LLM-v10-Training)

### Training Configuration

<table>
<tr><td>

**14B Model (SFT)**
| Parameter | Value |
|-----------|-------|
| Base model | Qwen2.5-14B-Instruct |
| Method | Full SFT alignment |
| Precision | bfloat16 |
| Hardware | NVIDIA A100 80GB |

</td><td>

**7B Model (LoRA)**
| Parameter | Value |
|-----------|-------|
| Base model | Turkcell-LLM-7b-v1 |
| Method | LoRA (r=64, α=128) |
| Learning rate | 5e-6 |
| Batch size | 16 |
| Seq length | 2,048 |
| Training time | ~10 hours |
| Final loss | 1.88 |
| Precision | bfloat16 |
| Hardware | NVIDIA A100 80GB |

</td></tr>
</table>

Training was orchestrated using the [LowResource-LLM-Forge](https://github.com/ogulcanaydogan/LowResource-LLM-Forge) pipeline, a custom framework designed for efficient fine-tuning of LLMs for low-resource languages.

## Quickstart

### Python (Transformers)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "ogulcanaydogan/Turkish-LLM-14B-Instruct"
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

### Ollama (Local)

```bash
# Direct from HuggingFace (no setup needed)
ollama run hf.co/ogulcanaydogan/Turkish-LLM-14B-Instruct-GGUF:Q4_K_M

# Or with a local GGUF file
ollama create turkish-llm-14b -f Modelfile
ollama run turkish-llm-14b "Turkiye'nin baskenti neresidir?"
```

<details>
<summary>Example Modelfile</summary>

```
FROM Turkish-LLM-14B-Instruct-Q4_K_M.gguf
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER repeat_penalty 1.1
SYSTEM "Sen yardimci bir Turkce yapay zeka asistanisin."
TEMPLATE "<|im_start|>system
{{.System}}<|im_end|>
<|im_start|>user
{{.Prompt}}<|im_end|>
<|im_start|>assistant
"
```

</details>

### llama.cpp

```bash
# Download
huggingface-cli download ogulcanaydogan/Turkish-LLM-14B-Instruct-GGUF Turkish-LLM-14B-Instruct-Q4_K_M.gguf

# Run inference
./llama-cli -m Turkish-LLM-14B-Instruct-Q4_K_M.gguf \
  -p "<|im_start|>system\nSen yardimci bir Turkce yapay zeka asistanisin.<|im_end|>\n<|im_start|>user\nTurkiye'nin baskenti neresidir?<|im_end|>\n<|im_start|>assistant\n" \
  -n 256 --temp 0.7
```

### vLLM (Production Serving)

```bash
pip install vllm
vllm serve ogulcanaydogan/Turkish-LLM-14B-Instruct \
    --dtype float16 \
    --max-model-len 4096
```

### LM Studio

Download any GGUF file from [Turkish-LLM-14B-Instruct-GGUF](https://huggingface.co/ogulcanaydogan/Turkish-LLM-14B-Instruct-GGUF) and load it directly in [LM Studio](https://lmstudio.ai/).

### CLI Inference

```bash
python inference.py --model 14b --prompt "Yapay zeka nedir?"
```

## Hardware Requirements

| Model | FP16 VRAM | GGUF Q4_K_M | Recommended GPU |
|-------|-----------|-------------|-----------------|
| 14B | ~30 GB | ~8.4 GB | A100 / RTX 4090 (FP16) or any 16GB+ (GGUF) |
| 7B | ~14 GB | ~4 GB | RTX 3090 / RTX 4080 / Apple M-series |

## Project Structure

```
Turkish-LLM/
├── README.md
├── inference.py          # CLI inference script (7B & 14B)
└── spaces/
    ├── app_14b.py        # Gradio chatbot app for 14B
    └── requirements.txt
```

## Related Projects

| Project | Description |
|---------|-------------|
| [LowResource-LLM-Forge](https://github.com/ogulcanaydogan/LowResource-LLM-Forge) | Fine-tuning pipeline for low-resource language models |
| [Turkish-LLM-14B-Instruct-GGUF](https://huggingface.co/ogulcanaydogan/Turkish-LLM-14B-Instruct-GGUF) | GGUF quantized models for local deployment |
| [CCTV Customer Analytics](https://huggingface.co/spaces/ogulcanaydogan/cctv-customer-analytics) | Computer vision for object detection and tracking |

## Limitations

- Primarily optimized for Turkish; English capabilities may be reduced compared to base models
- Best suited for informational Q&A; creative writing quality varies
- The 14B model requires ~30GB VRAM in FP16 (use quantized versions for consumer GPUs)
- Not recommended for production use without additional safety alignment and evaluation

## Citation

If you use Turkish-LLM in your research, please cite:

```bibtex
@misc{aydogan2026turkishllm,
  title     = {Turkish-LLM: Open-Source Turkish Language Models},
  author    = {Aydogan, Ogulcan},
  year      = {2026},
  publisher = {GitHub / Hugging Face},
  url       = {https://github.com/ogulcanaydogan/Turkish-LLM}
}
```

## License

This project is licensed under the [Apache License 2.0](LICENSE).

---

<p align="center">
  Built by <a href="https://ogulcanaydogan.com">Ogulcan Aydogan</a>
  &middot;
  <a href="https://github.com/ogulcanaydogan">GitHub</a>
  &middot;
  <a href="https://huggingface.co/ogulcanaydogan">Hugging Face</a>
  &middot;
  <a href="https://linkedin.com/in/ogulcanaydogan">LinkedIn</a>
</p>
