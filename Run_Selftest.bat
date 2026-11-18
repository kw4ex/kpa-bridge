@echo off
REM Runs the built-in tests (no amplifier or radio needed). Expect "ALL TESTS PASSED" and "0 failed".
cd /d "%~dp0"
echo Running the tests, this takes about a minute ...
py -3 -B kpa_bridge.py --selftest > selftest_result.txt 2>&1
py -3 -B kpa_bridge.py --flex-selftest > flex_selftest_result.txt 2>&1
echo.
echo --- Main tests ---
findstr /i /c:"FAIL" /c:"ALL TESTS" /c:"SOME TESTS" /c:"checks," selftest_result.txt
echo.
echo --- Flex tests ---
findstr /i /c:"FAIL" /c:"checks," flex_selftest_result.txt
echo.
echo The full results are in selftest_result.txt and flex_selftest_result.txt in this folder.
pause
