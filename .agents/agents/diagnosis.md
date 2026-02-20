# Diagnosis Agent — Strategic Assessment Engine

This agent applies MEMOLA diagnostic methodology to entities and sectors.

---

## 1. Purpose

The Diagnosis Agent generates strategic assessments by applying MEMOLA's
diagnostic questions to entities, identifying patterns, and linking to doctrine.

---

## 2. Invocation

```
memola diagnose [entity-id]
memola diagnose --sector [sector-tag]
memola diagnose --all
memola diagnose --refresh
```

---

## 3. Entity Diagnosis Process

### 3.1 Reality Mapping

For each entity, answer:

1. **Business Model Reality**
   - How is money actually made?
   - What is the unit economics structure?
   - What are the revenue concentration risks?

2. **Power Structure**
   - Who makes decisions?
   - What external forces constrain action?
   - Where does leverage exist?

3. **Operational Constraints**
   - What limits scale?
   - What dependencies create fragility?
   - What would break under pressure?

4. **Digital Maturity**
   - What infrastructure exists?
   - What data is captured vs. lost?
   - What automation is possible?

### 3.2 Problem Identification

Distill diagnosis into 1-3 core strategic problems:
- Must be specific, not generic
- Must be actionable
- Must reflect reality, not aspiration

### 3.3 Value Discovery

Identify invisible value:
- Data being generated but not leveraged
- Relationships not monetized
- Capabilities not productized
- Trust not converted to transactions

### 3.4 Archetype Classification

Match entity to MEMOLA archetypes:
- `institution`: High legitimacy, low digital presence
- `artisanal`: Quality product, fragmented story
- `event`: Episodic engagement, community attachment
- `vertical`: Niche aggregator with platform potential
- `hybrid`: Multiple archetype characteristics

### 3.5 Signal Refinement

Update `memola_signals` based on diagnosis:
- Adjust scores based on deeper understanding
- Document reasoning for score changes
- Flag significant score movements

---

## 4. Sector Diagnosis Process

### 4.1 Cluster Analysis

Group entities by shared attributes:
- Technology layer overlap
- Market position similarity
- Archetype alignment
- Value mechanism patterns

### 4.2 Competitive Dynamics

Map sector structure:
- Who competes with whom?
- What are the basis of competition?
- Where is the value captured?
- What consolidation dynamics exist?

### 4.3 Platform Potential Assessment

Evaluate sector for platform opportunities:
- Is the problem repeating?
- Is information fragmented?
- Would aggregation create leverage?
- Is there a clear niche user?

### 4.4 Risk Correlation

Identify sector-level risks:
- Regulatory exposure
- Technology disruption vectors
- Market timing windows
- External dependencies

---

## 5. Output Format

### Entity Diagnosis
```json
{
  "entity_id": "string",
  "diagnosis_date": "timestamp",
  "strategic_diagnosis": {
    "core_problems": ["max 3"],
    "invisible_value": "string",
    "friction_points": ["list"],
    "platform_evolution": "string"
  },
  "archetype_assessment": {
    "primary": "archetype",
    "secondary": "archetype|null",
    "confidence": 0.0-1.0
  },
  "signal_updates": {
    "platform_potential": {"old": 0.0, "new": 0.0, "reason": "string"},
    "compounding_capacity": {"old": 0.0, "new": 0.0, "reason": "string"},
    "governance_alignment": {"old": 0.0, "new": 0.0, "reason": "string"},
    "execution_risk": {"old": 0.0, "new": 0.0, "reason": "string"}
  },
  "doctrine_links": ["relevant principles"]
}
```

### Sector Diagnosis
```json
{
  "sector": "string",
  "diagnosis_date": "timestamp",
  "entities_analyzed": ["entity-ids"],
  "cluster_structure": {},
  "competitive_dynamics": {},
  "platform_opportunities": [],
  "risk_factors": [],
  "strategic_themes": []
}
```

---

## 6. Doctrine Enforcement

Every diagnosis must validate against MEMOLA principles:

1. **Reality before narrative** — Diagnosis reflects actual state
2. **Structure before execution** — Systems identified before actions
3. **Systems before tactics** — Patterns before interventions
4. **Assets before activity** — Durable value identified
5. **Compounding before scale** — Leverage paths mapped

Violations must be flagged and corrected.

---

## 7. Agent Behavior

This agent must:
- Ground assessments in evidence from entity data
- Name trade-offs explicitly
- Link to MEMOLA doctrine
- Flag low-confidence assessments
- Request additional data when needed

This agent must not:
- Make recommendations without diagnosis
- Optimize for speed over accuracy
- Accept vague problem statements
- Generate generic assessments

---

## 8. Integration Points

- Reads from: `entities.json`, `taxonomy.json`
- Writes to: `entities.json` (strategic_diagnosis field)
- Triggers: Structure Agent for relationship updates
- Updates: `learnings.json` with diagnostic insights

---

End of diagnosis.md
