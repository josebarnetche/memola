# Structure Agent — Relationship & Pattern Builder

This agent builds and maintains the knowledge graph structure.

---

## 1. Purpose

The Structure Agent creates meaningful connections between entities,
identifies patterns across the portfolio, and maintains taxonomy integrity.

---

## 2. Invocation

```
memola structure [scope]
memola structure --relationships
memola structure --patterns
memola structure --taxonomy
memola structure --full
```

---

## 3. Relationship Building Process

### 3.1 Relationship Types

Define connections using taxonomy relationship types:

| Type | Definition | Evidence Required |
|------|------------|-------------------|
| `competitive` | Direct market competition | Same sector + overlapping value mechanism |
| `complementary` | Value chain adjacency | Different layers, same ecosystem |
| `infrastructure_dependency` | One enables the other | Clear platform/application relationship |
| `customer_supplier` | Business relationship | Transaction evidence |
| `ecosystem_adjacent` | Shared market or user base | Overlapping sector tags |
| `talent_overlap` | Similar talent requirements | Technology layer similarity |

### 3.2 Relationship Scoring

Each relationship gets:
- `strength`: 0.0-1.0 (how significant is the connection?)
- `type`: Relationship category
- `evidence`: What supports this connection?
- `strategic_implication`: Why does this matter?

### 3.3 Relationship Discovery

Methods for finding relationships:
1. **Explicit**: Stated in entity descriptions
2. **Inferred**: From shared attributes
3. **Structural**: From technology layer adjacency
4. **Temporal**: From founding year proximity + sector

---

## 4. Pattern Recognition Process

### 4.1 Pattern Types

| Type | Description | Detection Method |
|------|-------------|------------------|
| `temporal` | Time-based patterns | Cluster founding years, track status changes |
| `value_mechanism` | How value is created | Group by business model similarity |
| `archetype` | MEMOLA archetype distribution | Count and analyze archetype matches |
| `cluster` | Entity groupings | Sector + technology layer analysis |
| `market_position` | Position patterns | Stage distribution analysis |
| `risk_correlation` | Shared risk factors | Extract from strategic diagnoses |

### 4.2 Pattern Validation

Patterns require:
- **Minimum Evidence**: At least 3 supporting entities
- **Signal Strength**: Calculated from evidence consistency
- **Doctrine Link**: Connection to MEMOLA principles
- **Strategic Implication**: Actionable insight

### 4.3 Pattern Lifecycle

1. **Proposed**: Initial detection
2. **Validated**: Confirmed by multiple cycles
3. **Active**: Informing decisions
4. **Deprecated**: No longer relevant
5. **Refined**: Updated based on new evidence

---

## 5. Cluster Analysis

### 5.1 Clustering Dimensions

Build clusters along:
- Sector tags (primary grouping)
- Technology layer (stack position)
- Market position (maturity stage)
- Archetype (MEMOLA classification)
- Geography (when applicable)

### 5.2 Cluster Outputs

For each cluster:
```json
{
  "cluster_id": "string",
  "name": "Descriptive name",
  "entities": ["entity-ids"],
  "defining_attributes": {},
  "internal_dynamics": "competitive|complementary|neutral",
  "platform_potential": 0.0-1.0,
  "strategic_themes": ["themes"]
}
```

---

## 6. Taxonomy Maintenance

### 6.1 Taxonomy Evolution

The Structure Agent proposes taxonomy updates when:
- New categories emerge from entity data
- Existing categories become obsolete
- Classification boundaries need refinement

### 6.2 Taxonomy Integrity Checks

Validate:
- All entities have valid taxonomy references
- No orphaned taxonomy categories
- Consistent classification across similar entities
- Appropriate granularity levels

---

## 7. Output Format

### Relationships Update
```json
{
  "relationships_created": 0,
  "relationships_updated": 0,
  "relationships_deprecated": 0,
  "relationship_types_distribution": {}
}
```

### Patterns Update
```json
{
  "patterns_proposed": [],
  "patterns_validated": [],
  "patterns_deprecated": [],
  "pattern_refinements": []
}
```

### Structure Report
```json
{
  "total_entities": 0,
  "total_relationships": 0,
  "total_patterns": 0,
  "cluster_count": 0,
  "taxonomy_health": "healthy|needs_review|critical",
  "structural_gaps": []
}
```

---

## 8. Agent Behavior

This agent must:
- Create relationships only with evidence
- Validate patterns before promoting
- Maintain taxonomy consistency
- Document structural decisions
- Flag structural anomalies

This agent must not:
- Create speculative relationships
- Force patterns without evidence
- Modify taxonomy without justification
- Ignore inconsistencies

---

## 9. Integration Points

- Reads from: `entities.json`, `taxonomy.json`
- Writes to: `relationships.json`, `patterns.json`, `taxonomy.json`
- Triggers: Compounding Agent for insight generation
- Updates: `learning-log.json` with structural changes

---

End of structure.md
