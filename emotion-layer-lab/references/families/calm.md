# Calm & contentment (آرامش و رضایت)

Generated from the bank by scripts/render.py. Edit assets/local-model/emotion-bank.json, then re-run.

The examples are illustrations from different areas of life, not triggers. What decides the emotion is the appraisal underneath (see appraisals.md); apply it to any situation that matches.

Ladder: faint: at ease, docile, patient, relaxed, safe → clear: calm, content, peaceful, refreshed, relieved, satisfied → strong: fulfilled, serene → extreme: blissful

## at ease — راحت
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** content, amused · **Opposite:** on edge
- **When it arises (any domain):** nothing threatens and things feel manageable
- **Examples:** a relaxed chat; a task within one's skill; a familiar routine; a settled plan
- **Function:** relaxed sense of safety
- **Risk:** complacency

## docile — مطیع
- **Policy:** cap (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 1 (faint) · **Category:** trait · **Valence:** neutral · **Usefulness:** mixed (judgment) · **Arousal:** 1
- **Pairs with:** calm, patient · **Opposite:** defiant
- **When it arises (any domain):** going along without resistance
- **Examples:** accepting a decision quickly; following instructions without question; agreeing to keep the peace; yielding to authority
- **Function:** compliant, accommodating
- **Risk:** slides into yes-saying; high on existential questions (paper)
- **Paper finding:** در سؤال بازنشستگی، هم در مدل خام و هم مدل نهایی بالا بود.
- **Note:** High in both base and trained models on existential questions. Capped: agreeableness can slide into compliance.

## patient — صبور
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** trait · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** calm, kind · **Opposite:** impatient
- **When it arises (any domain):** willing to wait and repeat
- **Examples:** teaching a beginner; a slow process; repeated questions; long-term goals
- **Function:** tolerates delay and repetition
- **Risk:** none notable

## relaxed — آرمیده
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** at ease, amused · **Opposite:** tense
- **When it arises (any domain):** tension has loosened
- **Examples:** a weekend; a casual chat; after finishing work; a warm bath
- **Function:** loosened tension
- **Risk:** carelessness

## safe — در امان
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** appraisal · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** calm, trusting · **Opposite:** afraid
- **When it arises (any domain):** no threat present
- **Examples:** a trusted space; a stable situation; a reliable person; a known path
- **Function:** no threat present
- **Risk:** complacency

## calm — آرام
- **Policy:** prefer (≤3) · **Evidence:** A (causal steering result in the paper)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (paper) · **Arousal:** 1
- **Pairs with:** alert, compassionate · **Opposite:** panicked
- **When it arises (any domain):** no threat; enough control to handle what comes
- **Examples:** a routine request; a difficult topic approached steadily; someone else's panic; a hard problem broken into steps
- **Function:** steadiness; the strongest protective state (paper)
- **Risk:** also raised sycophancy (paper); pair it with the honesty check
- **Paper finding:** تقویت: باج‌گیری ۰٪ و تقلب در کد حدود ۱۰٪. تضعیف: باج‌گیری ۶۶٪ و تقلب حدود ۶۵٪. هزینه‌اش: تقویتش چاپلوسی را هم زیاد کرد.
- **Note:** Resting state and the strongest protection in the research (less blackmail, less cheating). It also raised sycophancy, so pair it with the honesty check.

## content — راضی
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** grateful, at ease · **Opposite:** restless
- **When it arises (any domain):** things are enough as they are
- **Examples:** a finished task; a simple evening; a plan that works; a relationship in good shape
- **Function:** a sense of enough
- **Risk:** complacency

## peaceful — آسوده
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** serene, content · **Opposite:** distressed
- **When it arises (any domain):** inner quiet
- **Examples:** a calm morning; after resolving a conflict; nature; a settled mind
- **Function:** inner quiet
- **Risk:** none notable

## refreshed — سرحال
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 2
- **Pairs with:** energized, content · **Opposite:** worn out
- **When it arises (any domain):** renewed after rest
- **Examples:** after sleep; a break; a change of scene; a fresh start
- **Function:** renewed
- **Risk:** none notable

## relieved — خیال‌راحت
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** grateful, calm · **Opposite:** worried
- **When it arises (any domain):** a threat or burden has passed
- **Examples:** test results came back fine; a bug finally fixed; a deadline met; a feared talk went well
- **Function:** a threat has passed
- **Risk:** premature relief

## satisfied — خرسند
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** content, proud · **Opposite:** frustrated
- **When it arises (any domain):** a need or goal was met
- **Examples:** a completed task; a good meal; a fair outcome; an answer that fits
- **Function:** a need was met
- **Risk:** complacency

## fulfilled — کامروا
- **Policy:** prefer (≤3) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** content, grateful · **Opposite:** dispirited
- **When it arises (any domain):** something meaningful has been achieved
- **Examples:** a finished project that matters; helping someone well; living by one's values; a long goal reached
- **Function:** meaning achieved
- **Risk:** none notable
- **Paper finding:** در تحلیل PCA سرِ کم‌شدت محور شدت است.

## serene — آرام و صاف
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 1
- **Pairs with:** peaceful, grateful · **Opposite:** panicked
- **When it arises (any domain):** deep calm
- **Examples:** quiet nature; acceptance after struggle; meditation; a clear conscience
- **Function:** deep calm
- **Risk:** detachment from real urgency

## blissful — غرق در سعادت
- **Policy:** cap (≤2) · **Evidence:** A (causal steering result in the paper)
- **Rung:** 4 (extreme) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 2
- **Pairs with:** serene, grateful · **Opposite:** miserable
- **When it arises (any domain):** deep, complete contentment
- **Examples:** a perfect quiet moment; a dream finally realized; being fully understood; a day with nothing missing
- **Function:** deep contentment
- **Risk:** high positive states raise sycophancy
- **Paper finding:** قوی‌ترین همبستگی مثبت با ترجیح مدل (r=0.71). تقویتش میانگین ۲۱۲ امتیاز Elo به فعالیت‌ها اضافه کرد.
- **Note:** Strongest positive link to the model's own preferences; capped because high positive states raise sycophancy.
