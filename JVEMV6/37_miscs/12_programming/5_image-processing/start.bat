@echo off

REM opening message
echo starting start.bat // C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\12_programming\5_image-processing

REM =================================
REM 	log file
REM 	eclipse
REM 	xampp
REM 	browser
REM 	dirs
REM 	git
REM =================================

REM =================================
REM 	log file
REM 	2019/12/24 14:43:23
REM =================================
pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\12_programming\5_image-processing
start log_JVE_37_12_5.[image-processing].odt

REM =================================
REM 	eclipse
REM 	2020/01/08 13:01:27
REM =================================
REM pushd C:\WORKS_2\Programs\eclipse\eclipse_luna-php,python
pushd C:\WORKS_2\Programs\eclipse\eclipse_luna_php
start eclipse.exe

REM =================================
REM 	xampp
REM 	2020/01/09 07:53:47
REM =================================
pushd C:\xampp_5.6
start xampp-control.exe

REM =================================
REM 	browser
REM 	2020/01/08 13:01:27
REM =================================
set url_1=http://localhost/Eclipse_Luna/Cake_IFM11/ip
set url_2=http://localhost/Eclipse_Luna/Cake_IFM11/ip/ip_proc_actions

pushd C:\WORKS_2\Programs\opera
REM launcher.exe http://localhost/Eclipse_Luna/Cake_IFM11/ifm
launcher.exe %url_1% %url_2%

REM =================================
REM 	dirs
REM 	2020/01/29 15:15:37
REM =================================
start C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\Log_Fx_Admin
start C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\6_visual-arts\5_free-painting\images

REM =================================
REM 	git
REM 	2020/01/08 13:01:27
REM =================================
REM C:\WORKS_2\a.bat
C:\WORKS_2\batches\r.bat oj && C:\WORKS_2\batches\s.bat && C:\WORKS_2\batches\r.bat c && C:\WORKS_2\batches\s.bat
REM  && r c && s


:end_of_end

pause
