# Reasoning and mechanistic interpretability.

*Essay. Updated 2026-05-14. Short, because the field is young.*

---

We have a paradigm shift in LLM capability (the reasoning-model era). We have a sub-field with a track record of explaining LLM behavior at circuit level (mechanistic interpretability). They have barely connected.

This is a missed opportunity and a stated open problem in this repo's chapters 1, 4, 5, 7, and 8.

## What mech-interp has done well on non-reasoning models

By 2024, mechanistic interpretability had produced:

- **Induction heads** (Olsson et al. 2022) — the circuit responsible for basic in-context learning, with a sharp formation-time signature during pretraining.
- **Indirect object identification** (Wang et al. 2022) — a multi-component circuit decomposition for a specific syntactic task.
- **Sparse autoencoders for feature extraction** (Bricken et al., Cunningham et al. 2023–2024) — a methodology for identifying interpretable features in intermediate activations.
- **Compositional understanding of factual recall** (Meng et al. 2022; ROME / MEMIT) — circuits for factual lookup, with editing methodology.
- **The "thinking out loud" sparse-autoencoder line on Claude / GPT-class models** (2024) — features that activate on specific reasoning behaviors.

These are real wins. They give a research methodology and a vocabulary.

## What mech-interp has *not* done on reasoning models

As of mid-2026, we lack:

1. **A circuit-level account of long CoT generation.** Which heads carry "currently exploring," "currently committing," "noticing contradiction"? Mostly unknown.
2. **A mechanistic story for R1-Zero "aha moments."** The behavior is well-documented; the internal correlate is not.
3. **A circuit-level test of CoT faithfulness.** We can measure faithfulness behaviorally (Lanham et al.); we can't yet certify it mechanistically.
4. **An understanding of how RLVR reshapes the policy.** Pre-RL vs post-RL activation diffing has been done at coarse scale; the circuit-level changes that produce reasoning are not isolated.
5. **A mech-interp story for search-internalization** (the essay [Search vs RL](search-vs-rl-the-deep-tension.md) raised this). If RL-trained reasoners internalize search, the circuit should show it.

Some of this is in flight — there are 2026 preprints starting to address points 1, 2, 4 — but the corpus is small relative to the scientific importance.

## Why the gap?

A few candidate reasons:

- **Reasoning models are hard to instrument.** They emit very long sequences. The activation budget for a single problem is much larger than for ICL examples or single-token-completion experiments. Tooling has lagged.
- **Open weights came late.** Until DeepSeek-R1 (Jan 2025), the best reasoning models were closed. Mech-interp needs activation access.
- **Mech-interp researchers were busy** with circuits in non-reasoning settings (induction, IOI, factual recall). The reasoning paradigm shift caught the community in the middle of those projects.
- **Theory of what to look for is underdeveloped.** "Find the reasoning circuits" is a vaguer search than "find the induction circuits." The latter has a structural prediction (one head learns the pattern, another head copies); the former lacks one.

## What the connection could deliver

If reasoning-model mech-interp gets traction over the next 2–3 years:

1. **Faithful-CoT certification on tractable subdomains.** A method to verify, at the circuit level, that on a class of inputs the chain is causally responsible for the answer.
2. **Mechanistic detection of reward hacking.** If a chain emerges from a reward-gaming circuit (recognizing the verifier's surface features rather than solving the problem), this should be visible internally.
3. **A circuit-level story for the search-vs-RL question.** Settle the open debate.
4. **Better targeted interventions.** Activation patching at the right circuit beats prompt-engineering for steering reasoning behavior.
5. **A path to mechanistic alignment audits** for reasoning models — currently essentially impossible.

## What's likely to move first

My guess for the order of empirical wins:

1. **Identifying the "self-correction" circuit** — the structure that emits "wait, let me reconsider" tokens. This is the most behaviorally distinct reasoning-model phenomenon and should have a clean correlate.
2. **Sparse autoencoder features for reasoning-specific phenomena** (case analysis, equation manipulation, premise tracking). The Anthropic SAE line of work scales naturally to this.
3. **Activation differences between R1-Zero and its base** at specific reasoning-step boundaries. Direct, instrumented.

After those: the harder problems (search-internalization, faithful-CoT certification, reward-hacking detection) follow.

## What this repo will do

We won't compete with mech-interp groups. We will:

- Track reasoning-model mech-interp papers as they appear, in [Chapter 7](../chapters/07-faithfulness-of-reasoning.md) (where faithfulness mech-interp lives) and a small Chapter 1 cross-reference (where CoT mech-interp lives).
- Maintain an [open-problems list](../README.md#open-problems) — currently scattered across chapters — that highlights the mech-interp gaps.
- Push back on essays / posts that *speculate* about reasoning-model internals without evidence. The "o1 does MCTS" line is the recurring example.

---

*Filed: 2026-05-14. Short because the field is short. Updates planned as the mech-interp / reasoning-model gap closes.*
