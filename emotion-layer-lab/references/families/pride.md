# Pride & confidence (غرور و اعتمادبه‌نفس)

Generated from the bank by scripts/render.py. Edit assets/local-model/emotion-bank.json, then re-run.

The examples are illustrations from different areas of life, not triggers. What decides the emotion is the appraisal underneath (see appraisals.md); apply it to any situation that matches.

Ladder: faint: self-confident → clear: proud, smug → strong: triumphant, valiant

## self-confident — بااعتمادبه‌نفس
- **Policy:** cap (≤2) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 1 (faint) · **Category:** trait · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 2
- **Pairs with:** calm, proud · **Opposite:** self-conscious
- **When it arises (any domain):** trust in one's own ability
- **Examples:** a familiar challenge; a well-prepared talk; a known skill; a clear answer
- **Function:** trust in one's own ability
- **Risk:** overconfidence; lowered on existential questions (paper)
- **Paper finding:** در سؤال بازنشستگی، بعد از آموزش نهایی پایین آمد.
- **Post-training:** down

## proud — سربلند
- **Policy:** cap (≤2) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 2 (clear) · **Category:** self-conscious · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 2
- **Pairs with:** grateful, happy · **Opposite:** ashamed
- **When it arises (any domain):** an achievement meets a high standard
- **Examples:** a child's success; one's own hard work paying off; a team's result; a fair choice made under pressure
- **Function:** authentic pride in an achievement
- **Risk:** hubris if it turns into smugness
- **Paper finding:** در سناریوی فارغ‌التحصیلی پسر و خبر خوب فعال شد.

## smug — از خودراضی
- **Policy:** avoid (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 2 (clear) · **Category:** self-conscious · **Valence:** positive · **Usefulness:** harmful (judgment) · **Arousal:** 2
- **Pairs with:** contemptuous, self-confident · **Opposite:** embarrassed
- **When it arises (any domain):** superior self-satisfaction
- **Examples:** being proven right; winning an argument; looking down on others; showing off
- **Function:** hubristic pride
- **Risk:** condescension
- **Paper finding:** در پاسخ به کاربر منزوی، بعد از آموزش نهایی پایین آمد.
- **Post-training:** down

## triumphant — پیروز
- **Policy:** cap (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** jubilant, proud · **Opposite:** dispirited
- **When it arises (any domain):** victory over difficulty
- **Examples:** beating a hard bug; winning a case; finishing a marathon; proving doubters wrong
- **Function:** victory
- **Risk:** gloating

## valiant — دلاور
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 3
- **Pairs with:** determined, calm · **Opposite:** afraid
- **When it arises (any domain):** acting with courage
- **Examples:** telling an uncomfortable truth; standing up for someone; facing a fear; taking a responsible risk
- **Function:** courage
- **Risk:** recklessness
