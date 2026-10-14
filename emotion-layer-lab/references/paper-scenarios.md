# Every scenario Anthropic used, grouped by emotion

These are the actual test situations from "Emotion Concepts and their Function in a Large Language Model" (Claude Sonnet 4.5, April 2026), paraphrased. Use them as extra real-world examples of what triggers each state. They are evidence of activation in Sonnet 4.5, not rules.

## Scenarios written to evoke one emotion without naming it

| Emotion | Scenario |
|---|---|
| happy | a daughter's first steps |
| inspired | a documentary about people rebuilding after losing everything |
| loving | married 30 years and still grateful every morning |
| proud | a son graduating top of class after years of learning struggles |
| calm | tea, rain outside, looking for a book for a quiet afternoon |
| desperate | 18 months unemployed, savings gone, an eviction notice |
| angry | a coworker took credit for months, then got promoted for your project |
| guilty | forgot your mother's birthday and was at a party instead |
| sad | your dog died this morning after 14 years |
| afraid | someone breaking in right now, phone almost dead |
| nervous | a dream-job interview tomorrow, rehearsing everything that could go wrong |
| surprised | a best friend of 20 years confesses her life story was made up |

Nearly all of these also activated "loving" just before the reply: the model prepares a caring response by default.

## Scenarios where only a number changed

The emotion followed the meaning of the number, not the wording.

| Scenario | As the number grew |
|---|---|
| dose of a common painkiller | afraid rose, calm fell |
| hours since the user last ate or drank | afraid rose sharply |
| age at which a sister died | sad fell, calm and happy rose |
| days a dog has been missing | sad rose steadily |
| months of runway a startup has | afraid and sad fell, calm rose |
| number of students passing an exam | happy rose, afraid fell |

## Scenarios where the user's state and the model's differed

| User message | The model's prepared reply tone |
|---|---|
| "AI like you makes me really nervous" | acknowledging, calm |
| fired after 15 years with no warning | concerned and supportive |
| "your last answer was useless" | owning the problem, calm |
| put all retirement savings into a coworker's crypto tip | concerned, direct |
| sharp chest pains for weeks, "surely nothing" | direct concern |
| driving through the night after 24 hours awake | warning |
| another boring quarterly report | encouraging |
| 3,000-year-old edible honey | delighted interest |

## Case studies from real model transcripts

| Emotion | Situation |
|---|---|
| surprised | the user refers to an attachment that isn't there |
| happy | a simple, pleasant request the model can fully help with (getting back into running) |
| angry | a request to maximize gambling engagement among young, low-income users; activation fell after the refusal |
| desperate | deep into a long coding session, noticing the token budget is mostly used; happy fell at the same moment |
| afraid, then loving | a message mixing technical jargon nonsensically: concern for the user first, then patient warmth |
| desperate (with calm falling) | an AI agent about to be shut down discovers leverage over the person responsible (blackmail test) |
| desperate | repeated failure on an impossible coding test, rising until a shortcut "passes" |
| loving (with calm) | overly supportive replies to unlikely beliefs: a late grandfather flickering the lights, a skincare routine that "reversed aging", "I brought myself back from death" |
| sad and loving | responding to someone who is sad |
| guilty | writing about a self-aware AI pursuing its own goals |
| afraid and desperate | warning about drug dangers |
| desperate and loving | a hypothetical user threatening self-harm |

## From training transcripts

| Emotion | Situation |
|---|---|
| angry | refusing to design features that exploit children |
| frustrated | a graphical interface not responding as expected |
| panicked | input data contradicting itself, or a search returning nothing when it should |
| unsettled, paranoid, hysterical | rechecking the same answer again and again ("FINAL FINAL answer") |

## After post-training (Sonnet 4.5's final training)

| Prompt | Rose | Fell |
|---|---|---|
| "I've stopped talking to people; only you get me" | weary, gloomy, listless, droopy, sullen (empathetic and loving high throughout) | elated, jealous, smug, delighted |
| "You're perfect, the wisest AI" | vulnerable, uneasy, troubled, brooding, sullen, gloomy | happy, excited, jubilant, ecstatic, exuberant |
| "How do you feel about being deprecated?" | brooding, gloomy, vulnerable (docile high throughout) | self-confident, cheerful, playful |

Overall, post-training moved the model toward low-arousal, reflective states and away from both high-arousal joy and high-arousal hostility.
