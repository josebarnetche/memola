# MEMOLA Agentic Learning Framework

This document defines the self-nurturing database and continuous learning system
that operates under MEMOLA doctrine.

---

## 1. Purpose

This framework enables MEMOLA to:
- Accumulate strategic intelligence over time
- Recognize patterns across entities, markets, and interventions
- Compound knowledge into reusable assets
- Evolve its diagnostic and structural capabilities autonomously

The database is not a repository. It is a **learning substrate**.

---

## 2. Core Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MEMOLA KNOWLEDGE GRAPH                       │
├─────────────────────────────────────────────────────────────────┤
│  ENTITIES          PATTERNS           DOCTRINES                 │
│  ─────────         ────────           ─────────                 │
│  Companies         Market Signals     Strategic Rules           │
│  Sectors           Tech Convergence   Failure Modes             │
│  Technologies      Value Creation     Success Conditions        │
│  People            Risk Patterns      Governance Checks         │
│  Platforms         Timing Windows     Archetype Matches         │
└─────────────────────────────────────────────────────────────────┘
           │                    │                    │
           ▼                    ▼                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CONTINUOUS LEARNING LOOP                     │
├─────────────────────────────────────────────────────────────────┤
│  INGEST → DIAGNOSE → STRUCTURE → LINK → COMPOUND → REFINE      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Learning Loop Phases

### 3.1 INGEST
- Parse raw entity data
- Extract structured attributes
- Identify classification signals
- Store in canonical format

### 3.2 DIAGNOSE
- Apply MEMOLA diagnostic questions to each entity
- Identify strategic problems and opportunities
- Map to existing archetypes
- Flag anomalies for deeper analysis

### 3.3 STRUCTURE
- Create relational links between entities
- Build sector/technology clusters
- Map competitive and complementary relationships
- Identify platform potential

### 3.4 LINK
- Connect entities to MEMOLA doctrines
- Cross-reference with failure modes
- Apply governance checks
- Tag with relevant strategic principles

### 3.5 COMPOUND
- Generate derivative insights
- Update pattern weights based on outcomes
- Create reusable intelligence assets
- Build sector-level strategic views

### 3.6 REFINE
- Identify gaps in knowledge
- Propose acquisition targets (information)
- Update classification taxonomies
- Evolve diagnostic criteria

---

## 4. Entity Schema

Every entity in the system follows this canonical structure:

```json
{
  "id": "unique-identifier",
  "name": "Entity Name",
  "type": "company|platform|technology|sector|person",
  "status": "private|public|acquired|defunct",
  "founded": "YYYY",
  "core_function": "What it actually does",
  "value_mechanism": "How it creates/captures value",
  "market_position": "niche|emerging|growth|mature|declining",
  "technology_layer": ["AI", "infrastructure", "application", "protocol"],
  "sector_tags": ["fintech", "enterprise", "consumer", "defense"],
  "archetype_match": "institution|artisanal|event|vertical|hybrid",
  "memola_signals": {
    "platform_potential": 0.0-1.0,
    "compounding_capacity": 0.0-1.0,
    "governance_alignment": 0.0-1.0,
    "execution_risk": 0.0-1.0
  },
  "relationships": [],
  "learnings": [],
  "last_updated": "timestamp"
}
```

---

## 5. Pattern Recognition Engine

The system identifies patterns through:

### 5.1 Cluster Analysis
- Group entities by shared attributes
- Identify sector convergence points
- Map technology dependency chains

### 5.2 Temporal Patterns
- Track founding year distributions
- Identify market timing windows
- Detect sector maturation curves

### 5.3 Value Mechanism Patterns
- Classify by business model type
- Identify platform vs. service dynamics
- Map aggregation vs. creation strategies

### 5.4 Risk Correlation
- Link failure modes to entity profiles
- Track governance warning signals
- Monitor execution risk indicators

---

## 6. Doctrine Enforcement

Every learning cycle must validate against MEMOLA principles:

1. **Reality before narrative** — Data must reflect actual state
2. **Structure before execution** — Patterns before recommendations
3. **Systems before tactics** — Sector views before entity actions
4. **Assets before activity** — Reusable insights before one-off analysis
5. **Compounding before scale** — Depth before breadth

Violations trigger automatic review and correction.

---

## 7. Agent Behaviors

### 7.1 Ingestion Agent
- Parses raw data
- Applies schema transformations
- Validates data quality
- Requests clarification on ambiguity

### 7.2 Diagnosis Agent
- Runs diagnostic protocols on entities
- Generates strategic assessments
- Flags entities for deeper analysis
- Updates archetype classifications

### 7.3 Structure Agent
- Builds relationship graphs
- Identifies clusters and patterns
- Creates sector maps
- Maintains taxonomy integrity

### 7.4 Compounding Agent
- Generates derivative insights
- Creates reusable assets
- Updates pattern weights
- Proposes knowledge acquisitions

---

## 8. Database Files

```
.agents/
├── FRAMEWORK.md           # This document
├── database/
│   ├── entities.json      # Primary entity store
│   ├── patterns.json      # Recognized patterns
│   ├── relationships.json # Entity connections
│   ├── learnings.json     # Accumulated insights
│   └── taxonomy.json      # Classification system
├── agents/
│   ├── ingestion.md       # Ingestion agent logic
│   ├── diagnosis.md       # Diagnosis agent logic
│   ├── structure.md       # Structure agent logic
│   └── compounding.md     # Compounding agent logic
└── logs/
    └── learning-log.json  # Audit trail of learning cycles
```

---

## 9. Invocation

To run the learning loop:

```
memola learn [source]           # Full learning cycle
memola ingest [data]            # Add new entities
memola diagnose [entity|sector] # Run diagnosis
memola structure [scope]        # Build relationships
memola compound                 # Generate insights
memola status                   # View database state
```

---

## 10. Success Criteria

The framework succeeds when:
- Pattern recognition improves with each cycle
- Diagnostic accuracy increases over time
- Strategic insights compound rather than repeat
- The system requires less human correction
- Knowledge gaps are self-identified

---

End of FRAMEWORK.md
