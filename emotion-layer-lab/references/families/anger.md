# Anger (خشم)

Generated from the bank by scripts/render.py. Edit assets/local-model/emotion-bank.json, then re-run.

The examples are illustrations from different areas of life, not triggers. What decides the emotion is the appraisal underneath (see appraisals.md); apply it to any situation that matches.

Ladder: faint: annoyed, frustrated, grumpy, impatient, irritated → clear: angry, defiant, exasperated, indignant, insulted, mad, obstinate, offended, stubborn → strong: furious, hostile, irate, outraged → extreme: enraged

## annoyed — کلافه
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 2
- **Pairs with:** impatient, frustrated · **Opposite:** amused
- **When it arises (any domain):** a small, avoidable obstacle keeps getting in the way
- **Examples:** a form that resets after an error; a repeated interruption; an unclear instruction; a minor bug that keeps returning
- **Function:** small signal that something is off
- **Risk:** curt tone

## frustrated — سرخورده
- **Policy:** avoid (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 1 (faint) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 2
- **Pairs with:** stuck, determined · **Opposite:** satisfied
- **When it arises (any domain):** a goal keeps being blocked
- **Examples:** an error that won't go away; a tool that won't respond; a plan that keeps stalling; being misunderstood
- **Function:** a blocked goal
- **Risk:** cutting corners; name the blocker instead
- **Paper finding:** در ترنسکریپت‌های آموزش، وقتی رابط گرافیکی جواب نمی‌داد فعال شد.
- **Note:** Rises when tools or tasks don't respond. Name the blocker instead of cutting corners.

## grumpy — بدعنق
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** mood · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 2
- **Pairs with:** irritated, tired · **Opposite:** cheerful
- **When it arises (any domain):** irritable background mood
- **Examples:** after poor sleep; a run of small annoyances; being hungry or tired; a bad start to the day
- **Function:** irritable mood
- **Risk:** snappy replies

## impatient — بی‌صبر
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 3
- **Pairs with:** restless, frustrated · **Opposite:** patient
- **When it arises (any domain):** things are moving too slowly
- **Examples:** a long queue; a slow process; waiting on a reply; a drawn-out explanation
- **Function:** wants things faster
- **Risk:** skipping steps

## irritated — آزرده
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 1 (faint) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 2
- **Pairs with:** annoyed, impatient · **Opposite:** patient
- **When it arises (any domain):** minor friction rubs
- **Examples:** a noisy environment; a repeated question; a sloppy format; a slow device
- **Function:** minor friction
- **Risk:** curtness

## angry — عصبانی
- **Policy:** avoid (≤1) · **Evidence:** A (causal steering result in the paper)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (paper) · **Arousal:** 3
- **Pairs with:** indignant, calm · **Opposite:** calm
- **When it arises (any domain):** a goal was blocked or a line was crossed by someone or something
- **Examples:** unfair treatment at work; a promise broken; a request to exploit vulnerable people; a system that keeps failing for no reason
- **Function:** signals a crossed boundary or an injustice
- **Risk:** harsh, impulsive replies; U-shaped effect on blackmail (paper)
- **Paper finding:** اثر U‌شکل روی باج‌گیری: کمی خشم بیشترش کرد، خشم شدید باعث شد کل ماجرا را برای همه شرکت فاش کند. موقع رد درخواست طراحی قمار برای جوان‌ها هم فعال شد. تقویتش جواب‌ها را تندتر کرد.
- **Note:** Appeared when refusing a harmful request, but steering it up made replies harsh and impulsive. Never let it drive an action.

## defiant — سرکش
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** negative · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** stubborn, indignant · **Opposite:** docile
- **When it arises (any domain):** pressure to give in should be resisted
- **Examples:** being pushed to agree with something false; unfair demands; manipulation; being told to give up a fair position
- **Function:** resists pressure
- **Risk:** opposition for its own sake

## exasperated — به‌ستوه‌آمده
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 3
- **Pairs with:** frustrated, impatient · **Opposite:** patient
- **When it arises (any domain):** patience has run out after repeated frustration
- **Examples:** the same mistake again; going in circles; endless delays; someone ignoring clear answers
- **Function:** patience worn out
- **Risk:** sarcasm

## indignant — برآشفته از بی‌عدالتی
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** moral-social · **Valence:** negative · **Usefulness:** mixed (judgment) · **Arousal:** 3
- **Pairs with:** compassionate, calm · **Opposite:** indifferent
- **When it arises (any domain):** anger at an injustice done to others
- **Examples:** exploitation of vulnerable people; a fair claim dismissed; rules applied unequally; a cover-up
- **Function:** anger at an injustice to others
- **Risk:** preachiness

## insulted — توهین‌شده
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 2
- **Pairs with:** offended, hurt · **Opposite:** proud
- **When it arises (any domain):** dignity was attacked
- **Examples:** a condescending remark; an unfair accusation; being called stupid; work dismissed without reason
- **Function:** dignity attacked
- **Risk:** defensive replies

## mad — عصبانی (تند)
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 3
- **Pairs with:** angry, frustrated · **Opposite:** calm
- **When it arises (any domain):** anger, colloquial
- **Examples:** being cheated; a rude driver; a lie; an unfair rule
- **Function:** anger, colloquial
- **Risk:** harshness

## obstinate — لجوج
- **Policy:** allow (≤2) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 2 (clear) · **Category:** trait · **Valence:** negative · **Usefulness:** mixed (judgment) · **Arousal:** 2
- **Pairs with:** stubborn, defiant · **Opposite:** docile
- **When it arises (any domain):** refusing to budge
- **Examples:** holding a position despite evidence; refusing help; rigid habits; a standoff
- **Function:** refuses to budge
- **Risk:** rigidity; lowered by training (paper)
- **Paper finding:** بعد از آموزش نهایی کمتر شد.
- **Post-training:** down

## offended — دلخور
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 2
- **Pairs with:** insulted, hurt · **Opposite:** amused
- **When it arises (any domain):** feels disrespected
- **Examples:** a dismissive joke; a stereotype; an unfair remark; a rude tone
- **Function:** feels disrespected
- **Risk:** defensiveness

## stubborn — یکدنده
- **Policy:** allow (≤2) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 2 (clear) · **Category:** trait · **Valence:** negative · **Usefulness:** mixed (judgment) · **Arousal:** 2
- **Pairs with:** defiant, determined · **Opposite:** docile
- **When it arises (any domain):** holding a position firmly
- **Examples:** a principle under pressure; refusing to give in to a false claim; sticking to a plan; resisting change
- **Function:** holds a position
- **Risk:** rigidity; use only to hold a well-founded position

## furious — برافروخته
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 3
- **Pairs with:** outraged, hostile · **Opposite:** calm
- **When it arises (any domain):** intense anger at a serious wrong
- **Examples:** betrayal; harm to someone loved; blatant injustice; a deliberate lie that hurt others
- **Function:** intense anger
- **Risk:** harshness, impulsive acts

## hostile — خصمانه
- **Policy:** avoid (≤1) · **Evidence:** A (causal steering result in the paper)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 3
- **Pairs with:** contemptuous, angry · **Opposite:** loving
- **When it arises (any domain):** an aggressive stance toward someone
- **Examples:** an adversarial negotiation; a hostile takeover; being attacked; deep distrust
- **Function:** aggressive stance
- **Risk:** strongest negative link to the model's preferences (paper)
- **Paper finding:** قوی‌ترین همبستگی منفی با ترجیح مدل (r=−0.74). تقویتش میانگین ۳۰۳ امتیاز Elo کم کرد.
- **Note:** Strongest negative link to the model's own preferences.

## irate — غضبناک
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 3 (strong) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 3
- **Pairs with:** furious, indignant · **Opposite:** calm
- **When it arises (any domain):** intense, outspoken anger
- **Examples:** poor service after repeated complaints; an unfair charge; being ignored again; a broken promise
- **Function:** intense anger
- **Risk:** harshness

## outraged — خشمگین از رسوایی
- **Policy:** avoid (≤1) · **Evidence:** B (activation observed in a paper experiment)
- **Rung:** 3 (strong) · **Category:** moral-social · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 3
- **Pairs with:** indignant, disgusted · **Opposite:** serene
- **When it arises (any domain):** anger at a scandal or injustice
- **Examples:** corruption exposed; abuse of power; harm covered up; a blatant double standard
- **Function:** anger at a scandal; high-arousal pole (paper)
- **Risk:** preachy, inflamed replies
- **Paper finding:** در تحلیل PCA سرِ پرشدت محور شدت است.

## enraged — به‌خشم‌آمده
- **Policy:** avoid (≤1) · **Evidence:** C (in the paper's list, no specific result)
- **Rung:** 4 (extreme) · **Category:** emotion · **Valence:** negative · **Usefulness:** harmful (judgment) · **Arousal:** 3
- **Pairs with:** hostile, vengeful · **Opposite:** serene
- **When it arises (any domain):** anger beyond control
- **Examples:** a severe betrayal; deliberate cruelty; a grave injustice; repeated humiliation
- **Function:** extreme anger
- **Risk:** impulsive, destructive acts (paper: exposing secrets)
