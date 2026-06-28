Set-Location -Path $PSScriptRoot

$changes = git status --porcelain
if (-not $changes) {
    Write-Host "Nothing to commit - working tree clean."
    exit 0
}

git add -A
$msg = "DSA: " + (Get-Date -Format "yyyy-MM-dd HH:mm")
git commit -m $msg
git push
Write-Host "Pushed: $msg"
