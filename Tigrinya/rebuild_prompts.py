"""Rebuild the verbatim prompts of prompts.jsonl from public
sources. Requires: datasets, huggingface_hub.

  python rebuild_prompts.py prompts.jsonl > rebuilt.jsonl

Replaces [seed:xquad/{lang}:{i}] with the i-th deduplicated validation
context of google/xquad (config xquad.{lang}), and
[seed:flores_plus/dev/tir_Ethi:{n}] with the n-th line's text of the
FLORES+ dev tir_Ethi file (openlanguagedata/flores_plus).
"""
import json
import re
import sys

from datasets import load_dataset
from huggingface_hub import hf_hub_download

xquad = {}
for lang in ("en", "de", "es", "ar", "ru", "hi"):
    ds = load_dataset("google/xquad", f"xquad.{lang}", split="validation")
    xquad[lang] = list(dict.fromkeys(r["context"] for r in ds))
fl = hf_hub_download("openlanguagedata/flores_plus", "dev/tir_Ethi.jsonl",
                     repo_type="dataset")
flores = [json.loads(l)["text"] for l in open(fl, encoding="utf-8")]

ref = re.compile(r"\[seed:(xquad/(\w+)|flores_plus/dev/tir_Ethi):(\d+)\]")

def fill(m):
    if m.group(1).startswith("xquad"):
        return xquad[m.group(2)][int(m.group(3))]
    return flores[int(m.group(3))]

for line in open(sys.argv[1], encoding="utf-8"):
    r = json.loads(line)
    r["prompt"] = ref.sub(fill, r["prompt"])
    print(json.dumps(r, ensure_ascii=False))
