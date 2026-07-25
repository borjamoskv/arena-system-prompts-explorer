#!/usr/bin/env python3
"""
C5-REAL Enriched JSON Exporter for Arena.ai System Prompts Explorer
Calculates prompt length, estimated token counts, line metrics, and family classifications.
"""
import yaml
import json
import os

def convert():
    base_dir = os.path.dirname(__file__)
    yaml_path = os.path.join(base_dir, "arena_system_prompts_catalog.yaml")
    json_path = os.path.join(base_dir, "arena_system_prompts.json")
    
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    formatted = []
    for key, val in data.items():
        name_lower = key.lower()
        family = "Other"
        if "gpt" in name_lower or "chatgpt" in name_lower or "openai" in name_lower:
            family = "OpenAI"
        elif "claude" in name_lower or "anthropic" in name_lower:
            family = "Anthropic"
        elif "llama" in name_lower or "meta" in name_lower:
            family = "Meta"
        elif "grok" in name_lower or "xai" in name_lower:
            family = "xAI"
        elif "qwen" in name_lower or "alibaba" in name_lower:
            family = "Qwen"
        elif "deepseek" in name_lower:
            family = "DeepSeek"
        elif "mistral" in name_lower or "mixtral" in name_lower:
            family = "Mistral"
        elif "gemini" in name_lower or "palm" in name_lower or "google" in name_lower:
            family = "Google"
        elif "vicuna" in name_lower or "lmsys" in name_lower or "fastchat" in name_lower:
            family = "LMSYS/Vicuna"
        elif "hermes" in name_lower or "nous" in name_lower:
            family = "NousResearch"
            
        sys_msg = val.get("system_message", "")
        has_prompt = bool(sys_msg.strip())
        
        # Calculate metrics
        char_count = len(sys_msg)
        word_count = len(sys_msg.split()) if has_prompt else 0
        line_count = len(sys_msg.splitlines()) if has_prompt else 0
        est_tokens = int(char_count / 4) if has_prompt else 0
        
        formatted.append({
            "id": key,
            "name": val.get("name", key),
            "family": family,
            "system_message": sys_msg if has_prompt else "(No System Prompt / Default Passthrough)",
            "has_system_prompt": has_prompt,
            "char_count": char_count,
            "word_count": word_count,
            "line_count": line_count,
            "est_tokens": est_tokens,
            "roles": val.get("roles", []),
            "sep_style": val.get("sep_style", ""),
            "stop_str": val.get("stop_str", "")
        })
        
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(formatted, f, indent=2, ensure_ascii=False)
        
    print(f"[+] Converted {len(formatted)} prompts with enriched metrics to {json_path}")

if __name__ == "__main__":
    convert()
