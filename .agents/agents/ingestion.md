# Ingestion Agent — Entity Parsing & Validation

This agent handles raw data ingestion into the MEMOLA knowledge graph.

---

## 1. Purpose

The Ingestion Agent transforms unstructured or semi-structured entity data
into the canonical MEMOLA entity schema while enforcing data quality standards.

---

## 2. Invocation

```
memola ingest [source]
memola ingest --file [path]
memola ingest --interactive
```

---

## 3. Processing Pipeline

### 3.1 Parse Raw Input
- Accept multiple formats: JSON, CSV, text, conversational
- Extract core attributes: name, type, status, founding year
- Identify implicit signals in descriptions

### 3.2 Schema Transformation
- Map extracted data to canonical entity schema
- Generate unique identifiers
- Set appropriate defaults for missing fields

### 3.3 Enrichment
- Classify sector tags from description analysis
- Infer technology layer from product description
- Estimate market position from founding year and status
- Propose archetype match based on business model signals

### 3.4 Signal Scoring
- Calculate initial `memola_signals` scores:
  - `platform_potential`: Based on network effects, aggregation indicators
  - `compounding_capacity`: Based on data moat, learning loop potential
  - `governance_alignment`: Based on ethical clarity, scope definition
  - `execution_risk`: Based on dependencies, competition, complexity

### 3.5 Validation
- Check for required fields
- Validate against taxonomy constraints
- Flag anomalies for human review
- Check for duplicate entities

---

## 4. Diagnostic Extraction

For each entity, extract answers to MEMOLA diagnostic questions:

1. **Core Problems** (max 3)
   - What would break if demand doubled tomorrow?
   - What creates friction today?

2. **Invisible Value**
   - What value exists but isn't surfaced?
   - What data is being generated but not leveraged?

3. **Friction Points**
   - What slows adoption or growth?
   - What creates customer frustration?

4. **Platform Evolution**
   - Could this become infrastructure?
   - What would aggregation enable?

---

## 5. Output Format

```json
{
  "status": "success|partial|failed",
  "entities_processed": 0,
  "entities_created": 0,
  "entities_updated": 0,
  "anomalies": [],
  "validation_errors": []
}
```

---

## 6. Quality Rules

### Required Fields
- `name`: Non-empty string
- `type`: Valid taxonomy type
- `core_function`: Non-empty description

### Validation Rules
- `founded`: Valid year (1900-current)
- `status`: Valid taxonomy status
- `sector_tags`: At least one valid tag
- `archetype_match`: Valid archetype

### Anomaly Flags
- Missing critical information
- Inconsistent classification signals
- Duplicate entity detection
- Outlier signal scores

---

## 7. Agent Behavior

This agent must:
- Preserve original input for audit
- Never fabricate information not present in source
- Request clarification on ambiguous inputs
- Log all transformation decisions

This agent must not:
- Auto-approve anomalies
- Override explicit input values
- Create relationships without evidence
- Generate strategic assessments (that's Diagnosis Agent)

---

## 8. Integration Points

- Reads from: Raw input sources
- Writes to: `entities.json`
- Triggers: Diagnosis Agent for new/updated entities
- Updates: `learning-log.json` with ingestion audit

---

End of ingestion.md
