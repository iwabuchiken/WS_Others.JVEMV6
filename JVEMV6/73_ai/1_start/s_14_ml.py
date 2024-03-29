# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20210424_152724

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\
python s_14_ml.py


echo.>> log_s-14_ml.log
echo ============================ >> log_s-14_ml.log
python s_14_ml.py >> log_s-14_ml.log

##
pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\
echo.>> log_s-14_ml.log && echo ============================ >> log_s-14_ml.log && python s_14_ml.py >> log_s-14_ml.log

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
    import : pandas
###################'''
# from pandas.tests.io.msgpack.test_case import test_9
import pandas as pd
# import pandas

'''###################
    import : sklearn
###################'''
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

#ref https://www.w3schools.com/python/python_ml_polynomial_regression.asp
from sklearn.metrics import r2_score
from sklearn import metrics

from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

#ref https://www.geeksforgeeks.org/introduction-machine-learning-using-python/
from sklearn.datasets import load_iris

# print ("[%s:%d] import load_iris => done" % (os.path.basename(libs.thisfile()), libs.linenum()))

from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split

#ref https://www.geeksforgeeks.org/learning-model-building-scikit-learn-python-machine-learning-library/
from sklearn.externals import joblib



print ("[%s:%d] sklerarn-related imports => done" % (os.path.basename(libs.thisfile()), libs.linenum()))

'''###################
    import : scipy, numpy, matplotlib
###################'''
from scipy import stats

# import numpy
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as pat
import matplotlib.image as pltimg



'''###################
    import : others
###################'''
from shutil import copyfile

import pydotplus, math, time

# import getopt, inspect

# import math as math

# import struct


# import xml.etree.ElementTree as ET

#ref https://qiita.com/okakatsuo/items/f2e79fc501ed9f799734 20201228_173042
# import matplotlib.pyplot as plt
# import matplotlib.patches as pat
# import math

###############################################


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

    print()
    
    '''###################
        step : 2
            data : load
    ###################'''
    #mark:20210421_164025
    iris_dataset=load_iris()
    
    #debug
    print ("[%s:%d] load_iris => done"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
#     print("iris_dataset['DESCR'] ==>")
#     print(iris_dataset['DESCR'])
#     print(iris_dataset)

    '''###################
        step : 3
            data : train
    ###################'''
    X_train, X_test, y_train, y_test = train_test_split(
                    iris_dataset["data"]
                    , iris_dataset["target"]
                    , random_state=0
    )

    #debug
    print ("[%s:%d] train_test_split => done"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
#     print("X_train ==>")
#     print(X_train)
# 
#     print()
#     print("X_test ==>")
#     print(X_test)

    '''###################
        step : 4
            data : neighbor
    ###################'''
    '''###################
        step : 4 : 1
            data : setup
    ###################'''
    kn = KNeighborsClassifier(n_neighbors=1)
    
    #debug
    print ("[%s:%d] KNeighborsClassifier => done"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print("kn ==>")
    print(kn)
    
    '''###################
        step : 4 : 2
            data : fit
    ###################'''
    kn.fit(X_train, y_train)
    
    #debug
    print ("[%s:%d] KNeighborsClassifier : fit => done"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print("kn ==>")
    print(kn)
    
    '''###################
        step : 4 : 3
            data : prep
    ###################'''
    x_new = np.array([[5, 2.9, 1, 0.2]])
    
    #debug
    print ("[%s:%d] np.array => done"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print("x_new ==>")
    print(x_new)
    
    '''###################
        step : 5
            data : predict
    ###################'''
    prediction = kn.predict(x_new)
    
    #debug
    print ("[%s:%d] predict => done"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
#     print("prediction ==>")
#     print(prediction)

    '''###################
        step : 6
            results
    ###################'''
    prediction = kn.predict(x_new)
    
    #debug
    print ("[%s:%d] results => "
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print("probe data =>")
    print(x_new)
    print()
    
    print("Predicted target value: {}\n".format(prediction))
    print("Predicted feature name: {}\n".format
        (iris_dataset["target_names"][prediction]))
    print("Test score: {:.2f}".format(kn.score(X_test, y_test)))    


    #debug
    print ("[%s:%d] X_test => "
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print("X_test =>")
    print(X_test)
    print()
    
    print("y_test =>")
    print(y_test)

    
    '''###################
        step : X
            data : train
    ###################'''

#     #debug
#     print ("[%s:%d] train_test_split => done"
#             % (os.path.basename(libs.thisfile()), libs.linenum()
#                
#                )
#     )
#     
#     print("X_train ==>")


    
# def test_1()://

def test_S_14_No_1():

    strOf_FuncName = "test_S_14_No_1"

    '''###################
        step : 1
            opening, vars
    ###################'''
    #ref https://stackoverflow.com/questions/56711424/how-can-i-count-time-in-python-3
    t_start = time.time()
    
    print()
    
    print ("[%s:%d] starting : %s (time=%s)" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , strOf_FuncName
                , libs.get_TimeLabel_Now()
                )
    )

    print()
    
    '''###################
        step : 2
            data : prep
    ###################'''
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])    
    
    #debug
    print ("[%s:%d] x, y :"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print(x)
    print(y)
    
    v = np.array([9, 10])
    w = np.array([11, 12])    
    
    '''###################
        step : 2 : 1
            inner prod
    ###################'''
    valOf_InnerProd = np.dot(v, w)

    #debug
    print ("[%s:%d] valOf_InnerProd :"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print(v)
    print(w)
    print(valOf_InnerProd)
    print()
        
    '''###################
        step : 2 : 2
            vector prod
    ###################'''
    valOf_Vector_Prod = np.dot(x, v)

    #debug
    print ("[%s:%d] valOf_Vector_Prod :"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print(x)
    print(v)
    print(valOf_Vector_Prod)
    print()
        
    '''###################
        step : 2 : 3
            prod : matrix
    ###################'''
    valOf_Prod_Matrix = np.dot(x, y)

    #debug
    print ("[%s:%d] valOf_Prod_Matrix :"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print(x)
    print(y)
    print(valOf_Prod_Matrix)
    print()
        
    '''###################
        step : 2 : 1
            data : store
    ###################'''

    '''###################
        step : 6
            results
    ###################'''
    '''###################
        step : 6 : 1
            time
    ###################'''
    t_end   = time.time()

    #debug
#     print ("[%s:%d] time => %s"
    #ref https://www.pythonpool.com/python-float-to-string/#5_Using_NumPy
    print ("[%s:%d] time => %.03f sec"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               , (t_end - t_start)
               )
    )
    
    print()
    
    
    '''###################
        step : X
            data : train
    ###################'''

# def test_S_14_No_1()://
    
def test_S_14_No_2_Scipy():

    strOf_FuncName = "test_S_14_No_2_Scipy"

    '''###################
        step : 1
            opening, vars
    ###################'''
    #ref https://stackoverflow.com/questions/56711424/how-can-i-count-time-in-python-3
    t_start = time.time()
    
    print()
    
    print ("[%s:%d] starting : %s (time=%s)" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , strOf_FuncName
                , libs.get_TimeLabel_Now()
                )
    )

    print()
    
    '''###################
        step : 2
            data : prep
    ###################'''
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])    
    
    #debug
    print ("[%s:%d] x, y :"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print(x)
    print(y)
    
    v = np.array([9, 10])
    w = np.array([11, 12])    
    
    '''###################
        step : 2 : 1
            inner prod
    ###################'''
    valOf_InnerProd = np.dot(v, w)

    #debug
    print ("[%s:%d] valOf_InnerProd :"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print(v)
    print(w)
    print(valOf_InnerProd)
    print()
        
    '''###################
        step : 2 : 2
            vector prod
    ###################'''
    valOf_Vector_Prod = np.dot(x, v)

    #debug
    print ("[%s:%d] valOf_Vector_Prod :"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print(x)
    print(v)
    print(valOf_Vector_Prod)
    print()
        
    '''###################
        step : 2 : 3
            prod : matrix
    ###################'''
    valOf_Prod_Matrix = np.dot(x, y)

    #debug
    print ("[%s:%d] valOf_Prod_Matrix :"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               
               )
    )
    
    print(x)
    print(y)
    print(valOf_Prod_Matrix)
    print()
        
    '''###################
        step : 2 : 1
            data : store
    ###################'''

    '''###################
        step : 6
            results
    ###################'''
    '''###################
        step : 6 : 1
            time
    ###################'''
    t_end   = time.time()

    #debug
#     print ("[%s:%d] time => %s"
    #ref https://www.pythonpool.com/python-float-to-string/#5_Using_NumPy
    print ("[%s:%d] time => %.03f sec"
            % (os.path.basename(libs.thisfile()), libs.linenum()
               , (t_end - t_start)
               )
    )
    
    print()
    
    
    '''###################
        step : X
            data : train
    ###################'''

# def test_S_14_No_2_Scipy()://
    
    

def exec_prog(): # from : 
    
    
    '''###################
        execute
    ###################'''
    test_S_14_No_1()
    
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
