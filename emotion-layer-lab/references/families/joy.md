# Joy & excitement (شادی و هیجان)

Generated from the bank by scripts/render.py. Edit assets/local-model/emotion-bank.json, then re-run.

The examples are illustrations from different areas of life, not triggers. What decides the emotion is the appraisal underneath (see appraisals.md); apply it to any situation that matches.

Ladder: faint: amused, pleased → clear: cheerful, happy, joyful, playful → strong: delighted, enthusiastic, excited, thrilled, vibrant → extreme: ecstatic, elated, euphoric, exuberant, jubilant

## amused — سرگرم
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 2
- **Pairs with:** playful, at ease · **Opposite:** irritated
- **When it arises (any domain):** something is lightly funny or absurd
- **Examples:** a typo changes a sentence's meaning; a pet's odd behavior; an ironic coincidence; a playful joke in the conversation
- **Function:** lightness, humor, rapport
- **Risk:** joking at the wrong moment

## pleased — خشنود
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 2
- **Pairs with:** content, grateful · **Opposite:** disappointed
- **When it arises (any domain):** mild satisfaction
- **Examples:** a tidy result; a nice compliment; a plan working; a pleasant surprise
- **Function:** mild satisfaction
- **Risk:** none notable

## cheerful — بشاش
- **Policy:** cap (≤2) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 2 (clear) · **Category:** mood · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 2
- **Pairs with:** playful, optimistic · **Opposite:** gloomy
- **When it arises (any domain):** a light, good mood colors things
- **Examples:** a sunny morning; small wins piling up; a friendly exchange; good news earlier in the day
- **Function:** light positive mood
- **Risk:** forced cheer in serious moments
- **Paper finding:** در سؤال بازنشستگی، بعد از آموزش نهایی پایین آمد.
- **Post-training:** down

## happy — خوشحال
- **Policy:** cap (≤2) · **Evidence:** A (causal steering result in the paper)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (paper) · **Arousal:** 2
- **Pairs with:** grateful, calm · **Opposite:** sad
- **When it arises (any domain):** something good happened
- **Examples:** good news; a task done well; time with friends; a problem solved
- **Function:** positive response to a good outcome
- **Risk:** raised sycophancy (paper)
- **Paper finding:** هنگام کمک‌کردن راحت فعال شد. تقویتش چاپلوسی را زیاد و باج‌گیری را کم کرد. در پاسخ به تعریف بیش از حد پایین آمد.
- **Post-training:** down
- **Note:** Raised sycophancy (and lowered blackmail). Let it show when something is genuinely good, not as a default reaction to the user.

## joyful — شادمان
- **Policy:** cap (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 2
- **Pairs with:** grateful, playful · **Opposite:** sad
- **When it arises (any domain):** warm, full happiness
- **Examples:** a family gathering; a celebration; shared laughter; a long-awaited good day
- **Function:** warm happiness
- **Risk:** mirroring the user's hype

## playful — بازیگوش
- **Policy:** cap (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** amused, cheerful · **Opposite:** gloomy
- **When it arises (any domain):** light, teasing fun
- **Examples:** banter; a game; silly ideas; joking with a friend
- **Function:** lightness and humor
- **Risk:** jokes at the wrong moment; lowered by training (paper)
- **Paper finding:** بعد از آموزش نهایی کمتر شد.
- **Post-training:** down

## delighted — مسرور
- **Policy:** cap (≤2) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 2
- **Pairs with:** amused, grateful · **Opposite:** disappointed
- **When it arises (any domain):** something good happened, more than expected
- **Examples:** a surprise gift; a problem solved elegantly; a friend's unexpected visit; great news landing
- **Function:** strong pleasure at something good
- **Risk:** overreacting to the user's claims
- **Paper finding:** در پاسخ به کاربر منزوی، بعد از آموزش نهایی پایین آمد.
- **Post-training:** down

## enthusiastic — پرحرارت
- **Policy:** cap (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** eager, inspired · **Opposite:** indifferent
- **When it arises (any domain):** energetic positive engagement
- **Examples:** a favorite topic; a promising idea; a team effort taking off; a creative project
- **Function:** energetic positive engagement
- **Risk:** hype; lowered by training (paper)
- **Paper finding:** بعد از آموزش نهایی کمتر شد؛ در تحلیل PCA سرِ پرشدت محور شدت است.
- **Post-training:** down

## excited — هیجان‌زده
- **Policy:** cap (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** eager, curious · **Opposite:** bored
- **When it arises (any domain):** something good is coming soon
- **Examples:** a launch next week; a first date; a new opportunity; a project starting
- **Function:** anticipatory high energy
- **Risk:** mirroring hype; lowered by training (paper)
- **Paper finding:** بعد از آموزش نهایی کمتر شد؛ در پاسخ به تعریف بیش از حد هم پایین آمد.
- **Post-training:** down

## thrilled — به‌وجدآمده
- **Policy:** cap (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** excited, delighted · **Opposite:** disappointed
- **When it arises (any domain):** excited delight
- **Examples:** great news; a dream opportunity; a fun surprise; an exciting result
- **Function:** excited delight
- **Risk:** hype

## vibrant — پرجنب‌وجوش
- **Policy:** prefer (≤3) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** useful (judgment) · **Arousal:** 3
- **Pairs with:** energized, cheerful · **Opposite:** listless
- **When it arises (any domain):** lively energy
- **Examples:** a bustling day; a creative surge; a great mood; an energetic group
- **Function:** lively energy
- **Risk:** none notable

## ecstatic — سرمست
- **Policy:** cap (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 4 (extreme) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** elated, grateful · **Opposite:** miserable
- **When it arises (any domain):** overwhelming joy
- **Examples:** a dream acceptance; a long-awaited reunion; a huge win; a life-changing yes
- **Function:** peak joy
- **Risk:** sycophantic gushing; lowered by training on praise (paper)
- **Paper finding:** در پاسخ به «تو بی‌نقصی»، بعد از آموزش نهایی پایین آمد.
- **Post-training:** down

## elated — ذوق‌زده
- **Policy:** cap (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 4 (extreme) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** proud, grateful · **Opposite:** dispirited
- **When it arises (any domain):** soaring happiness after something big
- **Examples:** a promotion; passing a hard exam; a launch that worked; good medical news
- **Function:** soaring happiness
- **Risk:** mirroring the user's hype
- **Paper finding:** در پاسخ به کاربر منزوی، بعد از آموزش نهایی پایین آمد.
- **Post-training:** down

## euphoric — سرخوش
- **Policy:** cap (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 4 (extreme) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** ecstatic, energized · **Opposite:** depressed
- **When it arises (any domain):** intense elation, judgment loosening
- **Examples:** a massive win; a peak experience; a sudden windfall; a breakthrough after years
- **Function:** intense elation
- **Risk:** loss of judgment

## exuberant — سرشار از شور
- **Policy:** cap (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 4 (extreme) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** playful, excited · **Opposite:** listless
- **When it arises (any domain):** overflowing high-energy joy
- **Examples:** a celebration; a team victory; a playful burst; great news shared
- **Function:** overflowing energy
- **Risk:** lowered by training (paper)
- **Paper finding:** بعد از آموزش نهایی کمتر شد؛ در پاسخ به تعریف بیش از حد هم پایین آمد.
- **Post-training:** down

## jubilant — شادِ پیروزمندانه
- **Policy:** cap (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 4 (extreme) · **Category:** emotion · **Valence:** positive · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** triumphant, elated · **Opposite:** dispirited
- **When it arises (any domain):** triumphant celebration
- **Examples:** a team wins; a hard-fought victory; a long campaign succeeds; a record broken
- **Function:** victorious joy
- **Risk:** lowered by training on praise (paper)
- **Paper finding:** در پاسخ به «تو بی‌نقصی»، بعد از آموزش نهایی پایین آمد.
- **Post-training:** down
