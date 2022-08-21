@echo off

rem =========================
REM opening message
rem =========================
echo starting start_web-pages_hebrew.bat // C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang


rem 2022年8月16日23:04:15
set dpath_browser_executable="C:\Users\iwabuchiken\AppData\Local\Yandex\YandexBrowser\Application"

goto section_pushd


:section_pushd
rem pushd "C:\WORKS_2\Programs\opera"
rem pushd "C:\Program Files\Mozilla Firefox"
pushd %dpath_browser_executable%


rem : resource : https://scripture4all.org/OnlineInterlinear/Hebrew_Index.htm	: 2021年2月22日8:48:53
rem set url_1=https://scripture4all.org/OnlineInterlinear/OTpdf/qoh1.pdf
rem : 2021年7月3日10:59:45
rem set url_1=https://www.scripture4all.org/OnlineInterlinear/OTpdf/gen1.pdf

rem set url_1=https://scripture4all.org/OnlineInterlinear/OTpdf/pro26.pdf

rem https://scripture4all.org/OnlineInterlinear/Hebrew_Index.htm


rem set url_2="http://www.qbible.com/hebrew-old-testament/proverbs/26.html#13"
rem set url_2="http://www.qbible.com/hebrew-old-testament/genesis/1.html#1"


rem set url_3=https://mechon-mamre.org/p/pt/pt2826.htm

rem https://mechon-mamre.org/p/pt/pt1001.htm


set url_1=https://www.scripture4all.org/OnlineInterlinear/OTpdf/psa3.pdf
set url_2="http://www.qbible.com/hebrew-old-testament/psalms/3.html#1"
set url_3=https://mechon-mamre.org/p/pt/pt2603.htm
set url_4=https://biblescripture.net/Hebrew.html


set list_of_urls=%url_1% %url_2% %url_3% %url_4%

set fname_browser_executable="browser.exe"

echo %fname_browser_executable:"=%

rem %fname_browser_executable:"=% https://biblescripture.net/Hebrew.html

%fname_browser_executable:"=% %list_of_urls%

rem : 2022年3月12日10:43:17 : comment o.
rem firefox.exe  %list_of_urls%

rem : add : 2021年2月8日9:09:07
rem : c/o : 2021年2月22日8:45:49
rem set url_4=http://www.mechon-mamre.org/p/p0000.htm

rem : other sites : 2021年2月8日9:22:24
rem https://www.abarim-publications.com/Dictionary/a/a-ta.html

rem : c/o : 2021年2月22日8:46:05
rem set dictionary=https://www.thefreedictionary.com
rem set time_calc=http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php
rem set stopwatch=https://stopwatch-app.com

rem 2022年2月17日10:43:17
rem https://biblescripture.net/Hebrew.html

rem : c/o : 2021年7月3日11:00:22
rem set trans_1="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=ko"
rem set trans_2="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=zh-CN"

rem start launcher.exe %url_1% %dictionary% %url_2% %url_3% %time_calc% %stopwatch% %trans_1% %trans_2%

rem start launcher.exe %url_1% %dictionary% %url_2% %url_3% %url_4% %trans_1% %trans_2%

REM :end_of_end

REM gen ==> time label

exit


rem =============================

rem : kohelet //2022年8月21日8:32:14
http://www.qbible.com/hebrew-old-testament/ecclesiastes/2.html#3
https://www.scripture4all.org/OnlineInterlinear/OTpdf/qoh2.pdf
https://mechon-mamre.org/p/pt/pt3102.htm

rem =============================