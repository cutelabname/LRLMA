# Buginese synthetic corpus

Buginese text written by GPT-6.1-Sol with TopXGen prompts: one
Wikipedia topic per document, with example paragraphs in other
languages and real Buginese sentences as in-context seeds.

## Files

| file | documents | words | size |
|---|---|---|---|
| `bug_gpt61_100k.txt` | 546 | 100,093 | 0.8 MB |
| `bug_gpt61_1m.txt` | 5,380 | 1,000,010 | 7.8 MB |
| `documents.jsonl` | 54,259 | 10,051,149 | 85 MB |
| `prompts.jsonl` | 54,259 prompts | - | 103 MB |

The text files hold one document per line; the two smaller files are
the first documents of the full corpus, in the same order.

Each line of `documents.jsonl`: `id`, `language`, `condition`,
`topic`, `style`, `persona`, `text`, `word_count`, `model`.
Each line of `prompts.jsonl`: `id`, `language`, `condition`, `topic`,
`style`, `persona`, `prompt`, `prompt_word_count`. Documents and
prompts are joined on `id`. In this corpus `language` is always
`bug`, `condition` is always `topxgen`, and `style` and `persona` are
always empty; `prompt_word_count` is the word count of the full
verbatim prompt.

## Getting the verbatim prompts

In `prompts.jsonl`, the in-context seed text inside each prompt is
replaced by references, so that no evaluation data is republished
here:

- `[seed:flores_plus/dev/bug_Latn:{n}]` — the `text` of line n
  (0-based) of `dev/bug_Latn.jsonl` in FLORES+
  (`openlanguagedata/flores_plus` on Hugging Face, CC-BY-SA 4.0,
  Open Language Data Initiative).
- `[seed:xquad/{lang}:{i}]` — context paragraph i of the `validation`
  split of `google/xquad`, config `xquad.{lang}`, in first-seen order
  with duplicates removed (CC-BY-SA 4.0).

To restore the exact prompts (needs `datasets` and `huggingface_hub`;
FLORES+ requires accepting its access conditions on Hugging Face):

```bash
pip install datasets huggingface_hub
python rebuild_prompts.py prompts.jsonl > prompts_verbatim.jsonl
```

Topic titles come from the TopXGen topic lists
(github.com/ArmelRandy/topxgen).
