@echo off

REM opening message
echo starting start_web-pages_hebrew.bat // C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang

pushd "C:\WORKS_2\Programs\opera"

set url_1="http://www.qbible.com/hebrew-old-testament/proverbs/8.html#1"
set url_2=https://www.scripture4all.org/OnlineInterlinear/OTpdf/pro8.pdf
set url_3=https://www.mechon-mamre.org/p/pt/pt2808.htm
set dictionary=https://www.thefreedictionary.com
set time_calc=http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php
set stopwatch=https://stopwatch-app.com

start launcher.exe %url_1% %url_2% %url_3%  %dictionary% %time_calc% %stopwatch%

REM :end_of_end

REM gen ==> time label
