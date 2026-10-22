# PROJECT CONTEXT — VAN7 SKLAD (updated: 2026-10-22)

## LANGUAGE RULE (mandatory)
- ALWAYS speak English with the user in every conversation on this project,
  regardless of the language the user writes in. All replies, explanations,
  summaries and questions — English only. (Code and file contents stay in their own language;
  data.json descriptions are English since 2026-10-14.)

## FULL PROJECT CONTEXT:
- CONTEXT.md — read first (stack, services, backups, data state, rules)
- This file is maintained in English (translated 2026-10-05; older Russian versions: CONTEXT.md.bak*)

## WHAT IT IS
Personal library of software/tools/links. Single-page app:
dark theme, compact sidebar tree of sections on the left, interactive
category map-graph in the center (Obsidian style), slide-out panel with
item list on the right. Categories can be dragged & dropped right on the
map (node onto node → becomes a subcategory). RMB — context menus everywhere.

## STACK
- `api.py` — Flask on 100.97.181.59:5055 (tailscale IP, access only inside private
  network), serves/stores `data.json` (GET/POST /api/data)
- `index.html` — entire front-end app in one file (HTML+CSS+vanilla JS, canvas graph)
- `data.json` — the only storage: `{cats:[…], items:[…]}`
  - cat: `{id, name, emoji, icon(base64|null), color, parentId}` — new ids: `cat_<timestamp>`
  - item: `{id, name, desc, url, cat}`
- nginx: 127.0.0.1:8181, server_name van7sklad.internal, root=/var/www/van7_sklad,
  /api/ → proxy 5055 (config: /etc/nginx/sites-available/van7_sklad)

## ACCESS (Tailscale only)
- http://van7sklad.internal:8181 (if tailscale MagicDNS is enabled)
- http://<tailscale-ip>:8181

## SYSTEMD SERVICES
- `van7-api.service` — Flask API (port 5055). Restart: `systemctl restart van7-api`
- nginx — shared, don't touch separately
- `van7-clean.timer` — temp files cleanup (04:30)
- `van7-sessions-backup.timer` — backup of AI-agent sessions (05:00), NOT the sklad
- `van7-notion-sync.timer` — sync data.json → Notion (every 6h, at :10).
  Service: `/etc/systemd/system/van7-notion-sync.service` (token inside, chmod 600).
  Script: `/var/www/van7_sklad/notion_sync.py`, state: `notion_sync_state.json`.
  Notion database "Склад" (now ~715 rows): columns Название/Описание/URL/Раздел/Категория/Склад ID.
  The database is incremental: adds new, updates changed, archives disappeared ones.
  IMPORTANT: item ids are compared as str() (old ids are numbers, new ones are it_<ts>).

## NOTION (mirror of the sklad for web-Claude)
- integration "vps", workspace "Van7 Склад", page Van7 + database "Склад"
- the page is shared with the bot via Connections
- web-Claude: connect the Notion connector → Claude sees the database and answers
  questions about the sklad ("какие тулзы для компа есть" etc.)

## BACKUPS (in order of importance)
1. **Mega (primary)**: `/etc/cron.d/van7-backup` → every night 03:00
   `rclone copy /var/www/van7_sklad/ "MEGA Sklad:van7-sklad-backup/"`
   Check: `rclone lsl "MEGA Sklad:van7-sklad-backup/data.json"`
2. **Local snapshots**: `/var/www/van7_sklad/backups/data_*.json` — created manually
   BEFORE EVERY data.json change (rule below)
3. "↓ бэкап" button in the UI downloads JSON locally into the browser
4. GitHub backup of the whole VPS: root crontab 03:00 → /backup/github/backup-v2.sh (not ours, don't touch)

## WORK RULES (mandatory)
- Before ANY edit of api.py/index.html/data.json: `cp file file.bak` +
  snapshot of data.json into backups/ with suffix `_pre_<operation>`
- After edits: `systemctl restart van7-api`, check `curl -s http://100.97.181.59:5055/api/data`
- JS check: `node -e "new Function(require('fs').readFileSync('/var/www/van7_sklad/index.html','utf8').match(/<script>([\s\S]*)<\/script>/)[1])"`
- After manual data.json changes: `rclone copy data.json "MEGA Sklad:van7-sklad-backup/"` (don't wait for the night)
- NEVER delete items/categories without confirm-logic and a backup. Data = the sklad itself.
- Every batch of new items must come with descriptions (empty desc is not allowed)
- When adding by URL list: dedupe against existing items by url and name first

## DATA STATE (2026-10-14)
- 16 root sections, 113 categories, 911 items, all have desc; all descriptions, category names
  and item names are in English (translated 2026-10-14; ids and urls unchanged)
- Root ids: ai, osint, hack, infra, auto, design, media, win, net, devices,
  chat, biz, edu, life, dev, games
- Largest sections: ИИ и агенты/ai (193) · Знания/edu (64) · OSINT (59) ·
  Автоматизация/auto (52) · Инфраструктура/infra (51) · Дизайн/design (51)
- Legacy item: find_bot_owner.py (id 498) — old schema (category/path/tags
  instead of cat/url), don't touch, front-end tolerates it
- VPS subcategories — 3rd level (Инфраструктура → VPS → Управление/Аренда/Безопасность)
- PNG category icons: win, auto_browser, devices_android, chat_bots
  (48x48 base64 in the icon field; if icon exists — emoji is empty, and vice versa)
- Known same-name items (not duplicates): NetViz (ShadowArcanist) / NetViz (CSU),
  Agent Skills (Osmani) / Agent Skills (standard)
- VanGram Release Script — the only item without url (local script
  scripts/vangram-release.sh, path in desc)

## BATCHES OF ADDED ITEMS (history)
- 2026-10-03 (+25 → 690): Clef; Neon, R2, Lambda, DynamoDB, Firestore, CloudFront,
  Workers, GCE (Облака); GitHub Actions + Pages docs (Хостинги); Resend (Рассылка);
  John the Ripper, Hydra (Брутфорс); BloodHound, NetExec, Metasploit, Nikto, ffuf,
  sqlmap, Burp Pro, Nuclei, Amass, Masscan (Пентест); Wireshark (Трафик и файрвол).
  Skipped as duplicates: AI Youtube Shorts Generator, Cloudflare Pages, Hashcat, GitHub Pages.
- 2026-10-05 (+33 → 723): REA (Тулзы); Reactive Resume, AIHawk, Hiring Agent (Собесы);
  ResumeSkills (Скиллы); mlcourse.ai, 30 Days of Python, Made With ML,
  ML Projects (Курсы); n8n (Самохост); Umami, Argus (Мониторинг); Coolify (Хостинги);
  LeakIX, GitGraber, DeHashed (Утечки); GeoIntel (GEOINT); Maigret (По нику);
  Shodan, FOFA, Censys (Анализ сайтов); Torch, Ahmia (OSINT-фреймворки);
  Tron (Настройка Win); Octotree (Редакторы); Subtitle Edit (Видеомонтаж);
  Ludusavi, ScummVM (Библиотеки); RetroArch, Cemu (Эмуляторы);
  Steam Headless (Сервера); Code2Video (ИИ-видео); Dify (AI-агенты).
  Skipped as duplicates: Nuclei, SigNoz, MCP Toolbox, GEO Optimizer skill, ExifTool,
  Blackbird (fork), Intelligence X (intelx.io).
- 2026-10-05 (+3 → 726): Flowsint (OSINT-фреймворки), AIPex (Браузер),
  YouTube Skills (Скиллы). Skipped as duplicate: Social Analyzer (qeeqbox).
- 2026-10-06 (+8 → 734): OSINT Catalog (OSINT-подборки); Definitive Open Source
  (Знания/Подборки); Haystack, Milvus, Qdrant (Память агентов); Aider, AutoGen
  (AI-агенты); Apache Doris (Архивы данных). No duplicates skipped.
- 2026-10-13 (+36 → 770): Clipchamp (Видеомонтаж); OnePromptDesign (ИИ-картинки);
  Kawai Text Animations (Анимации); Animator, Melies Cinematic Bible, Calliope,
  Diffusion Studio (ИИ-видео); AnyPS5, KytyPS5 (Эмуляторы); DroidDeck (Android);
  Awesome Claude Connectors (Подборки); Project Maya (Локальные модели); Knotra,
  Claude Commerce Agents, Orca AI (AI-агенты); OnlyDrive (Облака); Talkaside (Собесы);
  OSS Scanner (Защита); ScopeWeaver, Burp Suite (PortSwigger) (Пентест); disktree
  (Чистка и файлы); Exploding Topics, AnswerThePublic, Google Trends, Quora, Google
  Keyword Planner, vidIQ, Social Blade, Semrush, Ahrefs (Маркетинг и SEO); Webstudio
  (Инструменты); OpenSign (Самохост-тулзы); Twenty, Chatwoot (CRM); Rybbit
  (Мониторинг); Mimic (Парсинг). Skipped as duplicate: FreeToken (id 491).
  New descriptions in this batch are written in English.
- 2026-10-14 (+5 → 775): HOL Plugin Directory (Подборки); Pipedream (Самохост-тулзы);
  Social Media Skills (Скиллы); DNSDumpster (Анализ сайтов); Dorks Collections List
  (OSINT-подборки). No duplicates skipped. Descriptions in English.
- 2026-10-15 (+1 → 776): Stealth Browser MCP (Browser). Skipped as duplicate: ProxyBridge (id 500).
- 2026-10-17 (+3 → 779): PhoneInfoga (OSINT / By Phone Number); Raven (GeoSpy), a 404 Media report (GEOINT); chartli (Visualization). No duplicates skipped.
- 2026-10-17 (+2 → 781): Homelable (Monitoring); Horizon (Research). Skipped as duplicate: Uncover (id 56).
- 2026-10-17 (+3 → 784): ArtCraft (Design / Tools); MCP.so (AI / Collections); Composio (AI / API & MCP). No duplicates skipped.
- 2026-10-17 (+2 → 786): Contrack (Business / CRM); MTProxyMax (Communications / Messengers). No duplicates skipped.
- 2026-10-21 (+3 → 789): Reddrix (Scraping); Marketing for Founders (Marketing & SEO); Qwen3.8-27B Defiance Uncensored (Local Models). No duplicates skipped.
- 2026-10-21 (+5 → 794): VideoSOS (AI Video); Agentbox (AI Agents); treg (Marketing & SEO); Mantis (Skills); OpenCreator (AI Video). No duplicates skipped.
- 2026-10-21 (+5 → 799): Social Media Research Skills (Skills); AI Short Video Factory (AI Video); OpenChatCut (Video Editing); Herk Edit Kit (Skills); AutoSubs (Voice & Transcription). No duplicates skipped.
- 2026-10-21 (+5 → 804): FunClip (Video Editing); Polymarket Insider Tracker (Trading); Bitwarden (VPS / Security); Botasaurus (Scraping); NemoClaw (AI Agents). No duplicates skipped.
- 2026-10-21 (+5 → 809): PortCheck (Traffic & Firewall); netcheck (Monitoring); Mercury Agent (AI Agents); OpenCompute (AI Agents); PentestCode (Pentest). No duplicates skipped.
- 2026-10-21 (+4 → 813): Clean Code Skills (Skills); OpenRouter (Routers & Gateways); Ollama (Local Models); AgentCrew (AI Agents). No duplicates skipped.
- 2026-10-21 (+3 → 816): Harness2 (AI Agents); Pentagi (Pentest); Miro (Design). No duplicates skipped. Short machine-oriented descriptions; immediate push per Maxim's 2026-10-21 pre-approval.

- 2026-10-22 (+8 → 824): Ninite (Windows); APInex CLI (CLI); Chops, Skill Issue, Vibe Prompts (Skills); OpenCode Zen, Inception Labs, Cerebras Inference (API & MCP). No duplicates skipped; descriptions ≤200 chars.

- 2026-10-22 (+8 → 832): Mistral Console, Cloudflare Workers AI, Google AI Studio API Keys (API & MCP); gtrk CLI (AI Video); Motion Design Skill, Awesome Motion Design Agent Skills, Animation Principles Skills, claude-motion (Skills). No duplicates skipped.

- 2026-10-22 (+8 → 840): Claude Design Skillstack, Motion.dev Animations Skill, Remotion Agent Skills, Claude Remotion Skill, Remotion Motion Graphics Skills, Claude Code Video Toolkit, Motion Skills, motion-designer (Skills). No duplicates skipped.

- 2026-10-22 (+8 → 848): HyperFrames Motion Reel Skill, Motion Graphics Skill Pack (Skills); openInvest (AI Agents); Clon1X (Browser); Vibe Coding Toolkit (Skills); ModelMatrix, Medulla (CLI); dsh-data-quality (Skills). No duplicates skipped.

- 2026-10-22 (+8 → 856): dsh-fund-research (Skills); Awesome Opus 5.5 Videos (Collections); Gr8r Studio (CRM); herdr-reviewr (CLI); Mailflare for macOS (Clients); PolyHistorical (Trading); editonny (Skills); Uniichat (AI Agents). No duplicates skipped.

- 2026-10-22 (+8 → 864): OpenShell (AI Agents); Muxin (PC Control); httpx, subfinder, waybackurls (OSINT); katana (Scraping); gitleaks (Defense); ghidraMCP (Hacking). No duplicates skipped.

- 2026-10-22 (+8 → 872): IDA Pro MCP, jadx, Apktool, Frida, ILSpy, radare2, x64dbg, ImHex (Hacking). No duplicates skipped.

- 2026-10-22 (+8 → 880): angr, mitmproxy, dnSpyEx, rizin, RAD Debugger (Hacking); Awesome Reversing (Collections); VibeSkills (Skills); xMatrix (Clients). No duplicates skipped. Batch E complete: 64 added; skipped duplicates transitions.dev (id 144), gsap-skills (411), taste-skill (257), harness2 (it_17926171777641), amass (it_1791034692215), trufflehog (361); opendesign.dev skipped (dead/sunset site).

- 2026-10-22 (+8 → 888): ccswap (CLI); Firecrawl (Scraping); Minke, GPT Researcher (AI Agents); Awesome AI Startups (Collections); prompts.chat (Skills); Duck.ai (Routers & Gateways); PhoneHackScan (Defense). No duplicates skipped.

- 2026-10-22 (+8 → 896): aifree.dev Offers (Collections); reKover (Pentest); Crypto Trading Desk, Freqtrade (Trading); ADCode (Editors); APInexGate Reseller (Routers & Gateways); Hermes DaVinci Resolve Plugin (Skills); Hy-MT2 (Local Models). No duplicates skipped.

- 2026-10-22 (+8 → 904): Awesome Reverse-Engineered (Collections); TinyFish Hermes Plugin (Skills); oly (CLI); Atomic Agent (AI Agents); Apify (Scraping); Docling (OCR); LlamaIndex (Agent Memory); web-retrieval-mcp (API & MCP). No duplicates skipped.

- 2026-10-22 (+7 → 911): Oxylabs Web API MCP, Tavily MCP (API & MCP); Birdbrain (Website Analysis); proxy-scraper (Scraping); cobalt (Downloads); MobileUse (AI Agents); Kiro (Editors). No duplicates skipped. Batch F complete: 31 added; skipped duplicates Crawl4AI (308), SearXNG (it_178982395593123), RAGFlow (462), Haystack (it_1791310598948), Agent Reach (264), Hermes Agent (393), Osiris (156); list repeats 7/31 and 15/33 processed once.

## FRONT-END: MAP (main)
- buildGraph(): center "СКЛАД" → ring of 16 roots (R=420) → subcategories fanned
  outward (R=360) in the parent's sector
- Zoom wheel/buttons/pinch, panning with inertia, auto-fit on first render
- Node click → selectNode → panel + branch highlight; dblclick → openPanelFor
- Node drag onto another node → reparent (parentId changes, persist()) with
  cycle protection (can't drop into own subtree)
- Sidebar synced with the map (shared state view.sel); rendered from draw()
  keyed by G._sbKey to avoid rebuilding every frame
- Topbar search: filter by name+desc, grouped by categories, link to category
- Icons: iconH() — unified PNG/emoji render for map, sidebar, panel, search;
  onerror swaps broken PNG for emoji fallback; imgOf() does the same on canvas
- UI (2026-09-29): large fonts (sidebar 13.5px, titles 15px, desc 13px),
  enlarged buttons/zoom/icons — comfort mode, no tiny text

## WHAT THE PROJECT DOESN'T HAVE / don't do
- No bundlers, packages, CDN dependencies except Google Fonts (Geist/Geist Mono)
- No auth — access is closed by the Tailscale network
- Don't split the front-end into separate files — everything in one index.html
- Don't change ports 5055/8181 or API paths

## JUNK (can be cleaned if desired)
- `*.bak`, `*.bak2`, `opencode.json.direct`, `__pycache__` — historical copies
- keep backups/ entirely — it's the sklad's history
