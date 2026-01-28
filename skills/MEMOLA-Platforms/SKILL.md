---
name: MEMOLA-Platforms
slug: memola-platforms
description: Platform viability assessment and phased building methodology
category: strategy
complexity: complex
version: "1.0.0"
author: "MEMOLA"
parent_skill: "MEMOLA"
triggers:
  - "platform assessment"
  - "should we build a platform"
  - "platform viability"
  - "marketplace analysis"
  - "aggregator potential"
  - "platform vs service"
  - "directory opportunity"
tags:
  - platforms
  - marketplaces
  - aggregation
  - network-effects
  - phased-building
dependencies:
  skills: ["MEMOLA", "MEMOLA-Diagnosis"]
---

# MEMOLA-Platforms — Platform Viability Skill

A focused skill for assessing whether a platform should be built, and how to build it without premature scaling.

---

## 1. Purpose

MEMOLA-Platforms answers:

> **Should this be a platform? If so, how do we build it without dying?**

Platform prematurity is a known MEMOLA failure mode. This skill prevents it.

---

## 2. Platform Definition

A **platform** is infrastructure that enables value exchange between multiple parties, where the platform captures value through facilitation rather than direct service delivery.

### Platform vs Service

| Aspect | Service | Platform |
|--------|---------|----------|
| Value creation | You do the work | Others do the work through you |
| Scaling | Linear (more work = more people) | Non-linear (more users = more value) |
| Moat | Expertise/relationships | Network effects/data |
| Risk | Execution | Adoption |

### Platform Types

1. **Directories** — Organized information (lowest complexity)
2. **Marketplaces** — Transaction facilitation (medium complexity)
3. **Tools** — Workflow enablement (medium complexity)
4. **Ecosystems** — Multi-sided value networks (highest complexity)

---

## 3. Platform Viability Criteria

### Criterion 1: Problem Repetition

> **Does this problem repeat across multiple actors?**

Required evidence:
- Same problem observed in 5+ entities
- Problem is structural, not idiosyncratic
- Actors would pay to solve it

Score: 0 (unique problem) to 3 (universal problem)

### Criterion 2: Information Fragmentation

> **Is relevant information scattered and hard to aggregate?**

Required evidence:
- No single source of truth exists
- Aggregation creates value
- Information asymmetry causes friction

Score: 0 (information centralized) to 3 (severely fragmented)

### Criterion 3: Aggregation Leverage

> **Does bringing parties together create value neither could create alone?**

Required evidence:
- Clear network effect potential
- Value increases with participation
- Chicken-and-egg problem is solvable

Score: 0 (no network effect) to 3 (strong network effect)

### Criterion 4: Niche Definition

> **Is there a clearly defined initial user?**

Required evidence:
- Specific user persona identifiable
- User has budget and authority
- User is reachable through known channels

Score: 0 (vague user) to 3 (precisely defined)

### Criterion 5: MEMOLA Fit

> **Is this foundation terrain for a platform?**

Required evidence:
- Platform serves slow-decay sectors
- Trust/legitimacy matter in the space
- Platform can compound value over time

Score: 0 (camp terrain) to 3 (strong foundation)

---

## 4. Viability Scoring

### Calculate Total Score

Sum all five criteria (max 15 points).

### Decision Thresholds

| Score | Viability | Recommendation |
|-------|-----------|----------------|
| 12 - 15 | High | Proceed to phased build |
| 9 - 11 | Medium | Proceed with reduced scope |
| 6 - 8 | Low | Consider service model instead |
| 0 - 5 | None | Do not build platform |

---

## 5. The Phased Building Method

### Why Phases Matter

Platform prematurity kills:
- Building technology before proving demand
- Scaling before achieving product-market fit
- Automating before understanding the manual process

MEMOLA builds platforms in **four irreversible phases**.

### Phase 1: Manual Platform (0-6 months)

**What**: Do the platform's job manually.

Activities:
- Aggregate information by hand
- Facilitate connections personally
- Process transactions manually
- Document every friction point

Success criteria:
- 10+ successful manual transactions
- Clear pattern of value creation
- Users willing to pay for manual service

**Do NOT proceed if**: Manual version doesn't create obvious value.

### Phase 2: Assisted Platform (6-18 months)

**What**: Add tools that help YOU, not users.

Activities:
- Build internal tools for efficiency
- Create databases and tracking systems
- Develop templates and processes
- Begin light automation of repetitive tasks

Success criteria:
- 3x efficiency improvement
- 50+ active users/transactions
- Unit economics work at current scale

**Do NOT proceed if**: Efficiency gains don't materialize.

### Phase 3: Self-Service Platform (18-36 months)

**What**: Let users do what you've been doing for them.

Activities:
- Build user-facing interfaces
- Create self-service workflows
- Implement automated matching/transactions
- Develop trust/verification systems

Success criteria:
- 70%+ transactions happen without intervention
- Retention rates stable
- Marginal cost approaches zero

**Do NOT proceed if**: Users prefer the human-assisted version.

### Phase 4: Ecosystem Platform (36+ months)

**What**: Enable others to build on your platform.

Activities:
- Open APIs for third parties
- Create developer/partner programs
- Build marketplace for add-ons
- Establish platform governance

Success criteria:
- Third-party value creation exceeds your own
- Platform is defensible moat
- Network effects are measurable

---

## 6. Platform Assessment Workflow

### Step 1: Opportunity Identification

Document:
- What problem are we solving?
- Who has this problem?
- How are they solving it now?
- Why would a platform be better?

### Step 2: Criteria Scoring

Score each of the five criteria (0-3).
Sum total. Check threshold.

### Step 3: Phase Determination

If viable, determine:
- Are we starting Phase 1? (New platform)
- Are we in Phase 1 ready for Phase 2? (Existing manual operation)
- Are we already in Phase 2/3? (Existing platform)

### Step 4: Phase-Specific Planning

For current phase:
- Define success criteria
- Set timeline
- Identify risks
- Plan resources

### Step 5: Exit Conditions

Define what would cause:
- Abandonment (platform fails)
- Pivot (platform becomes service)
- Hold (pause before next phase)
- Proceed (advance to next phase)

---

## 7. Output Format

```
PLATFORM ASSESSMENT: [Platform Name]
Date: [Date]

Opportunity:
- Problem: [Description]
- Affected parties: [List]
- Current solutions: [List]

Viability Scores:
1. Problem Repetition: [X/3]
2. Information Fragmentation: [X/3]
3. Aggregation Leverage: [X/3]
4. Niche Definition: [X/3]
5. MEMOLA Fit: [X/3]

Total: [X/15]
Viability: [High/Medium/Low/None]

Recommended Phase: [1/2/3/4 or "Do Not Build"]
Timeline: [X months]
Key Success Criteria: [List]

Exit Conditions:
- Abandon if: [Condition]
- Pivot if: [Condition]
- Proceed when: [Condition]

MEMOLA Role: [Build/Advise/Invest/Partner]
```

---

## 8. Common Platform Failure Modes

### Premature Technology

Building the app before proving the value manually.

*Prevention*: Complete Phase 1 before any code.

### Chicken-Egg Paralysis

Can't get supply without demand, can't get demand without supply.

*Prevention*: Pick one side to subsidize initially. Be the supply yourself.

### Feature Creep

Adding features instead of achieving core value.

*Prevention*: Phase gates require specific criteria, not feature lists.

### Trust Vacuum

Platform can't verify quality of participants.

*Prevention*: Manual curation in Phase 1-2. Trust systems in Phase 3.

### Leakage

Users meet on platform, transact off platform.

*Prevention*: Make platform add value to every transaction, not just first.

---

## 9. MEMOLA's Platform Role

MEMOLA can engage with platforms as:

### Builder
Own and operate the platform. Highest risk, highest reward.

### Advisor
Guide platform strategy without ownership. Lower risk, recurring revenue.

### Investor
Capital + strategic support. Requires portfolio approach.

### Partner
Provide specific capabilities (content, users, expertise) to platform.

Choose role based on:
- Capital availability
- Risk tolerance
- Operational capacity
- Strategic alignment

---

## 10. Integration with MEMOLA Core

This skill supports **Workflow 3: Platform Assessment** in MEMOLA v2.0.0.

Prerequisites:
- MEMOLA-Diagnosis passed (foundation terrain confirmed)
- Strategic Diagnosis completed (problem understood)

Outputs feed into:
- System Design (if building)
- Governance Check (ownership structure)
- Execution planning (phased roadmap)

---

End of MEMOLA-Platforms SKILL.md
Version 1.0.0 — January 2026
