@echo off

REM opening message
echo starting start_web-pages_hebrew.bat // C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang

pushd "C:\WORKS_2\Programs\opera"

set url_1=https://www.scripture4all.org/OnlineInterlinear/OTpdf/pro11.pdf
set url_2="http://www.qbible.com/hebrew-old-testament/proverbs/11.html#1"
set url_3=https://www.mechon-mamre.org/p/pt/pt2811.htm
set dictionary=https://www.thefreedictionary.com
set time_calc=http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php
set stopwatch=https://stopwatch-app.com

set trans_1="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=ko"
set trans_2="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=zh-CN"

start launcher.exe %url_1% %dictionary% %url_2% %url_3% %time_calc% %stopwatch% %trans_1% %trans_2%

REM :end_of_end

REM gen ==> time label
