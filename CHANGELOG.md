# Changelog

## 0.1.0 (2026-10-13), experimental

First public release.
- A Claude skill that appraises each moment and lets a blend of up to 3 functional emotions shape the reply. It has 19 cross-domain patterns, display rules, and an automatic one-line tag at turning points.
- An emotion bank of 181 emotions: 171 from Anthropic's paper and 10 from psychology. Each emotion has an evidence level, a policy and a cap, an appraisal, and examples from four areas of life.
- Anti-sycophancy policies and honesty guardrails. The skill was reviewed twice by ChatGPT, Gemini and Grok; the design record is in `references/display-rules.md`.
- A local-model kit for Ollama: compact and full prompts, an explicit appraisal step, a build script, 16 evals, and local chat-labeling scripts. Its control-vector stage is experimental.
- 6 self-expression evals, including a comparison against no layer. No results have been measured yet.
