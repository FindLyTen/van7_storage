# VAN7 Storage

Public catalog of **734 tools, scripts, skills and templates** for AI agents and automation.

## Why
Any AI (Claude, GPT, Gemini, local agents) can read this catalog **without connectors, tokens or logins** — just fetch the raw file. Built to be the "first rule" lookup before writing anything from scratch.

## Structure
- `data.json` — machine-readable catalog: name, tags, description, links for every item
- `skills/` — canonical AI skills:
  - `ecc.md` — experienced-developer coding style
  - `impeccable.md` — polished UI guidelines
  - `ponytail.md` — keep-it-simple principle
- `CONTEXT.md` — origin notes

## Usage
**For AI agents:** before creating any tool/skill/template — fetch `data.json`, search by keywords, reuse what exists. Do not duplicate.

**For humans:** browse the catalog on GitHub, every entry has a link to source or docs.

## Integration
Used as the primary tool lookup across a multi-server infrastructure (2 VPS, opencode agents). Referenced in project instructions as the "first rule": search here before building.

Raw catalog URL:
```
https://raw.githubusercontent.com/FindLyTen/van7_storage/main/data.json
```
