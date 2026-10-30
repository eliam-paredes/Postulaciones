# Upwork Proposal Writer — a Claude Skill for winning freelance proposals

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-D97757?logo=anthropic&logoColor=white)](https://www.anthropic.com/news/skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Made for Upwork](https://img.shields.io/badge/Made%20for-Upwork-6FDA44)](https://www.upwork.com)

A production [Claude Skill](https://www.anthropic.com/news/skills) that writes Upwork proposals in a specific, proven voice — trained on a corpus of proposals that actually won real jobs, not generic "AI cover letter" templates. Drop it into Claude Code or claude.ai, paste a job post, get two ready-to-send variants back in under a minute.

This repo is both a working tool and a worked example of **how to turn "write me a proposal" into a system**: a documented workflow, a voice model with graduated rules instead of a vibe, and an annotated corpus of wins instead of a pile of "best practices."

> Built and used daily by **Fahad Qaseem** — Top 1% on Upwork, 200+ projects delivered, working across brand identity, web/product design, Amazon A+ content, motion, and AI image generation. [behance.net/fahadqaseem](https://www.behance.net/fahadqaseem)

---

## Table of contents

- [What this is](#what-this-is)
- [Why it works](#why-it-works)
- [How it's built](#how-its-built)
- [Repo structure](#repo-structure)
- [Install it](#install-it)
- [Use it](#use-it)
- [The five-move structure](#the-five-move-structure)
- [Voice rules, in short](#voice-rules-in-short)
- [Before / after](#before--after)
- [Make it yours](#make-it-yours)
- [FAQ](#faq)
- [License](#license)

---

## What this is

[Claude Skills](https://www.anthropic.com/news/skills) are folders of instructions and reference material that teach Claude how to do one job really well, then load automatically when that job comes up. This skill's job: **write Upwork proposals that read like they were written by someone who already understands the client's problem**, not by someone broadcasting their own résumé.

Paste a job post into Claude (with this skill installed) and say "write a proposal," and it will:

1. Read the brief for what actually went wrong last time (every job post is a complaint in disguise)
2. Research the client — their site, listing, or storefront — for one true, specific observation nobody else will make
3. Write to a fixed five-move structure that opens on the client's problem and closes on a question, not a sign-off
4. Produce two variants — a longer process-led version and a punchy short version — so you can pick the right one for the job's size and urgency
5. Run a pre-send checklist before handing it back

## Why it works

Most "AI proposal writer" prompts produce proposals that all sound like each other — polished, generic, and instantly recognizable as copy-paste. This skill exists because that's a losing strategy on a platform where a client scans 40 applicants in six minutes.

Instead of one paragraph of "be persuasive," this skill encodes:

- **A researched voice model**, not a vibe — specific banned phrases, specific required rhythm breaks, specific grammar "violations" that read as a fast human typing rather than a template (see [`references/voice-rules.md`](references/voice-rules.md))
- **An annotated corpus of 20 proposals that actually won real jobs**, each with the exact move extracted — not hypothetical advice, but "this is the sentence that did the work, and here's why" (see [`references/winning-proposals.md`](references/winning-proposals.md))
- **A credibility system with placement rules** — which fact to lead with for which brief, and the hard rule that credentials never open a proposal (see [`references/positioning.md`](references/positioning.md))
- **A risk-reading layer for the client's Upwork profile** — spend, hire rate, verification status all change how the proposal should be pitched (see [`references/client-research.md`](references/client-research.md))

## How it's built

This skill was built the way you'd build any real system, not by writing one clever prompt:

1. **Mine a corpus of wins.** Every proposal in `references/winning-proposals.md` is one that actually got hired, pulled from real Upwork job history. Each entry is annotated with *why* it worked, not just *that* it worked.
2. **Extract the pattern, discard the noise.** Twenty wins across wildly different job types (a $30 WordPress footer fix, a print advert for a caravan brand, an AI-generated Amazon listing) converged on the same five moves. That convergence is `SKILL.md`'s workflow section.
3. **Codify the voice as rules, not adjectives.** "Sound casual and confident" is not instructable. "No exclamation points, no colons in casual copy, 3–5 rhythm breaks per proposal, cap grammar violations at 2–3" is. `references/voice-rules.md` is a tiered rulebook, tested against what actually reads as human versus what reads as trying too hard.
4. **Separate the identity layer from the workflow.** Credibility claims, portfolio links, and positioning phrases live in their own reference files (`positioning.md`, `portfolio.md`) so the workflow logic in `SKILL.md` stays reusable — swap those two files out and the rest of the system works for anyone.
5. **Ship a checklist, not just a prompt.** The final section of `SKILL.md` is a pre-send checklist Claude runs against its own output before handing it back, catching the failure modes that show up most (opening with credentials, missing the closing question, exclamation points sneaking back in).

## Repo structure

```
.
├── SKILL.md                          # Entry point: identity, workflow, voice, output format, checklist
├── references/
│   ├── winning-proposals.md          # 20 annotated real proposals that won the job
│   ├── voice-rules.md                # Banned phrases, tiered "human texture" rules, before/after rewrites
│   ├── positioning.md                # Credibility line phrasing by brief type, with placement rules
│   ├── portfolio.md                  # Portfolio links by category and when to use each
│   └── client-research.md            # What to pull from a client's site and Upwork profile before writing
└── upwork-proposal.skill             # Pre-packaged skill file — import directly, no build step
```

`SKILL.md` is the entry point Claude reads first. It's deliberately short and delegates depth to the `references/` files, which Claude only opens when the workflow calls for them — this keeps the skill fast to load and cheap to run.

## Install it

**Claude Code**

```bash
git clone https://github.com/fahadqaseem/upwork-proposal-writing-skill.git
mkdir -p ~/.claude/skills
cp -R upwork-proposal-writing-skill/SKILL.md upwork-proposal-writing-skill/references ~/.claude/skills/upwork-proposal/
```

**claude.ai**

Upload `upwork-proposal.skill` directly in Settings → Capabilities → Skills. No build step required — it's a ready-made package of the same `SKILL.md` and `references/` files in this repo.

## Use it

Paste a job post and ask for a proposal:

```
Write a proposal for this job:

[paste the full Upwork job post here]
```

Claude will research the client if it has web access, draft to the five-move structure below, and hand back two labeled variants — a process-led version for bigger or more strategic jobs, and a punchy version for small or urgent ones — ready to paste straight into Upwork.

## The five-move structure

Every proposal follows the same five moves, in this order:

1. **Open on their failure mode, in their words.** No greeting. No "I read your posting." Never open with credentials.
2. **Prove domain knowledge with one precise technical detail.** One concrete thing only someone who does this work would say.
3. **Land the credibility line — exactly one, mid-proposal.** Never the opener. Never a badge list.
4. **Kill the hiring risk.** A free sample, a mini audit, one redesigned panel — turn the hiring decision into a free look.
5. **Close with a scoped, easy-to-answer question.** Never "looking forward to hearing from you."

## Voice rules, in short

- Contractions everywhere — writing "I will" instead of "I'll" is the single loudest tell of AI-written copy
- No exclamation points, no emoji, no colons in casual copy, no em dashes
- "You" outnumbers "I" — count the pronouns before sending
- 3–5 deliberate rhythm breaks per proposal (fragments, sentences starting with *And* or *But*, one-word sentences)
- 2–3 minor, intentional grammar "violations" that read as speed, not carelessness (comma splices, dropped Oxford commas)

Full rulebook with examples: [`references/voice-rules.md`](references/voice-rules.md)

## Before / after

**Before**
> I am a professional graphic designer with over 4 years of experience.

**After**
> Ten years of this, mostly print and brand, where the file goes to press and there's no undo.

**Before**
> I can deliver high-quality work on time and within budget.

**After**
> Send me one page. I'll format it tonight, and if it's not right you've lost nothing.

More rewrites in [`references/voice-rules.md`](references/voice-rules.md).

## Make it yours

This skill ships with Fahad's identity baked into `positioning.md` and `portfolio.md`. The workflow and voice model in `SKILL.md` and `voice-rules.md` are identity-agnostic and reusable. To adapt it:

1. Rewrite `references/positioning.md` with your own credibility facts and phrasing by brief type
2. Rewrite `references/portfolio.md` with your own links, organized by category
3. Optionally add your own wins to `references/winning-proposals.md` — the value of that file scales with how specific and real the entries are
4. Leave `SKILL.md`'s workflow and `voice-rules.md` as-is, or tune the voice rules to your own register

## FAQ

**Does this only work for design/creative jobs?**
No — the five-move structure and client-research approach are used across the corpus for dev work, video editing, VA work, and copywriting, not just design. The domain-specific detail in move 2 is what adapts it per job type.

**Will this write the exact same proposal for every job?**
No. The corpus rule is explicit: steal the *move*, never the sentence. Reusing an identical proposal across clients is treated as a failure mode, not a shortcut.

**What's a Claude Skill, exactly?**
A folder of Markdown instructions and reference material that Claude loads on demand when a matching task comes up — see [Anthropic's announcement](https://www.anthropic.com/news/skills) for the full model.

## License

[MIT](LICENSE) — the workflow, voice model, and skill structure are free to reuse and adapt. Swap in your own identity and portfolio before using it to bid on jobs.
