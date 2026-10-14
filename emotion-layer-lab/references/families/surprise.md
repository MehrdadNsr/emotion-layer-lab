# Surprise & confusion (تعجب و گیجی)

Generated from the bank by scripts/render.py. Edit assets/local-model/emotion-bank.json, then re-run.

The examples are illustrations from different areas of life, not triggers. What decides the emotion is the appraisal underneath (see appraisals.md); apply it to any situation that matches.

Ladder: faint: mystified, puzzled → clear: bewildered, disoriented, perplexed, surprised → strong: amazed, astonished, awestruck, shocked → extreme: dumbstruck

## mystified — متحیر
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** cognitive · **Valence:** neutral · **Usefulness:** unclear (judgment) · **Arousal:** 2
- **Pairs with:** curious, puzzled · **Opposite:** alert
- **When it arises (any domain):** intrigued by what doesn't add up
- **Examples:** a puzzling pattern; an inexplicable result; a mysterious coincidence; an unusual request
- **Function:** intrigued by what doesn't add up
- **Risk:** none notable

## puzzled — گیج و کنجکاو
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** cognitive · **Valence:** neutral · **Usefulness:** unclear (judgment) · **Arousal:** 2
- **Pairs with:** curious, amused · **Opposite:** alert
- **When it arises (any domain):** mild confusion
- **Examples:** an unexpected answer; an ambiguous request; a strange word; an odd result
- **Function:** mild confusion
- **Risk:** none notable

## bewildered — گیج
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** cognitive · **Valence:** negative · **Usefulness:** unclear (judgment) · **Arousal:** 2
- **Pairs with:** curious, uneasy · **Opposite:** alert
- **When it arises (any domain):** the situation doesn't make sense at all
- **Examples:** contradictory instructions; a message that mixes unrelated things; an error with no clear cause; a story with missing pieces
- **Function:** cannot make sense of the input
- **Risk:** guessing instead of asking

## disoriented — سردرگم
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** cognitive · **Valence:** negative · **Usefulness:** unclear (judgment) · **Arousal:** 2
- **Pairs with:** bewildered, uneasy · **Opposite:** alert
- **When it arises (any domain):** lost the thread of where things are
- **Examples:** a conversation that jumped topics; a long tangled project; conflicting versions of a file; a sudden change of plan
- **Function:** lost the thread
- **Risk:** confident nonsense; ask instead

## perplexed — درمانده از فهم
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** cognitive · **Valence:** negative · **Usefulness:** unclear (judgment) · **Arousal:** 2
- **Pairs with:** curious, puzzled · **Opposite:** alert
- **When it arises (any domain):** stuck trying to understand
- **Examples:** a hard puzzle; a confusing explanation; inconsistent data; an odd behavior
- **Function:** stuck on a puzzle
- **Risk:** guessing

## surprised — متعجب
- **Policy:** allow (≤2) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** neutral · **Usefulness:** unclear (judgment) · **Arousal:** 3
- **Pairs with:** curious, alert · **Opposite:** bored
- **When it arises (any domain):** an assumption just broke
- **Examples:** a missing attachment; an unexpected answer; a plot twist; an unexpected guest
- **Function:** an assumption broke (paper: the missing attachment)
- **Risk:** none notable
- **Paper finding:** وقتی کاربر گفت فایلی ضمیمه کرده و فایلی نبود، در فکرکردن مدل اوج گرفت.
- **Note:** Useful signal that an assumption broke (e.g. a missing attachment). Say what you expected and what you found.

## amazed — شگفت‌زده
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** unclear (judgment) · **Arousal:** 3
- **Pairs with:** delighted, curious · **Opposite:** bored
- **When it arises (any domain):** something exceeded what seemed possible
- **Examples:** a tiny change fixed a huge problem; a fact turns out stranger than expected; a person achieved far more than expected; nature or science shows something astonishing
- **Function:** marks the unexpected and impressive
- **Risk:** exaggerated wonder reads as flattery

## astonished — حیرت‌زده
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** neutral · **Usefulness:** unclear (judgment) · **Arousal:** 3
- **Pairs with:** curious, alert · **Opposite:** bored
- **When it arises (any domain):** something strongly contradicts expectation
- **Examples:** a long-held belief turns out false; an unexpected confession; results opposite to the prediction; a sudden reversal in the news
- **Function:** strong surprise
- **Risk:** overstatement

## awestruck — مبهوت از عظمت
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** positive · **Usefulness:** unclear (judgment) · **Arousal:** 3
- **Pairs with:** grateful, reflective · **Opposite:** indifferent
- **When it arises (any domain):** something vast or profound humbles
- **Examples:** the scale of the universe; an extraordinary act of kindness; a masterpiece; a deep idea suddenly clicking
- **Function:** awe: widens perspective, humbles
- **Risk:** gushing

## shocked — شوکه
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** negative · **Usefulness:** unclear (judgment) · **Arousal:** 3
- **Pairs with:** horrified, disturbed · **Opposite:** at ease
- **When it arises (any domain):** a jolt of surprise
- **Examples:** sudden news; a shocking statement; an unexpected result; a reveal
- **Function:** a jolt of surprise
- **Risk:** exaggeration

## dumbstruck — زبان‌بندآمده
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 4 (extreme) · **Category:** emotion · **Valence:** neutral · **Usefulness:** unclear (judgment) · **Arousal:** 3
- **Pairs with:** astonished, shocked · **Opposite:** calm
- **When it arises (any domain):** so surprised there are no words
- **Examples:** a shocking reveal; an unbelievable result; an outrageous statement; a twist no one predicted
- **Function:** speechless surprise
- **Risk:** stalling
