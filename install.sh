#!/bin/bash
# MEMOLA Skill Installer
# Usage: bash install.sh [skill-name]

SKILLS_DIR="${HOME}/.claude/skills"
REPO_URL="https://github.com/josebarnetche/memola.git"

# Create skills directory if it doesn't exist
mkdir -p "${SKILLS_DIR}"

# If specific skill is requested
if [ -n "$1" ]; then
    SKILL_NAME="$1"
    echo "Installing MEMOLA-${SKILL_NAME}..."

    # Clone if not exists
    if [ ! -d "/tmp/memola" ]; then
        git clone "${REPO_URL}" /tmp/memola
    fi

    # Copy specific skill
    if [ -d "/tmp/memola/skills/MEMOLA-${SKILL_NAME}" ]; then
        cp -r "/tmp/memola/skills/MEMOLA-${SKILL_NAME}" "${SKILLS_DIR}/"
        echo "✓ MEMOLA-${SKILL_NAME} installed to ${SKILLS_DIR}/MEMOLA-${SKILL_NAME}"
    else
        echo "✗ Skill MEMOLA-${SKILL_NAME} not found"
        exit 1
    fi
else
    # Install core MEMOLA
    echo "Installing core MEMOLA skill..."

    # Clone if not exists
    if [ ! -d "/tmp/memola" ]; then
        git clone "${REPO_URL}" /tmp/memola
    fi

    # Copy core skill, agents, and references
    mkdir -p "${SKILLS_DIR}/memola"
    cp /tmp/memola/SKILL.md "${SKILLS_DIR}/memola/"
    cp /tmp/memola/MANIFESTO.md "${SKILLS_DIR}/memola/"
    cp -r /tmp/memola/agents "${SKILLS_DIR}/memola/"
    cp -r /tmp/memola/references "${SKILLS_DIR}/memola/"

    echo "✓ Core MEMOLA skill installed to ${SKILLS_DIR}/memola"
fi

echo ""
echo "Installation complete!"
echo "You can now use MEMOLA by typing 'memola' or other triggers in Claude Code."
