---
name: MEMOLA-Diagnosis
slug: memola-diagnosis
description: Terrain assessment and regime classification for strategic fit analysis
category: strategy
complexity: moderate
version: "1.0.0"
author: "MEMOLA"
parent_skill: "MEMOLA"
triggers:
  - "terrain assessment"
  - "regime fit"
  - "diagnostic questions"
  - "castle or camp"
  - "should we take this client"
  - "is this MEMOLA terrain"
  - "fit analysis"
tags:
  - diagnosis
  - terrain-classification
  - regime-analysis
  - client-screening
  - strategic-fit
dependencies:
  skills: ["MEMOLA"]
---

# MEMOLA-Diagnosis — Terrain Assessment Skill

A focused skill for determining whether an opportunity, client, or market fits MEMOLA methodology.

---

## 1. Purpose

MEMOLA-Diagnosis answers one question:

> **Is this MEMOLA terrain?**

Before any engagement, before any strategy, before any execution — run this diagnostic.

---

## 2. The Two Terrains

### Castle Terrain (MEMOLA Applies)

Characteristics:
- Failure mode: slow erosion over years
- Trust compounds and transfers
- Legitimacy > speed
- Reputation outlasts hype cycles
- History creates advantage

Examples:
- Institutions (100+ year organizations)
- Heritage brands (family businesses, artisanal producers)
- Professional services (law, medicine, consulting)
- Regional anchors (rural cooperatives, local media)
- Cultural organizations (museums, foundations)

### Camp Terrain (MEMOLA Does NOT Apply)

Characteristics:
- Failure mode: sudden death
- Speed determines survival
- First-mover advantage dominates
- Network effects are the only moat
- Pivoting is the primary skill

Examples:
- Consumer apps
- Viral products
- Speculative ventures
- Growth-at-all-costs startups
- Trend-dependent businesses

---

## 3. The Five Diagnostic Questions

### Question 1: Survival Horizon

> **Can this survive long enough for structure to matter?**

Scoring:
- 10+ year likely survival → YES (1 point)
- 5-10 year horizon → PARTIAL (0.5 points)
- <5 year or uncertain → NO (0 points)

Red flags:
- Runway < 18 months
- Dependent on single funding round
- No clear path to sustainability

### Question 2: Failure Mode

> **Does failure here look like erosion, not explosion?**

Scoring:
- Gradual decline over years → YES (1 point)
- Mixed or uncertain → PARTIAL (0.5 points)
- Sudden collapse possible → NO (0 points)

Red flags:
- Single point of failure
- Platform dependency
- Regulatory cliff
- Key person risk without succession

### Question 3: Legitimacy vs Speed

> **Is legitimacy more valuable than speed?**

Scoring:
- Trust/reputation is primary asset → YES (1 point)
- Both matter equally → PARTIAL (0.5 points)
- Speed/timing is primary → NO (0 points)

Red flags:
- "We need to launch before competitor"
- "First to market wins"
- "Move fast and break things" culture

### Question 4: Clarity Impact

> **Will clarity actually change outcomes?**

Scoring:
- Strategic clarity directly improves results → YES (1 point)
- Clarity helps but isn't decisive → PARTIAL (0.5 points)
- Execution/luck matters more than strategy → NO (0 points)

Red flags:
- "We just need to execute"
- No decision-making authority
- Strategy disconnected from operations

### Question 5: Virality Independence

> **Does this work without going viral?**

Scoring:
- Success doesn't require virality → YES (1 point)
- Virality helps but isn't required → PARTIAL (0.5 points)
- Must go viral to survive → NO (0 points)

Red flags:
- Business model requires exponential growth
- No path to profitability without scale
- Depends on network effects not yet present

---

## 4. Scoring and Interpretation

### Calculate Total Score

Sum all five questions (max 5 points).

### Decision Thresholds

| Score | Classification | Recommendation |
|-------|---------------|----------------|
| 4.5 - 5.0 | Strong Castle | Proceed with full MEMOLA |
| 3.5 - 4.0 | Castle-Leaning | Proceed with attention |
| 2.5 - 3.0 | Mixed Terrain | Caution — scope carefully |
| 1.5 - 2.0 | Camp-Leaning | Likely decline |
| 0.0 - 1.0 | Strong Camp | Decline — wrong terrain |

### Override Conditions

Even with high scores, decline if:
- No clear decision authority exists
- Ethical concerns present
- Payment/governance structure problematic
- Scope cannot be defined

---

## 5. Diagnostic Workflow

### Step 1: Gather Initial Information

Required inputs:
- Entity type (company, institution, project, individual)
- Age/history
- Business model basics
- Why they're seeking help
- Who makes decisions

### Step 2: Run Five Questions

Ask each question. Score honestly.
Document reasoning for each score.

### Step 3: Calculate and Classify

Sum scores. Apply thresholds.
Classify as Castle, Mixed, or Camp.

### Step 4: Identify Red Flags

Review for override conditions.
Note any concerns regardless of score.

### Step 5: Generate Recommendation

Output format:
```
TERRAIN ASSESSMENT: [Entity Name]
Date: [Date]

Scores:
1. Survival Horizon: [X/1] — [reasoning]
2. Failure Mode: [X/1] — [reasoning]
3. Legitimacy vs Speed: [X/1] — [reasoning]
4. Clarity Impact: [X/1] — [reasoning]
5. Virality Independence: [X/1] — [reasoning]

Total: [X/5]
Classification: [Castle/Mixed/Camp]

Red Flags: [List or "None identified"]

Recommendation: [Proceed/Proceed with caution/Decline]
Reasoning: [1-2 sentences]
```

---

## 6. Quick Diagnostic (2-Minute Version)

When full assessment isn't possible, ask:

1. **How old is this entity?** (<3 years = camp signal)
2. **What happens if they do nothing for 6 months?** (Death = camp, decline = castle)
3. **Who decides?** (Committee = caution, clear authority = proceed)

If all three pass → likely castle terrain.
If any fail → run full diagnostic.

---

## 7. Common Patterns

### Pattern: The Disguised Camp

Looks like castle (old institution) but operates like camp (desperate for quick results, no patience for structure).

*Diagnostic tell*: Question 3 scores low despite institutional age.

### Pattern: The Premature Castle

Young entity trying to build castle in camp terrain. Good intentions, wrong environment.

*Diagnostic tell*: High scores on Q3-Q5 but Q1 scores low.

### Pattern: The Eroding Castle

Once-strong castle terrain now shifting to camp (industry disruption, regulatory change).

*Diagnostic tell*: Historical castle indicators but current scores declining.

---

## 8. Integration with MEMOLA Core

This skill is **Workflow 0** in MEMOLA v2.0.0.

After terrain assessment passes:
- Proceed to Strategic Diagnosis (Workflow 1)
- Apply full MEMOLA method

If terrain assessment fails:
- Decline engagement
- Or recommend alternative approach outside MEMOLA

---

## 9. Skill Boundaries

MEMOLA-Diagnosis does:
- Classify terrain
- Score fit
- Recommend proceed/decline

MEMOLA-Diagnosis does NOT:
- Design strategy
- Create structures
- Execute tactics

For those, use core MEMOLA skill after diagnosis passes.

---

End of MEMOLA-Diagnosis SKILL.md
Version 1.0.0 — January 2026
