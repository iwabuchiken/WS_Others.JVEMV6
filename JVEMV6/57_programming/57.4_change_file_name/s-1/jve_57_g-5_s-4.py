# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20221001_110812

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57_programming\57.4_change_file_name\s-1\
python jve_57_g-5_s-4.py


pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57_programming\57.4_change_file_name\s-1\
echo.>> log_g-5_s-4.log && echo ============================ >> log_g-5_s-4.log && C:\WORKS_2\t.bat >> log_g-5_s-4.log && echo.>> log_g-5_s-4.log && jve_57_g-5_s-4.py >> log_g-5_s-4.log


echo.>> log_g-5_s-4.log
echo ============================ >> log_g-5_s-4.log
jve_57_g-5_s-4.py >> log_g-5_s-4.log




###################
    import : basics
###################'''
import sys, os, getopt, inspect

os.environ["PATH"] += os.pathsep + 'C:/WORKS_2/Programs/Python/Python_3.5.1/lib_additional/'

pathOf_Python_3_5_1 = "C:\\WORKS_2\\Programs\\Python\\Python_3.5.1\\Lib\\site-packages"

#code:20210707_175722
os.environ["PATH"] += os.pathsep + pathOf_Python_3_5_1

'''###################
    import : orig files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

print(sys.path)

from libs import libs

print()

print ("[%s:%d] 'from libs import libs' ==> comp." % (
            os.path.basename(os.path.basename(libs.thisfile()))
            , libs.linenum()
            )
)

'''###################
    import : math
###################'''
# from math import pi, sin, cos
import math

'''###################
    import : scipy, numpy, matplotlib
###################'''
import numpy as np

import matplotlib.pyplot as plt



'''###################
    import : others
###################'''
#ref https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from os import listdir
from os.path import isfile, join

#re https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern
import re

# from shutil import copyfile
# 
# import pydotplus, math, time

# from PIL import Image

print ("[%s:%d] 'from PIL import Image' => done" % (os.path.basename(libs.thisfile()), libs.linenum()))

###############################################


'''###################
    test_1()
    at : 20211114_162850
###################'''
def test_1():

    strOf_FuncName = "func : test_1"

    '''###################
        step : 1
            opening, vars
    ###################'''
    print()
    
    print ("[%s:%d] starting : %s (time=%s)" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , strOf_FuncName
                , libs.get_TimeLabel_Now()
                )
    )
    
    '''###################
        step : 2
            prep
    ###################'''
    dpath   = "G:\\images\\2022"
    
    #ref https://stackoverflow.com/questions/2690324/list-directories-and-get-the-name-of-the-directory
    listOf_Dirs    = onlyfiles = [f for f in listdir(dpath) if os.path.isdir(join(dpath, f))]
#     listOf_Files    = onlyfiles = [f for f in listdir(dpath) if isfile(join(dpath, f))]

    # report
    print ("[%s:%d] dpath : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , dpath
                )
    )
    
        
    print ("[%s:%d] listOf_Dirs : " % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
#                 , strOf_FuncName
#                 , libs.get_TimeLabel_Now()
                )
    )
    
#     print(listOf_Dirs)
    
    # iterate
    for folder_name in listOf_Dirs:
    
        print(folder_name)
        
    #/for folder_name in listOf_Dirs:

#     print ("[%s:%d] listOf_Files : " % (
#                 os.path.basename(os.path.basename(libs.thisfile()))
#                 , libs.linenum()
# #                 , strOf_FuncName
# #                 , libs.get_TimeLabel_Now()
#                 )
#     )
#     
#     print(listOf_Files)
#     
    
    '''###################
        step : 3 : 1
            prep : pattern
    ###################'''
    #ref https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern
#     strOf_Pattern   = " "
    strOf_Pattern   = "21"
#     strOf_Pattern   = "21"
    
    print ("[%s:%d] strOf_Pattern : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , strOf_Pattern
                )
    )
    
     
    pattern = re.compile(strOf_Pattern)
#     pattern = re.compile(" - .+$")
    
    # iterate
    for folder_name in listOf_Dirs:
    
        res = re.match(r"21", folder_name)
#         res = pattern.match(folder_name)

        print ("[%s:%d] match result : " % (
                    os.path.basename(os.path.basename(libs.thisfile()))
                    , libs.linenum()
#                     , strOf_FuncName
#                     , libs.get_TimeLabel_Now()
                    )
        )
        
        print(res)
        
        if res : #if res
        
            # report
            print ("[%s:%d] match : %s" % (
                        os.path.basename(os.path.basename(libs.thisfile()))
                        , libs.linenum()
                        , folder_name
                        )
            )
        
        else : #if res
        
            # report
            print ("[%s:%d] NOT match : %s" % (
                        os.path.basename(os.path.basename(libs.thisfile()))
                        , libs.linenum()
                        , folder_name
                        )
            )
        
        #/if res
        
        
    
    
    
        
        
    '''###################
        step : 4
            
    ###################'''
    '''###################
        step : 4 : 1
            prep : data
    ###################'''
    
# def test_1()://


def exec_prog(): # from : 
    
    
    '''###################
        execute
    ###################'''
    test_1()
    
    '''###################
        Report        
    ###################'''
    print ("[%s:%d] exec_prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
 
#/def exec_prog(): # from : 20180116_103908

'''
<usage>
'''
if __name__ == "__main__" :

    '''###################
        validate : help option        
    ###################'''
    '''###################
        Report        
    ###################'''
    
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
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))




'''###################
    playarea

###################'''
