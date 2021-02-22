@echo off

rem =========================
REM opening message
rem =========================
echo starting start_web-pages_hebrew.bat // C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang

pushd "C:\WORKS_2\Programs\opera"

rem : resource : https://scripture4all.org/OnlineInterlinear/Hebrew_Index.htm	: 2021年2月22日8:48:53
set url_1=https://scripture4all.org/OnlineInterlinear/OTpdf/qoh1.pdf
set url_2="http://www.qbible.com/hebrew-old-testament/ecclesiastes/1.html#4"
set url_3=https://www.mechon-mamre.org/p/pt/pt3101.htm

rem : add : 2021年2月8日9:09:07
rem : c/o : 2021年2月22日8:45:49
rem set url_4=http://www.mechon-mamre.org/p/p0000.htm

rem : other sites : 2021年2月8日9:22:24
rem https://www.abarim-publications.com/Dictionary/a/a-ta.html

rem : c/o : 2021年2月22日8:46:05
rem set dictionary=https://www.thefreedictionary.com
rem set time_calc=http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php
rem set stopwatch=https://stopwatch-app.com

set trans_1="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=ko"
set trans_2="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=zh-CN"

rem start launcher.exe %url_1% %dictionary% %url_2% %url_3% %time_calc% %stopwatch% %trans_1% %trans_2%

start launcher.exe %url_1% %dictionary% %url_2% %url_3% %url_4% %trans_1% %trans_2%

REM :end_of_end

REM gen ==> time label
