# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20210707_174437

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\26\1MPF_drink-alcohol\
python s_1.py


echo.>> log_s-1.log
echo ============================ >> log_s-1.log
python s_1.py >> log_s-1.log

##
pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\26\1MPF_drink-alcohol\
echo.>> log_s-1.log && echo ============================ >> log_s-1.log && python s_1.py >> log_s-1.log

###
>echo.>> log_s-1.log && echo ============================ >> log_s-1.log && python s_1.py a,b,c >> log_s-1.log
# >echo.>> log_s-1.log && echo ============================ >> log_s-1.log && python s_1.py [a,b,c] >> log_s-1.log

###################
    import : basics
###################'''
import sys, os, getopt, inspect

os.environ["PATH"] += os.pathsep + 'C:/WORKS_2/Programs/Python/Python_3.5.1/lib_additional/'

pathOf_Python_3_5_1 = "C:\\WORKS_2\\Programs\\Python\\Python_3.5.1\\Lib\\site-packages"

os.environ["PATH"] += os.pathsep + pathOf_Python_3_5_1


'''###################
    import : orig files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

print(sys.path)

from libs import libs
# # from libs import libfx
# 
# from libs import cons

print()

print ("[%s:%d] 'from libs import libs' ==> comp." % (
            os.path.basename(os.path.basename(libs.thisfile()))
            , libs.linenum()
            )
)


'''###################
    import : sklearn
###################'''

'''###################
    import : scipy, numpy, matplotlib
###################'''
# from scipy import stats
# 
# # import numpy
# import numpy as np
# 
# import matplotlib.pyplot as plt
# import matplotlib.patches as pat
# import matplotlib.image as pltimg

'''###################
    import : others
###################'''
# from shutil import copyfile
# 
# import pydotplus, math, time




'''###################
    def test_1():
    at : 20210708_155754
###################'''
def test_1():

    strOf_FuncName = "test_1"

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
    
    # path var
    print ("[%s:%d] PATH variable : " % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print(sys.path)

    '''###################
        step : 2
            sys.argv
    ###################'''
    print()
    
    print ("[%s:%d] sys.argv ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print(sys.argv)

    '''###################
        step : 2 : 1
            arg : 2nd arg
    ###################'''
    arg_2 = sys.argv[1]
    
    print()
    
    print ("[%s:%d] sys.argv[1] ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print(arg_2)
    print("type(arg_2) => ", type(arg_2))
    
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
