# ARENA.AI System Prompts Explorer (C5-REAL)

[![Ledger Status](https://img.shields.io/badge/CORTEX-C5--REAL-2B3BE5)](https://github.com/borjamoskv/arena-system-prompts-explorer)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An interactive, high-exergy explorer and catalog of all **102 System Prompts and Conversation Templates** extracted from the **LMSYS FastChat Engine** behind [Arena.ai](https://arena.ai).

Designed with **Industrial Noir 2026** aesthetics (`#0A0A0A` / `#2B3BE5` / Humanist Sans & Monospace).

---

## ⚡ Key Features

- 🔍 **Real-Time Search & Filtering**: Instant search across 102 LLM System Prompts.
- 🏷️ **Provider Classification**: Filter by model family (OpenAI, Anthropic, Meta, DeepSeek, Qwen, xAI, LMSYS/Vicuna, NousResearch).
- 📋 **One-Click Copy**: Copy exact prompt definitions directly to your clipboard.
- ⚙️ **Automated Extractor**: Python pipeline (`extract_arena_templates.py`) for live extraction from official FastChat repositories.
- 🌐 **Zero Dependencies**: Pure HTML/CSS/JS single-page dashboard with glassmorphism UI.

---

## 🛠️ Quick Start

### 1. Launch Web Dashboard Locally

```bash
# Clone the repository
git clone https://github.com/borjamoskv/arena-system-prompts-explorer.git
cd arena-system-prompts-explorer

# Start local HTTP server
python3 -m http.server 8765
```

Open [http://localhost:8765](http://localhost:8765) in your browser.

### 2. Update Catalog from Upstream FastChat

```bash
# Re-extract System Prompts from FastChat GitHub repo
python3 extract_arena_templates.py

# Convert YAML to JSON for web interface
python3 export_json.py
```

---

## 📊 Catalog Overview

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
