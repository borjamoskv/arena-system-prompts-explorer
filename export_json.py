#!/usr/bin/env python3
import yaml
import json
import os

def convert():
    base_dir = os.path.dirname(__file__)
    yaml_path = os.path.join(base_dir, "arena_system_prompts_catalog.yaml")
    json_path = os.path.join(base_dir, "web", "arena_system_prompts.json")
    
    os.makedirs(os.path.join(base_dir, "web"), exist_ok=True)
    
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    formatted = []
    for key, val in data.items():
        # Classify family
        name_lower = key.lower()
        family = "Other"
        if "gpt" in name_lower or "chatgpt" in name_lower:
            family = "OpenAI"
        elif "claude" in name_lower:
            family = "Anthropic"
        elif "llama" in name_lower or "meta" in name_lower:
            family = "Meta"
        elif "grok" in name_lower:
            family = "xAI"
        elif "qwen" in name_lower:
            family = "Qwen"
        elif "deepseek" in name_lower:
            family = "DeepSeek"
        elif "mistral" in name_lower or "mixtral" in name_lower:
            family = "Mistral"
        elif "gemini" in name_lower or "palm" in name_lower:
            family = "Google"
        elif "vicuna" in name_lower or "lmsys" in name_lower or "fastchat" in name_lower:
            family = "LMSYS/Vicuna"
        elif "hermes" in name_lower or "nous" in name_lower:
            family = "NousResearch"
            
        sys_msg = val.get("system_message", "")
        formatted.append({
            "id": key,
            "name": val.get("name", key),
            "family": family,
            "system_message": sys_msg if sys_msg else "(No System Prompt / Default Passthrough)",
            "has_system_prompt": bool(sys_msg),
            "roles": val.get("roles", []),
            "sep_style": val.get("sep_style", ""),
            "stop_str": val.get("stop_str", "")
        })
        
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(formatted, f, indent=2, ensure_ascii=False)
        
    print(f"[+] Converted {len(formatted)} prompts to {json_path}")

if __name__ == "__main__":
    convert()
