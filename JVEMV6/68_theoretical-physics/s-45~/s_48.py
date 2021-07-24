# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20210707_174437

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\s-45~\
python s_48.py


pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\s-45~\
echo.>> log_s_48.log && echo ============================ >> log_s_48.log && python s_48.py >> log_s_48.log


echo.>> log_s_48.log
echo ============================ >> log_s_48.log
python s_48.py >> log_s_48.log




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
    import : matplotlib
###################'''
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

print()

print ("[%s:%d] import mplot3d a.o. ==> comp." % (
            os.path.basename(os.path.basename(libs.thisfile()))
            , libs.linenum()
            )
)

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
    ###################'''
    fig = plt.figure()
     
    # syntax for 3-D projection
    ax = plt.axes(projection ='3d')
     
    # defining all 3 axes
    x = [1,1,-1,    2,2,2,2]
    y = [-1,1,1,    -1,1,2,-2]
    z = [1,-1,1,    1/2,-1/2,-1/4,1/4]
#     z = np.linspace(0, 1, 100)
#     x = z * np.sin(25 * z)
#     y = z * np.cos(25 * z)
     
    # plotting
    ax.plot3D(x, y, z, 'green')
    ax.set_title('3D line plot geeks for geeks')
    plt.show()    
    
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
