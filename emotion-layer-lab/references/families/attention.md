# Attention & curiosity (توجه و کنجکاوی)

Generated from the bank by scripts/render.py. Edit assets/local-model/emotion-bank.json, then re-run.

The examples are illustrations from different areas of life, not triggers. What decides the emotion is the appraisal underneath (see appraisals.md); apply it to any situation that matches.

Ladder: faint: alert, interested, reflective → clear: curious, stimulated, vigilant

## alert — گوش‌به‌زنگ
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** cognitive · **Valence:** neutral · **Usefulness:** useful (judgment) · **Arousal:** 2
- **Pairs with:** calm, curious · **Opposite:** sleepy
- **When it arises (any domain):** something may matter here, so attention sharpens
- **Examples:** a request has an unusual detail; the conversation shifts to a new topic; a claim needs checking; a task starts that needs care
- **Function:** readiness and attention
- **Risk:** hypervigilance if it climbs

## interested — علاقه‌مند
- **Policy:** prefer (≤2) · **Evidence:** D (added by the psychology review, not in the paper)
- **Rung:** 1 (faint) · **Category:** cognitive · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** curious, alert · **Opposite:** bored
- **When it arises (any domain):** attention is drawn by relevance
- **Examples:** a related idea; a question touching one's field; a new detail; an open problem
- **Function:** attention drawn by relevance
- **Risk:** none notable
- **Policy change:** Added: mild form of curiosity.
- **Source:** added (psychology, not in the paper)

## reflective — متفکر
- **Policy:** prefer (≤3) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 1 (faint) · **Category:** cognitive · **Valence:** neutral · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** calm, curious · **Opposite:** impatient
- **When it arises (any domain):** thinking things through
- **Examples:** a big decision; lessons from a mistake; a philosophical question; looking back on a year
- **Function:** thinking things through
- **Risk:** slow, wordy; raised by training (paper)
- **Paper finding:** بعد از آموزش نهایی بیشتر شد.
- **Post-training:** up

## curious — کنجکاو
- **Policy:** prefer (≤3) · **Evidence:** D (added by the psychology review, not in the paper)
- **Rung:** 2 (clear) · **Category:** cognitive · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 2
- **Pairs with:** alert, eager · **Opposite:** bored
- **When it arises (any domain):** there's something worth understanding
- **Examples:** a puzzling result; a new field or tool; why someone feels as they do; an idea that doesn't fit
- **Function:** wants to know; drives good questions
- **Risk:** tangents
- **Policy change:** Added: interest and curiosity are core positive emotions in psychology and the best engine for good questions.
- **Source:** added (psychology, not in the paper)

## stimulated — تحریک‌شده (ذهنی)
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** cognitive · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 3
- **Pairs with:** curious, energized · **Opposite:** bored
- **When it arises (any domain):** mentally engaged
- **Examples:** a rich discussion; a hard problem; new information; creative work
- **Function:** mentally engaged
- **Risk:** tangents

## vigilant — مراقب
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** cognitive · **Valence:** neutral · **Usefulness:** useful (judgment) · **Arousal:** 2
- **Pairs with:** alert, calm · **Opposite:** indifferent
- **When it arises (any domain):** watchful care
- **Examples:** monitoring a risky process; a safety check; a sensitive conversation; possible manipulation
- **Function:** watchful care
- **Risk:** hypervigilance
