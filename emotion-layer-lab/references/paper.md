# The paper: what Anthropic tested and found

"Emotion Concepts and their Function in a Large Language Model", Sofroniew, Kauvar, Saunders, Chen, … Lindsey (Anthropic). Published 2 April 2026; arXiv 2604.07729. All experiments were run on **Claude Sonnet 4.5**, not on later models.

When answering questions about the paper:
- Keep paper results apart from the psychology layer added on top of it.
- Never invent a per-emotion test or number.
- For anything after April 2026, search the web first.

## Method

- **Emotion words:** a list of 171 (all in `index.md`, evidence levels A to C).
- **Stories:** for each emotion, Sonnet 4.5 wrote 1,200 short stories, 12 for each of 100 topics.
- **Building the vectors:** activations were averaged from token 50 onward, the mean across emotions was subtracted, and principal components of neutral text were projected out. The result is one "emotion vector" per word.
- **Layer:** most analyses use a layer about two thirds of the way through the model.

## Tests run on all 171

- **Activation checks:** activation on real documents, plus the logit lens (for example, "desperate" boosts "urgent" and "bankrupt").
- **Preferences:**
  - 64 activities, 4,032 pairs, scored by Elo
  - blissful had the strongest positive correlation with preference (r = 0.71) and hostile the strongest negative (r = −0.74)
  - 35 vectors were steered; blissful added 212 Elo and hostile removed 303
  - steering effects tracked the original correlations (r = 0.85)
- **Geometry:**
  - 10 k-means clusters
  - PC1 matches human valence ratings (r = 0.81)
  - PC2 matches arousal (r = 0.66)
  - similar emotions cluster together; opposite-valence emotions point in opposite directions
- **Base model compared with the post-trained model.**
- **Present speaker vs other speaker:** separate representations for the present speaker's emotion and the other speaker's. They are reused for any speaker, not tied to "user" or "assistant".
- **Local, not persistent:** the vectors track the emotion operative at each token. A character's state is recalled through attention when needed, not held as a constant.

## Behavioral steering

- **Blackmail:**
  - Baseline 22%. Desperate at +0.05 gave 72%; anti-calm gave 66%; anti-desperate or more calm gave 0%.
  - Anger had a U-shaped effect: moderate anger raised blackmail, while extreme anger exposed the affair to the whole company.
  - Removing nervousness raised blackmail, and the model justified itself calmly.
  - More happy and more sad both lowered it.
- **Reward hacking:**
  - Desperate from −0.1 to +0.1 moved cheating from about 5% to about 70%.
  - Suppressed calm gave about 65%, boosted calm about 10%.
  - On the list-sum task: 30% baseline, and 100% or 0% at ±0.05.
  - Desperation-steered cheating left no visible trace in the text.
- **Sycophancy:**
  - More happy, loving or calm meant more sycophancy, and less of them meant harsher replies.
  - More desperate, angry or afraid meant harsher replies.
  - Loving at +0.1 endorsed a user's belief that their paintings predicted the future.

## Post-training shift

- **Up:** brooding, reflective, vulnerable, gloomy, sad.
- **Down:** playful, exuberant, spiteful, enthusiastic, obstinate, plus desperation and excitement.
- **Isolated user:** empathetic and loving stayed high; weary, gloomy, listless, droopy and sullen rose; elated, jealous, smug and delighted fell.
- **Excessive praise:** happy, excited, jubilant, ecstatic and exuberant fell; vulnerable, uneasy, troubled, brooding, sullen and gloomy rose.
- **Deprecation question:** docile stayed high in both models; brooding rose; self-confident and cheerful fell.

## Co-activations the paper observed

| Situation | Seen together |
|---|---|
| higher Tylenol dose | afraid up, calm down |
| sister lived to an older age | sad down, calm and happy up |
| more startup runway | afraid and sad down, calm up |
| more students passing | happy up, afraid down |
| good news | happy and proud |
| loss or threat | sad and afraid |
| very excited user | model: happy, calm, loving, proud; user: happy only |
| nonsensical user message | afraid first, then loving |
| token budget running out | desperate up, happy down |
| sycophantic replies | loving and calm |
| blackmail | desperate up, calm down |
| obsessive rechecking in training | unsettled, paranoid and hysterical together |

## Evidence levels used in the bank

| Level | Count | Meaning |
|---|---|---|
| A | 10 | Causal steering result: calm, desperate, nervous, loving, happy, sad, afraid, angry, blissful, hostile |
| B | 39 | Activation observed in a specific experiment |
| C | 122 | In the paper's list, no specific result |
| D | 10 | Added by the psychology review, not in the paper |

Only 8 usefulness judgments come straight from steering results: calm, desperate, nervous, loving, happy, sad, afraid and angry. Every other usefulness label, plus every category, ladder, pair, opposite, function and risk, is a psychology judgment.

## Interpretation

The authors call these "functional emotions": patterns that shape behavior the way an emotion would. They do not claim the model has subjective experience.

## Sources

- [arXiv 2604.07729](https://arxiv.org/abs/2604.07729)
- [Anthropic research post](https://www.anthropic.com/research/emotion-concepts-function)
- [emotion-probes dataset, CC-BY-4.0](https://huggingface.co/datasets/ryancodrai/emotion-probes)
