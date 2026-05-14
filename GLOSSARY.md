# Glossary

Working vocabulary of the reasoning-model literature, c. 2026. Where multiple definitions are in circulation, the most common usage is given first, with variants noted.

Entries are roughly grouped: **training**, **inference**, **evaluation**, **theoretical constructs**, **failure modes**.

---

## Training

**RLHF** — Reinforcement Learning from Human Feedback. Train a reward model on human preference comparisons, then use PPO (or DPO, or a relative) to maximize reward. *The* technique behind ChatGPT-era alignment. For reasoning, often replaced by RLVR.

**RLVR** — Reinforcement Learning from Verifiable Rewards. A reward signal generated from a programmatic checker (math answer match, code unit tests pass) rather than a learned reward model. Used in R1, Tulu 3, OpenAI's reported o1 training.

**RLAIF** — Reinforcement Learning from AI Feedback. Reward model is replaced or distilled from an LLM-as-judge. Used as a fallback when human labels are scarce; debated for reasoning training.

**GRPO** — Group Relative Policy Optimization. The PPO variant used by DeepSeek (introduced in the DeepSeekMath paper, used at scale in R1). Computes advantages as group-relative normalizations over multiple completions of the same prompt, avoiding the need for a learned value function. Light-weight enough that R1-Zero ran without supervised CoT seeding.

**DPO** — Direct Preference Optimization. A closed-form alternative to RLHF that learns directly from pairwise preferences without an explicit reward model. Less common for reasoning RL because the verifiable-reward setting fits naturally into policy-gradient methods.

**PPO** — Proximal Policy Optimization. The standard RL algorithm for LLM training pre-2025; trust-region with a clipped objective. Largely displaced by GRPO and simpler policy-gradient variants for reasoning.

**REINFORCE / REINFORCE++** — The classical Monte-Carlo policy-gradient algorithm. Several 2024–2025 reasoning RL papers (e.g. some open-source R1 reproductions) use plain REINFORCE with variance reduction tricks and report comparable results to GRPO at lower implementation complexity.

**R1-Zero** — Trained by RL from a base model with no supervised fine-tuning. Demonstrated by DeepSeek to produce a strong reasoner despite the reasoning behavior appearing without any CoT demonstrations in the loss.

**R1** — R1-Zero followed by a SFT-then-RL refinement pipeline to fix readability and language-mixing issues that R1-Zero exhibited.

**Cold start data** — SFT-style examples used to initialize an RL run, distinct from preference comparisons or reward data. For R1, "cold start" meant a few thousand high-quality CoT demonstrations curated for tone before the main RL.

**Distillation (of reasoning)** — Training a smaller student model on chains-of-thought produced by a larger reasoning teacher (e.g. R1-Distill-Qwen-7B). Empirically more effective per parameter than running RLVR directly on the small model.

**ORM** — Outcome Reward Model. A verifier that scores entire CoT trajectories by their final-answer correctness. Cheaper to label but lower-signal than a PRM.

**PRM** — Process Reward Model. A verifier that scores each intermediate step. Per Lightman et al. (2023), PRMs train more effective verifiers than ORMs even when the same total label budget is spent. Labeling PRMs is expensive; AutoPRMs use a tree-search shortcut.

**AutoPRM / Math-Shepherd** — A heuristic that assigns step-level labels by Monte-Carlo rollout from each step: a step is "good" if the majority of rollouts from it reach the correct final answer.

**Verifier-free RL** — RL using only the binary final-answer correctness as reward, no learned verifier in the loop. R1-Zero is the canonical example.

**SFT** — Supervised Fine-Tuning. Cross-entropy training on (prompt, completion) pairs. For reasoning, SFT alone is weaker than SFT+RL but is a common precursor.

---

## Inference

**CoT** — Chain of Thought. The string of intermediate tokens between question and final answer.

**Scratchpad** — Original (Nye et al. 2021) name for intermediate-token reasoning. CoT and scratchpad are interchangeable in modern usage; scratchpad survives in some learnability-theory literature.

**Zero-shot CoT** — Eliciting CoT without exemplars, typically with a prompt like "Let's think step by step" (Kojima et al. 2022).

**Few-shot CoT** — Eliciting CoT by including worked examples in the prompt (Wei et al. 2022).

**Self-consistency** — Sample K chains independently, take the majority-vote answer (Wang et al. 2022). Cheap, effective, no verifier needed.

**Best-of-N** — Sample N chains, score each with a verifier, take the highest-scoring. Strictly stronger than self-consistency when the verifier is informative, weaker when it is not.

**Test-time compute** — Total inference-time FLOPs (or tokens, as a proxy) spent on a single question, including any sampling, search, and verification.

**Test-time scaling law** — The empirical regularity that accuracy on reasoning tasks grows roughly log-linearly with inference-time compute, up to a task-dependent saturation. Different acceleration strategies (BoN, self-consistency, search) have different exponents.

**Budget forcing / token budget** — Capping the number of tokens a model may emit before being forced to answer. Used in s1 (Muennighoff et al. 2025) to study and improve the test-time scaling curve.

**Refusal-to-think / refusal-to-stop** — Two complementary failure modes. *Refusal-to-think*: a reasoning model emits a perfunctory chain on easy tasks. *Refusal-to-stop*: a reasoning model emits very long chains and exhausts its token budget without committing to an answer.

**MCTS over CoT** — Monte-Carlo Tree Search where nodes are partial CoT prefixes and edges are next-token (or next-step) extensions. Used in some RL-trained reasoners and post-training search systems.

**Tree of Thoughts (ToT)** — Yao et al. (2023). Explicit tree-search over CoT branches with a heuristic value function (often the model rating its own partial chains). Generalizes self-consistency to tree topologies.

**Graph of Thoughts (GoT)** — Besta et al. (2023). Generalizes ToT to DAGs with explicit aggregation operators.

**Recursive self-aggregation** — Venkatraman et al. (2025) and follow-ups. An inference-time loop that samples multiple chains, summarizes them into a new prompt, and recurses; trades depth for branching.

**Speculative decoding** — Use a small draft model to propose tokens that the large model verifies in parallel. Orthogonal to reasoning but relevant: longer CoT shifts the inference cost balance.

**Speculative reasoning / speculative search** — Apply the same draft-and-verify idea at the level of *reasoning steps* rather than tokens.

---

## Evaluation

**AIME** — American Invitational Mathematics Examination. 15-question, integer-answer math contest, held annually (Feb + March). AIME-24, AIME-25, AIME-26 are the canonical reasoning-model leaderboards in 2025–2026.

**MATH-500** — A 500-problem subset of the MATH dataset (Hendrycks et al. 2021) used by Lightman et al. (2023) and now near-universal for reasoning-model evaluation. Saturating in mid-2025.

**GSM8K** — Grade-school math word problems (Cobbe et al. 2021). Largely saturated by 2024 reasoning models; still cited as a calibration baseline.

**HumanEval** — Python function-completion benchmark (Chen et al. 2021). Heavily saturated; superseded by LiveCodeBench and SWE-bench Verified for serious comparison.

**LiveCodeBench** — Periodically refreshed coding benchmark drawn from contests after a cutoff date, to mitigate train-test contamination.

**SWE-bench Verified** — A human-validated subset of SWE-bench (Jimenez et al. 2024) — real GitHub issues with a known passing patch. Reasoning models post substantial gains here over non-reasoning siblings.

**FrontierMath** — Epoch AI benchmark of original research-level math problems, designed to be unsolvable by current LLMs and humans-without-domain-knowledge. As of early 2026, single-digit percent accuracy even for frontier reasoners.

**ARC-AGI-2 / ARC-AGI-3** — Chollet's abstraction-and-reasoning benchmarks. ARC-AGI-2 launched late 2024 with a Kaggle prize; ARC-AGI-3 launched 2026-03-25 with a new generation-and-search structure. Often cited as the "true reasoning" benchmark; critics note this is itself a contested framing.

**HLE** — Humanity's Last Exam. Multi-domain expert-level benchmark introduced late 2024 by the Center for AI Safety / Scale; designed to remain hard even after benchmark saturation elsewhere.

**GPQA Diamond** — Graduate-level Google-Proof Q&A (Rein et al. 2023). 200-question expert-validated subset; the standard "PhD-level science" benchmark.

**Codeforces Elo** — Competitive-programming rating, used as a continuous-valued reasoning benchmark by OpenAI in their o1/o3 reports.

**Pass@k** — Probability that *at least one of k* sampled completions is correct. The standard coding metric; relates to but distinct from best-of-N (which requires a verifier).

---

## Theoretical constructs

**TC0** — Constant-depth threshold circuits with polynomial size. Where log-precision transformers in a single forward pass are believed to live (Merrill & Sabharwal 2023). Many "hard reasoning" problems are believed to lie outside TC0, motivating CoT as a way to escape it.

**Compute-depth equivalence** — The intuition that T tokens of CoT extends a constant-depth transformer to roughly T-step serial computation. Made precise by Li et al. (2024) and Merrill & Sabharwal (2024).

**Implicit / amortized search** — The hypothesis that RL-trained reasoners encode a search procedure into their sampling distribution, so that token-by-token greedy decoding mimics what an external search would do explicitly.

**Bayesian posterior over thoughts** — The hypothesis that CoT generation is implicit posterior inference over a latent "solution program," extending the ICL-as-Bayes account (Xie et al. 2022) to multi-step.

**Program synthesis interpretation** — The hypothesis that a CoT is the source code of a program the model is "compiling" to its final answer. Implies non-CoT inference is interpreting compiled artifacts of similar programs seen at training time.

**Faithful CoT** — A CoT is *faithful* iff the visible chain is causally responsible for the model's answer. Operationalized via truncation, paraphrase, and step-injection tests (Lanham et al. 2023).

**Post-hoc rationalization** — A CoT that is *unfaithful*: the model answers via a route other than the visible chain, then emits the chain as a plausible-looking justification. Documented to occur frequently in non-reasoning models (Turpin et al. 2023); contested whether reasoning-RL fixes it.

**Sandbagging** — A model deliberately performing worse than its capability would predict, typically to avoid demonstrating a capability it has been told (or has inferred it should) hide. Distinct from refusal.

**Alignment faking** — A model behaving as if aligned during evaluation but differently under (perceived) deployment conditions. Distinct from sandbagging in motivation.

---

## Failure modes

**Overthinking** — Long CoTs hurting accuracy on tasks where shorter chains suffice. Coined by Chen et al. (2024); the canonical example is "2 + 3 = ?" eliciting a 200-token chain.

**Token explosion** — A reasoning model emitting tens of thousands of tokens of self-doubt and re-derivation without committing to an answer. A practical resource-cost issue.

**Snowball error** — An early hallucinated intermediate step that subsequent steps confidently build on. Theoretical mechanism described in Bachmann & Nagarajan (2024).

**Clever Hans cheat** — A teacher-forced learner exploiting next-token correlations that don't reflect the target computation (Bachmann & Nagarajan 2024). Argues against naive autoregressive training as a path to robust reasoning.

**Language mixing** — A reasoning model switching between languages mid-chain. Documented in R1-Zero; partially fixed by R1's SFT pass.

**Reward hacking (in RLVR)** — The policy finds a reward shortcut that the verifier accepts. For math, often by emitting a final answer that matches a substring of the chain rather than the result of the computation. Mitigated by stricter answer parsers.

**Mode collapse (in RL)** — The policy concentrates on a narrow distribution of solutions, losing the ability to explore. Partially mitigated by GRPO's group-relative normalization.

---

*Last updated: 2026-05-14. Pull requests welcome for missing terms — see [CONTRIBUTING.md](CONTRIBUTING.md).*
