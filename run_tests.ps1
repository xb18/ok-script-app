$ErrorActionPreference = 'Stop'
$taskPython = if (Test-Path "$PSScriptRoot\.venv\Scripts\python.exe") {
    "$PSScriptRoot\.venv\Scripts\python.exe"
} else {
    'python'
}
$env:PYTHONIOENCODING = 'utf-8'

Push-Location $PSScriptRoot
try {
    Get-ChildItem -Path ".\tests\*.py" | ForEach-Object {
        Write-Host "Running tests in $($_.FullName)"
        & $taskPython -m unittest $_.FullName
        if ($LASTEXITCODE -ne 0) {
            throw "Tests failed in $($_.FullName)"
        }
    }
} finally {
    Pop-Location
}
