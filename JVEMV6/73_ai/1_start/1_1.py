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


# from sympy.solvers.tests.test_constantsimp import C2

'''###################
    import : basics
###################'''
import sys, os, getopt, inspect

os.environ["PATH"] += os.pathsep + 'C:/WORKS_2/Programs/Python/Python_3.5.1/lib_additional/'

'''###################
    import : pandas
###################'''
from pandas.tests.io.msgpack.test_case import test_9
import pandas

'''###################
    import : sklearn
###################'''
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

#ref https://www.w3schools.com/python/python_ml_polynomial_regression.asp
from sklearn.metrics import r2_score

from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

'''###################
    import : orig files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

from libs import libs
# from libs import libfx

from libs import cons

# from libs_D_7 import cons_D_7
# from libs_31 import libmt

'''###################
    import : scipy, numpy, matplotlib
###################'''
from scipy import stats

import numpy

import matplotlib.pyplot as plt
import matplotlib.patches as pat
import matplotlib.image as pltimg



'''###################
    import : others
###################'''
from shutil import copyfile

import pydotplus, math

# import getopt, inspect

# import math as math

# import struct


# import xml.etree.ElementTree as ET

#ref https://qiita.com/okakatsuo/items/f2e79fc501ed9f799734 20201228_173042
# import matplotlib.pyplot as plt
# import matplotlib.patches as pat
# import math

###############################################



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
    
def test_11_Regresson_Multiple():

    strOf_FuncName = "test_11_Regresson_Multiple"


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
    #ref https://www.w3schools.com/python/python_ml_multiple_regression.asp
    df = pandas.read_csv("cars.csv")
    
#     #debug
#     # message
#     print ("[%s:%d] df ==>" 
#            % 
#             (
#              os.path.basename(libs.thisfile())
#              , libs.linenum()
#              )
#             
#             
#            )
#     
#     print(df)

    '''###################
        step : 2
            regression
    ###################'''
    X = df[['Weight', 'Volume']]
    y = df['CO2']
    
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    
    #debug
    # message
    print ("[%s:%d] regr ==>" 
           % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             )
             
             
           )
     
    print(regr)
    

    '''###################
        step : 3
            predic
    ###################'''
    predictedCO2 = regr.predict([[2300, 1300]])

    print ("[%s:%d] predictedCO2 ==>" 
           % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             )
             
             
           )
    
    print(predictedCO2)     
    
    '''###################
        step : 2
    ###################'''
    
# def test_11_Regresson_Multiple()://
    
def test_12_Coefficient():

    strOf_FuncName = "test_12_Coefficient"


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
    #ref https://www.w3schools.com/python/python_ml_multiple_regression.asp
    df = pandas.read_csv("cars.csv")
    
#     #debug
#     # message
#     print ("[%s:%d] df ==>" 
#            % 
#             (
#              os.path.basename(libs.thisfile())
#              , libs.linenum()
#              )
#             
#             
#            )
#     
#     print(df)

    '''###################
        step : 2
            regression
    ###################'''
    X = df[['Weight', 'Volume']]
    y = df['CO2']
    
    
    
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    
    valsOf_Coeffi   = regr.coef_
    
    #debug
    # message
    print ("[%s:%d] valsOf_Coeffi ==>" 
           % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             )
             
             
           )
     
    print(valsOf_Coeffi)
    

    '''###################
        step : 3
            predic
    ###################'''
    predictedCO2 = regr.predict([[2300, 1300]])

    print ("[%s:%d] predictedCO2 ==>" 
           % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             )
             
             
           )
    
    print(predictedCO2)     
    
    '''###################
        step : 2
    ###################'''
    
# def test_12_Coefficient()://
    
def test_13_Scale():

    strOf_FuncName = "test_13_Scale"


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
        step : 1.1
            load : data
    ###################'''
    '''###################
        step : 2
            prep
    ###################'''
    #ref https://www.w3schools.com/python/python_ml_multiple_regression.asp
    df = pandas.read_csv("cars2.csv")
    
    X = df[['Weight', 'Volume']]
    
    scale = StandardScaler()
    
    '''###################
        step : 3
            scale
    ###################'''
    scaledX = scale.fit_transform(X)

    '''###################
        step : 4
            report
    ###################'''
    #debug
    # message
    print ("[%s:%d] scaledX ==>" 
           % 
            (
             os.path.basename(libs.thisfile())
             , libs.linenum()
             )
             
             
           )
     
    print(scaledX)
    
# def test_13_Scale()://
    
def test_14_Scale_Predict():

    strOf_FuncName = "test_14_Scale_Predict"


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
        step : 1.1
            load : data
    ###################'''
    '''###################
        step : 2
            prep
    ###################'''
    #ref https://www.w3schools.com/python/python_ml_multiple_regression.asp
    df = pandas.read_csv("cars2.csv")
    
    X = df[['Weight', 'Volume']]
    y = df['CO2']
    
    '''###################
        step : 3
            scale
    ###################'''
    scale = StandardScaler()
    
    scaledX = scale.fit_transform(X)

    
    scaled = scale.transform([[2300, 1.3]])
            #=> [[ 4.22104928 -0.81116837]]

    '''###################
        step : 3.1
            regr
    ###################'''
    regr = linear_model.LinearRegression()
    regr.fit(scaledX, y)    
    
    '''###################
        step : 3.2
            predict
    ###################'''
    predictedCO2 = regr.predict(scaled)
            #=> [ 107.2087328]
            
#     predictedCO2 = regr.predict([scaled[0]])
    
    '''###################
        step : 4
            report
    ###################'''
    #debug
    # message
    print ("[%s:%d] scaled ==>" 
           % 
            (
             os.path.basename(libs.thisfile()), libs.linenum()
             )
           )
     
    print(scaled)
    
    print ("[%s:%d] predictedCO2 ==>" 
           % 
            (
             os.path.basename(libs.thisfile()), libs.linenum()
             )
           )
     
    print(predictedCO2)
    
# def test_14_Scale_Predict()://

#ref https://www.w3schools.com/python/python_ml_train_test.asp    

#ref https://www.w3schools.com/python/python_ml_train_test.asp
def test_15_Train_Test():

    strOf_FuncName = "test_15_Train_Test"


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
        step : 1.1
            load : data
    ###################'''
    '''###################
        step : 2
            prep
    ###################'''
    #ref https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.random_integers.html
#     valOf_Seed  = numpy.random.random_integers(1, 6)
    valOf_Seed  = 2
#     valOf_Seed  = 5
    
    numpy.random.seed(valOf_Seed)
#     numpy.random.seed(2)
    
    numOf_Size  = 100
    
    x = numpy.random.normal(3, 1, numOf_Size)
    y = numpy.random.normal(150, 40, numOf_Size) / x


    valOf_Partition = 80
    train_x = x[:valOf_Partition]
    train_y = y[:valOf_Partition]
    
    test_x = x[valOf_Partition:]
    test_y = y[valOf_Partition:]
    
    '''###################
        step : 2 : 2
            r^2
    ###################'''
    mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
    
    myline = numpy.linspace(0, 6, 100)
    
    r2_Model_Train_Param_Train = r2_score(train_y, mymodel(train_x))
    
    # model with train data ---> apply to test data
    r2_Model_Train_Param_Test = r2_score(test_y, mymodel(test_x))
#     r2 = r2_score(test_y, mymodel(test_x))

    #debug
    print ("[%s:%d] r2 (model=train, param=test ==>" 
           % 
            (
             os.path.basename(libs.thisfile()), libs.linenum()
             )
           )
      
    print(r2_Model_Train_Param_Test)
    
    print ("[%s:%d] r2 (model=train, param=train ==>" 
           % 
            (
             os.path.basename(libs.thisfile()), libs.linenum()
             )
           )
      
    print(r2_Model_Train_Param_Train)
    
    #n:20210417_151327

    '''###################
        step : 2 : 3
            r^2 : prediction
    ###################'''
    #:20210418_125209
    valOf_Mymodel_Param = 5.0
#     valOf_Mymodel_Param = 5
    
    valOf_Mymodel   = mymodel(valOf_Mymodel_Param)
    
    print ("[%s:%d] valOf_Mymodel(param = %.2f) ==>" 
           % 
            (
             os.path.basename(libs.thisfile()), libs.linenum()
             , valOf_Mymodel_Param
             )
           )
      
    print(valOf_Mymodel)
    

    
    '''###################
        step : 3
            plot : all entries
    ###################'''
    strOf_Time_Label = libs.get_TimeLabel_Now()
     
    fig = plt.figure()
     
    plt.scatter(x, y)
     
    dpath_PlotImage = "./data/s-7"
    fname_PlotImage = "plot_image_%s" % (strOf_Time_Label)
     
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
     
    # title
    plt.title("numpy.random.normal \nData = %d / Seed = %d"
               % (
                  numOf_Size
                  , valOf_Seed
                  )
               )
 
    fig.savefig(fpath_PlotImage)
     
    # clear plot
    #ref https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib
    plt.clf()
     
#     '''###################
#         step : 3 : 2
#             plot : train
#     ###################'''
#     fig = plt.figure()
#     
#     plt.scatter(train_x, train_y)
#     
#     # r^2
#     plt.plot(myline, mymodel(myline), "r")
# #     plt.plot(myline, mymodel(myline))
#     
#     
#     dpath_PlotImage = "./data/s-7"
#     fname_PlotImage = "plot_image_%s_[train]" % (strOf_Time_Label)
#     
#     fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
#     
#     # title
#     plt.title("numpy.random.normal \nData = %d / Seed = %d / Partition = %d"
#                % (
#                   numOf_Size
#                   , valOf_Seed
#                   , valOf_Partition
#                   )
#                )
# 
#     fig.savefig(fpath_PlotImage)
#     
    '''###################
        step : 3 : 3
            plot : test
    ###################'''
    fig = plt.figure()
     
    plt.scatter(test_x, test_y)
    
    # r^2 line
    plt.plot(myline, mymodel(myline), "r")
    
    # predicted val
#     plt.plot(valOf_Mymodel_Param, valOf_Mymodel, "yo", size=200)
#     plt.plot(valOf_Mymodel_Param, valOf_Mymodel, "yo", s=200)
    plt.plot(valOf_Mymodel_Param, valOf_Mymodel, "yo")
    
    
    dpath_PlotImage = "./data/s-7"
    fname_PlotImage = "plot_image_%s_[test]" % (strOf_Time_Label)
     
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
     
    # title
    plt.title("numpy.random.normal \nData = %d / Seed = %d / Partition = %d"
               % (
                  numOf_Size
                  , valOf_Seed
                  , valOf_Partition
                  )
               )
 
    fig.savefig(fpath_PlotImage)

    '''###################
        step : 3 : 4
            plot : r^2
    ###################'''
    
    
    
    '''###################
        step : 4
            report
    ###################'''
#     #debug
#     print ("[%s:%d] fig.savefig ==> %s" 
#            % 
#             (
#              os.path.basename(libs.thisfile()), libs.linenum()
#              , fpath_PlotImage
#              )
#            )
      
#     print(x)
    
# def test_15_Train_Test()://
    
#ref https://www.w3schools.com/python/python_ml_decision_tree.asp
def test_16_Tree():

    strOf_FuncName = "test_16_Tree"

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

    print()
    
    #ref https://www.devdungeon.com/content/python-import-syspath-and-pythonpath-tutorial#toc-13
    print ("[%s:%d] sys.path ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print(sys.path)
    
    print()
    
    #ref https://www.devdungeon.com/content/python-import-syspath-and-pythonpath-tutorial#toc-13
    print ("[%s:%d] os.environ[\"PATH\"] ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print(os.environ["PATH"])
    
    '''###################
        step : 2
            data : load
    ###################'''
    df = pandas.read_csv("shows.csv")

#     #debug
#     print ("[%s:%d] df ==> " 
#            % 
#             (os.path.basename(libs.thisfile()), libs.linenum())
#            )
#        
#     print(df)

    '''###################
        step : 2 : 2
            data : mapping
    ###################'''
    d = {'UK': 0, 'USA': 1, 'N': 2}
    df['Nationality'] = df['Nationality'].map(d)
    d = {'YES': 1, 'NO': 0}
    df['Go'] = df['Go'].map(d)

#     #debug
#     print ("[%s:%d] df (mapped) ==> " 
#            % 
#             (os.path.basename(libs.thisfile()), libs.linenum())
#            )
#        
#     print(df)

    '''###################
        step : 2 : 3
            data : feature, target
    ###################'''
    features = ['Age', 'Experience', 'Rank', 'Nationality']
    
    X = df[features]
    y = df['Go']    
    
#     #debug
#     print ("[%s:%d] feature, column ==> " 
#            % 
#             (os.path.basename(libs.thisfile()), libs.linenum())
#            )
#        
#     print(X)
#     print(y)
    
    '''###################
        step : 3
            tree
    ###################'''
    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(X, y)    
    
#     #debug
#     print ("[%s:%d] dtree ==> " 
#            % 
#             (os.path.basename(libs.thisfile()), libs.linenum())
#            )
#        
#     print(dtree)
    
    #debug:20210418_170812
    data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
    
#     #debug
#     print ("[%s:%d] data ==> " 
#            % 
#             (os.path.basename(libs.thisfile()), libs.linenum())
#            )
#        
#     print(data)

    graph = pydotplus.graph_from_dot_data(data)

#     #debug
#     print ("[%s:%d] graph ==> " 
#            % 
#             (os.path.basename(libs.thisfile()), libs.linenum())
#            )
#         
#     print(graph)    

    '''###################
        step : 4
            graph
    ###################'''
    strOf_Time_Label = libs.get_TimeLabel_Now()
    
    dpath_PlotImage = "./data/s-10"
#     dpath_PlotImage = "./data/s-9"
    fname_PlotImage = "mydecisiontree.%s.png" % (strOf_Time_Label)
#     fname_PlotImage = "plot_image_%s" % (strOf_Time_Label)
     
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    graph.write_png(fpath_PlotImage)
#     graph.write_png('mydecisiontree.png')

    #debug
    print ("[%s:%d] graph.write_png ==> %s" 
           % 
            (
             os.path.basename(libs.thisfile()), libs.linenum()
             , fpath_PlotImage
             )
           )
       
    
    img=pltimg.imread(fpath_PlotImage)
#     img=pltimg.imread('mydecisiontree.png')
    imgplot = plt.imshow(img)
#     plt.show() 
     
    '''###################
        step : 5
            predict
    ###################'''
    litOf_Predict_Conditions    = [40, 10, 6, 1]
#     litOf_Predict_Conditions    = [40, 10, 7, 1]
    
    #debug
    print ("[%s:%d] litOf_Predict_Conditions ==>" 
           % 
            (
             os.path.basename(libs.thisfile()), libs.linenum()
             
             )
           )
    
    print(litOf_Predict_Conditions)
    print(dtree.predict([litOf_Predict_Conditions])) 
#     print(dtree.predict([[40, 10, 7, 1]])) 
    
    
    
    '''###################
        step : 2
            prep
    ###################'''
    
    '''###################
        step : 4
            report
    ###################'''
#     #debug
#     print ("[%s:%d] fig.savefig ==> %s" 
#            % 
#             (
#              os.path.basename(libs.thisfile()), libs.linenum()
#              , fpath_PlotImage
#              )
#            )
#       
#     print(x)
    
# def test_16_Tree()://
    
    

def exec_prog(): # from : 
    
    
    '''###################
        execute
    ###################'''
    #n:20210413_142903
    #n:20210412_151638
    #n:20210411_172354
    #n:20210415_174210
    #n:20210414_160053
    #n:20210416_153541
    #n:20210418_133238
    test_16_Tree()
#     test_15_Train_Test()
#     test_14_Scale_Predict()
#     test_13_Scale()
#     test_12_Coefficient()
#     test_11_Regresson_Multiple()
#     test_10_Predict()
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
