# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20210707_174437

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\s-41~\
python s_41.py


pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\s-41~\
echo.>> log_s_41.log && echo ============================ >> log_s_41.log && python s_41.py >> log_s_41.log


echo.>> log_s_41.log
echo ============================ >> log_s_41.log
python s_41.py >> log_s_41.log




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


'''###################
    import : others
###################'''
# from shutil import copyfile
# 
# import pydotplus, math, time


###############################################


'''###################
    test_1()
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
    
    '''###################
        step : 2
            build : string
    ###################'''
    strOf_Coordinates   = "(a_i^%d)*(a_j^%d)"
#     strOf_Coordinates   = "(a_i^k)*(a_i^l)"
#     strOf_Coordinates   = "a_i^k*a_i^l"
    strOf_Formula       = ""
#     strOf_Formula       = strOf_Coordinates
    
    # wedge
    #ref https://wiki.python.org/moin/ForLoop
    for x in range(1, 4):
        
        for y in range(1, 4):
            
            #ref https://stackoverflow.com/questions/5309978/sprintf-like-functionality-in-python
            strOf_Formula += strOf_Coordinates % (x, y)
            
            strOf_Formula += "("
            strOf_Formula += "e->_%d∧e->_%d" % (x, y)
#             strOf_Formula += "e->_%d" % (x)
            strOf_Formula += ")"
            
            strOf_Formula += "+"
        
    #/for x in range(1, 4):


    
    print()
    
    print ("[%s:%d] strOf_Formula ==> " % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print(strOf_Formula)
    print()
    
    '''###################
        step : 3
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
