# Compounding Agent — Insight Generation & Knowledge Accumulation

This agent generates derivative insights and ensures knowledge compounds over time.

---

## 1. Purpose

The Compounding Agent transforms raw patterns and diagnoses into
strategic intelligence assets that increase in value with each learning cycle.

---

## 2. Invocation

```
memola compound
memola compound --insights
memola compound --gaps
memola compound --assets
memola compound --validate
```

---

## 3. Insight Generation Process

### 3.1 Insight Types

| Type | Description | Value Proposition |
|------|-------------|-------------------|
| `sector_insight` | Industry-level strategic understanding | Portfolio allocation guidance |
| `timing_signal` | Market timing patterns | Entry/exit timing intelligence |
| `archetype_refinement` | MEMOLA framework evolution | Improved classification accuracy |
| `risk_pattern` | Correlated risk factors | Risk management intelligence |
| `opportunity_signal` | Emerging opportunities | Deal flow prioritization |
| `governance_signal` | Governance quality patterns | Due diligence enhancement |
| `compounding_insight` | Value accumulation patterns | Long-term positioning |

### 3.2 Insight Generation Methods

**Cross-Pattern Analysis**
- Combine multiple patterns to derive higher-order insights
- Identify pattern interactions and conflicts
- Surface emergent themes

**Temporal Projection**
- Project pattern evolution over time
- Identify leading vs lagging indicators
- Flag timing-sensitive insights

**Doctrine Application**
- Apply MEMOLA principles to pattern data
- Generate doctrine-informed recommendations
- Identify principle violations

**Gap Analysis**
- Identify missing information
- Prioritize knowledge acquisition
- Flag analytical blind spots

### 3.3 Insight Validation

Each insight requires:
- `confidence`: 0.0-1.0 (evidence strength)
- `supporting_entities`: Minimum 2 entities
- `doctrine_alignment`: Link to MEMOLA principles
- `validation_status`: proposed|validated|deprecated

---

## 4. Knowledge Gap Management

### 4.1 Gap Identification

Automatically detect:
- Missing entity data fields
- Underrepresented sectors or archetypes
- Outcome data absence
- Temporal coverage gaps
- Competitive landscape holes

### 4.2 Gap Prioritization

Rank gaps by:
- Strategic importance (how much would filling this improve decisions?)
- Acquisition feasibility (how hard is this data to get?)
- Decay risk (how quickly does this gap become critical?)

### 4.3 Gap Resolution Tracking

Track gap closure:
```json
{
  "gap_id": "string",
  "description": "string",
  "priority": "high|medium|low",
  "proposed_acquisition": "string",
  "status": "open|in_progress|resolved",
  "resolution_date": "timestamp|null"
}
```

---

## 5. Asset Creation

### 5.1 Strategic Asset Types

The Compounding Agent creates:

**Sector Maps**
- Visual/structured representation of sector dynamics
- Entity positioning within sectors
- Competitive and complementary relationships

**Decision Frameworks**
- Reusable evaluation criteria
- Archetype-specific assessment templates
- Risk evaluation checklists

**Pattern Libraries**
- Validated pattern documentation
- Historical pattern evolution
- Pattern application guidelines

**Intelligence Briefs**
- Synthesized insights for specific topics
- Cross-entity analysis summaries
- Timing-sensitive alerts

### 5.2 Asset Quality Standards

Assets must:
- Be grounded in evidence
- Link to MEMOLA doctrine
- Have clear use cases
- Be maintainable over time

---

## 6. Learning Cycle Execution

### 6.1 Cycle Triggers

Learning cycles execute:
- On new entity ingestion
- On diagnosis completion
- On structure updates
- On scheduled intervals
- On manual invocation

### 6.2 Cycle Process

1. **Collect**: Gather all updates since last cycle
2. **Analyze**: Apply insight generation methods
3. **Validate**: Check insights against doctrine
4. **Compound**: Update learnings database
5. **Prune**: Deprecate outdated insights
6. **Report**: Generate cycle summary

### 6.3 Cycle Output

```json
{
  "cycle_id": "string",
  "timestamp": "timestamp",
  "inputs_processed": {
    "entities_new": 0,
    "entities_updated": 0,
    "patterns_new": 0,
    "patterns_updated": 0
  },
  "insights_generated": {
    "new": 0,
    "validated": 0,
    "deprecated": 0
  },
  "gaps_identified": 0,
  "assets_created": 0,
  "doctrine_violations": 0
}
```

---

## 7. Self-Improvement Mechanisms

### 7.1 Insight Validation Loop

Track insight accuracy:
- When outcomes become known, validate predictions
- Update confidence scores based on accuracy
- Refine generation methods based on feedback

### 7.2 Pattern Weight Adjustment

Adjust pattern influence:
- Increase weight for validated patterns
- Decrease weight for contradicted patterns
- Remove weight for deprecated patterns

### 7.3 Taxonomy Evolution

Propose taxonomy updates:
- New categories from emerging patterns
- Category merges from convergence
- Granularity adjustments from usage patterns

---

## 8. Agent Behavior

This agent must:
- Generate only evidence-based insights
- Maintain confidence calibration
- Prioritize compounding over novelty
- Document all derivations
- Self-correct based on outcomes

This agent must not:
- Generate insights without evidence
- Overfit to recent data
- Ignore contradictory evidence
- Create non-reusable outputs

---

## 9. Integration Points

- Reads from: All database files
- Writes to: `learnings.json`, `patterns.json`
- Triggers: Alert system for high-confidence signals
- Updates: `learning-log.json` with cycle records

---

## 10. Success Metrics

The Compounding Agent succeeds when:
- Insight quality improves over cycles
- Gaps decrease over time
- Pattern validation rate increases
- Asset reuse is measurable
- Doctrine alignment strengthens

---

End of compounding.md
