# MEMOLA®

**Strategic assessment system for AI-native operators.**

---

## What Is MEMOLA®?

MEMOLA® is a multi-agent strategic assessment system. It helps operators evaluate projects, platforms, and engagements before committing resources.

Born in provincial Argentina solving slow-moving institutions.
Now used by builders deploying autonomous agents.

---

## Installation

```bash
npx skills add https://github.com/josebarnetche/memola --skill MEMOLA
```

---

## Agent Hierarchy

MEMOLA® operates through a command structure with four specialized agents:

```
                         ┌─────────────────┐
                         │     MEMOR       │
                         │ Strategic Command│
                         └────────┬────────┘
                                  │
           ┌──────────────────────┼──────────────────────┐
           │                      │                      │
           ▼                      ▼                      ▼
    ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
    │    VIGIL    │       │    NEXO     │       │    PULSO    │
    │   Revenue   │       │  Operations │       │    Intel    │
    └─────────────┘       └─────────────┘       └─────────────┘
```

### MEMOR — Strategic Command
**Reports to:** Operator
**Commands:** VIGIL, NEXO, PULSO

The supreme commander. Maintains doctrine, runs weekly audits, enforces priorities, detects drift.

**Asks:** "Are we doing what we said we'd do?"

### VIGIL — Revenue & Opportunities
**Reports to:** MEMOR

Watches for money. Scans networks, qualifies opportunities, monitors client health.

**Asks:** "Where is the money?"

### NEXO — Operations & Delivery
**Reports to:** MEMOR

Ships work. Coordinates execution, tracks deliverables, manages billing.

**Asks:** "Is it shipped? Is it billed?"

### PULSO — Market Intelligence
**Reports to:** MEMOR

Reads the market. Gathers data, identifies patterns, builds intelligence.

**Asks:** "What does the data say?"

---

## Sub-Skills

| Skill | Purpose | Trigger |
|-------|---------|---------|
| **MEMOLA-Diagnosis** | Terrain assessment | `memola diagnose [project]` |
| **MEMOLA-Governance** | Authority verification | `memola governance [project]` |
| **MEMOLA-Platforms** | Platform viability | `memola platform [idea]` |
| **MEMOLA-Local** | Regional strategy | `memola local [market]` |
| **MEMOLA-Creative** | Creative industry | `memola creative [project]` |
| **memola-strategy** | Full strategic system | `memola strategy` |

---

## Quick Reference

| Command | Action |
|---------|--------|
| `memor status` | System state |
| `memor audit` | Weekly strategic audit |
| `memor terrain [project]` | Terrain classification |
| `vigil sweep` | Opportunity scan |
| `vigil qualify [lead]` | Lead assessment |
| `nexo status` | Delivery state |
| `nexo ship` | Ready deliverables |
| `pulso intel [topic]` | Gather intelligence |
| `pulso patterns` | Identified patterns |

---

## Core Concepts

### Terrain Classification

Before engagement, MEMOLA® classifies the environment:

**Foundation Terrain** — MEMOLA® applies:
- Trust compounds over time
- Legitimacy matters more than speed
- Failure looks like erosion, not explosion

**Sprint Terrain** — MEMOLA® does not apply:
- Speed determines survival
- First-mover advantage is everything
- Network effects are the only moat

### The Five Diagnostic Questions

1. Can this survive long enough for structure to matter?
2. Does failure here look like erosion, not explosion?
3. Is legitimacy more valuable than speed?
4. Will clarity actually change outcomes?
5. Does this work without going viral?

**Scoring:** 4-5 yes = proceed. 2-3 = caution. 0-1 = decline.

### Foundational Principles

1. Reality before narrative
2. Structure before execution
3. Systems before tactics
4. Assessment before commitment
5. Compounding before scale

---

## Repository Structure

```
memola/
├── README.md              # This file
├── SKILL.md               # Root authority
├── MANIFESTO.md           # Philosophy
├── LICENSE
│
├── agents/                # Agent definitions
│   ├── MEMOR.md           # Strategic command
│   ├── VIGIL.md           # Revenue intelligence
│   ├── NEXO.md            # Operations
│   └── PULSO.md           # Market intelligence
│
├── skills/                # Sub-skills
│   ├── MEMOLA-Diagnosis/
│   ├── MEMOLA-Governance/
│   ├── MEMOLA-Platforms/
│   ├── MEMOLA-Local/
│   ├── MEMOLA-Creative/
│   └── memola-strategy/
│
├── references/            # Doctrine documents
│   ├── memola-method.md
│   ├── memola-economics.md
│   ├── memola-governance.md
│   ├── memola-platforms.md
│   ├── memola-failure-modes.md
│   ├── brand-principles.md
│   ├── case-archetypes.md
│   └── diagnosis.md
│
└── .agents/               # Learning system
    ├── database/          # Pattern storage
    ├── logs/              # Session history
    └── reports/           # Analysis outputs
```

---

## Use Cases

### Pre-Deployment Assessment
Before deploying an AI agent or launching a platform:
```
memor terrain [project]
```
Assess whether the environment suits structured approaches.

### Client Qualification
Before accepting new engagements:
```
vigil qualify [lead]
```
Evaluate fit against MEMOLA® criteria.

### Strategic Audit
Weekly system health check:
```
memor audit
```
Review all agent outputs, detect drift, set priorities.

### Market Intelligence
Gather data on a topic or market:
```
pulso intel [topic]
```
Build the intelligence layer.

---

## Philosophy

MEMOLA® was born solving problems for slow-moving institutions in provincial Argentina. The framework values:

- **Precision over hype**
- **Depth over visibility**
- **Structure over improvisation**
- **Assessment over assumption**

> "Provincial origin is a feature. From the periphery, you see what centralized thinking misses."

---

## One Sentence

> **MEMOLA® doesn't make everything better — it makes the right things durable.**

---

## License

MIT

---

## Origin

**MEMOLA MEDIOS S.A.S.**
Mercedes, Corrientes, Argentina
Est. 2024

---
