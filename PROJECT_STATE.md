# MinBox - Project State

## 1. Product Summary
MinBox is a fast, privacy-respecting messaging and productivity aggregator that brings everyday communication apps (WhatsApp, Slack, Gmail, Discord, Notion) into one unified desktop hub with a sidebar, unread indicators, and a fast command bar (`Ctrl+K`).

## 2. Architectural Decisions
- **Desktop Runtime (v1):** Electron (Chromium + Node.js) with isolated session partitions.
  - *Why:* Pure web browsers block third-party embedding via `X-Frame-Options` and `CSP frame-ancestors`. Personal messaging platforms (WhatsApp, Instagram, etc.) offer no open personal REST APIs. Electron allows isolated, full-fidelity local rendering.
- **Frontend:** React + Vite + TypeScript.
- **Backend:** Python + FastAPI.
- **Database:** PostgreSQL with SQLAlchemy 2.x (ORM) and Alembic (migrations).
- **Privacy Boundary (Zero Knowledge):** Third-party login cookies, credentials, and message content remain strictly on the local machine inside sandboxed Electron partitions. MinBox's PostgreSQL database only stores MinBox user accounts, hashed passwords, and pinned app configurations.

## 3. Current Phase
- **Phase 0 (Completed):** Discovery, Architecture Decisions, and Threat Model.
- **Next Phase:** Phase 1 — Repository structure, tooling, Docker + PostgreSQL setup, and initial health check endpoint.

## 4. Monorepo Folder Structure
```
MinBox/
├── apps/
│   ├── api/             # FastAPI backend (routers, models, schemas, services)
│   ├── desktop/         # Electron main process & preload scripts
│   └── web/             # React + Vite frontend (UI, components, styles)
├── docker-compose.yml   # Local PostgreSQL service
├── PROJECT_STATE.md     # Source of truth for project progress
└── README.md            # Contributing and developer guide
```

## 5. Running Concepts Learned
1. `X-Frame-Options` and `CSP frame-ancestors` (Anti-clickjacking browser headers)
2. `OAuth 2.0` (Delegated authorization protocol)
3. `Electron Architecture` (Main Node.js Process vs Renderer Chromium Process)
4. `Walled Gardens & Restricted Scopes` (Why personal messaging APIs are locked down)
5. `End-to-End Encryption (E2EE) & Client-Side Decryption` (Local decryption vs backend APIs)
6. `Electron Auto-Updater & Bundled Runtimes` (How desktop Chromium gets patched)
7. `User-Agent Header & Spoofing` (Preventing "unsupported browser" false alarms)
8. `Threat Modeling (STRIDE & Zero-Knowledge Architecture)` (Isolating sessions, securing auth)
9. `PostgreSQL Architecture` (Docker for local development vs Serverless cloud Postgres)
