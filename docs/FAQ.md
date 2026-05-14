# FAQ

Common questions about the list, the scope, and the reasoning-model field. Answers reflect the curator position; reasonable disagreement is welcome via issue.

---

### Why a separate list from `awesome-llm-reasoning-foundations`?

Different methodologies, different evidence standards, different reader expectations. The sister list is formal-theorems-about-transformers (expressivity, circuit complexity, learnability bounds). This list is *empirical-and-mechanistic-theory of why reasoning models work* (test-time compute, RL recipes, faithfulness empirics, scaling phenomena).

A theorem-prover entering the sister list shouldn't have to wade through DeepSeek-R1 reverse-engineering. A practitioner choosing between best-of-N and self-consistency shouldn't have to wade through TC0 separations. Splitting respects both audiences. The [boundary cases](../DECISIONS.md#2026-05-14--scope-split-with-the-sister-list) are explicitly enumerated.

### Why not include CoT prompting tricks?

Three reasons.

1. There are excellent applied lists already; we link to [atfortes/Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) and others.
2. Prompt-engineering tricks rarely correspond to a *mechanism* claim. Without a mechanism, an entry doesn't serve this list's purpose.
3. The trick literature ages poorly; mechanism-level claims don't.

If your trick paper *does* make a mechanism claim, it may be in scope — open an issue.

### Why don't you list o1 / o3 numbers as canonical?

Closed-model headline numbers are vendor-reported. They are *primary sources* in the technical sense — the lab that made the model is telling you what they observed — but they aren't *independently verified evidence* in the way an open-weights benchmark run is. We list them with `(closed-model, vendor-reported)` and note where independent reproductions exist (e.g. DeepSeek-R1, s1).

This isn't anti-OpenAI/Anthropic — it's a consistent epistemic stance. We'd do the same for any organization shipping closed models. See [DECISIONS.md](../DECISIONS.md).

### Is this list pro-open-source?

We are pro-evidence. Open-weight evidence is, by construction, more verifiable than closed-weight evidence; in practice this means the list cites a lot of open work. But the closed labs ship the frontier of capabilities and we cite their writeups where they have methodological content. The asymmetry in evidence-quality is real, and we surface it.

### Why are the chapter annotations longer than usual for an awesome-list?

Because mechanism-level claims need elaboration. A one-line "this paper proposes X for Y" annotation is fine for "this paper exists" but useless for "this paper *changes our understanding of Z*." We're playing the second game.

### How do I cite this list?

Use the [CITATION.cff](../CITATION.cff) file. Or if you prefer manual BibTeX, see [bibtex.md](bibtex.md) for an export of the most-cited papers plus a list entry.

### Is reasoning solved?

No. Frontier reasoners are saturating math benchmarks (MATH-500, AIME 2024 at the top tier), making progress on code benchmarks (SWE-bench Verified), and barely scratching FrontierMath / ARC-AGI-3 / HLE. The "solved" framing is misleading; specific benchmark families have been solved or near-solved; the underlying capability is open.

The deeper question — whether reasoning models reason in any psychologically interesting sense — depends on the definition; the [faithfulness chapter](../chapters/07-faithfulness-of-reasoning.md) is where to start.

### Why doesn't the tracker have more numbers?

Because the bar is "primary-source, verified, with reproducible test conditions." Every cell on the tracker required a real source read with the methodology checked. Cells we couldn't verify cleanly are marked ⏳ or annotated; they go onto [WANTED.md](../WANTED.md) for community help.

### What about reasoning + tool use?

Intentionally out of scope. Tool-augmented reasoning is its own sub-field with its own dynamics (agent frameworks, sandboxed execution, retrieval). We touch it where it bears on the *mechanism* of reasoning (e.g. AlphaProof's formal verifier in Chapter 4), and otherwise refer to dedicated lists.

### What about multi-modal reasoning?

Same answer: out of scope unless the paper is fundamentally about text-CoT mechanism with images as data.

### What about the safety / alignment angle?

In scope where it bears on the mechanism (faithfulness, sandbagging, alignment faking). Not in scope as a general alignment list. See [Chapter 7](../chapters/07-faithfulness-of-reasoning.md).

### Why are some sections short?

Because the field is short. Where the literature is sparse (mech-interp of long CoTs, faithfulness scaling laws, theoretical unification frameworks), the right thing to do is say so and put the gap on [WANTED.md](../WANTED.md), not fill space with low-quality entries.

### Why is the open-vs-closed flag so important?

Because, in the reasoning-model era specifically, vendor-reported numbers have repeatedly turned out to be load-bearing for downstream community claims and have *not* been independently reproduced (or have been reproduced to lower-than-stated). The flag is a 60-second epistemic hygiene cost; the lack-of-flag is a months-of-confusion cost.

### How often is the list updated?

Aim is *event-driven for content* (new chapter additions when a paper shifts the field) plus *monthly for the tracker*. See the [launch playbook](../_internal/launch_playbook.md) — public when the list goes public.

### Can I add my own paper?

If it makes a mechanism claim and is verifiable per [CONTRIBUTING.md](../CONTRIBUTING.md), yes — open a PR. Self-promotion is fine when the paper meets the bar. Do disclose in the PR if you are an author; we do not penalize, but we appreciate the transparency.

### How do I disagree with a curator position?

Open an issue. Argued disagreements that update us are *exactly* what makes the list useful; "you've hedged the faithfulness debate" is a critique we'd want to hear. Tone-policing is not a thing here.

---

*Updated 2026-05-14. PR new entries to this FAQ if you have a question the list community keeps asking.*
