@echo off

echo param is '%1'

set param=%1

REM ==================================
REM 	validate : param ?
REM ==================================
rem if "%param%"=='' (
if "%param%"=="" (

	echo param is blank
	
	goto end
)

REM ==================================
REM 	git push
REM ==================================
rem C:\WORKS_2\a.bat && r oj && git add -A && git commit -m "%param%" && e && p
C:\WORKS_2\a.bat && r oj && git add -A && git commit -m ^"%param%^" && e && p

rem C:\WORKS_2\a.bat && r oj && git add -A && git commit -m %1 && e && p

rem C:\WORKS_2\a.bat && r oj && e && p && r c && e && p && C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\12_programming\3_fx-log-file\end_apps.bat


goto end

taskkill /im wish.exe
taskkill /im sakura.exe

taskkill /im eclipse.exe

taskkill /im metaeditor.exe

echo.>> C:\Users\iwabuchiken\Desktop\shortcuts_docs\start_log_JVE_44_10_2.[fx-php-tester].bat


:end

pause
