---
name: MEMOLA-Governance
slug: memola-governance
description: Decision authority verification and engagement boundary setting
category: governance
complexity: moderate
version: "1.0.0"
author: "MEMOLA"
parent_skill: "MEMOLA"
triggers:
  - "governance check"
  - "decision authority"
  - "who decides"
  - "engagement boundaries"
  - "scope definition"
  - "exit conditions"
  - "should we work with this client"
tags:
  - governance
  - boundaries
  - authority
  - scope
  - ethics
  - exit-conditions
dependencies:
  skills: ["MEMOLA", "MEMOLA-Diagnosis"]
---

# MEMOLA-Governance — Boundary & Authority Skill

A focused skill for verifying decision authority, setting engagement boundaries, and defining exit conditions.

---

## 1. Purpose

MEMOLA-Governance answers:

> **Can this engagement be governed properly? Should we enter it?**

Good strategy with bad governance produces nothing. This skill prevents governance failures.

---

## 2. The Four Governance Requirements

MEMOLA requires all four to proceed:

1. **Clear Decision Authority** — Someone can say yes
2. **Defined Scope** — Boundaries are explicit
3. **Explicit Ownership** — Responsibilities are assigned
4. **Exit Conditions** — How and when to leave

Missing any one = do not proceed.

---

## 3. Decision Authority Check

### The Authority Question

> **Who can approve strategic decisions, and can they actually do it?**

### Authority Types

**Strong Authority** (Proceed):
- Founder/Owner with full control
- CEO with board alignment
- Department head with budget authority
- Single decision-maker with clear mandate

**Weak Authority** (Caution):
- Committee consensus required
- Multiple stakeholders with veto power
- Decision-maker lacks budget control
- Authority unclear or contested

**No Authority** (Decline):
- "We'll need to check with..."
- Decisions require unanimous approval
- Political environment prevents action
- Authority holder is absent/unengaged

### Authority Verification Questions

Ask directly:
1. "If we recommend X, who approves it?"
2. "What's the largest decision you can make without checking with anyone?"
3. "What happened with the last strategic initiative?"
4. "Who could block this project?"

### Red Flags

- Answers change depending on who you ask
- Authority figure never attends meetings
- "Let me get back to you" on simple decisions
- History of approved projects being reversed

---

## 4. Scope Definition

### The Scope Question

> **What exactly are we doing, and what are we explicitly NOT doing?**

### Scope Components

**Included** (explicit list):
- Deliverables with specifications
- Timelines with milestones
- Resources being committed
- Decisions within mandate

**Excluded** (explicit list):
- Adjacent work we won't do
- Decisions outside our authority
- Dependencies we don't control
- Future phases not yet approved

**Boundaries**:
- Geographic limits
- Temporal limits
- Budget limits
- Authority limits

### Scope Documentation Format

```
SCOPE: [Engagement Name]

INCLUDED:
- [Deliverable 1]: [Specification]
- [Deliverable 2]: [Specification]

EXCLUDED:
- [Item 1]: [Why excluded]
- [Item 2]: [Why excluded]

BOUNDARIES:
- Timeline: [Start] to [End]
- Budget: [Amount]
- Geography: [Limits]
- Authority: [What we can/cannot decide]

DEPENDENCIES (outside our control):
- [Dependency 1]: [Owner]
- [Dependency 2]: [Owner]
```

### Scope Creep Prevention

At engagement start:
- Document scope in writing
- Get explicit sign-off
- Define change request process

During engagement:
- Reference scope document when asked for additions
- Treat additions as new scope requiring new agreement
- Track scope creep attempts (patterns reveal governance issues)

---

## 5. Ownership Assignment

### The Ownership Question

> **Who is responsible for what, and do they accept that responsibility?**

### Ownership Matrix (RACI)

For each major deliverable/decision:

| Role | Responsible | Accountable | Consulted | Informed |
|------|-------------|-------------|-----------|----------|
| [Name] | What they do | What they own | What they advise on | What they're told |

### Critical Ownerships to Define

**Client side**:
- Project sponsor (ultimate accountability)
- Day-to-day contact (operational decisions)
- Budget holder (financial authority)
- Subject matter experts (domain input)

**MEMOLA side**:
- Engagement lead (strategy and quality)
- Delivery lead (execution and timeline)
- Specialist resources (specific expertise)

### Ownership Verification

Confirm with each owner:
1. "You're responsible for X — is that understood?"
2. "If X fails, it's on you — accepted?"
3. "You have authority to make decisions about X — confirmed?"

Document acceptances in writing.

---

## 6. Exit Conditions

### The Exit Question

> **Under what circumstances do we leave, and how do we leave cleanly?**

### Exit Triggers

**Performance exits** (we leave because of results):
- Objectives not met after [timeframe]
- Metrics below threshold for [duration]
- No measurable progress on [criteria]

**Governance exits** (we leave because of process):
- Decision authority withdrawn/unclear
- Scope expanded without agreement
- Payment terms violated
- Key personnel changed

**Ethical exits** (we leave because of values):
- Asked to do work that violates principles
- Discover misrepresentation
- Conflict of interest emerges
- Harm to third parties identified

**Strategic exits** (we leave because of fit):
- Terrain shifts from foundation to camp
- Better opportunities require focus
- Relationship no longer serves either party

### Exit Process

**Graceful exit**:
1. Document exit trigger with evidence
2. Notify client of concern
3. Offer remedy period (if appropriate)
4. Execute transition plan
5. Complete knowledge transfer
6. Final documentation

**Immediate exit** (ethical triggers only):
1. Document trigger
2. Notify client
3. Stop work immediately
4. No transition obligation

### Exit Documentation

```
EXIT CONDITIONS: [Engagement Name]

PERFORMANCE TRIGGERS:
- If [metric] < [threshold] for [duration], exit
- If [objective] not achieved by [date], exit

GOVERNANCE TRIGGERS:
- If decision authority becomes unclear, exit
- If scope changes without agreement, exit
- If payment delayed > [days], pause then exit

ETHICAL TRIGGERS:
- If asked to [specific action], exit immediately
- If [misrepresentation] discovered, exit immediately

PROCESS:
- Notice period: [X days/weeks]
- Transition requirements: [List]
- Final deliverables: [List]
```

---

## 7. Governance Assessment Workflow

### Step 1: Authority Verification

- Identify claimed decision-maker
- Ask verification questions
- Test with small decision
- Document authority structure

### Step 2: Scope Definition

- Draft scope document
- Review with client
- Negotiate boundaries
- Get written sign-off

### Step 3: Ownership Assignment

- Create RACI matrix
- Confirm with each owner
- Document acceptances
- Identify gaps

### Step 4: Exit Condition Setting

- Define all trigger types
- Set specific thresholds
- Document process
- Get mutual agreement

### Step 5: Governance Ruling

Issue one of:
- **CLEARED**: All four requirements met
- **CONDITIONAL**: Requirements met with noted concerns
- **NOT CLEARED**: One or more requirements failed

---

## 8. Output Format

```
GOVERNANCE CHECK: [Engagement/Entity Name]
Date: [Date]

DECISION AUTHORITY:
- Decision-maker: [Name/Role]
- Authority type: [Strong/Weak/None]
- Verification: [How confirmed]
- Concerns: [Any red flags]

SCOPE:
- Defined: [Yes/No/Partial]
- Documented: [Yes/No]
- Signed off: [Yes/No]
- Exclusions clear: [Yes/No]

OWNERSHIP:
- RACI completed: [Yes/No]
- Acceptances documented: [Yes/No]
- Gaps identified: [List]

EXIT CONDITIONS:
- Performance triggers: [Defined/Not defined]
- Governance triggers: [Defined/Not defined]
- Ethical triggers: [Defined/Not defined]
- Process documented: [Yes/No]

RULING: [CLEARED / CONDITIONAL / NOT CLEARED]

Conditions (if CONDITIONAL):
- [Condition 1]
- [Condition 2]

Reasons (if NOT CLEARED):
- [Reason 1]
- [Reason 2]
```

---

## 9. Governance Patterns

### Pattern: The Phantom Sponsor

Project has nominal sponsor who never engages. Real decisions made by committee or not at all.

*Detection*: Sponsor doesn't attend key meetings, decisions get reversed, "checking with sponsor" never resolves.

*Response*: Require sponsor presence or decline.

### Pattern: The Expanding Mandate

Scope creeps through small additions until original engagement is unrecognizable.

*Detection*: "While you're at it..." requests, deliverables grow without budget growth.

*Response*: Rigorous scope documentation, change request process enforcement.

### Pattern: The Responsibility Vacuum

Everyone assumes someone else is responsible. Nothing gets owned.

*Detection*: Finger-pointing when things fail, unclear RACI, "I thought you were handling that."

*Response*: Written ownership acceptance before proceeding.

### Pattern: The Inescapable Engagement

No exit conditions defined. Leaving damages relationship. Staying wastes resources.

*Detection*: Discomfort discussing exit scenarios, "we'll figure it out," relationship-based instead of contract-based.

*Response*: Exit conditions are non-negotiable entry requirement.

---

## 10. Integration with MEMOLA Core

This skill supports **Workflow 4: Governance Check** in MEMOLA v2.0.0.

Prerequisites:
- MEMOLA-Diagnosis passed (terrain confirmed)
- Strategic opportunity identified

Outputs:
- CLEARED → Proceed to engagement
- CONDITIONAL → Address conditions first
- NOT CLEARED → Decline or restructure

Governance check is **required before any paid engagement**.

---

## 11. MEMOLA Refusals

MEMOLA governance requires refusing:

- **"Just execution"** — Strategy without implementation authority
- **Committee paralysis** — No clear decision path
- **Metric theater** — Reporting without action authority
- **Ethical ambiguity** — Unclear alignment with values

These are non-negotiable. No governance structure fixes these.

---

End of MEMOLA-Governance SKILL.md
Version 1.0.0 — January 2026
