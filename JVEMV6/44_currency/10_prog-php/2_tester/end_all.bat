@echo off

echo param is '%1'

echo all params are : '%*'

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
REM 	git push : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11
REM ==================================

rem @echo on

echo setting param...

rem set param="%1"
set param="%*"


echo executing...
C:\WORKS_2\a.bat && r c && git add -A && git commit -m %param% && e && p && C:\WORKS_2\a.bat && r oj && git add -A && git commit -m %param% && e && p && echo.>> C:\WORKS_2\shortcuts_docs\start_log_JVE_44_10_2.[fx-php-tester].bat

goto end

rem goto end

rem echo executing commands...

rem echo "C:\WORKS_2\a.bat && r c && git add -A && git commit -m %param% && e && p"

rem goto end

rem C:\WORKS_2\a.bat && r c && git add -A && git commit -m %param% && e && p

rem @echo off



REM ==================================
REM 	git push : C:\WORKS_2\WS\WS_Others.JVEMV6
REM ==================================
rem C:\WORKS_2\a.bat && r oj && git add -A && git commit -m "%param%" && e && p

rem echo executing commands...

rem echo "C:\WORKS_2\a.bat && r oj && git add -A && git commit -m %param% && e && p"

rem goto end

rem C:\WORKS_2\a.bat && r oj && git add -A && git commit -m %param% && e && p

rem C:\WORKS_2\a.bat && r oj && git add -A && git commit -m ^"%param%^" && e && p

rem C:\WORKS_2\a.bat && r oj && git add -A && git commit -m %1 && e && p

rem C:\WORKS_2\a.bat && r oj && e && p && r c && e && p && C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\12_programming\3_fx-log-file\end_apps.bat


rem goto end

REM ==================================
REM 	closing
REM ==================================
rem echo.>> C:\WORKS_2\shortcuts_docs\start_log_JVE_44_10_2.[fx-php-tester].bat

rem goto end

taskkill /im wish.exe
taskkill /im sakura.exe

taskkill /im eclipse.exe

taskkill /im metaeditor.exe

echo.>> C:\Users\iwabuchiken\Desktop\shortcuts_docs\start_log_JVE_44_10_2.[fx-php-tester].bat


:end

pause
