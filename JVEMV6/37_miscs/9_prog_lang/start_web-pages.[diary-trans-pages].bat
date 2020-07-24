@echo off

REM opening message
echo starting start_web-pages.[diary-trans-pages].bat // C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang

pushd "C:\WORKS_2\Programs\opera"

set trans_1_1="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=pl&tl=en"
set trans_1_2="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=pl"

set trans_2_1="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=ru&tl=en"
set trans_2_2="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=ru"

set trans_3_1="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=ar&tl=en"
set trans_3_2="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=ar"

set trans_4_1="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=zh-CN&tl=en"
set trans_4_2="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=zh-CN"

rem %trans_1_1% %trans_1_2% %trans_2_1% %trans_2_2% %trans_3_1% %trans_3_2% %trans_4_1% %trans_4_2%

start launcher.exe %trans_1_1% %trans_1_2% %trans_2_1% %trans_2_2% %trans_3_1% %trans_3_2% %trans_4_1% %trans_4_2%

REM :end_of_end

REM gen ==> time label
