# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20210424_152724

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\
python s_20_ml.py


echo.>> log_s-20_ml.log
echo ============================ >> log_s-20_ml.log
python s_20_ml.py >> log_s-20_ml.log

##
pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\
echo.>> log_s-20_ml.log && echo ============================ >> log_s-20_ml.log && python s_20_ml.py >> log_s-20_ml.log

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
import sys, os
# import sys, os, getopt, inspect

os.environ["PATH"] += os.pathsep + 'C:/WORKS_2/Programs/Python/Python_3.5.1/lib_additional/'

'''###################
    import : orig files        
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

from libs import libs

from libs import cons

# '''###################
#     import : pandas
# ###################'''
# import pandas as pd

'''###################
    import : sklearn
###################'''
# from sklearn import linear_model
# from sklearn.preprocessing import StandardScaler

#ref https://www.w3schools.com/python/python_ml_polynomial_regression.asp
# from sklearn.metrics import r2_score
# from sklearn import metrics

# from sklearn.preprocessing import StandardScaler

# from sklearn.tree import DecisionTreeClassifier
# from sklearn import tree

#ref https://www.geeksforgeeks.org/introduction-machine-learning-using-python/
# from sklearn.datasets import load_iris

# print ("[%s:%d] import load_iris => done" % (os.path.basename(libs.thisfile()), libs.linenum()))

# from sklearn.neighbors import KNeighborsClassifier

# from sklearn.model_selection import train_test_split

#ref https://www.geeksforgeeks.org/learning-model-building-scikit-learn-python-machine-learning-library/
# from sklearn.externals import joblib

#ref https://www.geeksforgeeks.org/decision-tree-implementation-python/
# from sklearn.metrics import confusion_matrix
# from sklearn.cross_validation import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import classification_report
# 
# from sklearn import tree

#ref https://www.geeksforgeeks.org/python-decision-tree-regression-using-sklearn/
from sklearn.tree import DecisionTreeRegressor


print ("[%s:%d] sklerarn-related imports => comp. (tree, too)" 
            % (os.path.basename(libs.thisfile()), libs.linenum())
       )
# print ("[%s:%d] sklerarn-related imports => done" % (os.path.basename(libs.thisfile()), libs.linenum()))

'''###################
    import : scipy, numpy, matplotlib, pandas
    matplotlib
###################'''
from scipy import stats

# import numpy
import numpy as np, pandas as pd, matplotlib.pyplot as plt

# import matplotlib.pyplot as plt
# import matplotlib.patches as pat
# import matplotlib.image as pltimg

'''###################
    import : others
###################'''
# from shutil import copyfile

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


def main_20210506_164920():

    strOf_FuncName = "main_20210506_164920()"

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
            vars
    ###################'''
    #code:20210506_170631
    dataset = np.array(
    [['Asset Flip', 100, 1000],
    ['Text Based', 500, 3000],
    ['Visual Novel', 1500, 5000],
    ['2D Pixel Art', 3500, 8000],
    ['2D Vector Art', 5000, 6500],
    ['Strategy', 6000, 7000],
    ['First Person Shooter', 8000, 15000],
    ['Simulator', 9500, 20000],
    ['Racing', 12000, 21000],
    ['RPG', 14000, 25000],
    ['Sandbox', 15500, 27000],
    ['Open-World', 16500, 30000],
    ['MMOFPS', 25000, 52000],
    ['MMORPG', 30000, 80000]
    ])

    print ("[%s:%d] dataset =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )


    # print the dataset
    print(dataset)
    print()
    
    '''###################
        step : 3
            data : select
    ###################'''
    # select all rows by : and column 1
    # by 1:2 representing features
    X = dataset[:, 1:2].astype(int) 
    
    print ("[%s:%d] X = dataset[:, 1:2] =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    # print X
    print(X)
    print()    

    '''###################
        step : 4
            data : select
    ###################'''
    #code:20210506_171149
    # select all rows by : and column 2
    # by 2 to Y representing labels
    y = dataset[:, 2].astype(int) 

    print ("[%s:%d] y = dataset[:, 2] =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    # print y
    print(y)    
    print()

    '''###################
        step : 5
            regressor
    ###################'''
    # create a regressor object
    regressor = DecisionTreeRegressor(random_state = 0)     

    # fit the regressor with X and Y data
    regressor.fit(X, y)
    
    print ("[%s:%d] regressor =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    # print y
    print(regressor)    
    print()
    

    '''###################
        step : 6
            predict
    ###################'''
    #code:20210506_172247
    
    valOf_Target_Val    = 3750
    
    # test the output by changing values, like 3750
    y_pred = regressor.predict(valOf_Target_Val)    #=> 3,7550 as a val for 2nd column
#     y_pred = regressor.predict(3750)    #=> 3,7550 as a val for 2nd column

    print ("[%s:%d] y_pred => (for target : %d" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , valOf_Target_Val
                )
    )

    # print the predicted price
    print("Predicted price: % d\n"% y_pred)     
    
    print()

    #n:20210506_172536

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

# def main_20210506_164920()()://

    

def exec_prog(): # from : 
    
    
    '''###################
        execute
    ###################'''
    main_20210506_164920()
    
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
