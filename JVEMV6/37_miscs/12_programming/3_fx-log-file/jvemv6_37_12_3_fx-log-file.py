# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\12_programming\3_fx-log-file\jvemv6_37_12_3_fx-log-file.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\jvemv6_37_12_1_guitar-memo.py
at : 2019/12/24 14:57:50

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\12_programming\3_fx-log-file\
python jvemv6_37_12_3_fx-log-file.py

### env
pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL
start_env.bat
pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\12_programming\3_fx-log-file\

<Usage> 2019/09/17 09:51:58
    1. file : memo_guitar.txt // C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar
        1. prep text
    2. run this program
        pushd C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL
        start_env.bat
        pushd C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\11_guitar\
        python jvemv6_37_12_1_guitar-memo.py
    3. open the newly-gen-ed file : memo_guitar.(replaced).(20190917_094828).txt

<git>
r a && s


'''
###############################################
import sys
from _datetime import datetime
from numpy import append

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects')
# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    import : built-in modules        
###################'''
import os, re

'''###################
    import : others
###################'''

'''###################
    vars : global
###################'''
SWITCH_DEBUG = True

DPATH_SETTINGS_FILE = "C:\\WORKS_2\\WS\\WS_Others.JVEMV6\\JVEMV6\\37_miscs\\12_programming\\3_fx-log-file"

FNAME_SETTINGS_FILE = "settings.dat"

DPATH_DAT_FILE = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE708E60511E\\MQL4\\Files\\Logs\\20191223_172758[eap-2.id-1].[AUDJPY-1].dir"
# DPATH_DAT_FILE = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE708E60511E\\MQL4\\Files\\Logs\\20190829_223434[eap-2.id-1].[EURJPY-1].dir"

# FNAME_DAT_FILE = "[eap-2.id-1].(20190829_223434).dat"
FNAME_DAT_FILE = "[ea-3].(20191223_172758).log.(20191223_182001).copy"

DPATH_REPORT_FILE = "C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE708E60511E\\MQL4\\Logs\\logs_trading"

FNAME_REPORT_FILE = "DetailedStatement.[20191224_145931].htm"
# FNAME_REPORT_FILE = "DetailedStatement.[20190901_145309].htm"

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    '''
    
    print (msg)

###################'''
    
'''###################
    _tester_BuyUps_SellLows__BUSL_3__Set_Conf
    
    at : 2019/12/24 16:40:52
    
    @return: confs
    
        {'FNAME_FILE_LOG': '[ea-3].(20191223_172758).log.(20191223_182001).copy', 'DPATH_FILE_LOG'
        : 'C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE7
        08E60511E\\MQL4\\Files\\Logs\\20191223_172758[eap-2.id-1].[AUDJPY-1].dir'}
        {'FNAME_FILE_LOG': '[ea-3].(20191223_172758).log.(20191223_182001).copy', 'DPATH_FILE_LOG'
        : 'C:\\Users\\iwabuchiken\\AppData\\Roaming\\MetaQuotes\\Terminal\\34B08C83A5AAE27A4079DE7
        08E60511E\\MQL4\\Files\\Logs\\20191223_172758[eap-2.id-1].[AUDJPY-1].dir'}    

###################'''
def _tester_BuyUps_SellLows__BUSL_3__Set_Conf(_dpath_Conf, _fname_Conf):
#_20191224_163909:head
#_20191224_163927:caller
#_20191224_163935:wl

    '''###################
        file : conf        
    ###################'''
    dpath_Conf = _dpath_Conf
    fname_Conf = _fname_Conf
#     dpath_Conf = cons_fx.FPath.DPATH_CONF_BUSL_3.value
#     fname_Conf = cons_fx.FPath.FNAME_CONF_BUSL_3.value
    
    f_conf = open(os.path.join(dpath_Conf, fname_Conf), "r")

    '''###################
        build : parmas set
    ###################'''
    confs = {}
    
    # build : conf 
    conf_lines = []
    
    conf_lines_tmp = f_conf.readlines()
    
    for item in conf_lines_tmp:
    
        # strip
        item_tmp = item.strip()
        
        #
        if not item_tmp.startswith("#") \
            and not item_tmp == "" : 
#         if not item.startswith("#") \
#             and not item == "" : 
            
            conf_lines.append(item.strip())
        
    #/for item in conf_lines_tmp:

    

#     print("[%s:%d] conf_lines ==>" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         
#                         ), file=sys.stderr)
#     print(conf_lines)
    
    # iterate
    for item in conf_lines:
    
        # trim
        tmp = item.strip()
        
        #
        tokens = tmp.split("=")
        
        confs[tokens[0]] = tokens[1]
        
    #/for item in conf_lines:

    '''###################
        file : close
    ###################'''
    f_conf.close()
    
    '''###################
        set : conf values
    ###################'''
    '''###################
        set : conf values : 
    ###################'''
#     cons_fx.FPath.BUSL_3_FNAME_PEAK_LIST.value = confs["BUSL_3_FNAME_PEAK_LIST"]
    
#     result = cons_fx.FPath.set_BUSL_3_CSV_Name("abc")
    
#     print("[%s:%d] result = %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , result
#                     ), file=sys.stderr)

    '''###################
        report
    ###################'''
    print("[%s:%d] conf ==> loaded" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        
                        ), file=sys.stderr)
    
    print(confs)

    '''###################
        return
    ###################'''
    return confs

#/ def _tester_BuyUps_SellLows__BUSL_3__Set_Conf():

def test_1():
    
    '''###################
        step : 1
            prep : vars
    ###################'''
    '''###################
        step : 2
            load : settings
    ###################'''
    confs = _tester_BuyUps_SellLows__BUSL_3__Set_Conf(DPATH_SETTINGS_FILE, FNAME_SETTINGS_FILE)
    
    msg = "[%s:%d] confs ==> (%d keys)" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , len(confs)
                    )
 
    print(confs)
    print(msg, file=sys.stderr)

    '''###################
        step : 2 : 2
            unpack
    ###################'''
    dpath_File_Log = confs['DPATH_FILE_LOG']
    
    fname_File_Log = confs['FNAME_FILE_LOG']
    
    
    '''###################
        step : 3
            load : log file
    ###################'''
    #_20191224_163832:next
#     get_ListOf_Ticket_Nums(dpath_File_Log, fname_File_Log)
    
    '''###################
        ops        
    ###################'''
    print("[%s:%d] test_1() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#def exec_prog()

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_1()

    print("[%s:%d] exec_prog() => done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#def exec_prog()

if __name__ == "__main__" :

    '''###################
    	validate : help option		
    ###################'''

    '''###################
    	get options		
    ###################'''

    '''###################
    	evecute		
    ###################'''
    exec_prog()

    print()
    
    print("[%s:%d] done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     print "[%s:%d] done" % (thisfile(), linenum())
