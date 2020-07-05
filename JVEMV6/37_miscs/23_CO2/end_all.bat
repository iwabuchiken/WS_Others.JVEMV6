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
rem C:\WORKS_2\a.bat && r oj && git add -A && git commit -m %param% && e && p && echo.>> C:\WORKS_2\shortcuts_docs\start_log_JVE_37#23.[CO2].bat
C:\WORKS_2\a.bat && r oj && git add -A && git commit -m %param% && e && p && cd C:\WORKS_2\WS\FM_2_20171104_225946 && git add -A && git commit -m %param% && e && p && echo.>> C:\WORKS_2\shortcuts_docs\start_log_JVE_37#23.[CO2].bat


goto end

:end

pause
