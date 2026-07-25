#!/usr/bin/env python3
"""
C5-REAL System Prompt & Conversation Template Extractor for Arena.ai (FastChat Engine)
Loads fastchat_conversation_raw.py dynamically and extracts all registered System Prompts.
"""
import sys
import os
import json
import yaml
import importlib.util

def extract_templates():
    raw_path = os.path.join(os.path.dirname(__file__), "fastchat_conversation_raw.py")
    spec = importlib.util.spec_from_file_location("fastchat_conv_module", raw_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["fastchat_conv_module"] = module
    spec.loader.exec_module(module)
    
    conv_templates = getattr(module, "conv_templates", {})
    
    extracted = {}
    for name, conv in conv_templates.items():
        extracted[name] = {
            "name": conv.name,
            "system_template": getattr(conv, "system_template", "{system_message}"),
            "system_message": getattr(conv, "system_message", ""),
            "roles": list(getattr(conv, "roles", ())),
            "sep_style": str(getattr(conv, "sep_style", "")),
            "sep": getattr(conv, "sep", ""),
            "sep2": getattr(conv, "sep2", None),
            "stop_str": getattr(conv, "stop_str", None)
        }
    
    out_yaml = os.path.join(os.path.dirname(__file__), "arena_system_prompts_catalog.yaml")
    with open(out_yaml, "w", encoding="utf-8") as f:
        yaml.dump(extracted, f, default_flow_style=False, allow_unicode=True)
    
    print(f"[+] Successfully extracted {len(extracted)} model templates to {out_yaml}")
    return extracted

if __name__ == "__main__":
    extract_templates()
