<p align="center">
  <img src="assets/hero.png" alt="Cold Message Writer" width="100%">
</p>

<h1 align="center">Cold Message Writer</h1>

<p align="center">
  A Claude skill for writing cold outreach that actually gets replies — on email, LinkedIn, or X DMs.
</p>

<p align="center">
  <a href="#install"><img alt="Install" src="https://img.shields.io/badge/install-claude.ai%20%2B%20Claude%20Code-d97757"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue"></a>
  <img alt="No code, just instructions" src="https://img.shields.io/badge/code-none%2C%20readable-success">
</p>

---

## Why this exists

Almost every cold message fails for the same reason: it's about the sender, and it reads like it was pasted into a list of 500 names. Title, company, CV, "we just shipped X" — the reader filters that out in two seconds because they get dozens of them a day.

The entire job of a cold message is to make **one real person feel like you wrote it only for them.** Get that right and the reply takes care of itself. This skill writes the opposite of the blast: short, specific, human, and easy to say yes to.

It's not a clever-words generator. It encodes the actual mechanics that get replies — making the reader feel chosen, opening with a hook about *them* not you, naming their objection before they can, making the ask weightless, proving demand with quiet specifics instead of adjectives, and sounding like a person typing between meetings rather than a polished template.

## What's inside

```
SKILL.md                        the core instructions Claude loads when the skill triggers
references/templates.md         situation playbooks, ready-to-send templates,
                                the ghost follow-up sequence, annotated real examples
dist/cold-message-writer.zip    prebuilt zip for uploading to claude.ai
```

It covers five situations end to end — **fundraising, hiring, partnerships/BD, press & podcasts, and job-seeking** — each with its own hook, proof, and ask, plus a follow-up sequence for when people ghost (which is most of the time).

## Install

This skill is plain instructions. No code runs. You can read every line before you install it.

### claude.ai (Pro, Max, Team, or Enterprise)

1. Download [`dist/cold-message-writer.zip`](dist/cold-message-writer.zip).
2. In claude.ai, open **Settings → Capabilities → Skills**. Make sure **code execution** is on.
3. Click **Upload skill** and select the zip.

That's it. Claude reads the skill automatically and uses it whenever you ask for cold outreach. Custom skills are per-user and don't sync across claude.ai, the API, and Claude Code, so install it on each surface you want it on.

### Claude Code

Clone straight into your skills folder:

```bash
git clone https://github.com/felixleezd/cold-message-writer.git ~/.claude/skills/cold-message-writer
```

Claude Code discovers it on the next session. For a project-only install, clone into `.claude/skills/` inside the project instead.

## How to use it

Just ask in plain language. The skill triggers on its own — you don't have to name it.

- *"write a cold email to a founder I'd like to work for at a seed-stage startup"*
- *"DM this investor about our round, here's the context…"*
- *"help me reach out to a podcast host about coming on the show"*
- *"follow up with someone who ghosted my first message"*

By default you get **one tight message**. Ask for options and you get a few labeled variants that take genuinely different angles (lead with the mutual vs. lead with their post), not three tones of the same thing. Ask for follow-ups and you get the full ghost sequence.

> **Bring one true hook.** The skill writes far stronger messages when you give it something real — a post they wrote, a launch they shipped, a mutual connection, a role they're hiring for. It will *not* fabricate a fake "I loved your post about X." Honest and specific beats polished and generic, every time.

## The principles it runs on

If you read nothing else, read this. These are the moves the skill applies to every draft:

- **Make them feel chosen.** "I made a short list of people I wanted in early — you're on it." Specificity is what separates *chosen* from *blasted*.
- **Open about them, not you.** The first line is the notification preview. If it starts with "I," "we," or your company, it gets rewritten.
- **Say their objection first.** "You don't know me, feel free to ignore this — but I think it's actually for you." Naming it disarms it.
- **Make the ask weightless.** Not 30 minutes. A glance. "want the 90-second version? I'll drop it right here."
- **Prove demand quietly.** "showed five people Monday, four asked in" beats "everyone loves it." Ladder every claim to its hardest specific.
- **Sound human, not polished.** Lowercase, contractions, asymmetric rhythm, one real detail. Polish is the tell of a template — and a template is exactly what the reader filters out.

## License

MIT — see [LICENSE](LICENSE). Use it, fork it, adapt it, ship your own version.

Contributions welcome. If you have a cold message that worked, or a situation the playbooks don't cover yet, open a PR.
