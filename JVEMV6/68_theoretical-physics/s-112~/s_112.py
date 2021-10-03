# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20211003_115755

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\s-45~\
python s_112.py


pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\s-112~\
echo.>> log_s_112.log && echo ============================ >> log_s_112.log && python s_112.py >> log_s_112.log


echo.>> log_s_112.log
echo ============================ >> log_s_112.log
python s_112.py >> log_s_112.log




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


###############################################


'''###################
    test_1()
    at : 20210728_131213
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
            prep
    ###################'''
    
    '''###################
        step : 3
            
    ###################'''
    a = math.pi
    
    cos_a   = math.cos(a)
    
    print()
    
    print ("[%s:%d] a = %.03f / cos(a) = %.03f" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , a
                , cos_a
                )
    )

    '''###################
        step : 4
            
    ###################'''
    '''###################
        step : 4 : 1
            prep : data
    ###################'''
    '''###################
        step : 4 : 1 : 
            prep : data : basics
    ###################'''
    #ref https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
#     numOf_Data_X    = 12
    numOf_Data_X    = 24
    
    valOf_Linspace_Start    = - math.pi / 2
    valOf_Linspace_End      = math.pi / 2
#     valOf_Linspace_Start    = 0
#     valOf_Linspace_End      = math.pi
    
    #ref https://matplotlib.org/stable/tutorials/introductory/customizing.html#sphx-glr-tutorials-introductory-customizing-py
    data_x  = np.linspace(
            valOf_Linspace_Start
            , valOf_Linspace_End
            , numOf_Data_X)

    '''###################
        step : 4 : 1 : 2
            prep : data : cosine values
    ###################'''
    k   = 1
    
    data_x_1    = [(2*k+1) * x for x in data_x]
    
    data_y      = np.cos(data_x)
    data_y_1    = np.cos(data_x_1)
    data_y_1_final    = [math.pow(-1, k) / (2 * k + 1) * x for x in data_y_1]
    

    print()
    
    print ("[%s:%d] numOf_Data_X = %d" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , numOf_Data_X
                )
    )
    
    print()
    
#     print ("[%s:%d] data_x =>" % (
#                 os.path.basename(os.path.basename(libs.thisfile()))
#                 , libs.linenum()
#                 )
#     )
#     
#     print(data_x)
# 
#     print ("[%s:%d] data_y =>" % (
#                 os.path.basename(os.path.basename(libs.thisfile()))
#                 , libs.linenum()
#                 )
#     )
#     
#     print(data_y)

    '''###################
        step : 4 : 2
            plot
    ###################'''
    '''###################
        step : 4 : 2 : 1
            plot : prep savefig
    ###################'''
    strOf_Time_Label = libs.get_TimeLabel_Now()
    
    #ref C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\1_1.py
    fig = plt.figure()

    dpath_PlotImage = "./data"
    fname_PlotImage = "plot_image_%s_[test]" % (strOf_Time_Label)
     
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    # title
#     plt.title("cos(a)\n numOf_Data_X = %d\n x [%.02f, %.02f]"
#     plt.title("cos(a), data_y_1\n numOf_Data_X = %d\n x [%.02f, %.02f]"
    plt.title("cos(a), data_y_1_final\n numOf_Data_X = %d\n x [%.02f, %.02f]"
               % (
                  numOf_Data_X
                  , valOf_Linspace_Start
                  , valOf_Linspace_End
                  )
               )    
    
    # axis
    #ref https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
    plt.axis([- math.pi/2, math.pi/2, -1.5, 1.5])
#     plt.axis([- math.pi/2, math.pi/2, -1.0, 1.0])
    
    '''###################
        step : 4 : 2 : 2
            plot : set data
    ###################'''
    plt.plot(data_x, data_y + data_y_1_final, 'y-o')
    plt.plot(data_x, data_y_1_final, 'b-o')
    plt.plot(data_x, data_y, 'r-o')
#     plt.plot(data_x, data_y_1, 'r-o')
#     plt.plot(data_x, data_y, 'r-o')
    
#     plt.show()

    '''###################
        step : 4 : 2 : 3
            plot : save image
    ###################'''
    fig.savefig(fpath_PlotImage)

    print ("[%s:%d] plot image saved => %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , fpath_PlotImage
                )
    )
    
    
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
