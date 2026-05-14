# How to read a reasoning-model paper

*Essay. Updated 2026-05-14. Operational guide, not a survey.*

The reasoning-model literature is producing 30+ relevant papers per week as of mid-2026. Most are noise; some are signal. This essay is a checklist for triaging, then reading deeply when warranted.

---

## The 60-second triage

Open the abstract and the first figure. Ask:

1. **Is there a mechanism claim, or just a benchmark number?** A paper that says "we improve MATH-500 by 2 points using [X]" without a mechanism is a leaderboard entry. Leaderboard entries aren't worth more than a glance unless you care about that exact benchmark.

2. **Is the base model named?** If a paper reports reasoning numbers without specifying the exact base model and version, treat it as preliminary. Most of the 2025–2026 noise is on this axis.

3. **Is the reward / verifier described, or is it a black box?** RLVR papers without specifics about the reward function are unfalsifiable.

4. **Is the comparison fair?** Look for: same base, same compute, same prompt format. If any of these differ from the comparison baseline, the claim is weakened proportionally.

5. **Is there an open-source release?** If yes, the paper is reproducible-in-principle and the bar is higher. If no, treat the numbers as upper bounds on the actual capability.

If at least three of these are "yes" with specifics, read the paper. Otherwise skim the conclusion and move on.

---

## The 10-minute deep read

For papers that pass triage, the actually-useful sections in order:

### 1. Methodology section, especially the *training data* sub-section

Most of the unstated assumptions live here. Look for:

- **Pretraining data composition.** Is it a public mix or proprietary?
- **Reasoning training data.** Is it synthetic, distilled from another model, or human-authored?
- **Cold-start SFT details.** If the recipe involves SFT before RL, the SFT data is often the load-bearing variable.

### 2. RL details (if applicable)

- **Algorithm**: PPO, GRPO, REINFORCE++, or some variant. The choice usually doesn't matter much; the *implementation details* do.
- **Reward**: exact form, including format-bonus terms. Reward hacking lives here.
- **KL coefficient**: a tuning knob whose value affects everything.
- **Number of training steps and total token budget**.

### 3. Evaluation conditions

- **pass@1 vs cons@k vs pass@k**: state which.
- **Tool use**: yes, no, or selectively-enabled.
- **Prompt format**: identical to baseline or bespoke for the new model.
- **Temperature**: 0 (deterministic), > 0 (samples averaged), or both reported.

### 4. The *failure cases* section, if there is one

This is often the most informative part of the paper and the most-skipped. Honest failure-case analysis distinguishes serious work from leaderboard work.

### 5. Comparisons table

Read the *footnotes* of the comparison table before the numbers. The footnotes often disclose conditions (e.g., "for [competitor], we use *prompts from* [reference]") that change interpretation.

---

## Red flags

A paper that exhibits any of these warrants extra skepticism:

- **"o1-style"** in the title without specifying which o1 capability is reproduced.
- **No specification of test conditions** when reporting headline numbers.
- **Comparing against a baseline with different compute budget** without normalization.
- **Closed-model comparisons** based on screenshot evidence rather than reproducible inference.
- **CoT prompted strongly differently** for the proposed method vs baseline.
- **Eval set overlap with the training set** unaddressed.
- **Strong claims about emergent behaviors** at the scale of the paper's experiments, without controlled smaller-scale comparisons.

A paper without any of these is doing the field a service even if its result is small.

---

## What to look for in different paper types

### A new RLVR recipe

- Strength of the base model used.
- Whether the recipe works on a *weaker* base (most papers report only on a strong base).
- Compute relative to comparable open recipes (Tulu 3, SimpleRL, R1-derivatives).
- Honest reward-hacking analysis.

### A new test-time scaling result

- The compute axis: tokens, FLOPs, or sample count.
- The verifier setup. Same verifier or comparable across strategies?
- Whether the scaling holds for non-math tasks.

### A new faithfulness or interpretability paper

- The Lanham test battery or equivalent — does the paper run the standard tests?
- Is the finding model-specific or general across families?
- Is the empirical setup adversarial (worst-case) or distributional (average-case)?

### A new search-at-inference paper

- The value function source. Trained verifier or model self-rating?
- The compute comparison. Search-N vs sampling-N at the *same* compute, or just at the same N?
- Whether the search adds value *over* an RL-trained policy, not just over a base.

### A new theoretical paper

- Is it expressivity-only, learnability-only, or end-to-end?
- The assumptions (precision, attention type, position encodings) — these often hide the strength of the result.
- Whether the formal result is matched to a real model class (most are not).

### A benchmark paper

- Contamination analysis. Are the problems verifiably new?
- Difficulty calibration. Is "hard" defined relative to human performance, model performance, or absolutely?
- Refresh schedule. A static benchmark saturates; living ones don't.

---

## How to read closed-source announcements

A closed-source announcement isn't a paper but the same triage applies, with adjustments.

1. Are the test conditions specified in the announcement, or only in a follow-up technical report?
2. Has the company previously revised numbers downward post-announcement?
3. Is the methodology described, even at a high level?
4. Is the model accessible for independent evaluation (API access counts; weights not required)?
5. Are the headline benchmarks chosen against the company's prior weaknesses or its prior strengths?

Treat closed-source announcements as *priors* about what is possible. They tell you the upper bound the lab is willing to claim. They are usually higher than the verified post-release reality.

---

## What changed in the reasoning-model era

A few things you don't have to do anymore that you used to:

- **Prompt-engineer for CoT elicitation**. Reasoning models emit chains by default.
- **Worry about temperature for chain quality on math.** RLVR has stabilized the relevant regimes.
- **Argue about whether CoT is a real technique.** It is. The argument is about what *kind* of technique.

A few things you have to do more carefully than before:

- **Disambiguate pass@1 vs cons@k.** Different by-default in different communities.
- **Specify the tool harness on SWE-bench-class benchmarks.** Headline numbers vary by 20+ points.
- **Flag closed-vs-open at every claim.** The 2024–2026 reasoning literature blurred this; some normalization is needed.
- **Read the methodology before believing the headline.** Always true but never more important than now.

---

## When the paper is good — the second-day read

A paper that passes triage and deep-read deserves a second pass:

1. Re-read the limitations section. (Authors are usually more honest there than in the abstract.)
2. Run a sanity check on a 50-problem slice if the model and code are open.
3. Check the cited prior work. A paper that mis-cites prior work is often mis-engaging with the substance.
4. Look at the GitHub issues on the released code. The first 20 issues after release are usually the most informative debug.
5. If the paper makes a strong claim, check whether the strongest possible counter-example would actually disprove it. If yes, search for the counter-example.

---

## What this list helps with

For papers in our scope, the chapters and essays already pass triage and at least one deep-read. The annotations tell you the mechanism, not just the result. The [WANTED.md](../WANTED.md) flags gaps where the literature is incomplete. Use the list as a triage shortcut, not a substitute for reading.

---

*Filed 2026-05-14. For corrections or additional patterns, PR.*
