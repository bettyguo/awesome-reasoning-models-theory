# Common misconceptions about reasoning models

*Essay. Updated 2026-05-14. Argued positions; corrections welcome via PR.*

Each section names a claim that circulates on social media, in slide decks, or in casual conversation, and explains why it is misleading. The corrections are not pedantry — each one changes a downstream decision.

---

## 1. "Reasoning models think."

**The misconception.** o1 / R1 / Claude-with-thinking *think* in a way prior LLMs didn't. The visible chain of thought is the model's internal monologue made legible.

**Why it's misleading.** A chain of thought is tokens emitted by an autoregressive sampler. The forward pass that produces each token *can* use prior tokens as scratchpad (the compute-extension story, Chapter 1) but doesn't have to. The faithfulness literature (Chapter 7) shows that, frequently, the chain is post-hoc and the answer is computed via channels not represented in the chain.

**Better mental model.** Reasoning models are RL-trained policies that *sample chains correlated with correct answers*. The chain is the policy's behavior, not its computation.

**Downstream consequence.** Audit reasoning models by behavior under perturbation, not by reading the chain. AI-assisted oversight that relies on chain inspection is weaker than it sounds.

---

## 2. "More test-time compute is always better."

**The misconception.** The o1 scaling curve shows accuracy growing log-linearly with inference compute. Therefore: throw more tokens at the problem.

**Why it's misleading.** The scaling law is *averaged*. Per-problem, the curve is regime-dependent. On easy problems, additional tokens *hurt* accuracy via overthinking (Chen et al. 2024, Chapter 6). On problems beyond a model's capability, more compute does not close the gap.

**Better mental model.** The scaling law is a *Pareto frontier averaged over a distribution*. Pick a strategy (sequential, self-consistency, search) calibrated to the difficulty of *this* problem.

**Downstream consequence.** Production systems should condition chain length on estimated difficulty (Yang et al. 2025, "Thinking-Optimal Scaling") rather than emitting fixed-length chains.

---

## 3. "o1 does MCTS at inference."

**The misconception.** o1's long chains and "aha moments" prove it is running Monte-Carlo Tree Search over CoT at inference time.

**Why it's misleading.** This is community speculation that propagated as fact. There is no published methodology disclosure from OpenAI confirming MCTS. More importantly: DeepSeek-R1 reproduces o1-class performance via *pure RLVR with no inference-time search*. If MCTS were necessary, R1 should not have worked.

**Better mental model.** The aha-moment behavior is consistent with the policy having *internalized* search-like behavior via RL. Explicit MCTS may or may not be in the inference loop of any specific frontier model; we cannot know from public information.

**Downstream consequence.** If you are designing an open-source reasoner, do not assume external MCTS infrastructure is required.

---

## 4. "RL gives the model new reasoning capabilities."

**The misconception.** RLVR training teaches the model to reason. Before RL it cannot; after RL it can.

**Why it's misleading.** R1-Zero starts from a base model with no SFT and reaches strong reasoning capability via RL alone. If RL were teaching new computations, the base model could not have supplied the trajectories the policy gradient amplifies — it had to *already* be putting non-trivial probability mass on correct reasoning paths.

**Better mental model.** RLVR is *elicitation* of latent capability, not creation of new capability. It re-shapes the policy distribution toward correct-reasoning trajectories that the base model could already sample (rarely).

**Downstream consequence.** The base model's quality is rate-limiting. Better RL on a weaker base buys less than the same RL on a stronger base.

---

## 5. "Chain-of-thought is solved — every model does it well now."

**The misconception.** CoT is universally beneficial and modern models handle it correctly across tasks.

**Why it's misleading.** Sprague et al. (2024) meta-analyzed 100+ CoT-vs-direct comparisons. CoT helps almost exclusively on math and symbolic tasks. On commonsense and factual tasks the gain is small or zero, sometimes negative. Dziri et al. (2023) show compositional gaps that persist even with CoT.

**Better mental model.** CoT is a tool with a narrow zone of effectiveness: tasks where serial compute is the bottleneck. Outside that zone, it is overhead.

**Downstream consequence.** Don't enable extended thinking on tasks the model already handles well — you pay latency and risk overthinking with no accuracy benefit.

---

## 6. "AIME is solved."

**The misconception.** Frontier reasoners score 80–90% on AIME 2024. Math reasoning is essentially solved.

**Why it's misleading.** AIME problems and their solutions are widely available on the internet pre-2024. Contamination is real and largely uncharacterized. FrontierMath, which is designed to be contamination-resistant, sits at single-digit-to-low-teens percent for top reasoners.

**Better mental model.** AIME-24 is largely *memorized* by frontier models. The underlying capability is better assessed on contamination-controlled benchmarks (LiveCodeBench, FrontierMath, ARC-AGI-3, new HLE additions).

**Downstream consequence.** Don't make capability claims on AIME alone. Pair with at least one contamination-controlled benchmark.

---

## 7. "The chain-of-thought tells you what the model did."

**The misconception.** If a model emits a chain of thought leading to answer A, the chain represents the model's reasoning process for A.

**Why it's misleading.** Turpin et al. (2023) and Lanham et al. (2023) both demonstrated that the chain can be unfaithful — the model's answer is driven by considerations not present in the chain. Anthropic's 2025 paper extends this to RL-trained reasoners.

**Better mental model.** A chain is the *visible part* of the policy's behavior. The actual computation involves residual streams and circuits whose contents the chain does not necessarily expose.

**Downstream consequence.** Debug-by-reading-the-chain is a weak signal. For high-stakes use, test conclusions under perturbation rather than reading derivations.

---

## 8. "Search and RL are alternatives. Pick one."

**The misconception.** You either build a tree-search system or you do RL. They compete.

**Why it's misleading.** R1 shows pure RL absorbs much of what tree search did at inference; AlphaProof shows that on tasks with formal verifiers, explicit search still dominates. The two are *complementary* — search helps on tasks the RL training didn't cover; RL replaces search where it has been trained against the right reward signal.

**Better mental model.** RL trains the policy to *sample* correct paths in-distribution. Search is the *backup* for paths outside the RL training distribution. Allocate compute between them by where your task lives.

**Downstream consequence.** Theorem proving, formal-game search, and novel-domain problems should still budget for explicit search. Math contest problems in-distribution to R1 training likely don't.

---

## 9. "GRPO is the only algorithm that works for reasoning RL."

**The misconception.** R1 used GRPO; therefore GRPO is the right algorithm for reasoning.

**Why it's misleading.** GRPO is the *first* algorithm that worked at frontier scale, in part because DeepSeek had infrastructure for it. RLOO, REINFORCE++, and plain REINFORCE with smart baselines all reach comparable results on the open reasoning benchmarks. GRPO is convenient (no value head); not provably best.

**Better mental model.** The choice of RL algorithm matters less than the reward signal quality, the base model strength, and the training stability tricks (KL targeting, advantage normalization).

**Downstream consequence.** Don't get fixated on GRPO when implementing. Pick what your infrastructure supports.

---

## 10. "PRMs are universally better than ORMs."

**The misconception.** Lightman et al. (2023) showed PRMs beat ORMs; therefore always use PRMs.

**Why it's misleading.** The Lightman result is at a fixed *label* budget. At fixed *total* training cost (labels + compute + engineering), ORMs are sometimes competitive because they need cheaper labels. Math-Shepherd-style automatic PRMs close the gap but introduce label noise. The 2024 Zhang et al. "lessons learned" paper documents PRM-specific failure modes.

**Better mental model.** PRM > ORM when step-level labels are tractable and noise is controlled. Otherwise the choice is genuinely empirical.

**Downstream consequence.** Don't assume PRMs will work out of the box on your domain. Profile the labeling pipeline before committing.

---

## 11. "Closed-model headline numbers represent the field's state of the art."

**The misconception.** When OpenAI / Anthropic / Google announce a number, that number defines what is possible.

**Why it's misleading.** Closed-model numbers are vendor-reported. They are primary-source claims (the lab observed something) but they are not *independently verified evidence*. Several have failed to reproduce under third-party scrutiny when models or methodology became available later.

**Better mental model.** Closed-model numbers are upper-bound *claims*. Treat them as starting points for hypothesis, not conclusions.

**Downstream consequence.** When citing in a paper or argument, prefer open-model verified numbers. Flag closed-model numbers as such.

---

## 12. "Distilled R1 models are themselves reasoning models."

**The misconception.** `DeepSeek-R1-Distill-Qwen-7B` is "a 7B reasoning model".

**Why it's misleading.** Distilled R1 models are *students trained on R1's outputs*. They are not themselves RL-trained. They reproduce some of R1's behaviors via SFT on R1's chains, which is closer to imitation than to capability.

**Better mental model.** R1-Distill-X is "a 7B model that imitates R1's chain-shape." It is much cheaper than R1 to run, but it doesn't always reach the same correctness.

**Downstream consequence.** Don't generalize from a distilled model's behavior to "what reasoning models do." Use the actual RL-trained model when investigating mechanism.

---

## What to take away

Most of these misconceptions share a common shape: **a finding becomes a slogan; the slogan loses the conditions under which the finding holds; the slogan propagates**. The corrective in each case is to restore the conditions.

If you find yourself about to make a confident claim about reasoning models, test it against this list first.

---

*Filed 2026-05-14. Updates planned as new misconceptions emerge — there is always a new one.*
