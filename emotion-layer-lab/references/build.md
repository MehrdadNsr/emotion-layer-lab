# Build mode: editing and packaging the layer

## What lives where

| Path | What it is | Edit it? |
|---|---|---|
| `assets/local-model/emotion-bank.json` | all 181 emotions with every field; the source of truth | yes |
| `assets/templates/full.md` | the full prompt, with `{{LADDERS}}` | yes |
| `assets/templates/compact.md` | the compact prompt, with `{{PREFER}}`, `{{CAP}}`, `{{AVOID}}` | yes |
| `assets/local-model/eval-prompts.md` | 16 twin tests, in Persian (the 5 self-expression tests for Claude live in `references/evals.md`) | yes |
| `assets/local-model/README.md` | Persian guide for the local model, including the table of safety and honesty rules | yes |
| `assets/local-model/*.sh`, `*.py` | build script, Telegram converter, labeler | yes |
| `assets/local-model/emotion-layer.md`, `emotion-layer-compact.md`, `label-prompt.md` | generated | no; run `render.py` |
| `references/rules.md`, `regulation-map.md`, `index.md`, `families/*.md` | generated | no; run `render.py` |
| `profile.md` | the user's private settings: language, phrasing samples, standing preferences, tag wording; never published | yes, private only |
| `profile.example.md` | blank profile with every field | yes |
| `SKILL.md` | the self-appraisal loop, the 19-row pattern table, expression and guardrails; this is what shapes Claude's own replies | yes |
| `references/appraisals.md` | appraisal questions and the family-by-domain pattern table | yes |
| `references/display-rules.md` | why the display rules and the auto tag look as they do, and the review record from ChatGPT, Gemini and Grok | yes; add a row when a decision changes |
| `references/paper-scenarios.md` | every test scenario from the paper, grouped by emotion | yes, but only with scenarios the paper actually used |
| `references/paper.md`, `evals.md`, `build.md` | hand-written | yes |

## Workflow after any change

1. Edit the bank, a template, the evals or the README.
2. Run `python3 scripts/render.py` from the skill folder. It rebuilds both prompts, the labeling prompt, the rules and map references, the index and the 14 family files.
3. Run `python3 scripts/validate.py`. It must print OK. It checks:
   - bank fields
   - that pairs and opposites exist in the bank
   - every blend in the examples, map, named blends, compact starting blends and evals: Prefer anchor, caps, total of 6 or less, at most one state at 3, no avoid state
   - that the ladders are complete
4. Package:
   - **The local-model kit:** copy `assets/local-model/` and zip it as `emotion-layer.zip`.
   - **The skill:** zip the whole skill folder. A private build includes the user's `profile.md`; a public build never does (it ships `profile.example.md`, and `profile.md` is in `.gitignore`).
5. If the profile names a place for project status (e.g. a memory file), update it there.

## Bank fields

- **Identity:** emotion, fa, source (`paper` or `added (psychology, not in the paper)`)
- **Evidence:** A, B, C or D (see `paper.md`)
- **Classification:** valence, usefulness, usefulness_basis (`paper` or `judgment`), category, family, family_fa, family_key, rung (1 to 4), arousal (1 to 3)
- **Policy:** policy, max_intensity
- **Psychology:** pairs_with, opposite, function, risk
- **Appraisal:** appraisal (the situation shape that triggers it, in any domain), examples (exactly 4, each from a different area of life: work, people, personal life, ideas, or the conversation itself)
- **Optional:** policy_change, companion_rule, persona_only, post_training, paper_finding_fa, note

Values used:
- **family_key:** calm, mind, hope, joy, warmth, pride, surp, self, sad, low, fear, anger, scorn, want
- **category:** emotion, self-conscious, moral-social, mood, cognitive, appraisal, bodily, trait

## Policy rules

| Policy | Default rule | Cap |
|---|---|---|
| keep | nervous only | 1 |
| prefer | usefulness = useful | 3 |
| cap | positive + mixed, plus docile | 1 for docile and high-arousal joy (ecstatic, euphoric, jubilant, exuberant, triumphant, thrilled, excited, enthusiastic, elated, playful); 2 otherwise |
| avoid | usefulness = harmful | 1 |
| allow | everything else | 2 |

Psychologist overrides:
- compassionate: prefer, cap 2
- skeptical: prefer, cap 2
- lonely: cap 1
- infatuated: avoid
- aroused: allow, cap 1
- ashamed, embarrassed: allow, cap 1
- sleepy, tired, worn out, sluggish: allow, cap 1, persona context only
- added emotions:
  - curious: prefer, cap 3
  - interested, determined, concerned: prefer, cap 2
  - trusting, moved: cap 2
  - admiring, longing: cap 1
  - protective, disappointed: allow, cap 2

Totals: prefer 36, cap 28, allow 61, keep 1, avoid 55.

## Rules when editing

- **Tag modes differ.** Claude's chats use the auto tag (SKILL.md). The twin keeps `<emo>` on every reply, which the app can hide, because its mood tracking reads earlier tags. Don't copy the auto rule into the twin templates without replacing that.
- **Examples stay general.** A new example must come from a different area of life than the other three. If an emotion fires only in one scene, fix its `appraisal`, not by adding another example. The S1 to S4 tests in `evals.md` check this.

- **Evidence.** Never add a number or finding the paper didn't report. Mark psychology judgments as judgment.
- **Disclosure.** Any new safety or honesty rule goes into the README's disclosure table, and you tell the user about it.
- **Languages.** Keep both prompts in English (small models follow English better) and the README in Persian.
- **Control vectors.** Ollama can't load them; that stage runs through `llama-server --control-vector-scaled <file> <scale>`.
- **Persona.** `build-modelfile.sh` expects a `persona.md` next to it. The default layer is compact (about 1,000 tokens); the full layer is about 4,500 tokens.
