@echo off
REM Closes a running bridge (this one or an older one) and its window.
cd /d "%~dp0"
py -3 kpa_bridge.py --stop-running
timeout /t 3 >nul
