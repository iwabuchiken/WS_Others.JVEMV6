REM @ECHO OFF

REM *************************************
REM 	folders
REM *************************************
start  C:\WORKS_2\WS\WS_Others.JVEMV6\VX7GLZ\28_\3CVF

REM *************************************
REM 	freemind
REM 	2019/06/27 13:53:48
REM *************************************
pushd C:\WORKS_2\Programs\FreeMind_1.0.1

start FreeMind.exe

REM *************************************
REM 	sakura
REM 	2019/07/05 16:56:01
REM *************************************
start C:\WORKS_2\Programs\sakura\sakura.exe

REM *************************************
REM 	browser
REM *************************************
REM : dispatch
goto twistor

pushd "C:\Program Files (x86)\Google\Chrome\Application"

REM : stopwatch
start chrome.exe "https://stopwatch-app.com/"

REM : time
start chrome.exe "http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php"

REM : doc
REM start chrome.exe "https://writer.zoho.com/writer/open/evojo0ac2afd051f8447d8185fb8d85268245"
start chrome.exe "https://docs.google.com/document/d/1IrkPHZlHc2_JV_CHsmY6Lk8SRx3bBDkPbW1IdHYV0pI/edit"

REM : cake
REM start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=VX7GLZ+27#15&RBs_AND_OR_Memo=AND&direction=desc"
REM start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=VX7GLZ+28#3CVF&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
REM start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=VX7GLZ+28^#3CVF&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
REM start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=VX7GLZ+28##3CVF&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
REM start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=VX7GLZ+28\#3CVF&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"
start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=VX7GLZ+28#3CVF&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"

goto end

REM *************************************
REM 	browser
REM *************************************
:twistor

pushd "C:\Program Files (x86)\Google\Chrome\Application"

REM *******************
REM 	util pages
REM *******************
REM : stopwatch
start chrome.exe "https://stopwatch-app.com/"

REM : time
start chrome.exe "http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php"

REM *******************
REM 	doc
REM *******************
REM : doc
REM start chrome.exe "https://writer.zoho.com/writer/open/evojo0ac2afd051f8447d8185fb8d85268245"
start chrome.exe "https://docs.google.com/document/d/1zeE0p2jhM-QX3KPPsnwMgPi6FeJojvHqxOpA414sUjw/edit"

REM *******************
REM 	memos
REM *******************
REM : cake
start chrome.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=VX7GLZ+twistor&sort=file_name&direction=desc&RBs_AND_OR_Memo=AND"

goto end

:end
