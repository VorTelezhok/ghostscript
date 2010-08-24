@REM based on http://bugs.python.org/file13578/install_scripts.py
@echo off
set SCRIPT=%~dp0\run-string.py
set PYTHON=C:\Python25\python.exe

set SCRIPT_ERRORLEVEL=
@REM Credit where credit is due:  we return the exit code despite our
@REM use of setlocal+endlocal using a technique from Bear's Journal:
@REM http://code-bear.com/bearlog/2007/06/01/getting-the-exit-code-from-a-batch-file-that-is-run-from-a-python-program/

setlocal
@REM ensure the script will be executed with the Python it was installed for
set path=%~dp0;%~dp0..;%path%
%PYTHON% "%SCRIPT%" %*
endlocal & set SCRIPT_ERRORLEVEL=%ERRORLEVEL%

if NOT "%COMSPEC%" == "%SystemRoot%\\system32\\cmd.exe" goto returncode
if errorlevel 9009 echo You do not have python in your PATH.
goto endscript

:returncode
exit /B %SCRIPT_ERRORLEVEL%

:endscript
call :returncode %SCRIPT_ERRORLEVEL%
