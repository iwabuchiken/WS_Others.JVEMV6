REM =================================
REM 	log file
REM 	git
REM 	browser
REM =================================
@echo off

REM opening message
echo starting start.bat // C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\44_currency\10_prog-php\2_tester

REM =================================
REM 	log file
REM 	2020/01/04 15:21:38
REM =================================
pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\44_currency\10_prog-php\2_tester
start log_JVE_44_10_2.[fx-php-tester].odt

REM =================================
REM 	eclipse
REM 	2020/01/04 15:21:38
REM =================================
REM pushd C:\WORKS_2\Programs\eclipse\eclipse_luna-php,python
pushd C:\WORKS_2\Programs\eclipse\eclipse_luna_php
start eclipse.exe

REM =================================
REM 	git
REM 	2020/01/04 15:21:38
REM =================================
REM C:\WORKS_2\a.bat
C:\WORKS_2\batches\r.bat oj && C:\WORKS_2\batches\s.bat && C:\WORKS_2\batches\r.bat c && C:\WORKS_2\batches\s.bat
REM  && r c && s

REM =================================
REM 	browser
REM 	2020/01/07 14:44:50
REM =================================
pushd C:\WORKS_2\Programs\opera
launcher.exe http://localhost/Eclipse_Luna/Cake_IFM11/fx_test http://localhost/Eclipse_Luna/Cake_IFM11/fx_test/fx_tester_T_1 

:end_of_end

pause
