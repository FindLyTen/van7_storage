# VAN7 Storage

Public catalog of **1215 tools, scripts, skills and templates** for AI agents and automation.

## Why
Any AI (Claude, GPT, Gemini, local agents) can read this catalog **without connectors, tokens or logins** — just fetch the raw file. Built to be the "first rule" lookup before writing anything from scratch.

## Data format
`data.json` is the single source of truth — top level `{"cats": [...], "items": [...]}`:
- item: `{"id", "name", "desc", "url", "cat"}` (no other fields)
- cat: `{"id", "name", "emoji", "icon", "color", "parentId"}`

## For AI agents
1. Fetch [`catalog/INDEX.json`](https://raw.githubusercontent.com/FindLyTen/van7_storage/main/catalog/INDEX.json) — pick the section you need.
2. Fetch `catalog/<section-id>.json` for that section's items.
3. Fallback: the full [`data.json`](https://raw.githubusercontent.com/FindLyTen/van7_storage/main/data.json).

## Catalog
| Section | Tools | Subsections | Human page | Machine file |
| --- | ---: | ---: | --- | --- |
| 🤖 AI & Agents | 451 | 12 | [catalog/ai.md](catalog/ai.md) | [catalog/ai.json](catalog/ai.json) |
| ⚙️ Automation | 76 | 6 | [catalog/auto.md](catalog/auto.md) | [catalog/auto.json](catalog/auto.json) |
| 💼 Business | 126 | 7 | [catalog/biz.md](catalog/biz.md) | [catalog/biz.json](catalog/biz.json) |
| 💬 Communications | 30 | 6 | [catalog/chat.md](catalog/chat.md) | [catalog/chat.json](catalog/chat.json) |
| 🎨 Design | 66 | 7 | [catalog/design.md](catalog/design.md) | [catalog/design.json](catalog/design.json) |
| 💻 Development | 30 | 4 | [catalog/dev.md](catalog/dev.md) | [catalog/dev.json](catalog/dev.json) |
| 📱 Devices | 24 | 4 | [catalog/devices.md](catalog/devices.md) | [catalog/devices.json](catalog/devices.json) |
| 🎮 Games | 14 | 4 | [catalog/games.md](catalog/games.md) | [catalog/games.json](catalog/games.json) |
| 🛡️ Hacking | 65 | 6 | [catalog/hack.md](catalog/hack.md) | [catalog/hack.json](catalog/hack.json) |
| 🖥️ Infrastructure | 88 | 5 | [catalog/infra.md](catalog/infra.md) | [catalog/infra.json](catalog/infra.json) |
| 📚 Knowledge | 73 | 6 | [catalog/edu.md](catalog/edu.md) | [catalog/edu.json](catalog/edu.json) |
| 🌍 Life | 15 | 3 | [catalog/life.md](catalog/life.md) | [catalog/life.json](catalog/life.json) |
| 🎬 Media | 37 | 5 | [catalog/media.md](catalog/media.md) | [catalog/media.json](catalog/media.json) |
| 📡 Networks & Hardware | 31 | 4 | [catalog/net.md](catalog/net.md) | [catalog/net.json](catalog/net.json) |
| 🕵️ OSINT | 71 | 12 | [catalog/osint.md](catalog/osint.md) | [catalog/osint.json](catalog/osint.json) |
| 🪟 Windows | 18 | 3 | [catalog/win.md](catalog/win.md) | [catalog/win.json](catalog/win.json) |

## Rules for adding items
- one item = `{id, name, desc, url, cat}`; desc ≤200 chars, English, one line
- dedupe by url and name first; new categories only with the maintainer's OK

## Skills
`skills/ecc.md` · `skills/impeccable.md` · `skills/ponytail.md`

## Raw catalog
```
https://raw.githubusercontent.com/FindLyTen/van7_storage/main/data.json
```
