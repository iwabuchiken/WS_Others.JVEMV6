# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20210411_164856

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\
python 1_1.py


echo.>> log_session-1.log
echo ============================ >> log_session-1.log
python 1_1.py >> log_session-1.log

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\
echo.>> log_session-1.log && echo ============================ >> log_session-1.log && python 1_1.py >> log_session-1.log

    Regex
print "[%s:%d] result => %s" % (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
^ +(print )(".+" %.+\(.+\).*)$
^( +)(print )(".+" %.+\(.+\).*)$
$1$2($3)

print "[%s:%d] result => %s" % \
        (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
^( +)(print )(".+" %) \\\r\n(.+)$
$1$2($3)$4$5
$1$2($3 \\\r\n$4)

print ("[%s:%d] all done" % (libs.thisfile(), libs.linenum()))
^( +)(print )(.+)(libs.+file\(\))(.+)
$1$2$3os.path.basename($4)$5


https://stackoverflow.com/questions/29817447/how-to-run-pip-commands-from-cmd
>python -m pip list



'''


import sys
# from sympy.solvers.tests.test_constantsimp import C2

import os
from pandas.tests.io.msgpack.test_case import test_9

sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

from libs import libs
# from libs import libfx

from libs import cons

# from libs_D_7 import cons_D_7
# from libs_31 import libmt

import getopt, os, inspect

# import math as math

# import struct

from shutil import copyfile

# import xml.etree.ElementTree as ET

#ref https://qiita.com/okakatsuo/items/f2e79fc501ed9f799734 20201228_173042
# import matplotlib.pyplot as plt
# import matplotlib.patches as pat
# import math

###############################################
import matplotlib.pyplot as plt, matplotlib.patches as pat, math, numpy

from scipy import stats

#ref https://www.w3schools.com/python/python_ml_polynomial_regression.asp
from sklearn.metrics import r2_score


def test_1_statistics():

    strOf_FuncName = "test_1_statistics"

    print()
    
    print ("[%s:%d] starting : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , strOf_FuncName
                )
    )
    
#     from scipy import stats
    
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    
    x_mode  = stats.mode(speed)
    x_median  = numpy.median(speed)
    x_mean  = numpy.mean(speed)
    
    print()
    print("speed : ", speed)
    print()
    
    print(x_mode)
    print("x_median : ", x_median)
    print("x_mean : ", x_mean)
#     print(x_median)
#     print(x_mean)
    
    
# def test_1_statistics()://
    
def test_2_statistics_StdDev():

    strOf_FuncName = "test_2_statistics_StdDev"


    '''###################
        step : 1
            std
    ###################'''
    print()
    
    print ("[%s:%d] starting : %s (time=%s)" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , strOf_FuncName
                , libs.get_TimeLabel_Now()
                )
    )
    #aaa
#     from scipy import stats
    
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    
    x_std  = numpy.std(speed)
    
    print()
    print("speed : ", speed)
    print()
    
    print("x_std : ", x_std)

    '''###################
        step : 2
            variance
    ###################'''
    x_var  = numpy.var(speed)
    
    print()
    
    print("x_var : ", x_var)
    
# def test_1_statistics()://
    
def test_3_stats_Percentile():

    strOf_FuncName = "test_2_statistics_StdDev"


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
    
    #code:20210411_171845
    ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
    
    numOf_Percentile    = 75
    
    '''###################
        step : 2
            percentile
    ###################'''
    x_Percentile  = numpy.percentile(ages, numOf_Percentile)
    
    print()
    print("ages : ", ages)
    print()
    
    print("x_Percentile : ", x_Percentile)

    '''###################
        step : 2
    ###################'''
    
# def test_3_stats_Percentile()://
    
    
def test_4_stats_Distribution():

    strOf_FuncName = "test_4_stats_Distribution"


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

#     x = numpy.random.uniform(0.0, 5.0, 250)
    
#     print(x)     
    '''###################
        step : 2
            histo
    ###################'''
    numOf_Data = 100000
    
    x = numpy.random.uniform(0.0, 5.0, numOf_Data)

    #ref https://www.codespeedy.com/saving-a-plot-as-an-image-in-python/
    fig = plt.figure()
    
    numOf_HistColumns   = 100
    
    plt.hist(x, numOf_HistColumns)
#     plt.show() 

#     #ref https://www.codespeedy.com/saving-a-plot-as-an-image-in-python/
#     fig = plt.figure()
#     
    '''###################
        step : 3
            plot
    ###################'''
    dpath_PlotImage = "./data"
    fname_PlotImage = "plot_image_%s" % (libs.get_TimeLabel_Now())
    
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    # title
    plt.title("numOf_Data = %d, numOf_HistColumns : %d" % (numOf_Data, numOf_HistColumns))
    
    fig.savefig(fpath_PlotImage)

    # message
    print ("[%s:%d] save fig => done : %s" % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             , fpath_PlotImage
             )
           
           
           )

    '''###################
        step : 2
    ###################'''
    
# def test_4_stats_Distribution()://
    
def test_5_stats_Normal_Distribution():

    strOf_FuncName = "test_5_stats_Normal_Distribution"


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

#     x = numpy.random.uniform(0.0, 5.0, 250)
    
#     print(x)     
    '''###################
        step : 2
            histo
    ###################'''
    numOf_Data = 100000
    
    valOf_Mean  = 5.0
    valOf_StdDev    = 2.0
#     valOf_StdDev    = 1.0
    
    x = numpy.random.normal(valOf_Mean, valOf_StdDev, numOf_Data)

    #ref https://www.codespeedy.com/saving-a-plot-as-an-image-in-python/
    fig = plt.figure()
    
    numOf_HistColumns   = 100
    
    plt.hist(x, numOf_HistColumns)
#     
    '''###################
        step : 3
            plot
    ###################'''
    dpath_PlotImage = "./data"
    fname_PlotImage = "plot_image_%s" % (libs.get_TimeLabel_Now())
    
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    # title
    plt.title("numOf_Data = %d, numOf_HistColumns : %d \n/ valOf_Mean = %.03f, valOf_StdDev = %.03f" 
              % (
                 numOf_Data
                 , numOf_HistColumns
                 , valOf_Mean, valOf_StdDev
                 )
              
              
              )
    
    fig.savefig(fpath_PlotImage)

    # message
    print ("[%s:%d] save fig => done : %s" % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             , fpath_PlotImage
             )
           
           
           )

    '''###################
        step : 2
    ###################'''
    
# def test_5_stats_Normal_Distribution()://
    
def test_6_plot_Scatter():

    strOf_FuncName = "test_6_plot_Scatter"


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

#     x = numpy.random.uniform(0.0, 5.0, 250)
    
#     print(x)     
    '''###################
        step : 2
            histo
    ###################'''
#     numOf_Data = 100000
#     
    valOf_Mean  = 5.0
    valOf_StdDev    = 2.0
#     valOf_StdDev    = 1.0
    
    #ref https://www.askpython.com/python/array/initialize-a-python-array
    a    = [0 for i in range(2000)] 
#     a    = [0 for i in range(200)] 
#     a = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    
    x = numpy.random.normal(valOf_Mean, valOf_StdDev, len(a))
    y = numpy.random.normal(valOf_Mean, valOf_StdDev, len(a))
#     y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    #ref https://www.codespeedy.com/saving-a-plot-as-an-image-in-python/
    fig = plt.figure()
    
#     numOf_HistColumns   = 100
#     
#     plt.hist(x, numOf_HistColumns)
#     
    
    plt.scatter(x, y)
    
    '''###################
        step : 3
            plot
    ###################'''
    dpath_PlotImage = "./data"
    fname_PlotImage = "plot_image_%s" % (libs.get_TimeLabel_Now())
    
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    # title
    plt.title("scatter : x, y --> normal dist \n(valOf_Mean = %.02f, valOf_StdDev = %.02f)\nentries = %d" 
            % (
#                  numOf_Data
#                  , numOf_HistColumns
                valOf_Mean, valOf_StdDev
                , len(a)
                )
              
              
              )
    
    fig.savefig(fpath_PlotImage)

    # message
    print ("[%s:%d] save fig => done : %s" % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             , fpath_PlotImage
             )
           
           
           )

    '''###################
        step : 2
    ###################'''
    
# def test_6_plot_Scatter()://
    
#ref https://www.w3schools.com/python/python_ml_linear_regression.asp
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

# def myfunc(x, slope, intercept):
def myfunc(x):
  return slope * x + intercept

def test_7_Linear_Regression():

    strOf_FuncName = "test_7_Linear_Regression"


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

#     x = numpy.random.uniform(0.0, 5.0, 250)
    
#     print(x)     
    '''###################
        step : 2
            histo
    ###################'''
#     numOf_Data = 100000
#     
#     valOf_Mean  = 5.0
#     valOf_StdDev    = 2.0
#     valOf_StdDev    = 1.0
    
    #ref https://www.askpython.com/python/array/initialize-a-python-array
#     a    = [0 for i in range(2000)] 
#     a    = [0 for i in range(200)] 
#     a = [5,7,8,7,2,17,2,9,4,11,12,9,6]
#     x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
#     y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#     x = numpy.random.normal(valOf_Mean, valOf_StdDev, len(a))
#     y = numpy.random.normal(valOf_Mean, valOf_StdDev, len(a))
#     y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    #ref https://www.codespeedy.com/saving-a-plot-as-an-image-in-python/
    fig = plt.figure()
    
#     numOf_HistColumns   = 100
#     
#     plt.hist(x, numOf_HistColumns)
#     
    
#     slope, intercept, r, p, std_err = stats.linregress(x, y)
    
    plt.scatter(x, y)
    
#     mymodel = list(map(myfunc, x, slope, intercept))
    mymodel = list(map(myfunc, x))
    plt.plot(x, mymodel)
    
    '''###################
        step : 3
            plot
    ###################'''
    dpath_PlotImage = "./data"
    fname_PlotImage = "plot_image_%s" % (libs.get_TimeLabel_Now())
    
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    # title
    plt.title("scatter : x, y" 
#             % (
# #                  numOf_Data
# #                  , numOf_HistColumns
#                 valOf_Mean, valOf_StdDev
#                 , len(a)
#                 )
              
              
              )
    
    fig.savefig(fpath_PlotImage)

    # vars
    print ("[%s:%d] 'r' =>" 
#            % 
#             (
#              os.path.basename(libs.thisfile())
#              , libs.linenum()
#              , fpath_PlotImage
#              )
           )
    print(r)
    
    print ("[%s:%d] 'slope' =>")
    print(slope)

    print ("[%s:%d] 'p' =>")
    print(p)
    
    print ("[%s:%d] 'map(myfunc, x)' =>")
    print(map(myfunc, x))
    
    print ("[%s:%d] 'list(map(myfunc, x))' =>")
    print(list(map(myfunc, x)))

    # message
    print ("[%s:%d] save fig => done : %s" % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             , fpath_PlotImage
             )
           
           
           )

    '''###################
        step : 2
    ###################'''
    
# def test_7_Linear_Regression()://
    
def test_8_Regression_Poly():

    strOf_FuncName = "test_8_Regression_Poly"


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
            histo
    ###################'''
    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
    
    #code:20210414_152625
#     mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
    valOf_Fit   = 5
    mymodel = numpy.poly1d(numpy.polyfit(x, y, valOf_Fit))

    myline = numpy.linspace(1, 22, 100)
    
#     #debug
#     print ("[%s:%d] myline =>" % 
#                 (
#                  os.path.basename(libs.thisfile())
#                  , libs.linenum()
#                  )
#            )
#     
#     print(myline)

    fig = plt.figure()
    
    plt.scatter(x, y)
    
    plt.plot(myline, mymodel(myline))
    
#     mymodel = list(map(myfunc, x))
#     plt.plot(x, mymodel)
    
    '''###################
        step : 3
            plot
    ###################'''
    dpath_PlotImage = "./data"
    fname_PlotImage = "plot_image_%s" % (libs.get_TimeLabel_Now())
    
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    # title
#     plt.title("scatter : x, y" 
    plt.title("scatter : x, y\nvalOf_Fit : %d" 
            % (
               valOf_Fit
                )
              
              
              )
    
    fig.savefig(fpath_PlotImage)

    # message
    print ("[%s:%d] save fig => done : %s" % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             , fpath_PlotImage
             )
           
           
           )

    '''###################
        step : 2
    ###################'''
    
# def test_8_Regression_Poly()://
    
def test_9_R_Square():

    strOf_FuncName = "test_9_R_Square"


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
            histo
    ###################'''
    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
    
    #code:20210414_152625
#     mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
    valOf_Fit   = 5
    mymodel = numpy.poly1d(numpy.polyfit(x, y, valOf_Fit))

    print ("[%s:%d] r2_score(y, mymodel(x)) ==>" 
#            % 
#             (
#              os.path.basename(libs.thisfile())
#              , libs.linenum()
#              , fpath_PlotImage
#              )
            
            
           )
    print(r2_score(y, mymodel(x)))
    
#     fig = plt.figure()
#     
#     plt.scatter(x, y)
#     
#     plt.plot(myline, mymodel(myline))
#     
# #     mymodel = list(map(myfunc, x))
# #     plt.plot(x, mymodel)
#     
#     '''###################
#         step : 3
#             plot
#     ###################'''
#     dpath_PlotImage = "./data"
#     fname_PlotImage = "plot_image_%s" % (libs.get_TimeLabel_Now())
#     
#     fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
#     
#     # title
# #     plt.title("scatter : x, y" 
#     plt.title("scatter : x, y\nvalOf_Fit : %d" 
#             % (
#                valOf_Fit
#                 )
#               
#               
#               )
#     
#     fig.savefig(fpath_PlotImage)
# 
#     # message
#     print ("[%s:%d] save fig => done : %s" % 
#             (
#              os.path.basename(libs.thisfile())
#              , libs.linenum()
#              , fpath_PlotImage
#              )
#            
#            
#            )

    '''###################
        step : 2
    ###################'''
    
# def test_9_R_Square()://
    
def test_10_Predict():

    strOf_FuncName = "test_10_Predict"


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
            histo
    ###################'''
    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
    
    #code:20210414_152625
#     mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
    valOf_Fit   = 5
    mymodel = numpy.poly1d(numpy.polyfit(x, y, valOf_Fit))
    
    myline = numpy.linspace(1, 22, 100)
    
#     print ("[%s:%d] r2_score(y, mymodel(x)) ==>" 
# #            % 
# #             (
# #              os.path.basename(libs.thisfile())
# #              , libs.linenum()
# #              , fpath_PlotImage
# #              )
#             
#             
#            )
#     print(r2_score(y, mymodel(x)))
    
    fig = plt.figure()
     
    plt.scatter(x, y)
     
    plt.plot(myline, mymodel(myline))
    
    # prediction
    numOf_Prediction_Target = 17
    
    #ref https://stackoverflow.com/questions/16006572/plotting-different-colors-in-matplotlib
    #ref https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html <== this
    plt.plot(numOf_Prediction_Target, mymodel(numOf_Prediction_Target), 'ro')
#     plt.plot(numOf_Prediction_Target, mymodel(numOf_Prediction_Target), col='red')
    
     
    '''###################
        step : 3
            plot
    ###################'''
    dpath_PlotImage = "./data"
    fname_PlotImage = "plot_image_%s" % (libs.get_TimeLabel_Now())
     
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
     
    # title
#     plt.title("scatter : x, y" 
    plt.title("scatter : x, y\nvalOf_Fit : %d\npredict-for : x = %d" 
            % (
               valOf_Fit
               , numOf_Prediction_Target
                )
               
               
              )
     
    fig.savefig(fpath_PlotImage)
 
    # message
    print ("[%s:%d] save fig => done : %s" % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             , fpath_PlotImage
             )
            
            
           )

    '''###################
        step : 2
    ###################'''
    
# def test_10_Predict()://
    
    

def exec_prog(): # from : 
    
    
    '''###################
        execute
    ###################'''
    #n:20210413_142903
    #n:20210412_151638
    #n:20210411_172354
    #n:20210414_160053
    test_10_Predict()
#     test_9_R_Square()
#     test_8_Regression_Poly()
#     test_7_Linear_Regression()
#     test_6_plot_Scatter()
#     test_5_stats_Normal_Distribution()
#     test_4_stats_Distribution()
#     test_3_stats_Percentile()
#     test_2_statistics_StdDev()
#     test_1_statistics()
    
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

20210414_151340
#ref https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html
import numpy as np
p = np.poly1d([1, 2, 3])
print(p)
           2
        1 x + 2 x + 3
p(1.5)
        8.25
p.r
        array([-1.+1.41421356j, -1.-1.41421356j])
        
print(p.r)
        [-1.+1.41421356j -1.-1.41421356j]

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

pf = np.polyfit(x, y, 3)
print(pf)
        [ -3.03208795e-02   1.34333191e+00  -1.55383039e+01   1.13768037e+02]
        
mymodel = np.poly1d(pf)
                  3         2
        -0.03032 x + 1.343 x - 15.54 x + 113.8


###################'''
