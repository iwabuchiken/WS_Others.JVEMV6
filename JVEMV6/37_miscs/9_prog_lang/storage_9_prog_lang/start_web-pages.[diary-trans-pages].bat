@echo off

REM opening message
echo starting start_web-pages.[diary-trans-pages].bat // C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang

pushd "C:\WORKS_2\Programs\opera"

set trans_pl_en="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=pl&tl=en"
set trans_en_pl="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=pl"

set trans_ru_en="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=ru&tl=en"
set trans_en_ru="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=ru"

set trans_ar_en="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=ar&tl=en"
set trans_en_ar="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=ar"

set trans_zhcn_en="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=zh-CN&tl=en"
set trans_en_zhcn="https://translate.google.co.jp/?hl=ja#view=home&op=translate&sl=en&tl=zh-CN"

rem %trans_pl_en% %trans_en_pl% %trans_ru_en% %trans_en_ru% %trans_ar_en% %trans_en_ar% %trans_zhcn_en% %trans_en_zhcn%

start launcher.exe %trans_pl_en% %trans_en_pl%
start launcher.exe  %trans_ru_en% %trans_en_ru%
start launcher.exe  %trans_ar_en% %trans_en_ar%
start launcher.exe  %trans_zhcn_en% %trans_en_zhcn%

REM :end_of_end

REM gen ==> time label
