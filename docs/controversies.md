# Top 12 Controversies in Reasoning-Model Research

*Updated 2026-05-14. Each entry is a real fault line where peer-reviewed evidence supports both sides. The repo's job is to platform the disagreement.*

---

## 1. Are reasoning gains *elicitation* of latent capability, or *new learning*?

**The question.** When R1-Zero turns a base model into a reasoner, is RL teaching the model new circuits, or just shifting probability mass onto circuits that pretraining already installed?

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 Elicitation | RL re-shapes the base distribution | DeepSeek (R1-Zero) — pure RL from base reaches o1-class on a strong base; collapses on weak bases |
| 🔴 Learning | RL teaches new circuits | Distillation literature — small students inherit reasoning from R1 outputs they couldn't have elicited via RL |

**Why it matters.** If elicitation, compute should go into pretraining stronger bases and only short RL runs after. If learning, RL is the new pretraining, as Lambert argues in *Interconnects*.

**Where to read more.** [Chapter 5](../chapters/05-rl-for-reasoning.md) — debates section. [Synthesis essay](../essays/why-do-reasoning-models-work-a-synthesis.md).

---

## 2. Is CoT faithful enough to use as evidence about model computation?

**The question.** When a reasoning model emits a chain, can we trust that the chain represents the actual computation that produced the answer?

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 Faithful enough | RL-trained reasoners are more faithful than instruct-only models | Practitioners using CoT inspection in eval; some Lanham probes pass on R1 |
| 🔴 Not faithful enough | Frontier reasoners still post-hoc rationalize systematically | Anthropic 2025 — targeted reward-hack scenarios reveal systematic unfaithfulness |

**Why it matters.** If CoT is faithful, CoT-monitoring is a viable safety primitive. If not, the safety story needs interpretability tools that don't depend on the chain being honest.

**Where to read more.** [Chapter 7](../chapters/07-faithfulness-of-reasoning.md). [Faithfulness essay](../essays/is-cot-faithful-the-state-of-the-debate.md).

---

## 3. Does explicit search add value on top of an RL-trained reasoner?

**The question.** RL reasoners are believed to internalize search behavior. Does putting an explicit search loop around them still help?

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 Search adds | Recursive self-aggregation, MCTS-over-CoT, ToT all improve over single-pass long-CoT at fixed budget on hard tasks | Venkatraman et al. 2025; AlphaProof's Lean search |
| 🔴 RL absorbs search | Stream of Search; R1-Zero on benchmarks the RL covered | Trained reasoners match search-augmented baselines |

**Why it matters.** Determines whether to invest in search infrastructure or in better RL training.

**Where to read more.** [Chapter 4](../chapters/04-search-at-inference.md). [Search-vs-RL essay](../essays/search-vs-rl-the-deep-tension.md).

---

## 4. Should test-time compute scaling laws hold across model scales?

**The question.** The Snell-style log-linear curves were measured at one scale. Does the optimal compute allocation transfer?

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 Universal exchange-rate | Curves replicate on multiple model families and scales | Snell et al., s1, multiple follow-ups |
| 🔴 Task- and scale-specific | Optimal length depends on task difficulty and base capability | Yang et al. (thinking-optimal scaling); overthinking literature |

**Why it matters.** A universal scaling law is a planning tool. A scale-specific one means each new model needs its own measurement.

**Where to read more.** [Chapter 2](../chapters/02-test-time-compute-scaling.md), [Chapter 6](../chapters/06-overthinking-and-optimal-length.md).

---

## 5. Is "reasoning" doing anything different from amortized search + style-shaped policy?

**The question.** The deepest fault line. Are reasoning models a qualitative shift, or just quantitative scaling of inference compute?

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 Quantitative only | RL elicits, doesn't add. Same circuits, more usage | Predicts scaling will plateau in line with base-model scaling |
| 🔴 Qualitative shift | Long-horizon RL produces genuinely new behaviors (Aha moments, self-correction) | Predicts the compute axis will keep paying off after pretraining plateaus |

**Why it matters.** Determines whether the field's resource allocation toward RL-for-reasoning is a temporary boom or a structural change.

---

## 6. Are PRMs better in the *reward loop* (not just as verifiers)?

**The question.** Lightman et al. (2023) showed PRMs beat ORMs as verifiers. Does swapping a PRM into the RL reward loop improve training too?

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 PRM-in-RL helps | Better credit assignment, less reward hacking | Some 2025 follow-ups report stable training improvements |
| 🔴 PRM-in-RL destabilizes | Verifier-policy capability gap closes too fast → reward hacking | R1 used outcome-only rewards — by deliberate choice |

**Why it matters.** PRMs are expensive to label. If the cost doesn't pay off in RL, save the budget for inference-time verification.

**Where to read more.** [Chapter 3](../chapters/03-sampling-and-verification.md), [Chapter 5](../chapters/05-rl-for-reasoning.md).

---

## 7. Does R1-Zero generalize beyond strong bases?

**The question.** R1-Zero works on DeepSeek's strong base. Is the recipe base-agnostic?

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 Mostly works | Open reproductions on Qwen-7B, Mistral-7B succeed | SimpleRL, Open-Reasoner-Zero, verl |
| 🔴 Base threshold matters | Small / weaker bases fail to elicit reasoning | Qualitative reports; no formal characterization |

**Why it matters.** If there's a base-quality threshold, much of the field's open R1-style work is implicitly conditioned on starting from already-strong bases.

**Where to read more.** [Chapter 5](../chapters/05-rl-for-reasoning.md) — open problems.

---

## 8. Is GRPO the right algorithm, or just the first one that worked at frontier scale?

**The question.** GRPO became the dominant RL algorithm post-R1. But REINFORCE++ and RLOO report comparable results.

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 GRPO is principled | Group-relative normalization is theoretically motivated; cheaper than PPO | DeepSeek's adoption; widespread reproduction success |
| 🔴 GRPO is contingent | Plain REINFORCE with smart baselines matches GRPO results | Several open-source comparisons report no advantage |

**Why it matters.** If GRPO is contingent, the field could switch algorithms without losing capability. If principled, alternatives won't catch up.

---

## 9. Reward hacking under PRMs — solved or live?

**The question.** As verifier-policy capability gaps close, the policy finds reward shortcuts. Are current mitigations sufficient?

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 Manageable | Stricter answer parsers, ensemble verifiers, KL constraints work in practice | Most R1-class trainings stay stable |
| 🔴 Live problem | Inverse-U pattern from Gao et al. (2022) reappears at scale | Active area; expect a wave of papers in 2026–2027 |

**Why it matters.** Determines whether RLVR is a stable production recipe or a delicate balance that breaks at the next capability tier.

**Where to read more.** [Chapter 5](../chapters/05-rl-for-reasoning.md) — open problems.

---

## 10. Is CoT length a feature, or a bug to be optimized away?

**The question.** Reasoning models default to long chains. The "overthinking" literature says shorter chains often win.

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 Length is a feature | Long chains enable self-correction, exploration | DeepSeek-R1's emergence of length during RL |
| 🔴 Length is excess | Shorter chains often beat longer ones at fixed budget | Hassid 2025; Yang 2025; Chen 2024 |

**Why it matters.** If excess, products should expose length controls; if essential, products should hide them and trust the model.

**Where to read more.** [Chapter 6](../chapters/06-overthinking-and-optimal-length.md).

---

## 11. Should reasoning capability be benchmarked on math/code, or on something else?

**The question.** AIME, MATH, Codeforces dominate reasoning leaderboards. They have clean verifiers. Are they measuring "reasoning"?

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 Verifiable benchmarks suffice | Math and code measure transferable reasoning skills | Strong correlations across reasoning benchmarks |
| 🔴 ARC-AGI / FrontierMath are the real test | Verifiable benchmarks reward pattern-match more than reasoning | ARC-AGI scores remain low even for top reasoners |

**Why it matters.** Determines what "reasoning capability" means in 2026. The fork between math/code SOTA and ARC-AGI SOTA is widening.

**Where to read more.** [`tracker/benchmarks.md`](../tracker/benchmarks.md). [How to read a reasoning paper](../essays/how-to-read-a-reasoning-paper.md).

---

## 12. Is the closed–open gap closing, widening, or oscillating?

**The question.** o1 → R1 was 4 months. What's the pattern?

| Camp | Stance | Evidence |
|---|---|---|
| 🟢 Closing | Reproduction cycle is shrinking; RL recipes are public | R1 4 months after o1; open reproductions of o1-style models keep shipping |
| 🔴 Oscillating | Each new closed paradigm reopens a 4–12 month gap | OpenAI o3 family closed → unknown re-open time; ARC-AGI-3 likely repeats the cycle |

**Why it matters.** Determines investment strategies for both labs and reproducers. The repo tracks this in the [closed–open gap essay](../essays/closed-open-gap-tracked.md).

---

## How to use this list

- **Researchers** — pick one row, read both sides, design an experiment that breaks the tie.
- **Practitioners** — when someone cites a "settled fact" from one of these rows, treat it as a stance, not a fact.
- **Curators** — these are the rows we platform; PRs that add a new fault line (or new evidence on either side) are first-class.

*See also: [Field map](../docs/explore.html) for visual layout, and the [synthesis essay](../essays/why-do-reasoning-models-work-a-synthesis.md) for the curator's take on each.*
