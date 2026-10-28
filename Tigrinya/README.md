# Tigrinya synthetic corpus

Tigrinya text written by GPT-6.1-Sol with TopXGen prompts: one topic
per document, with example paragraphs in other languages and real
Tigrinya sentences as in-context seeds.

## Files

| file | documents | words | size |
|---|---|---|---|
| `tir_gpt61sol_100k.txt` | 508 | 100,000 | 1.3 MB |
| `tir_gpt61sol_1m.txt` | 5,409 | 1,000,000 | 12.5 MB |
| `documents.jsonl` | 54,589 | 10,017,482 | 138.3 MB |
| `prompts.jsonl` | 55,000 prompts | 46,102,966 original prompt words | 117.1 MB |

The two smaller text files contain the first 100,000 and 1,000,000
whitespace-separated words of the full corpus, in the same order;
their document counts include a partial final document. Sizes are
decimal MB.

Prompt words are whitespace-separated words summed over all 55,000
original prompts before replacing seed text with references, counting
repeated instructions and in-context examples each time.

Each line of `documents.jsonl`: `id`, `language`, `condition`,
`topic`, `style`, `persona`, `text`, `word_count`, `model`.
Each line of `prompts.jsonl`: `id`, `language`, `condition`, `topic`,
`style`, `persona`, `prompt`, `prompt_word_count`. Documents and
prompts are joined on `id`. In this corpus `language` is always
`tir`; `style` and `persona` are populated where applicable and
otherwise `null`. `prompt_word_count` is the word count of the full
verbatim prompt. All 55,000 prompts are retained, including 411
without accepted documents.

`condition`

- `broad_topic` — Generate text on a broad topic (503 topics)
- `topxgen` — Generate text on a fine-grained Wikipedia topic (66,361 topics)
- `topic_style` — `topxgen` + writing style
- `topic_style_persona` — `topxgen` + writing style and target audience (`persona`)

`style`: Textbook section, personal blog, how-to guide, news report,
short story, interview/conversation

`persona`: Young children, high-school students, university-educated
experts, elderly readers, casual social-media readers, rural farmers
and fishers

## Getting the verbatim prompts

In `prompts.jsonl`, the in-context seed text inside each prompt is
replaced by references, so that no evaluation data is republished
here:

- `[seed:flores_plus/dev/tir_Ethi:{n}]` — the `text` of line n
  (0-based) of `dev/tir_Ethi.jsonl` in FLORES+
  (`openlanguagedata/flores_plus` on Hugging Face, CC-BY-SA 4.0,
  Open Language Data Initiative).
- `[seed:xquad/{lang}:{i}]` — context paragraph i of the `validation`
  split of `google/xquad`, config `xquad.{lang}`, in first-seen order
  with duplicates removed (CC-BY-SA 4.0).

To restore the exact prompts (needs `datasets` and `huggingface_hub`;
FLORES+ requires accepting its [access conditions on Hugging Face](https://huggingface.co/datasets/openlanguagedata/flores_plus)
and having authenticated access configured):

```bash
pip install datasets huggingface_hub
python rebuild_prompts.py prompts.jsonl > prompts_verbatim.jsonl
```

Topic titles come from the TopXGen topic lists
([github.com/ArmelRandy/topxgen](https://github.com/ArmelRandy/topxgen)).
