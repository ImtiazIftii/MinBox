# MinBox - Project State

## 1. Product Summary
MinBox is a fast, privacy-respecting messaging and productivity aggregator that brings everyday communication apps (WhatsApp, Slack, Gmail, Discord, Notion) into one unified desktop hub with a sidebar, unread indicators, and a fast command bar (`Ctrl+K`).

## 2. Architectural Decisions
- **Desktop Runtime (v1):** Electron (Chromium + Node.js) with isolated session partitions.
  - *Why:* Pure web browsers block third-party embedding via `X-Frame-Options` and `CSP frame-ancestors`. Personal messaging platforms offer no open personal REST APIs. Electron allows isolated, full-fidelity local rendering.
- **Frontend:** React + Vite + TypeScript.
- **Backend:** Python 3.13 + FastAPI.
- **Database:** PostgreSQL 16 (running via Docker Compose locally) with SQLAlchemy 2.x and Alembic.
- **Privacy Boundary (Zero Knowledge):** Third-party login cookies, credentials, and message content remain strictly on the local machine inside sandboxed Electron partitions. MinBox's PostgreSQL database only stores MinBox user accounts, hashed passwords, and pinned app configurations.

## 3. Current Phase
- **Phase 0 (Completed):** Discovery, Architecture Decisions, and Threat Model.
- **Phase 1 (Completed):** Repository structure, tooling (Ruff, Mypy), Docker + PostgreSQL running locally, and health check endpoint with automated pytest test suite.
- **Next Phase:** Phase 2 — Database schema + Alembic migrations for the first feature.

## 4. Current Folder Structure
```
MinBox/
├── .agents/             # Project guidelines and teaching rules
├── .gitignore           # Defense-in-depth git ignore rules
├── apps/
│   ├── api/             # FastAPI backend (src layout)
│   │   ├── .env.example # 12-factor environment template
│   │   ├── pyproject.toml # Modern PEP 621 packaging & tool config
│   │   ├── src/
│   │   │   └── minbox_api/
│   │   │       ├── core/
│   │   │       │   └── config.py # Strongly-typed Pydantic settings
│   │   │       └── main.py       # FastAPI application & /health route
│   │   └── tests/
│   │       └── test_health.py    # Automated test verifying HTTP 200 & JSON
│   ├── desktop/         # Electron desktop client (v1 shell)
│   └── web/             # React + Vite frontend
├── docker-compose.yml   # PostgreSQL 16 Alpine + persistent volume + healthcheck
├── PROJECT_STATE.md     # Ongoing source of truth
└── README.md            # Project documentation
```

## 5. Running Concepts Learned
1. `X-Frame-Options` & `CSP frame-ancestors` (Anti-clickjacking browser headers)
2. `OAuth 2.0` (Delegated authorization protocol)
3. `Electron Architecture` (Main Node.js Process vs. Renderer Chromium Process)
4. `Walled Gardens & Restricted Scopes` (Why personal messaging APIs are locked down)
5. `End-to-End Encryption (E2EE) & Client-Side Decryption` (Local decryption vs. backend APIs)
6. `Electron Auto-Updater & Bundled Runtimes` (How desktop Chromium gets patched)
7. `User-Agent Header & Spoofing` (Preventing "unsupported browser" false alarms)
8. `Threat Modeling (STRIDE & Zero-Knowledge Architecture)` (Isolating sessions, securing auth)
9. `PostgreSQL Architecture` (Docker for local development vs. Serverless cloud Postgres)
10. `Monorepo Architecture & Separation of Concerns (SoC)` (Apps decoupling)
11. `12-Factor App & Config Management` (Environment variables vs. hardcoded secrets)
12. `Python Packaging & PEP 621 (pyproject.toml)` (Modern unified Python config)
13. `ASGI & Uvicorn` (Asynchronous Server Gateway Interface web server)
14. `Asynchronous Programming (async/await & Event Loop)` (Non-blocking I/O in FastAPI)
15. `HTTP Request-Response Lifecycle` (Methods, paths, headers, status codes)
16. `Automated Testing with Pytest & TestClient` (In-memory mock HTTP assertions)
17. `Linters, Formatters, & Type Checkers (Ruff & Mypy)` (Automated code quality & strict typing)
18. `Docker Containers & Images` (Standardized, reproducible deployment boxes)
19. `Docker Compose, Port Forwarding & Named Volumes` (Multi-container orchestration & data persistence)
