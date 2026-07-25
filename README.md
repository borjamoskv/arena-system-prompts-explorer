# ARENA.AI System Prompts Explorer (C5-REAL)

[![Ledger Status](https://img.shields.io/badge/CORTEX-C5--REAL-2B3BE5)](https://github.com/borjamoskv/arena-system-prompts-explorer)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An interactive, high-exergy explorer and catalog of all **102 System Prompts and Conversation Templates** extracted from the **LMSYS FastChat / SGLang Engine** behind [Arena.ai](https://arena.ai).

Designed with **Industrial Noir 2026** aesthetics (`#0A0A0A` / `#2B3BE5` / Humanist Sans & Monospace).

---

## ⚡ Key Findings from Arena.ai Infrastructure

1. **Zero User System Prompt Override**: In standard Battle Mode and Leaderboard runs on [Arena.ai](https://arena.ai), custom user system prompts are disabled to prevent bias in human preference voting.
2. **Vendor-Native Deployment Prompts**: Models run on their official provider-defined system instructions or standard FastChat / SGLang formatting templates.
3. **Arena Max Auto-Router**: Uses dual routing backends:
   - **`theta-hat`**: Performance-optimized quality routing.
   - **`arcstride`**: Latency-aware speed routing (Pareto frontier).
4. **Arena-Hard Parity**: Prompt formatting standardization prevents open-weight models from being penalized against commercial models with default system instructions.

---

## 🛠️ Quick Start & Local Server

### 1. Launch Web Dashboard Locally

```bash
# Clone repository
git clone https://github.com/borjamoskv/arena-system-prompts-explorer.git
cd arena-system-prompts-explorer

# Start local server
python3 -m http.server 8765
```

Open [http://localhost:8765](http://localhost:8765) in your browser.

### 2. Update Catalog from Upstream FastChat

```bash
# Extract templates from GitHub repository
python3 extract_arena_templates.py

# Convert YAML catalog to JSON
python3 export_json.py
```

---

## 📊 Catalog Overview (102 Model Templates)

| Model Family | System Prompt Type | Example / Default |
| :--- | :--- | :--- |
| **OpenAI** (`gpt-4`, `chatgpt`) | Vendor Prompt | `"You are ChatGPT, a large language model trained by OpenAI..."` |
| **Anthropic** (`claude-3`) | Vendor Prompt | `"The assistant is Claude, created by Anthropic..."` |
| **Meta** (`llama-3`) | ChatML / Native | `<|begin_of_text|><|start_header_id|>system<|end_header_id|>` |
| **DeepSeek** (`deepseek-coder`) | Vendor Prompt | `"You are an AI programming assistant, utilizing the DeepSeek Coder..."` |
| **Qwen** (`qwen2.5`) | Bilingual Prompt | `"You are a helpful assistant. 你是一个乐于助人的助手..."` |
| **xAI** (`grok-2`) | Vendor Prompt | `"You are Grok-2, a smart and helpful AI assistant created by xAI."` |
| **LMSYS** (`vicuna_v1.1`) | FastChat Default | `"A chat between a curious user and an artificial intelligence assistant..."` |

---

## 📜 License

MIT © [borjamoskv](https://github.com/borjamoskv)
