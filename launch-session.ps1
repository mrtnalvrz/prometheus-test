# =============================================================================
# DROIDSCOUTS — Claude Code Session Launcher
# =============================================================================
# Usage:
#   Right-click -> "Run with PowerShell"
#   OR from terminal: .\launch-session.ps1
#   OR double-click launch-session.bat
# =============================================================================

$ProjectPath  = "C:\users\jmalv\DOcuments\Github\prometheus-test"
$ProjectName  = "DROIDSCOUTS SERIES"
$RepoRemote   = "origin/main"

# ── Helpers ──────────────────────────────────────────────────────────────────

function Write-Banner {
    param([string]$Text, [string]$Color = "Cyan")
    $line = "=" * 72
    Write-Host ""
    Write-Host $line                  -ForegroundColor $Color
    Write-Host "  $Text"              -ForegroundColor $Color
    Write-Host $line                  -ForegroundColor $Color
}

function Write-Section {
    param([string]$Text, [string]$Color = "Yellow")
    Write-Host ""
    Write-Host "── $Text " -ForegroundColor $Color -NoNewline
    Write-Host ("─" * [Math]::Max(0, 68 - $Text.Length)) -ForegroundColor DarkGray
}

# ── Header ───────────────────────────────────────────────────────────────────

Clear-Host
Write-Banner "THE MODERN PROMETHEUS  //  $ProjectName" "Magenta"
Write-Host ""
Write-Host "  Project path : $ProjectPath" -ForegroundColor Gray
Write-Host "  Date         : $(Get-Date -Format 'yyyy-MM-dd  HH:mm')" -ForegroundColor Gray

# ── Navigate ─────────────────────────────────────────────────────────────────

if (-not (Test-Path $ProjectPath)) {
    Write-Host ""
    Write-Host "  ERROR: Project path not found: $ProjectPath" -ForegroundColor Red
    Write-Host "  Edit the `$ProjectPath variable in this script to fix." -ForegroundColor Red
    Read-Host  "`n  Press Enter to exit"
    exit 1
}

Set-Location $ProjectPath

# ── Pull latest ──────────────────────────────────────────────────────────────

Write-Section "Syncing with remote"
$gitCheck = git remote -v 2>&1
if ($gitCheck -match "origin") {
    git fetch origin --quiet 2>&1 | Out-Null
    $behind = git rev-list HEAD..origin/main --count 2>&1
    if ($behind -gt 0) {
        Write-Host "  $behind new commit(s) on remote — pulling..." -ForegroundColor Yellow
        git pull origin main
    } else {
        Write-Host "  Already up to date." -ForegroundColor Green
    }
} else {
    Write-Host "  No remote configured — skipping sync." -ForegroundColor DarkGray
}

# ── Recent commits ───────────────────────────────────────────────────────────

Write-Section "Recent commits"
git log --oneline -6 --color=never | ForEach-Object {
    Write-Host "  $_" -ForegroundColor Gray
}

# ── Git status ───────────────────────────────────────────────────────────────

$dirty = git status --porcelain 2>&1
if ($dirty) {
    Write-Section "Uncommitted changes" "Yellow"
    $dirty | ForEach-Object { Write-Host "  $_" -ForegroundColor Yellow }
} else {
    Write-Section "Working tree"
    Write-Host "  Clean — nothing uncommitted." -ForegroundColor Green
}

# ── Latest session summary ───────────────────────────────────────────────────

Write-Section "Last session summary"
$summaries = Get-ChildItem -Path $ProjectPath -Filter "session-summary-*.txt" `
             | Sort-Object Name -Descending
if ($summaries) {
    $latest = $summaries[0]
    Write-Host "  File: $($latest.Name)" -ForegroundColor Cyan
    Write-Host ""

    # Extract only the "WHAT REMAINS TO BE DONE" section
    $content   = Get-Content $latest.FullName -Raw
    $marker    = "WHAT REMAINS TO BE DONE"
    $endMarker = "END OF SESSION SUMMARY"

    if ($content -match "(?s)$marker.*?(?=$endMarker)") {
        $section = $Matches[0] -replace "={10,}", ""
        $section.Trim().Split("`n") | ForEach-Object {
            Write-Host "  $_" -ForegroundColor White
        }
    } else {
        # Fallback: show last 30 lines
        Get-Content $latest.FullName | Select-Object -Last 30 | ForEach-Object {
            Write-Host "  $_" -ForegroundColor White
        }
    }
} else {
    Write-Host "  No session summaries found." -ForegroundColor DarkGray
}

# ── Checklist status ─────────────────────────────────────────────────────────

Write-Section "Checklist — open tasks"
$checklist = Get-Content "$ProjectPath\Final-Productization-Checklist.md" -ErrorAction SilentlyContinue
if ($checklist) {
    $open = $checklist | Where-Object { $_ -match "^\- \[ \]" }
    if ($open) {
        $open | ForEach-Object {
            Write-Host "  $_" -ForegroundColor Yellow
        }
    } else {
        Write-Host "  No open tasks — checklist is clear." -ForegroundColor Green
        Write-Host "  (Documentation audit phase active)" -ForegroundColor DarkGray
    }
}

# ── Launch ───────────────────────────────────────────────────────────────────

Write-Banner "LAUNCHING CLAUDE CODE" "Green"
Write-Host ""
Write-Host "  Tip: Start your message with:" -ForegroundColor DarkGray
Write-Host "       'resume the session' — to continue from where we left off" -ForegroundColor DarkGray
Write-Host "       'what's next'        — to get the next priority task" -ForegroundColor DarkGray
Write-Host ""

# Brief pause so the user can read the summary
Start-Sleep -Seconds 2

# Launch Claude Code in the project directory
claude
