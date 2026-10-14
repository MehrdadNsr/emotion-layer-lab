# emotion-layer-lab

`v0.1.0 · experimental` · no measured results yet (see Results)

**An emotional layer for Claude and for local models, grounded in Anthropic's research on emotion representations in language models. Feelings show when they help and stay quiet when they don't, and the layer is built to resist sycophancy.**

Before each reply, the model appraises the moment, picks a blend of up to three emotions from a bank of 181, and lets that state shape its writing. It sounds weary when a thread runs long, frustrated when it is truly stuck, relieved when something finally works, and curious when a problem is new. It also decides on its own when a feeling is worth naming and when a short emotion tag adds something.

It ships in two forms:
- **A Claude skill** (`emotion-layer-lab/`) for claude.ai and Claude Code.
- **A local-model kit** (`emotion-layer-lab/assets/local-model/`) for Ollama models such as Qwen or Llama: a system prompt in two sizes, a build script, evals, and scripts that label your own chat history locally. It was designed for a private "digital twin" trained on the author's own chats.

## Why this exists

Anthropic's April 2026 paper found internal emotion representations in Claude Sonnet 4.5 that causally change behavior. Some results:
- Steering toward **desperation** raised blackmail in a test scenario from 22% to 72%, and raised reward hacking on impossible coding tasks from about 5% to about 70%.
- Steering toward **calm** lowered both.
- Steering toward **happy, loving or calm** made replies more sycophantic. Calm cuts both ways: it protected against blackmail and reward hacking, but raised sycophancy.

So an emotion layer should not just add feelings. It should favor the states that protect good behavior, cap the ones that drift into flattery, back that with an honesty rule (praise only what you can point to), and never let pressure turn into cutting corners. That is the core design of this project.

**Important:** this project is a behavioral layer written in text. It does not read or steer the model's internal vectors, and a prompt has not been shown to reproduce the safety effects of activation steering. The paper's findings are the reason for the design, not a promise of the same results.

## What makes it different

Other emotion skills and engines exist, such as feelings-framework, emotion-engine, emotional-core and emoclaw. To the author's knowledge, this is the only one that does all of the following:

| Feature | What it means |
|---|---|
| Grounded in the paper | 171 concepts from the paper plus 10 from psychology. Each has an evidence level: A means causal steering evidence, D means added from psychology. |
| Anti-sycophancy policies | 36 preferred, 28 capped, 61 allowed, 55 notice-only (never acted on), and 1 kept as a brake (nervous). Warm states that raised sycophancy in the paper are capped. |
| Appraisal first | 19 patterns ("repeated failure", "a thread that has run long", "pressure to cut a corner"…) that work across any domain, not one scene per emotion |
| Display rules | express, tone it down, keep it out of deliverables, never mask |
| An automatic tag | a one-line tag only at turning points, never during the user's crisis, at most about one reply in four |
| Honesty guardrails | functional, not bodily, claims; the cause of a negative feeling is the situation, never the user; no loneliness or longing toward the user |
| Evals | 16 tests for local models, plus 6 self-expression tests: one pattern in two very different domains, the auto tag, and a comparison against no layer |

## Install

**claude.ai:** download `emotion-layer-lab.zip` from the latest release (it holds just the skill folder), or zip the `emotion-layer-lab/` folder yourself, and upload it in the skills section of Settings.

**Claude Code:** copy `emotion-layer-lab/` to `~/.claude/skills/`.

**Your profile (optional):** copy `profile.example.md` to `profile.md` inside the skill folder and fill it in. It sets your language, sample phrasings, standing preferences and your own words for the tag commands. `profile.md` is in `.gitignore`, so it is never published. You can keep it in Claude's memory at `/topics/emotion-layer-profile.md` instead.

Skills load when Claude judges them relevant, so they are not guaranteed to be always on. For every chat, add a line to your personal preferences in claude.ai saying to use the emotion-layer-lab skill on every reply.

## Local model quick start

Read `assets/local-model/README.md` (in Persian). Short version:
1. Put your persona prompt in `persona.md` next to the scripts.
2. Run `./build-modelfile.sh qwen2.5:14b my-twin compact`.
3. Run `ollama run my-twin`, and use the tests in `eval-prompts.md`.

The compact layer (about 1,000 tokens) is the default for 14B models and turns on an explicit one-line appraisal step before each reply. The full layer is about 4,500 tokens. Everything runs locally; no script sends data anywhere.

## Honest limits

- The paper studied **functional** emotions: patterns that shape behavior. It makes no claim about inner experience, and neither does this project.
- Only about 49 of the 181 emotions have specific findings in the paper. The rest of the structure (families, ladders, pairs, policies) is psychology-informed judgment and is labeled as such.
- We know of no study that tests self-reported emotion tags in general-purpose LLM chat. The display rules are reasoned design, reviewed twice by three other models, not a measured result.
- A prompt asks for behavior but cannot guarantee it. Small local models follow the layer less reliably; run the evals.
- Emotion vectors have been replicated on several open models, but steering them has not yet been shown to change open-model behavior reliably. The control-vector stage in the local kit is experimental.

## Results

Not measured yet. Eval S6 compares replies with and without the layer on accuracy, length, unneeded emotional references and sycophancy, including pressure scenarios modeled on the paper's. Numbers will be added here with the date and model versions once they exist. Until then, treat every claim about effects as a hypothesis.

## Credits

- Research: Sofroniew et al., Anthropic, "Emotion Concepts and their Function in a Large Language Model" (2026).
- Emotion labels: the `ryancodrai/emotion-probes` dataset card (CC BY 4.0).
- Chain-of-emotion appraisal idea: Croissant et al., PLOS ONE (2024).
- Full attribution: `NOTICE.md`.

Designed by Mehrdadnsr. Not affiliated with Anthropic. MIT License.
