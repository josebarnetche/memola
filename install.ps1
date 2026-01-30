# MEMOLA Skill Installer for Windows
# Usage: powershell install.ps1 [skill-name]

param(
    [string]$SkillName = ""
)

$SkillsDir = "$env:USERPROFILE\.claude\skills"
$RepoUrl = "https://github.com/josebarnetche/memola.git"
$TempDir = "$env:TEMP\memola"

# Create skills directory if it doesn't exist
New-Item -ItemType Directory -Force -Path $SkillsDir | Out-Null

# Clone repo if not exists
if (-not (Test-Path $TempDir)) {
    Write-Host "Cloning MEMOLA repository..."
    git clone $RepoUrl $TempDir
}

if ($SkillName -ne "") {
    # Install specific skill
    Write-Host "Installing MEMOLA-$SkillName..."

    $SkillPath = "$TempDir\skills\MEMOLA-$SkillName"
    if (Test-Path $SkillPath) {
        Copy-Item -Path $SkillPath -Destination "$SkillsDir\MEMOLA-$SkillName" -Recurse -Force
        Write-Host "✓ MEMOLA-$SkillName installed to $SkillsDir\MEMOLA-$SkillName" -ForegroundColor Green
    } else {
        Write-Host "✗ Skill MEMOLA-$SkillName not found" -ForegroundColor Red
        exit 1
    }
} else {
    # Install core MEMOLA
    Write-Host "Installing core MEMOLA skill..."

    $CoreDir = "$SkillsDir\memola"
    New-Item -ItemType Directory -Force -Path $CoreDir | Out-Null

    Copy-Item -Path "$TempDir\SKILL.md" -Destination $CoreDir -Force
    Copy-Item -Path "$TempDir\references" -Destination $CoreDir -Recurse -Force

    Write-Host "✓ Core MEMOLA skill installed to $CoreDir" -ForegroundColor Green
}

Write-Host ""
Write-Host "Installation complete!" -ForegroundColor Cyan
Write-Host "You can now use MEMOLA by typing 'memola' or other triggers in Claude Code."
