# MEMOLA Governance Council

**Version:** 1.0
**Authority:** Required for all public repository operations
**Principle:** No commit without unanimous council approval

---

## Council Structure

```
                    ┌─────────────────────┐
                    │      COUNCIL        │
                    │  Unanimous Required │
                    └──────────┬──────────┘
                               │
       ┌───────────┬───────────┼───────────┬───────────┐
       │           │           │           │           │
       ▼           ▼           ▼           ▼           ▼
   ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐
   │MEMOR  │   │VIGIL  │   │NEXO   │   │PULSO  │   │CENTINELA│
   │Strategy│   │Revenue│   │Ops    │   │Intel  │   │Security│
   └───────┘   └───────┘   └───────┘   └───────┘   └───────┘
```

---

## Council Members & Responsibilities

### MEMOR — Strategic Veto
**Question:** "Does this align with what we committed to?"
**Checks:**
- [ ] Aligns with MEMOLA doctrine
- [ ] No scope creep beyond approved plan
- [ ] Maintains brand positioning
- [ ] No premature commitments

**Veto triggers:**
- Contradicts stated strategy
- Commits to deliverables not approved
- Damages positioning

---

### VIGIL — Revenue & Client Protection
**Question:** "Does this expose client relationships or revenue intelligence?"
**Checks:**
- [ ] No client names without approval
- [ ] No prospect databases
- [ ] No pricing strategies meant to be internal
- [ ] No pipeline or deal information
- [ ] No client contact details

**Veto triggers:**
- Real client data exposed
- Prospect lists included
- Internal pricing leaked
- Revenue projections visible

---

### NEXO — Operational Integrity
**Question:** "Does this break operations or expose internal processes?"
**Checks:**
- [ ] No internal SOPs meant to be private
- [ ] No capacity/availability information
- [ ] No vendor relationships exposed
- [ ] No internal communication patterns

**Veto triggers:**
- Operational secrets exposed
- Vendor pricing leaked
- Internal workflows that give competitive advantage

---

### PULSO — Competitive Intelligence
**Question:** "Does this give away our intelligence advantage?"
**Checks:**
- [ ] No proprietary research methods
- [ ] No data sources we don't want public
- [ ] No analysis frameworks meant to be internal
- [ ] No market intelligence compilations

**Veto triggers:**
- RADAR methodology exposed beyond intended
- Data source lists leaked
- Competitive analysis shared

---

### CENTINELA — Security & Secrets
**Question:** "Is there anything technically dangerous here?"
**Checks:**
- [ ] No API keys (even in defaults)
- [ ] No passwords or tokens
- [ ] No private keys (SSH, crypto, signing)
- [ ] No internal URLs/endpoints
- [ ] No database connection strings
- [ ] No PII (emails, phones, addresses, IDs)
- [ ] No file paths exposing system structure

**Veto triggers:**
- Any secret pattern detected
- Any credential pattern detected
- Any PII pattern detected

**Patterns to scan:**
```
# API Keys
xkeysib-
sk-
pk_live_
pk_test_
AKIA
ghp_
gho_

# Tokens
Bearer
token=
api_key=
apikey=
secret=

# Credentials
password
passwd
pwd
credentials

# PII
@gmail
@hotmail
@yahoo
CUIT
DNI
[0-9]{10,}  # phone numbers

# Paths
C:\\Users\\
/home/
/Users/
```

---

## Approval Process

### Step 1: Pre-Commit Review
Before any `git add` to a public repo:

```
COUNCIL REVIEW — [repo-name]
Date: [YYYY-MM-DD HH:MM]
Files changed: [list]

MEMOR:     [ ] APPROVE  [ ] VETO  [ ] ABSTAIN
VIGIL:     [ ] APPROVE  [ ] VETO  [ ] ABSTAIN
NEXO:      [ ] APPROVE  [ ] VETO  [ ] ABSTAIN
PULSO:     [ ] APPROVE  [ ] VETO  [ ] ABSTAIN
CENTINELA: [ ] APPROVE  [ ] VETO  [ ] ABSTAIN

DECISION: [PROCEED / BLOCKED]
```

### Step 2: Veto Resolution
If ANY agent vetoes:

1. **Identify concern** — What specific content triggered veto?
2. **Propose remediation** — How to fix?
3. **Re-review** — Run council again after fix
4. **Escalate if needed** — Human decision required

### Step 3: Commit Execution
Only after unanimous APPROVE:

```bash
git add [specific files]
git commit -m "[message]"
git push
```

---

## Automation Integration

### Pre-Commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "=== MEMOLA GOVERNANCE COUNCIL ==="
echo "Running security scan..."

# CENTINELA: Pattern scanning
if grep -rE "(xkeysib-|sk-|api_key=|password|@gmail|@hotmail|CUIT|DNI)" --include="*.py" --include="*.md" --include="*.json" .; then
    echo "CENTINELA: VETO — Sensitive pattern detected"
    exit 1
fi

# Check for hardcoded paths
if grep -rE "C:\\\\Users\\\\|/home/|/Users/" --include="*.py" --include="*.md" --include="*.json" .; then
    echo "CENTINELA: VETO — Local path detected"
    exit 1
fi

echo "CENTINELA: APPROVE — No patterns detected"
echo ""
echo "Manual review required for:"
echo "  MEMOR:  Strategic alignment"
echo "  VIGIL:  Client/revenue data"
echo "  NEXO:   Operational secrets"
echo "  PULSO:  Intelligence exposure"
echo ""
read -p "All agents approve? (y/n): " confirm
if [ "$confirm" != "y" ]; then
    echo "COUNCIL: BLOCKED — Commit aborted"
    exit 1
fi

echo "COUNCIL: UNANIMOUS APPROVAL — Proceeding"
```

### Agent Invocation
When reviewing changes, each agent runs:

```
/council review [files]
```

Returns structured approval or veto with specific concerns.

---

## Escalation Matrix

| Situation | Action |
|-----------|--------|
| 1 agent vetos | Fix concern, re-review |
| 2+ agents veto | Major issue, human review required |
| CENTINELA vetos | Hard block, no override without human |
| Disagreement | MEMOR has tiebreaker authority |
| Time pressure | No acceleration — governance is non-negotiable |

---

## Council Log

All council decisions logged:

```
council-log/
├── 2026-02-20-memola-sales-workflows.md
├── 2026-02-20-[next-review].md
└── ...
```

Log format:
```markdown
# Council Review — [repo]/[branch]

**Date:** YYYY-MM-DD HH:MM
**Initiator:** [agent or human]
**Files:** [list]

## Votes
- MEMOR: APPROVE — "Aligns with sales skill scope"
- VIGIL: APPROVE — "No client data exposed"
- NEXO: APPROVE — "No operational secrets"
- PULSO: APPROVE — "No intelligence leaked"
- CENTINELA: APPROVE — "Patterns scan clean"

## Decision
PROCEED

## Commit
[commit hash]
```

---

## Retroactive Review

For commits already pushed (like today):

```
RETROACTIVE COUNCIL REVIEW — memola/skills/memola-sales

Files: [all files in memola-sales]

MEMOR:     [x] APPROVE — Aligns with skill documentation purpose
VIGIL:     [?] CONCERN — Client names (Mi Ajuar, Agronorte, Platería Lossada) as references
NEXO:      [x] APPROVE — No operational secrets
PULSO:     [x] APPROVE — No intelligence methods exposed
CENTINELA: [?] CONCERN — WhatsApp number, family history

DECISION: CONDITIONAL — Requires human decision on:
1. Remove client name references? [Y/N]
2. Remove WhatsApp number? [Y/N]
3. Remove family history? [Y/N]
```

---

## Integration with OpenClaw

For autonomous agent operations:

```yaml
# openclaw-governance.yaml
council:
  required: true
  unanimous: true
  members:
    - memor
    - vigil
    - nexo
    - pulso
    - centinela

  auto_veto:
    - secrets_detected
    - pii_detected
    - client_data_detected

  human_escalation:
    - any_veto
    - new_repo_creation
    - monetization_changes
    - crypto_operations
```

**No autonomous commit to public repos without council approval.**
**No monetization launch without human sign-off.**
**No crypto/payment integration without legal review.**

---

## Principle

> "Speed without governance is entropy acceleration."

The council exists not to slow things down, but to prevent the compounding cost of mistakes made at speed.

One leaked API key costs more to remediate than a thousand careful reviews.

---

*Council established: 2026-02-20*
*Authority: Binding on all MEMOLA repository operations*
