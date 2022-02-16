@echo off

rem =========================
REM opening message
rem =========================
echo starting start_web-pages_hebrew.bat // C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang

pushd "C:\WORKS_2\Programs\opera"

rem : resource : https://scripture4all.org/OnlineInterlinear/Hebrew_Index.htm	: 2021�N2��22��8:48:53
rem set url_1=https://scripture4all.org/OnlineInterlinear/OTpdf/qoh1.pdf
rem : 2021�N7��3��10:59:45
rem set url_1=https://www.scripture4all.org/OnlineInterlinear/OTpdf/gen1.pdf
set url_1=https://scripture4all.org/OnlineInterlinear/OTpdf/pro26.pdf

set url_2="http://www.qbible.com/hebrew-old-testament/proverbs/26.html#13"
rem set url_2="http://www.qbible.com/hebrew-old-testament/genesis/1.html#1"

set url_3=https://www.mechon-mamre.org/p/pt/pt0101.htm

rem : add : 2021�N2��8��9:09:07
rem : c/o : 2021�N2��22��8:45:49
rem set url_4=http://www.mechon-mamre.org/p/p0000.htm

rem : other sites : 2021�N2��8��9:22:24
rem https://www.abarim-publications.com/Dictionary/a/a-ta.html

rem : c/o : 2021�N2��22��8:46:05
rem set dictionary=https://www.thefreedictionary.com
rem set time_calc=http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php
rem set stopwatch=https://stopwatch-app.com

rem : c/o : 2021�N7��3��11:00:22
rem set trans_1="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=ko"
rem set trans_2="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=zh-CN"

rem start launcher.exe %url_1% %dictionary% %url_2% %url_3% %time_calc% %stopwatch% %trans_1% %trans_2%

start launcher.exe %url_1% %dictionary% %url_2% %url_3% %url_4% %trans_1% %trans_2%

REM :end_of_end

REM gen ==> time label
