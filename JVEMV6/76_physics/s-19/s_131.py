# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20211003_115755

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\s-45~\
python s_131.py


pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\s-131\
echo.>> log_s_131.log && echo ============================ >> log_s_131.log && python s_131.py >> log_s_131.log


echo.>> log_s_131.log
echo ============================ >> log_s_131.log
python s_131.py >> log_s_131.log




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
        step : 2 : 1
            prep : data : x
    ###################'''
    #mark:20211030_153553
#     numOf_Data_X    = 24
    numOf_Data_X    = 36
    
    valOf_Linspace_Start    = - math.pi / 2
    valOf_Linspace_End      = math.pi / 2
    
    #ref https://matplotlib.org/stable/tutorials/introductory/customizing.html#sphx-glr-tutorials-introductory-customizing-py
    data_x  = np.linspace(
            valOf_Linspace_Start
            , valOf_Linspace_End
            , numOf_Data_X)

    print()
    
    print ("[%s:%d] data_x =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print(data_x)
    
    '''###################
        step : 2 : 2
            prep : data : y --> cos(x)
    ###################'''
    data_y  = [math.cos(x) for x in data_x]

    print()
    
    print ("[%s:%d] data_y =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print(data_y)
    

        
    '''###################
        step : 3
            plot
    ###################'''
    '''###################
        step : 3 : 1
            plot : prep
    ###################'''
    # folder
    strOf_Time_Label = libs.get_TimeLabel_Now()
    
#     dpath_data = "./data"
    dpath_data = "data"
    dname_PlotImage = "plot_%s" % (strOf_Time_Label)
#     dname_PlotImage = "plot_image_%s" % (strOf_Time_Label)
     
    dpath_PlotImage = os.path.join(dpath_data, dname_PlotImage)
    
    # file name
    fname_Plot      = "plot_%s" % (strOf_Time_Label)
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_Plot)
    
    #ref https://www.askpython.com/python/examples/create-a-directory-in-python
    res = os.mkdir(dpath_PlotImage)
    
    print()
    
    print ("[%s:%d] os.mkdir for => : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , dpath_PlotImage
                )
    )
    
    print(res)

    '''###################
        step : 3 : 2
            plot : plot
    ###################'''
    #ref C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\1_1.py
    fig = plt.figure()
    
    # title
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
    
    # plot
    plt.plot(data_x, data_y,'b-o')
    
    # grid
    #ref https://www.w3schools.com/python/matplotlib_grid.asp
    plt.grid()
    
    # save image
    res = fig.savefig(fpath_PlotImage)
    
    print()
    
    print ("[%s:%d] result for 'fig.savefig' : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , fpath_PlotImage
                )
    )
    
    print(res)
    
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
    at : 20210728_131213
###################'''
def test_2():

    strOf_FuncName = "test_2"

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
    #mark:20211030_153553
#     numOf_Data_X    = 24
    numOf_Data_X    = 36
    
    valOf_Linspace_Start    = - math.pi / 2
    valOf_Linspace_End      = math.pi / 2
    
    #ref https://matplotlib.org/stable/tutorials/introductory/customizing.html#sphx-glr-tutorials-introductory-customizing-py
    data_x  = np.linspace(
            valOf_Linspace_Start
            , valOf_Linspace_End
            , numOf_Data_X)

#     print()
#     
#     print ("[%s:%d] data_x =>" % (
#                 os.path.basename(os.path.basename(libs.thisfile()))
#                 , libs.linenum()
#                 )
#     )
#     
#     print(data_x)
    
    '''###################
        step : 2 : 2
            prep : data : y --> cos(x)
    ###################'''
    #mark:20211030_154118
    k = 3
#     k = 1
#     k = 2
    
    coord_1 = math.pow(-1, k) / (2*k+1)
    
    data_y  = [math.cos(x) for x in data_x]
    
    data_y_with_coord  = [coord_1 * y for y in data_y]

    # y vals --> add
    #mark:20211030_155934
    data_y_sum = data_y + data_y_with_coord

    #mark:20211030_162412
    lenOf_data_y    = len(data_y)
    
    data_y_sum_2 = [data_y[i] + data_y_with_coord[i] for i in range(lenOf_data_y)]

    #debug:20211030_160239
    print()
     
    print ("[%s:%d] len(data_y) => %d / len(data_y_with_coord) => %d" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , len(data_y)
                , len(data_y_with_coord)
                )
    )
     
    print ("[%s:%d] len(data_y_sum) => %d / len(data_y_sum_2) => %d" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , len(data_y_sum)
                , len(data_y_sum_2)
                )
    )
     
    
    print()

#     #debug
#     return

#     print()
#      
#     print ("[%s:%d] data_y =>" % (
#                 os.path.basename(os.path.basename(libs.thisfile()))
#                 , libs.linenum()
#                 )
#     )
#      
#     print(data_y)
#     
#     print()
#      
#     print ("[%s:%d] data_y_with_coord =>" % (
#                 os.path.basename(os.path.basename(libs.thisfile()))
#                 , libs.linenum()
#                 )
#     )
#      
#     print(data_y_with_coord)
    

        
    '''###################
        step : 3
            plot
    ###################'''
    '''###################
        step : 3 : 1
            plot : prep
    ###################'''
    # folder
    strOf_Time_Label = libs.get_TimeLabel_Now()
    
#     dpath_data = "./data"
    dpath_data = "data"
    dname_PlotImage = "plot_%s" % (strOf_Time_Label)
#     dname_PlotImage = "plot_image_%s" % (strOf_Time_Label)
     
    dpath_PlotImage = os.path.join(dpath_data, dname_PlotImage)
    
    # file name
    #mark:20211030_163128
    fname_Plot      = "plot_%s_(k=%d)" % (strOf_Time_Label, k)
#     fname_Plot      = "plot_%s" % (strOf_Time_Label)
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_Plot)
    
    #ref https://www.askpython.com/python/examples/create-a-directory-in-python
    res = os.mkdir(dpath_PlotImage)
    
    print()
    
    print ("[%s:%d] os.mkdir for => : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , dpath_PlotImage
                )
    )
    
    print(res)

    '''###################
        step : 3 : 2
            plot : plot
    ###################'''
    #ref C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\1_1.py
    fig = plt.figure()
    
    # title
#     plt.title("cos(a), data_y_1_final\n numOf_Data_X = %d\n x [%.02f, %.02f]"
#     plt.title("cos(a), data_y_with_coord\n numOf_Data_X = %d\n x [%.02f, %.02f]"
    plt.title("cos(a), data_y_with_coord\n numOf_Data_X = %d\n x [%.02f, %.02f] / k = %d"
               % (
                  numOf_Data_X
                  , valOf_Linspace_Start
                  , valOf_Linspace_End
                  , k
                  )
               )    
    
    # axis
    #ref https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
    plt.axis([- math.pi/2, math.pi/2, -1.5, 1.5])
    
    # plot
    #mark:20211030_154535
    plt.plot(data_x, data_y,'b-o')
    plt.plot(data_x, data_y_with_coord,'r-o')
    
    #mark:20211030_160000
    plt.plot(data_x, data_y_sum_2,'y-+')
#     plt.plot(data_x, data_y_sum,'y-+')
    
    # grid
    #ref https://www.w3schools.com/python/matplotlib_grid.asp
    plt.grid()
    
    # save image
    res = fig.savefig(fpath_PlotImage)
    
    print()
    
    print ("[%s:%d] result for 'fig.savefig' : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , fpath_PlotImage
                )
    )
    
    print(res)
    
    '''###################
        step : 4
            
    ###################'''
    '''###################
        step : 4 : 1
            prep : data
    ###################'''
    
# def test_2()://


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
