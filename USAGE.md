# MEMOLA Skill Usage Guide

## Installation Methods

### Method 1: NPX (Recommended - After Anthropic Approval)

```bash
# Core skill
npx skills add josebarnetche/memola

# Specific variants
npx skills add josebarnetche/memola/tree/main/skills/MEMOLA-Diagnosis
npx skills add josebarnetche/memola/tree/main/skills/MEMOLA-Platforms
npx skills add josebarnetche/memola/tree/main/skills/MEMOLA-Governance
npx skills add josebarnetche/memola/tree/main/skills/MEMOLA-Local
npx skills add josebarnetche/memola/tree/main/skills/MEMOLA-Creative
```

**Note**: This method will work once your skill is approved in the Anthropic skills catalog (PR #294).

---

### Method 2: Quick Install Scripts

**On Windows:**
```powershell
# Install core skill
powershell -ExecutionPolicy Bypass -File install.ps1

# Install specific skill variant
powershell -ExecutionPolicy Bypass -File install.ps1 -SkillName Diagnosis
```

**On Mac/Linux:**
```bash
# Install core skill
bash install.sh

# Install specific skill variant
bash install.sh Diagnosis
```

---

### Method 3: Manual Installation

**Windows:**
```powershell
# Create skills directory
mkdir $env:USERPROFILE\.claude\skills\memola

# Copy files
xcopy SKILL.md $env:USERPROFILE\.claude\skills\memola\ /Y
xcopy references $env:USERPROFILE\.claude\skills\memola\references\ /E /I
```

**Mac/Linux:**
```bash
# Create skills directory
mkdir -p ~/.claude/skills/memola

# Copy files
cp SKILL.md ~/.claude/skills/memola/
cp -r references ~/.claude/skills/memola/
```

---

### Method 4: Per-Project Reference

In your project directory, create `.claude/settings.json`:

```json
{
  "skills": [
    "/absolute/path/to/memola/SKILL.md",
    "/absolute/path/to/memola/skills/MEMOLA-Diagnosis/SKILL.md"
  ]
}
```

Or use as git submodule:

```bash
cd your-project
git submodule add https://github.com/josebarnetche/memola.git .memola
```

Then reference in `.claude/settings.json`:

```json
{
  "skills": [
    "./.memola/SKILL.md"
  ]
}
```

---

## Using MEMOLA in Claude Code

Once installed, MEMOLA activates with these triggers:

### Essential Commands

| Trigger | What It Does | When to Use |
|---------|--------------|-------------|
| `terrain assessment [project]` | Runs the 5 diagnostic questions | **ALWAYS START HERE** |
| `diagnostic questions [project]` | Same as above | First step for any engagement |
| `diagnose [project/client]` | Full strategic diagnosis | After terrain assessment passes |
| `structure [project]` | Design system architecture | After diagnosis complete |
| `governance check [project]` | Verify decision authority | Before committing to engagement |

### Specialized Commands

| Trigger | What It Does |
|---------|--------------|
| `evaluate platform for [domain]` | Assess platform viability |
| `failure mode analysis` | Review potential failure modes |
| `brand filter [content]` | Apply MEMOLA brand principles |
| `what has MEMOLA learned about [topic]` | Query learning database |

---

## Example Session

```
User: terrain assessment for a 120-year-old rural cooperative going digital

Claude (with MEMOLA): I'll assess terrain fit using the five diagnostic questions...

[Claude runs assessment, determines it's Foundation terrain]

User: governance check

Claude: Verifying governance requirements...
- Decision authority: ✓ Board president has clear mandate
- Defined scope: ✓ Digital transformation, not cultural change
- Explicit ownership: ✓ Project manager assigned
- Exit conditions: ⚠️ Need to define success metrics

User: diagnose cooperative digital transformation

Claude: Running strategic diagnosis...
[Generates complete diagnosis document]

User: structure the platform

Claude: Designing system architecture...
[Creates brand architecture, asset hierarchy, roadmap]
```

---

## Skill Variants

Different MEMOLA skills for different contexts:

### MEMOLA-Diagnosis
**Use for**: Initial terrain assessment, regime classification
**Triggers**: `terrain assessment`, `diagnostic questions`

### MEMOLA-Platforms
**Use for**: Evaluating platform opportunities
**Triggers**: `evaluate platform`, `platform viability`

### MEMOLA-Governance
**Use for**: Setting engagement boundaries
**Triggers**: `governance check`, `authority verification`

### MEMOLA-Local
**Use for**: NEA Argentina regional context
**Best for**: Corrientes/Misiones/Chaco/Formosa clients

### MEMOLA-Creative
**Use for**: Music, art, cultural sector projects
**Best for**: Artists, labels, festivals, cultural events

---

## Skill Stacking

Skills work best in sequence:

```
1. MEMOLA-Diagnosis (REQUIRED)
   ↓
2. MEMOLA-Governance (REQUIRED)
   ↓
3. MEMOLA (Core) OR specialized variant
   (Platforms | Local | Creative)
```

You can have multiple skills active simultaneously. They layer their context.

---

## Verification

To verify MEMOLA is installed:

```bash
# List installed skills (if Claude Code has this command)
claude skills list

# Or just try invoking it
User: terrain assessment test
```

If MEMOLA is installed, Claude will respond with structured terrain assessment questions.

---

## Troubleshooting

### Skill Not Activating

1. **Check installation path**:
   - Windows: `%USERPROFILE%\.claude\skills\memola\SKILL.md`
   - Mac/Linux: `~/.claude/skills/memola/SKILL.md`

2. **Verify references folder exists**:
   The `references/` folder must be alongside `SKILL.md`

3. **Check .claude/settings.json syntax**:
   ```json
   {
     "skills": [
       "path/to/SKILL.md"
     ]
   }
   ```
   (Note: No trailing comma in JSON)

4. **Restart Claude Code**:
   Skills are loaded at startup

### Skill Conflicts

If you have multiple MEMOLA variants installed and they conflict:

1. Use explicit per-project settings
2. Remove unused variants from `~/.claude/skills/`
3. Use only the core skill + one specialized variant at a time

---

## Sharing with Team

### Option 1: Submodule in Team Repo

```bash
# Add to team repo
git submodule add https://github.com/josebarnetche/memola.git .memola

# Team members clone with submodules
git clone --recurse-submodules [your-team-repo]
```

### Option 2: Install Instructions in Team Docs

Add to your team's onboarding docs:

```markdown
## MEMOLA Skill Setup

1. Install MEMOLA skill:
   ```
   npx skills add josebarnetche/memola
   ```

2. Verify installation:
   ```
   User: terrain assessment test
   ```

3. Read the doctrine:
   - [MEMOLA README](https://github.com/josebarnetche/memola)
```

### Option 3: Custom Internal Fork

If you're adapting MEMOLA for your agency:

```bash
# Fork the repo on GitHub
# Clone your fork
git clone https://github.com/your-org/memola-custom.git

# Team installs from your fork
npx skills add your-org/memola-custom
```

---

## Advanced: Custom Modifications

To customize MEMOLA for your context:

1. **Fork the repository**
2. **Edit `SKILL.md`** - Add your specific triggers, constraints, or domain knowledge
3. **Edit `references/`** - Adapt examples to your industry
4. **Update `.agents/database/`** - Add your own pattern library
5. **Use your fork**:
   ```bash
   npx skills add your-username/memola-fork
   ```

---

## Learning System

MEMOLA evolves through use. It stores learnings in:

```
.agents/
├── database/
│   ├── entities.json     # Clients, projects analyzed
│   ├── patterns.json     # Recurring strategic patterns
│   ├── relationships.json # How entities connect
│   ├── learnings.json    # Extracted insights
│   └── taxonomy.json     # Classification system
└── logs/
    └── session-*.md      # Thinking sessions
```

To query what MEMOLA has learned:

```
User: what has MEMOLA learned about platform timing?
User: show me patterns for artisanal brands
User: what does MEMOLA know about governance failure?
```

---

## Support

- **Issues**: [github.com/josebarnetche/memola/issues](https://github.com/josebarnetche/memola/issues)
- **Email**: agencia@memola.com.ar
- **Web**: [memola.com.ar](https://memola.com.ar)

---

## Philosophy Reminder

> "MEMOLA doesn't make everything better — it makes the right things durable."

MEMOLA is **regime-specific**. It works in Foundation terrain, not Sprint terrain.

**Always start with terrain assessment.** Let the framework decline work it's not suited for.

Self-selection is precision, not weakness.
