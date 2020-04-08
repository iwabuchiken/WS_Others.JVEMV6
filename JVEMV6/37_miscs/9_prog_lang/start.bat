@echo off

REM opening message
echo starting start.bat // C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang

REM =================================
REM 	dispatch
REM 	2019/06/15 09:53:28
REM =================================
if "%1"=="" (
	
	echo %%1 is blank. go to 'all'
	
	goto all
	
)

REM ================================================
REM 	each lang
REM 	2019/06/15 09:53:28
REM ================================================
REM =================================
REM 	hebrew
REM 	2019/06/15 09:53:28
REM =================================
if "%1"=="he" (

	echo %%1 is %1!

	pushd "C:\WORKS_2\Programs\opera"
REM 	pushd "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application"

REM ===============
REM 	trans
REM ===============
REM 	start brave.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=en&tl=zh-CN"
REM 	start launcher.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=en&tl=zh-CN"

REM ===============
REM 	lang
REM ===============
REM : doc
REM 	start chrome.exe "https://docs.google.com/document/d/1rvbIPLG4V6oanqnqkGwmfYU5kO4Ifo7EawcHxkqbTsY/edit"
REM 	start chrome.exe "https://docs.google.com/document/d/16zGryKeY6f_oFqsRFjtbKPPZ-3A-HBsVbdAQRMGX2FE/edit"

REM 	start brave.exe "https://docs.google.com/document/d/1fa29-r2ZEB1eB3TAgaMzlvCi9G_gy6X-IJnlTjauHnw/edit"

REM 	start brave.exe "http://www.qbible.com/hebrew-old-testament/ecclesiastes/1.html"
REM : text
REM 	start brave.exe "http://www.qbible.com/hebrew-old-testament/ecclesiastes/2.html"
REM 	start brave.exe "http://www.qbible.com/hebrew-old-testament/ecclesiastes/3.html"
REM 	start brave.exe "http://www.qbible.com/hebrew-old-testament/isaiah/2.html#1"
REM start launcher.exe "http://www.qbible.com/hebrew-old-testament/nahum/3.html"
REM start launcher.exe http://www.qbible.com/hebrew-old-testament/habakkuk/3.html#3
REM start launcher.exe http://www.qbible.com/hebrew-old-testament/zephaniah/3.html#1

start launcher.exe "http://www.qbible.com/hebrew-old-testament/obadiah/1.html#1"
start launcher.exe https://www.scripture4all.org/OnlineInterlinear/OTpdf/oba1.pdf
start launcher.exe https://www.mechon-mamre.org/p/pt/pt1601.htm

REM 	start launcher.exe "http://www.qbible.com/hebrew-old-testament/micah/7.html#1"
REM 	start launcher.exe "http://www.qbible.com/hebrew-old-testament/micah"
REM : wiki
REM 	start launcher.exe "https://ja.wikipedia.org/wiki/ヘブライ文字#文字"
REM : pronunciations
REM 	start launcher.exe "https://biblescripture.net/Hebrew.html"

REM ===============
REM 	resources
REM ===============
REM : 2019/07/05 11:15:25
set dictionary=https://www.thefreedictionary.com
REM start launcher.exe "https://dictionary.cambridge.org/dictionary/english/imbibe"
start launcher.exe %dictionary%

start launcher.exe http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php
start launcher.exe https://stopwatch-app.com

REM 	start brave.exe "https://docs.google.com/spreadsheets/d/1SFebXPC8pWMXHu3NjxDeGDX-GgtGDLjg0pRbmse_-B0/edit#gid=1396336879"

REM : word list : 2019/08/15 09:22:49
	start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\ancient_hebrew.odt
	start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\ancient_hebrew.ods

	start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang

	goto end



REM =================================
REM 	korean
REM 	2019/06/15 10:34:12
REM =================================
) else if "%1"=="ko" (

	echo %%1 is %1!

REM ===============
REM 	trans
REM ===============
REM 	start chrome.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ja&tl=ko"
	REM start chrome.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ko&tl=ja"

	pushd C:\WORKS_2\Programs\opera
	start launcher.exe https://marisha39.com/phrase/page/2/
REM 	start launcher.exe "https://www.bing.com/translator/"
REM 	start launcher.exe "https://www.bing.com/translator/"
REM 	start launcher.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ko&tl=ja"
REM 	
REM 	start launcher.exe "https://gate2home.com/Korean-Keyboard/Translate#lang=ja"
	
REM ===============
REM 	docs
REM ===============
REM 	start chrome.exe "https://writer.zoho.com/writer/open/eovu1bbc85f4e6cc94063a7fa950aaed8aa56"	
REM 	start chrome.exe "https://docs.google.com/document/d/1BM1Rn73jF-EjadfN-HmbXJWVPOzRAW4pjXo6M5Qx02w/edit"
REM 	start chrome.exe "https://docs.google.com/document/d/1sdBMW5njvAqJL5_HkHTwWBisLknsXW3ORMUz_ErJEh0/edit"
REM 	start chrome.exe "https://docs.google.com/document/d/1sdBMW5njvAqJL5_HkHTwWBisLknsXW3ORMUz_ErJEh0/edit"	
REM 	start chrome.exe "https://docs.google.com/document/d/1B-yo_gJtRENYyYGzYy14KKv6-cVxUKYVdslIRCYHXcw/edit"
REM 	start chrome.exe "https://docs.google.com/document/d/10AhaA-6SPuuo0KbAo4-VXDzo6O4wTLUBEPO9i0HiuNA/edit"
REM 	pushd C:\WORKS_2\Programs\OpenOffice 4\program
REM 	start soffice.exe
	
	start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\korean.odt
	
REM ===============
REM 	resources
REM 	2019/06/30 10:49:12
REM ===============
REM 	start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/view/34706"

REM : sakura : 2019/07/27 11:44:07
REM 	start C:\WORKS_2\Programs\sakura\sakura.exe

	goto end

REM =================================
REM 	arabic
REM 	2019/06/15 11:06:33
REM =================================
) else if "%1"=="ar" (

	echo %%1 is %1!

	pushd "C:\WORKS_2\Programs\opera"

REM ===============
REM 	trans
REM ===============
REM 	start launcher.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ar&tl=en"
REM 	start launcher.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ar&tl=en"
REM 	start launcher.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ar&tl=en"
REM 	start launcher.exe "https://www.bing.com/translator/"
	
REM ===============
REM 	docs
REM ===============
REM 	start launcher.exe "https://writer.zoho.com/writer/open/eovu101b2b5cc9dae4117b56a277773c427ab"
REM start launcher.exe "https://docs.google.com/document/d/1EWd6CKZptTbNfKgaCLR-hWeqSDDS8TTX1FQPjyjAdVQ/edit"
REM 	start launcher.exe "https://docs.google.com/document/d/1o2H_03TxGsesoIWeqXtbasTZkkSpXvT4ngZqOaclE-E/edit#"
REM 	start launcher.exe "https://docs.google.com/document/d/1K_2-9x0g_WTFwwDyV-M8V89Sk_L4fXFUIUE6gET5uV4/edit"
REM 	start launcher.exe "http://www.felesteen.ps/article/myladynwf-yhdhr-mn-anhyar-althdyt-fy-ghzt"
	start launcher.exe "https://ja.wikipedia.org/wiki/アラビア文字#字母"

REM 	start launcher.exe "http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php"
	
REM 	start launcher.exe "https://docs.google.com/spreadsheets/d/18P9jHbAxfMambOlr7llsahy5EYWImyEGrFEFsdVZepw/edit?ouid=114557293394362897307&usp=docs_home&ths=true"
	
REM 	start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\arabic.odt
REM 	start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\arabic.ods
start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\lang_arabic.odt
	
REM ===============
REM 	texts
REM ===============
REM 	start launcher.exe "https://www.hespress.com/international/439175.html"
	start launcher.exe https://quranonline.net/al-baqarah/
	start launcher.exe https://quran.com/2?translations=20
	
	goto end

REM =================================
REM 	russian
REM 	2019/06/17 09:47:46
REM =================================
) else if "%1"=="ru" (

	echo %%1 is %1!

REM ===============
REM 	trans
REM ===============
	
REM 	start chrome.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=en&tl=de"
REM 	start chrome.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=de&tl=ru"
REM 	start chrome.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=de&tl=ru"
REM start chrome.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ru&tl=en"
REM start chrome.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ru&tl=en"
REM 	start chrome.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ru&tl=ko"
REM 	start chrome.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ko&tl=ja"

	pushd C:\WORKS_2\Programs\opera
	start launcher.exe "https://www.bing.com/translator/"
	start launcher.exe "https://www.bing.com/translator/"
	
REM ===============
REM 	lang
REM ===============
REM 	start chrome.exe "https://writer.zoho.com/writer/open/eirjm1f770439a83d4d53a9700909fef4204c"
REM 	start chrome.exe "https://docs.google.com/document/d/1KMTaG_ojOHV2aNn7Etc1iz7-eBcjOuy2AybX59G8eEQ/edit"

REM ===============
REM 	docs
REM ===============
	start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\russian.odt
	
REM ===============
REM 	memo : steps
REM 	2019/06/29 17:50:40
REM ===============
REM 	start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=steps+russian&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
	
REM ===============
REM 	resources
REM 	2019/07/07 13:09:22
REM ===============
REM 	start chrome.exe "https://coal-liza.livejournal.com/39295.html"
REM 	start chrome.exe "https://nauka.vesti.ru/article/1046760"
	
	pushd C:\WORKS_2\Programs\opera
REM 	start launcher.exe "https://nauka.vesti.ru/article/1046760"
	
	goto end

)

REM =================================
REM 	greek(ancient)
REM 	2019/07/04 10:03:32
REM =================================
) else if "%1"=="gr" (

	echo %%1 is %1!

	pushd "C:\WORKS_2\Programs\opera"

REM ===============
REM 	trans
REM ===============
	
start launcher.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=el&tl=en"

REM ===============
REM 	lang
REM ===============
REM 	start launcher.exe "https://writer.zoho.com/writer/open/eirjm1f770439a83d4d53a9700909fef4204c"
REM 	start launcher.exe "https://docs.google.com/document/d/1iPQgSMStNaTSk6amjyu3gGYI2PyIzQhPBfsnOgTcWks/edit"
	
REM ===============
REM 	resources
REM ===============
REM ref : https://duckduckgo.com/?q=bible+online+in+greek&atb=v84-1&ia=web

	

REM 	start chrome.exe "https://biblehub.com/interlinear/acts/1.htm"
	start launcher.exe ""https://biblehub.com/interlinear/matthew/15.htm"
	start launcher.exe "http://greekbible.com/index.php"
	
REM 	start launcher.exe "https://docs.google.com/spreadsheets/d/10NSNuFVtup6FsuM18mIJvSS75nQLFjDQTUmbHE-eiFE/edit#gid=481191813"
	
	start "C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\ancient_greek.ods"
	
REM 	start launcher.exe "https://www.scripture4all.org/OnlineInterlinear/NTpdf/act1.pdf"
REM 	start launcher.exe "https://www.jw.org/en/publications/bible/study-bible/books/matthew/6/"
REM 	
REM 	start launcher.exe ""

REM 	start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\ancient_greek.odt
	start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\ancient_greek.ods

REM : dir
	startC:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang

REM ===============
REM 	memo : steps
REM 	
REM ===============

REM 	start launcher.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=steps+russian&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
	
	goto end

)

REM =================================
REM 	quran
REM 	2019/07/04 10:41:06
REM =================================
) else if "%1"=="qu" (

	echo %%1 is %1!

REM ===============
REM 	trans
REM ===============
	
start chrome.exe "https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=ar&tl=en"

REM ===============
REM 	lang
REM ===============

	start chrome.exe "https://docs.google.com/document/d/1-8vAIWQUg7IuGQBcABT2HhjTW0U_Qu-h1bb77hX2h7A/edit"
	
REM ===============
REM 	resources
REM ===============

REM ref : https://duckduckgo.com/?q=quran+online+in+arabic&atb=v84-1&ia=web

	start chrome.exe "https://al-quran.info/#1"
	start chrome.exe "https://www.searchtruth.com/chapter_display.php"
	start chrome.exe "https://www.scripture4all.org/OnlineInterlinear/NTpdf/act1.pdf"
REM 	
REM 	start chrome.exe ""

REM ===============
REM 	memo : steps
REM 	
REM ===============

REM 	start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=steps+russian&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
	
	goto end

)

REM flag
:all

REM debug
goto end

REM ================================================
REM 	all langs
REM 	2019/06/15 09:53:28
REM ================================================
REM =================================
REM 	trans
REM =================================
pushd "C:\Program Files (x86)\Google\Chrome\Application"
start chrome.exe  "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ja&tl=ko"
start chrome.exe "https://translate.google.co.jp/?hl=ja&tab=iT#view=home&op=translate&sl=ko&tl=ja"
REM REM start chrome.exe "https://docs.google.com/spreadsheets/d/1F1YZqjlwgDSTMxS5HhAAbjPL8sx1g184xxQqbgwWhps/edit#gid=1486363973"

start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=diary+K*&RBs_AND_OR_Memo=AND&sort=file_name&direction=desc"


REM =================================
REM 	korean
REM =================================
REM korean
REM start chrome.exe "https://docs.google.com/document/d/1XBlAyn1jrDdf-QcJrD6oXNI2efjbbCgISMt4UrjTTFI/edit"
REM start chrome.exe "https://docs.google.com/document/d/1nyvZkGJWZ8KolNpGZena8SwbgoyPcQ01XQnd7I0m8Ko/edit"
REM start chrome.exe "https://writer.zoho.com/writer/open/eovu1bbc85f4e6cc94063a7fa950aaed8aa56"
start chrome.exe "https://docs.google.com/document/d/1BM1Rn73jF-EjadfN-HmbXJWVPOzRAW4pjXo6M5Qx02w/edit"

REM =================================
REM 	arabic
REM =================================
REM start chrome.exe "https://docs.google.com/document/d/1EWd6CKZptTbNfKgaCLR-hWeqSDDS8TTX1FQPjyjAdVQ/edit"
start chrome.exe "https://writer.zoho.com/writer/open/eovu101b2b5cc9dae4117b56a277773c427ab"

REM =================================
REM 	russian
REM =================================
REM russian
REM start chrome.exe "https://docs.google.com/document/d/1zdKTuOCUMgt_YwwG3lNZsunkhGD2BvzVn_YF-oMaPMQ/edit"
start chrome.exe "https://writer.zoho.com/writer/open/eirjm1f770439a83d4d53a9700909fef4204c"

REM =================================
REM 	hebrew
REM =================================
start chrome.exe "https://docs.google.com/document/d/1rvbIPLG4V6oanqnqkGwmfYU5kO4Ifo7EawcHxkqbTsY/edit"
REM start chrome.exe "https://writer.zoho.com/writer/open/ek7i4618ec2e97cde46499c89be752e195db0"

REM =================================
REM 	greek
REM =================================
REM greek [2019/05/15 17:47:07]
start chrome.exe "https://docs.google.com/document/d/1iPQgSMStNaTSk6amjyu3gGYI2PyIzQhPBfsnOgTcWks/edit"

start chrome.exe "https://ja.wikipedia.org/wiki/アラビア文字#字母"
start chrome.exe "https://ja.wikipedia.org/wiki/ヘブライ文字#文字"
start chrome.exe "https://www.bing.com/translator/"

REM =================================
REM 	time
REM 	2019/05/29 09:57:55
REM =================================
start chrome.exe "http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php"


REM =================================
REM 	polish
REM =================================
start chrome.exe "https://docs.google.com/document/d/1IzGhkKgNIosYdD7yTyjr68Kl64A8erONeddxJPTwX-g/edit"

goto end

echo start C:\WORKS_2\WS\WS_Cake_IFM11\iphone_to_upload
start C:\WORKS_2\WS\WS_Cake_IFM11\iphone_to_upload
echo start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang
start C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang

:end

REM ===============
REM 	time-related pages
REM ===============

goto time_related_opera
REM goto time_related_brave


:time_related_opera

REM 2020/02/17 12:42:05

	goto end_of_end
	
	pushd "C:\WORKS_2\Programs\opera"

	start launcher.exe "http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php"
	start launcher.exe "https://stopwatch-app.com/"

	goto end_of_end

:time_related_brave

	pushd "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application"

	start brave.exe "http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php"
	start brave.exe "https://stopwatch-app.com/"

	goto end_of_end
	
if "%1"=="he" (

) else (	
REM : time
start chrome.exe "http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php"

REM : stopwatch
start chrome.exe "https://stopwatch-app.com/"

)

:end_of_end
