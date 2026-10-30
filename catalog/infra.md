# 🖥️ Infrastructure

> GENERATED from data.json by scripts/build_views.py — do not edit by hand.

## Contents
- [Cloud](#cloud) (18)
- [Domains](#domains) (13)
- [Hosting](#hosting) (12)
- [Monitoring](#monitoring) (22)
- [VPS](#vps) (24)

## Cloud
- [Appwrite](https://github.com/appwrite/appwrite) - Open-source backend cloud for agents and developers: auth, databases, storage, functions, messaging, hosting, realtime, MCP server; Docker self-host; TypeScript; BSD-3-Clause.
- [AWS Lambda](https://aws.amazon.com/lambda/) - Amazon serverless functions: event-driven code without servers, pay per millisecond of execution. Cheap for small tasks, 15 min limits.
- [CloudFlare ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) - photo storage on Cloudflare
- [Cloudflare R2](https://www.cloudflare.com/products/r2/) - S3-compatible object storage with no egress fees (egress = $0). Images, backups, static files — cheap and fast all over the world.
- [Cloudflare Workers](https://www.cloudflare.com/products/workers/) - Serverless code on Cloudflare edge nodes worldwide: JS/TS/Python/WASM, no cold starts, KV/R2/D1 nearby. 100k requests/day free.
- [CloudFront](https://aws.amazon.com/cloudfront/) - Amazon CDN: caching static files/video across 600+ points of presence, lambda@edge for logic at the edge. The basis of content delivery in AWS.
- [DriveBase](https://github.com/drivebase/drivebase) - all my clouds managed in one place
- [DynamoDB](https://aws.amazon.com/dynamodb/) - Amazon non-relational DB: key-value and document model, millisecond latency at any scale, serverless with autoscale, has a forever free tier (25GB).
- [Firestore](https://cloud.google.com/firestore/pricing) - Google non-relational document DB: realtime updates on clients, offline mode, serverless. The Firebase stack for apps. Pricing with a free quota.
- [Google Compute Engine](https://cloud.google.com/products/compute) - Google Cloud virtual machines: per-second billing, preemptible instances at up to 90% discount, free egress tier of 200GB. A VPS in the Google cloud.
- [MEGA](https://mega.io/ru/) - MEGA drive, free 20GB
- [Microsoft Azure](https://azure.microsoft.com/en-us) - Microsoft's public cloud platform: compute, storage, databases, AI services, networking; free account with always-free services and 12-month credits.
- [Neon](https://neon.com/) - Serverless Postgres: git-like database branching (a copy of the database for each branch/preview), autoscale to zero, generous free tier. A foundation for modern SaaS.
- [Nextcloud](https://nextcloud.com/) - Open-source personal cloud: files, calendars, contacts, office, sync — self-host.
- [OnlyDrive](https://github.com/yava-code/OnlyDrive) - Single Go binary (gd) mounts Google Drive as local drive without Cloud project/API keys; pools accounts, exposes S3/WebDAV/MCP. Wraps rclone, local web panel. Not for live DBs. Apache-2.0.
- [Ray](https://github.com/ray-project/ray) - Distributed AI compute engine: core distributed runtime plus libraries for training, serving, tuning and RL workloads, scales Python from laptop to cluster; Apache-2.0.
- [Supabase](https://supabase.com/) - Open-source Firebase alternative: Postgres, realtime subscriptions, auth, storage, edge functions, auto-generated API. Has a generous free tier.
- [TeraBox](https://www.terabox.com/russian) - free terabyte

## Domains
- [Cloudflare Registrar](https://domains.cloudflare.com/) - Domains at cost + free WHOIS privacy
- [Domain Searcher App](https://github.com/vasilytrofimchuk/domainsearcher-app) - AI domain name generator: describe your startup idea, get available names rated by length, sound, memorability.
- [Dynadot](https://www.dynadot.com/ru) - Registrar with a clear API and a domain auction
- [FreeDNS](https://freedns.afraid.org/) - free DNS addresses
- [FreeDomains](https://github.com/stackryze/FreeDomains) - free crappy domains and subdomains
- [GoDaddy](https://www.godaddy.com/en-ph) - Registrar with minimal prices from the creators of NameCheap
- [NameCheap](https://www.namecheap.com/) - Domain registrar and DNS hosting
- [Namesilo](https://www.namesilo.com/) - The largest domain registrar in the world
- [Nicnames](https://nicnames.com/en) - Search for available domains and brand synonyms
- [OVH Domains](https://www.ovhcloud.com/en/domains/) - The largest European registrar and hosting provider
- [Porkbun](https://porkbun.com/) - Cheap domains without hidden fees
- [Spaceship](https://www.spaceship.com/) - Domain registrar and related services
- [Tldes](https://tldes.com/cheapest-domains) - price comparer for specific domains

## Hosting
- [Cloudflare Pages](https://pages.cloudflare.com/) - also static html css
- [Coolify](https://github.com/coollabsio/coolify) - Self-host PaaS: deploy apps and databases on your own server with one button — an open-source alternative to Vercel/Heroku/Netlify.
- [DevPush](https://github.com/hunvreus/devpush) - local self-hosted hosting
- [GitHub Actions](https://github.com/features/actions) - CI/CD right in GitHub: build/test/deploy on push and on a schedule, thousands of ready-made actions, 2000 min/month free in private repos.
- [Github Pages](https://pages.github.com/) - html css lightweight hosting
- [GitHub Pages (docs)](https://docs.github.com/en/pages) - Official GitHub Pages documentation: setting up Jekyll, custom domains, HTTPS and deploying via Actions.
- [Hugging Face Spaces](https://huggingface.co/spaces) - Free hosting platform for ML and AI demos (Spaces): run community apps like image generators; CPU free, GPU paid.
- [Netlify](https://www.netlify.com/) - static html css
- [NGrok](https://ngrok.com/) - Tunnel a local port to a public URL in a second
- [Rathole](https://github.com/rathole-org/rathole) - A lightweight and very fast reverse proxy for bypassing NAT, written in Rust; an open alternative to frp and ngrok. Minimal resources, encryption via the Noise protocol.
- [Vercel](https://vercel.com/) - Hosting for frontend and serverless functions with auto-deploy from Git
- [Wispbyte](https://wispbyte.com/client/) - Free game server hosting: Minecraft, Rust, etc.

## Monitoring
- [Argus](https://github.com/release-argus/Argus) - Software release monitoring: tracks new versions on GitHub/Docker/GitLab and notifies via Apprise/webhooks. Self-hosted.
- [Checkmate](https://github.com/bluewave-labs/Checkmate) - server hardware monitoring
- [Gatus](https://github.com/TwiN/gatus) - Developer health dashboard: monitors services via HTTP, ICMP, TCP and DNS with conditions on status code, response time, certificate expiry; alerts to Slack, Teams, PagerDuty; Go, Docker.
- [Globalping MCP](https://github.com/jsdelivr/globalping-mcp-server) - Ping/traceroute/DNS from global probes: free, no key; official jsDelivr, active.
- [Grafana](https://grafana.com/) - monitoring of applications and servers
- [Healthchecks MCP](https://github.com/ni-c/healthchecks-mcp) - Cron/heartbeat liveness monitoring MCP: agent sees when a bot stops reporting; free, self-hostable; community, active.
- [HomeDashboard](https://github.com/demencia89/HomeDashboard) - Web dashboard for monitoring Linux devices via ssh
- [Homelable](https://github.com/Pouzor/homelable) - Homelab visualizer: network diagram, live status (ping, HTTP, TCP, SSH, Prometheus), nmap, Zigbee2MQTT, Z-Wave JS UI, Proxmox imports, canvas, Live View + MCP. Docker/LXC. MIT.
- [netcheck](https://github.com/m1/netcheck) - Checks availability of a list of network targets and exports Prometheus metrics for Alertmanager; Docker container and Helm chart for Kubernetes, pingdom alternative; Rust; GPL-3.0.
- [ntfy MCP](https://github.com/ni-c/ntfy-mcp) - Push notifications to phone via self-hosted ntfy: pairs with Healthchecks; free, self-hostable; community, active.
- [OpenPanel](https://github.com/Openpanel-dev/openpanel) - Open-source product/web analytics, an alternative to Mixpanel: funnels, cohorts, user profiles, session replay, A/B tests, real-time dashboards. Cookieless and GDPR-friendly, can be self-hosted (Docker).
- [Plausible](https://plausible.io/) - website analytics
- [PostHog](https://posthog.com/) - Product analytics in one project: event analytics, feature flags, A/B tests, session recordings, surveys, warehouse. Open-source, can be self-hosted.
- [Reserve](https://github.com/Apiruck-Corp/reserve) - macOS menu-bar app showing reported subscription capacity for OpenAI Codex, Claude, Grok, Cursor, Copilot, Gemini, Z.ai GLM coding plan and Kimi; local-only, no accounts or telemetry; Swift, MIT.
- [Rybbit](https://rybbit.com/) - Open-source cookieless web/product analytics (GA alt): events, session replay, funnels, journeys, Core Web Vitals, error tracking, API/MCP. ~11KB script, AGPL-3.0; self-host Docker or EU cloud.
- [Sentry MCP](https://mcp.sentry.dev) - Official hosted Sentry MCP for error tracking: agent reads app errors, stack traces; free Developer plan 5k errors/mo; official, very active.
- [SigNoz](https://github.com/SigNoz/signoz) - Open-source observability: traces, metrics, logs in one — a Datadog replacement, self-host.
- [socktop](https://github.com/jasonwitty/socktop) - Tool for remote monitoring of Linux systems with a convenient TUI interface in the style of top and btop
- [TrailBase](https://github.com/trailbaseio/trailbase) - self-hosted monitoring of databases, authorizations and APIs of my own projects, an alternative to Google Firebase
- [Umami](https://github.com/umami-software/umami) - Simple private self-hosted web analytics: a Google Analytics alternative without cookies and tracking. Lightweight, open-source, has a cloud plan.
- [UpTime Kuma](https://github.com/louislam/uptime-kuma) - Website monitoring and alerts
- [Zabbix](https://www.zabbix.com/) - powerful IT infrastructure monitoring

## VPS
- [Agent Vault](https://github.com/Infisical/agent-vault) - Credential broker by Infisical: agents route HTTP through it and never hold real secrets; placeholders swapped on outbound requests, egress filtering, request logging, pluggable stores; Go.
- [Apache Casbin](https://github.com/apache/casbin) - Access control library: enforces authorization across ACL, RBAC, ABAC models via a model+policy config; production-ready ports for Go, Java, Node, PHP, Python, .NET, C++, Rust; Apache-2.0.
- [Better Auth](https://github.com/better-auth/better-auth) - Framework-agnostic TypeScript authentication framework: email/social auth, 2FA, multi-tenant, sessions, plugin ecosystem; npm; MIT.
- [Bitwarden](https://github.com/bitwarden) - Open-source password manager: clients for web, browser, desktop, CLI (GPL-3.0) and self-hostable server (AGPL-3.0), secrets manager, passkeys, Docker image, SDKs.
- [Cerbos](https://github.com/cerbos/cerbos) - Authorization layer (PDP): context-aware access rules in YAML policies, gitops deployment, RBAC/ABAC, CheckResources and PlanResources APIs, SDKs; Go, self-hosted; Apache-2.0.
- [Fail2Ban](https://github.com/fail2ban/fail2ban) - This is a protective program for servers: it watches the logs and, if someone repeatedly fails to log in (for example, guessing an SSH password), it blocks their IP address through the firewall on its own.
- [gVisor](https://github.com/google/gvisor) - Sandbox container runtime from Google (application kernel in Go): container isolation stronger than regular Docker, for untrusted code.
- [Keycloak](https://github.com/keycloak/keycloak) - Identity and access management server: SSO, user federation (LDAP/AD), strong auth (2FA, passkeys), fine-grained authorization, admin console; Java, self-hosted; Apache-2.0.
- [OpenFGA](https://github.com/openfga/openfga) - Fine-grained authorization engine based on Google Zanzibar: HTTP/gRPC APIs, PostgreSQL/MySQL/SQLite storage, multi-language SDKs, CLI, playground; CNCF project, Go; Apache-2.0.
- [SpiceDB](https://github.com/authzed/spicedb) - Authorization database inspired by Google Zanzibar: scalable fine-grained permissions, relationships as data, consistent permission checks; Go; Apache-2.0.
- [Vaultwarden](https://github.com/dani-garcia/vaultwarden) - Lightweight self-hosted Bitwarden server (Rust): passwords, TOTP, syncing across all clients.
- [Contabo](https://contabo.com/en/) - Cheap VPS and dedicated servers in Europe/USA
- [Detalix.eu](https://datalix.eu/) - German VPS with hourly billing
- [Euronodes](https://euronodes.com/) - Budget VPS in Europe for personal projects
- [HostingByDesign](https://hostingby.design/) - Dutch VPS hosting for any tasks
- [NetCup](https://www.netcup.com/en) - Very cheap German VPS and servers
- [Servarica](https://servarica.com/) - VPS with DDoS protection and anonymous registration
- [Strato.nl](https://www.strato.nl/) - German hoster: VPS, servers, domains
- [Dashy](https://github.com/Lissy93/dashy) - VPS status monitoring
- [Foreman](https://github.com/theforeman/foreman) - Open-source server lifecycle management platform: configuration, orchestration, provisioning (Puppet), auditing. A classic for fleets of Linux machines.
- [Homelab Hub](https://github.com/RaidOwl/homelab-hub) - Self-hosted homelab tracker: hardware, VMs, services, storage, networks, shares (NFS/SMB/iSCSI) with auto paths. Interactive graph (Cytoscape.js), tree, markdown docs, JSON export/import.
- [MobaXTerm](https://mobaxterm.mobatek.net/download-home-edition.html) - SSH manager, terminal, VPS file manager
- [PatchMon](https://github.com/PatchMon/PatchMon) - Monitoring of vulnerabilities in WordPress plugins and themes
- [RS top](https://github.com/ruiiiijiiiiang/rs-top) - TUI monitor of Linux server resources in real time
