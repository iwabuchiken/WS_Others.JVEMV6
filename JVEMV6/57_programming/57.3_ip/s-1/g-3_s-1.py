# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20211003_115755

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57_programming\57.3_ip\s-1\
python g-3_s-1.py


pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57_programming\57.3_ip\s-1\
echo.>> log_g-3_s-1.log && echo ============================ >> log_g-3_s-1.log && python g-3_s-1.py >> log_g-3_s-1.log


echo.>> log_g-3_s-1.log
echo ============================ >> log_g-3_s-1.log
python g-3_s-1.py >> log_g-3_s-1.log




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
# from shutil import copyfile
# 
# import pydotplus, math, time

from PIL import Image

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
    '''###################
        step : 2 : 1
            prep : data : x
    ###################'''
    '''###################
        step : 4
            
    ###################'''
    '''###################
        step : 4 : 1
            prep : data
    ###################'''
    
# def test_1()://


'''###################
    test_2()
    at : 20211114_162850
###################'''
def test_2():

    strOf_FuncName = "func : test_2"

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
    dpath_Image = "C:\\WORKS_2\\WS\\WS_Others.JVEMV6\\JVEMV6\\57_programming\\57.3_ip\\s-1\\img"    
    fname_Image = "2021-07-21_07-12-58_000_resize-25-percent.jpg"
    
    #ref https://www.geeksforgeeks.org/python-os-path-join-method/
    fpath_Image = os.path.join(dpath_Image, fname_Image)
    
    img = Image.open(fpath_Image)
#     img = Image.open(dpath_Image + "\\" + fname_Image)
 
#     img.show()

    '''###################
        step : 3
            ops
    ###################'''
    '''###################
        step : 3 : 1
            ops : size, format
    ###################'''
    img_Size    = img.size
    img_Format  = img.format

    print()
    
    print ("[%s:%d] img_Size :" % (
            os.path.basename(os.path.basename(libs.thisfile()))
            , libs.linenum()
            )
    )
    
    print(img_Size, "data type : ", type(img_Size))
            #=> <class 'tuple'>
            
    print ("[%s:%d] img_Format :" % (
            os.path.basename(os.path.basename(libs.thisfile()))
            , libs.linenum()
            )
    )
    
    print(img_Format)


# def test_2():



def exec_prog(): # from : 
    
    
    '''###################
        execute
    ###################'''
    test_2()
#     test_1()
    
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
