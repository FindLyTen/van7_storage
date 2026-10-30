# 🛡️ Hacking

> GENERATED from data.json by scripts/build_views.py — do not edit by hand.

## Contents
- [Brute Force](#brute-force) (3)
- [DDoS](#ddos) (2)
- [Defense](#defense) (11)
- [Pentest](#pentest) (30)
- [Phishing](#phishing) (3)
- [Tools](#tools) (9)
- [Other](#other) (13)

## Brute Force
- [Hashcat](https://hashcat.net/hashcat/) - brute-forcing passwords of zips, folders, etc. via hash files
- [Hydra (THC)](https://hydra.cc/) - Network login brute-forcer over protocols: SSH, FTP, HTTP forms, RDP, SMB, MySQL and dozens of others. Parallel, fast, a pentest standard.
- [John the Ripper](https://www.openwall.com/john/) - Classic hash brute-forcer: hundreds of Unix/Windows/DB/archive formats, wordlist/rules/GPU modes. Jumbo build.

## DDoS
- [DDOS Ripper](https://github.com/palahsu/DDoS-Ripper) - Server stress-testing tool
- [Hping](https://github.com/antirez/hping) - Console TCP/UDP packet generator for testing networks

## Defense
- [Bandit](https://bandit.readthedocs.io/) - PyCQA static analyzer finding common security issues in Python code; free, Apache-2.0.
- [ClamAV](https://www.clamav.net/) - Open-source antivirus engine for mail gateways and file scanning with signature database; free, GPL.
- [gitleaks](https://github.com/gitleaks/gitleaks) - Tool for detecting secrets (passwords, API keys, tokens) in git repos, files and stdin with rules and entropy scanning; git/cron integration; Docker, Homebrew, Go installs; MIT.
- [MinerSearch](https://github.com/BlendLog/MinerSearch) - Finding and removing hidden miners on Windows
- [opencode-vibeguard](https://www.npmjs.com/package/opencode-vibeguard) - OpenCode plugin that auto-redacts secrets/PII before they reach the AI; free, no key; community.
- [OSS Scanner](https://github.com/anthropics/oss-scanner) - Anthropic model-driven vuln scanning for critical OSS: PR adds project.yaml+Dockerfile, built/scanned in VM, findings with reproducers/patches emailed. Not human-reviewed. Apache-2.0.
- [OWASP Cheatsheets](https://github.com/OWASP/CheatSheetSeries) - OWASP Cheat Sheet Series — proven application security checklists: authentication, sessions, SQLi, XSS, cryptography and dozens of other topics.
- [PhoneHackScan](https://github.com/UCYBERS/PhoneHackScan) - Android/iPhone spyware check: USB quick scan, androidqf + MVT full scan, iOS backup analysis, optional VirusTotal hashes; Python 3.10+; GPL-3.0.
- [PrivacyTools.io](https://privacytools.io/apps) - Curated privacy app directory: 350+ reviewed tools and services with filters, ratings and alternatives for encryption, VPN, browsers and self-hosting; web directory.
- [Trivy](https://trivy.dev/) - Aqua open-source scanner for vulnerabilities, misconfigurations, secrets and SBOM in containers and repos; free, Apache-2.0.
- [Veracode](https://www.veracode.com/) - Commercial static and dynamic application security testing platform; paid, vendor pricing.

## Pentest
- [Amass (OWASP)](https://github.com/owasp-amass/amass) - Powerful reconnaissance of domains and subdomains: passive sources, DNS brute force, scraping, building a map of external infrastructure.
- [BloodHound](https://github.com/specterops/bloodhound) - Graph analysis of an Active Directory domain: collects relationships between users/groups/hosts and finds hidden escalation paths to domain admin. SpecterOps.
- [Burp Suite (PortSwigger)](https://portswigger.net/burp) - Official Burp Suite (PortSwigger): standard web app security toolkit. Free Community for manual testing, Pro with Scanner for pentesters, DAST for automated CI scanning.
- [Burp Suite Professional](https://github.com/xiv3r/Burpsuite-Professional) - The main proxy for web pentesting: intercepting and replaying requests, vulnerability scanner, Intruder fuzzer, extensions via the BApp Store.
- [Decepticon](https://github.com/BitterSecurity/Decepticon) - autonomous AI agent for professional red team that goes through the full attack chain on its own
- [Deep Eye](https://github.com/zakirkun/deep-eye) - An AI-based pentest orchestrator: runs 10+ providers (OpenAI, Claude, Grok, Ollama...) to generate payloads, scans 45+ vulnerability types and produces professional reports with compliance mapping.
- [dnstwist MCP](https://github.com/elceef/dnstwist) - Typosquat detection, domain permutation checking: free, no key; community.
- [ffuf](https://github.com/ffuf/ffuf) - Fast web fuzzer in Go: brute-forcing directories/files/parameters, vhost fuzzing, recursion, filters by size/code/time. Based on gobuster, but more powerful.
- [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) - MCP server letting AI agents operate 150+ cybersecurity tools for authorized pentesting (recon, scanning, exploitation tooling); MIT; 13k stars.
- [Masscan](https://github.com/robertdavidgraham/masscan) - The fastest port scanner on the planet: the whole internet in 6 minutes, millions of packets/sec. To find open ports — only this. Account for the limitations of SYN scanning.
- [Metasploit](https://www.metasploit.com/) - The main exploit framework: thousands of exploits and payloads, post-exploitation, meterpreter, automatic exploitation of vulnerabilities.
- [NetExec](https://github.com/Pennyw0rth/NetExec) - A fork of CrackMapExec — a Swiss army knife for networks: credential checks on SMB/WinRM/LDAP/SSH/MSSQL, login dumping, password spraying. Alive and developing.
- [Nikto](https://github.com/sullo/nikto) - Classic web server scanner: outdated software, dangerous files, injections, misconfigurations. A quick first pass over a site.
- [Nmap](https://nmap.org/) - Network discovery and port scanning tool with NSE scripts, for authorized testing and inventory; free, GPL.
- [Nuclei](https://github.com/projectdiscovery/nuclei) - Template-based vulnerability scanner from ProjectDiscovery: thousands of ready-made templates (CVE, panels, exposure) + your own in YAML. Fast, accurate, CLI.
- [OWASP ZAP](https://www.zaproxy.org/) - OWASP open-source web app security scanner and proxy for finding vulnerabilities, for authorized testing; free, Apache-2.0.
- [Pentagi](https://github.com/vxcontrol/pentagi) - Autonomous AI agent system for complex penetration testing tasks; multi-agent pentest workflows; self-hosted via Docker; Go/React; pentagi.com; MIT.
- [Pentest Agent](https://github.com/0xSojalSec/PentestAgent) - AI pentest assistant: plain-language task ("check this server") triggers Nmap, Metasploit, SQLMap etc., outputs report.
- [PentestCode](https://github.com/s0ld13rr/pentestcode) - Autonomous pentest agent in the terminal: multi-agent attack chain with nmap, SMB/LDAP enumeration, AS-REP roast, spraying, post-exploit, engagement state, 20+ LLM providers; fork of OpenCode; MIT.
- [pwn.college](https://pwn.college/) - a platform for learning pentesting and binary exploitation from ASU: theory + hands-on labs
- [reKover](https://github.com/BruteLogic/reKover) - Bash URL mapper for recon: robots/sitemap parsing, weighted brute force, JS-aware crawl, Wayback CDX probes; JSON output; needs parallel+curl; MIT.
- [ScopeWeaver](https://github.com/cskwork/scopeweaver) - LLM multi-agent autonomous pentest (ARTEX): planner/worker agents over shared graphs, traffic proxy, tool-approval gate. Go+Next.js+PostgreSQL, needs LLM key. AGPL-3.0; personal study only.
- [Shannon](https://github.com/KeygraphHQ/shannon) - Autonomous AI pentester for authorized web/API testing: reads your source code, maps attack paths and runs POC exploits to prove findings; CLI agent; AGPL-3.0.
- [Shodan MCP](https://github.com/w0h1v/mcp-shodan) - Internet device/IP lookup, banners, CVE intel via Shodan API: server free, real use needs $49 membership; community, moderately active.
- [Skipfish](https://github.com/spinkham/skipfish) - website vulnerability scanner
- [sqlmap](https://github.com/sqlmapproject/sqlmap) - Automatic SQL injection combine: detects the DB type, dumps tables, reads files, gets a shell. The standard in web pentesting.
- [Strix](https://github.com/usestrix/strix) - autonomous AI agents for pentesting: they run code themselves, look for vulnerabilities (SQLi, XSS, SSRF, IDOR, etc.) and prove them with a real working exploit, not just a warning
- [T3MP3ST](https://github.com/elder-plinius/T3MP3ST) - An autonomous red-team platform from plinius: a multi-agent meta-harness for offensive security; agents plan and carry out attacks on their own.
- [VirusTotal MCP](https://github.com/w0h1v/mcp-virustotal) - URL/hash/domain maliciousness scans via VirusTotal API: freemium with rate-limited free tier; community.
- [Vulnerator AI](https://github.com/irraz/vulnerator-ai) - Autonomous agent for authorized penetration testing: OODA-loop reasoning, Kali and Playwright browser tools over MCP, ATT&CK-style orientation; MIT.

## Phishing
- [CamFish](https://github.com/firidon/CamFish) - phishing for camera shots
- [DockDroid](https://github.com/sickcodes/dock-droid) - Android in Docker: an isolated sandbox for testing
- [ZPhisher](https://github.com/htr-tech/zphisher) - A set of phishing pages of popular services for testing on people

## Tools
- [APK Reverse](https://github.com/newliver666/apk-reverse) - Tool for reverse engineering Android apps: APK unpacking, decompilation, code and resource analysis.
- [Binwalk](https://github.com/refirmlabs/binwalk) - A firmware analysis tool: finds embedded file systems, signatures and images inside binaries. A classic of firmware reversing, now in Rust.
- [F Society](https://github.com/Manisso/fsociety) - General hacking tools
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) - A legendary reverse engineering framework from the NSA: disassembler + decompiler, analysis of binaries of any architecture, scripts in Java/Python. A standard for RE and malware analysis. Current version 12.1.3.
- [Kong RE](https://github.com/amruth-sn/kong) - “Agentic reverse engineer”: LLM orchestration of binary analysis via Ghidra — recovers names/types/structures in obfuscated binaries in minutes instead of days.
- [mitmproxy](https://github.com/mitmproxy/mitmproxy) - Interactive intercepting HTTPS proxy in Python: TLS cert spoofing, replay, scripting, mitmdump CLI and mitmweb UI, HAR export; TLS-capable debugging of HTTP traffic; MIT.
- [REA](https://github.com/morluto/rea) - AI agent for reverse engineering: connects to Hopper/Ghidra via MCP and analyzes apps without source code — native binaries, Electron, .NET, websites. Shows evidence and helps rebuild a feature for your own project.
- [StegoForge](https://github.com/Nour833/StegoForge) - A steganography and digital forensics toolkit: hiding and extracting data in images, audio, video, documents and network packets + 11 engines for detecting hidden payloads.
- [x64dbg MCP Server](https://github.com/duty1g/x64dbg-mcp-server) - Native MCP plugin for x64dbg: exposes debugger over HTTP; AI sets breakpoints, steps code, reads memory, dumps registers. Reversing/malware analysis with Claude.

## Other
- [angr](https://github.com/angr/angr) - Platform-agnostic binary analysis framework: symbolic execution, decompilation, control-flow and data-dependency analysis, value-set analysis, program instrumentation; Python 3; BSD-2-Clause.
- [Apktool](https://github.com/iBotPeaches/Apktool) - Tool for reverse engineering closed Android apps: decode resources to near-original form and rebuild after modification, debug smali step-by-step; Java; Apache-2.0.
- [dnSpyEx](https://github.com/dnSpyEx/dnSpy) - Unofficial continuation of dnSpy: debugger and assembly editor for .NET and Unity without source code - edit metadata in C#/VB, breakpoints, tracepoints, hex memory window; C#; GPL-3.0.
- [Frida](https://github.com/frida/frida) - Dynamic instrumentation toolkit for reverse engineers and security researchers: inject code into running iOS/Android/desktop apps; C core, Python/Node bindings; custom license.
- [ghidraMCP](https://github.com/LaurieWired/GhidraMCP) - MCP server plus Ghidra plugin for LLM-driven reverse engineering: decompile and analyze binaries, auto-rename methods and data, list methods/classes/imports/exports; Python + uv; Apache-2.0.
- [IDA Pro MCP](https://github.com/mrexodia/ida-pro-mcp) - MCP server for 'vibe reversing' in IDA Pro 8.3+/9: LLM-guided decompile, analyze and inspect via tools exposed to any MCP client; Python 3.11, uv, idalib; MIT.
- [ILSpy](https://github.com/icsharpcode/ILSpy) - Open-source cross-platform .NET assembly browser and decompiler: Avalonia desktop UI, VS and VS Code extensions, ILSpyCmd dotnet tool, decompile F12 in Visual Studio; C#; MIT.
- [ImHex](https://github.com/WerWolv/ImHex) - Hex editor for reverse engineers and programmers: pattern language structures, bookmarks, data inspector, diffing, custom encodings and visualizes with themes; C++ (Qt); GPL-2.0.
- [jadx](https://github.com/skylot/jadx) - Dex to Java decompiler: command-line and GUI tools producing Java source from APK/dex/aab, plus Java bytecode and smali; deobfuscator, resource decoding, smali debugger; Java 11; Apache-2.0.
- [RAD Debugger](https://github.com/EpicGames/raddebugger) - Native, user-mode, multi-process graphical debugger from Epic Games: local x64 on Windows and early Linux, RDI debug-info format, radbin conversion, alpha; C; MIT.
- [radare2](https://github.com/radareorg/radare2) - Libre reversing framework: disassemble, debug, edit and emulate any binary on any architecture; embedded JS interpreter and r2pipe; pip-style install script; C; LGPL-3.0.
- [rizin](https://github.com/rizinorg/rizin) - Reversing framework born as a fork of radare2 focused on usability and cleanliness: analyze binaries, disassemble, debug, forensics, scriptable hex editor; C, meson build; LGPL-3.0.
- [x64dbg](https://github.com/x64dbg/x64dbg) - Open-source Windows user-mode debugger for x86/x64 aimed at malware analysis: CPU tracing graph, memory map, plugin system; C++; freeware.
