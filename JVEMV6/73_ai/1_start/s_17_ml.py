# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20210424_152724

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\
python s_17_ml.py


echo.>> log_s-17_ml.log
echo ============================ >> log_s-17_ml.log
python s_17_ml.py >> log_s-17_ml.log

##
pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\73_ai\1_start\
echo.>> log_s-17_ml.log && echo ============================ >> log_s-17_ml.log && python s_17_ml.py >> log_s-17_ml.log

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
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from sklearn import tree


print ("[%s:%d] sklerarn-related imports => comp. (tree, too)" 
            % (os.path.basename(libs.thisfile()), libs.linenum())
       )
# print ("[%s:%d] sklerarn-related imports => done" % (os.path.basename(libs.thisfile()), libs.linenum()))

'''###################
    import : scipy, numpy, matplotlib, pandas
###################'''
from scipy import stats

# import numpy
import numpy as np, pandas as pd

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

# Function importing Dataset
def importdata():
    
    #code:20210505_162927
    fpath_CSV   = "C:\\WORKS_2\\WS\\WS_Others.JVEMV6\\JVEMV6\\73_ai\\1_start\\data\\s-19\\balance-scale.data" 
    
    print ("[%s:%d] loading csv file... : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , fpath_CSV
                )
    )

    print()
    
    #ref https://datascienceparichay.com/article/read-csv-files-using-pandas-with-examples/
    balance_data = pd.read_csv(fpath_CSV)
#     balance_data = pd.read_csv(
# 'https://archive.ics.uci.edu/ml/machine-learning-'+
# 'databases/balance-scale/balance-scale.data',
#     sep= ',', header = None)
      
    # Printing the dataswet shape
    print ("Dataset Length: ", len(balance_data))
    print ("Dataset Shape: ", balance_data.shape)
            # (625, 5)
    # Printing the dataset obseravtions
    #ref https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html
#     print ("Dataset (first 3 rows): \n",balance_data.head(3))
            #     0  1  2  3  4
            # 0  B  1  1  1  1
            # 1  R  1  1  1  2
            # 2  R  1  1  1  3
    print ("Dataset: ",balance_data.head())
    return balance_data


# Function to perform training with giniIndex.
def train_using_gini(X_train, X_test, y_train):
  
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion = "gini",
            random_state = 100,max_depth=3, min_samples_leaf=5)
  
    # Performing training
    clf_gini.fit(X_train, y_train)
    return clf_gini

# Function to split the dataset

# Function to perform training with entropy.
def tarin_using_entropy(X_train, X_test, y_train):
  
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
            criterion = "entropy", random_state = 100,
            max_depth = 3, min_samples_leaf = 5)
  
    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy

def splitdataset(balance_data):
    
    #debug:20210502_170801
    print ("[%s:%d] balance_data.dtypes ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    #ref https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.values.html
    print(balance_data.dtypes)
            # 0    object
            # 1     int64
            # 2     int64
            # 3     int64
            # 4     int64
            
    print()
    
    # Separating the target variable
    X = balance_data.values[:, 1:5] #=> choose : all rows, columns of 1 thru 4 (index-wise, 5th not in)
    Y = balance_data.values[:, 0]
  
    # Splitting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split( 
    X, Y, test_size = 0.3, random_state = 100)

    return X, Y, X_train, X_test, y_train, y_test

def cal_accuracy(y_test, y_pred):
      
    print("Confusion Matrix: ",
        confusion_matrix(y_test, y_pred))
      
    print ("Accuracy : ",
    accuracy_score(y_test,y_pred)*100)
      
    print("Report : ",
    classification_report(y_test, y_pred))

# Function to make predictions
def prediction(X_test, clf_object):
  
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred

def main():

    strOf_FuncName = "main()"

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
# Building Phase
    data = importdata()

    print ("[%s:%d] importdata ==> comp." % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print()

    '''###################
        step : 2 : 1
            data : store
    ###################'''
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    #n:20210502_171207

    #debug
    print ("[%s:%d] type(X) ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print(type(X))
    print()

    #debug:20210503_160446
    print ("[%s:%d] X.shape ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    #ref https://note.nkmk.me/en/python-numpy-ndarray-ndim-shape-size/
    print(X.shape)
    print()
            # (625, 4)

    #debug:20210503_160757
    print ("[%s:%d] X[:3] ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print(X[:3])
    print()
            # [[1 1 1 1]
            #  [1 1 1 2]
            #  [1 1 1 3]]
    
    #code:20210503_162445
    clf_gini = train_using_gini(X_train, X_test, y_train)

    #debug:20210503_162611
    print ("[%s:%d] clf_gini ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print(clf_gini)
    print()
            # DecisionTreeClassifier(class_weight=None,... 
            
    #code:20210503_162857
    clf_entropy = tarin_using_entropy(X_train, X_test, y_train)    

    #debug:20210503_163047
    print ("[%s:%d] clf_entropy ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print(clf_entropy)
    print()
        
    '''###################
        step : 2 : 2
            data : graphviz, png file
    ###################'''
    data = tree.export_graphviz(clf_gini, out_file=None)
#     data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
    
    #debug:20210503_164342
    print ("[%s:%d] export_graphviz ==> comp" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

#     print(clf_entropy)
    print()
    
    # 
    graph = pydotplus.graph_from_dot_data(data)
    
    strOf_Time_Label = libs.get_TimeLabel_Now()
    
    dpath_PlotImage = "./data/s-18"
#     dpath_PlotImage = "./data/s-9"
    fname_PlotImage = "decisiontree.%s.png" % (strOf_Time_Label)
#     fname_PlotImage = "mydecisiontree.%s.png" % (strOf_Time_Label)
#     fname_PlotImage = "plot_image_%s" % (strOf_Time_Label)
     
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    graph.write_png(fpath_PlotImage)    
    
    #debug:20210503_165123
    print ("[%s:%d] decisiontree png file ==> comp : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , fpath_PlotImage
                )
    )

    print()
    
    '''###################
        step : 2 : 2.2
            data : graphviz, png file
    ###################'''
    data_entropy = tree.export_graphviz(clf_entropy, out_file=None)
    
    #debug:20210503_165911
    print ("[%s:%d] export_graphviz (clf_entropy) ==> comp" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

#     print(clf_entropy)
    print()
    
    # 
    graph = pydotplus.graph_from_dot_data(data_entropy)
    
    strOf_Time_Label = libs.get_TimeLabel_Now()
    
    dpath_PlotImage = "./data/s-18"
#     dpath_PlotImage = "./data/s-9"

    fname_PlotImage = "decisiontree.%s.[clf_entropy].png" % (strOf_Time_Label)
    
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    graph.write_png(fpath_PlotImage)    
    
    print ("[%s:%d] decisiontree png file ==> comp : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , fpath_PlotImage
                )
    )

    print()
    
    '''###################
        step : 3 : 1
            prediction : gini
    ###################'''
    #n:20210503_170550
    # Prediction using gini
    y_pred_gini = prediction(X_test, clf_gini)
    
    cal_accuracy(y_test, y_pred_gini)    
    
    '''###################
        step : 3 : 1
            prediction : gini
    ###################'''
    #code:20210505_164310
    # Prediction using entropy
    y_pred_entropy = prediction(X_test, clf_entropy)

    cal_accuracy(y_test, y_pred_entropy)
    
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

# def main()()://

#n:20210505_165121    
def main_202105XX():

    strOf_FuncName = "main_202105XX()"

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
# Building Phase
    data = importdata()

    print ("[%s:%d] importdata ==> comp." % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print()

    '''###################
        step : 2 : 1
            data : store
    ###################'''
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    #n:20210502_171207

    #debug
    print ("[%s:%d] type(X) ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print(type(X))
    print()

    #debug:20210503_160446
    print ("[%s:%d] X.shape ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    #ref https://note.nkmk.me/en/python-numpy-ndarray-ndim-shape-size/
    print(X.shape)
    print()
            # (625, 4)

    #debug:20210503_160757
    print ("[%s:%d] X[:3] ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print(X[:3])
    print()
            # [[1 1 1 1]
            #  [1 1 1 2]
            #  [1 1 1 3]]
    
    #code:20210503_162445
    clf_gini = train_using_gini(X_train, X_test, y_train)

    #debug:20210503_162611
    print ("[%s:%d] clf_gini ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print(clf_gini)
    print()
            # DecisionTreeClassifier(class_weight=None,... 
            
    #code:20210503_162857
    clf_entropy = tarin_using_entropy(X_train, X_test, y_train)    

    #debug:20210503_163047
    print ("[%s:%d] clf_entropy ==>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    print(clf_entropy)
    print()
        
    '''###################
        step : 2 : 2
            data : graphviz, png file
    ###################'''
    data = tree.export_graphviz(clf_gini, out_file=None)
#     data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
    
    #debug:20210503_164342
    print ("[%s:%d] export_graphviz ==> comp" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

#     print(clf_entropy)
    print()
    
    # 
    graph = pydotplus.graph_from_dot_data(data)
    
    strOf_Time_Label = libs.get_TimeLabel_Now()
    
    dpath_PlotImage = "./data/s-18"
#     dpath_PlotImage = "./data/s-9"
    fname_PlotImage = "decisiontree.%s.png" % (strOf_Time_Label)
#     fname_PlotImage = "mydecisiontree.%s.png" % (strOf_Time_Label)
#     fname_PlotImage = "plot_image_%s" % (strOf_Time_Label)
     
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    graph.write_png(fpath_PlotImage)    
    
    #debug:20210503_165123
    print ("[%s:%d] decisiontree png file ==> comp : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , fpath_PlotImage
                )
    )

    print()
    
    '''###################
        step : 2 : 2.2
            data : graphviz, png file
    ###################'''
    data_entropy = tree.export_graphviz(clf_entropy, out_file=None)
    
    #debug:20210503_165911
    print ("[%s:%d] export_graphviz (clf_entropy) ==> comp" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

#     print(clf_entropy)
    print()
    
    # 
    graph = pydotplus.graph_from_dot_data(data_entropy)
    
    strOf_Time_Label = libs.get_TimeLabel_Now()
    
    dpath_PlotImage = "./data/s-18"
#     dpath_PlotImage = "./data/s-9"

    fname_PlotImage = "decisiontree.%s.[clf_entropy].png" % (strOf_Time_Label)
    
    fpath_PlotImage = os.path.join(dpath_PlotImage, fname_PlotImage)
    
    graph.write_png(fpath_PlotImage)    
    
    print ("[%s:%d] decisiontree png file ==> comp : %s" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , fpath_PlotImage
                )
    )

    print()
    
    '''###################
        step : 3 : 1
            prediction : gini
    ###################'''
    #n:20210503_170550
    # Prediction using gini
    y_pred_gini = prediction(X_test, clf_gini)
    
    cal_accuracy(y_test, y_pred_gini)    
    
    '''###################
        step : 3 : 1
            prediction : gini
    ###################'''
    #code:20210505_164310
    # Prediction using entropy
    y_pred_entropy = prediction(X_test, clf_entropy)

    cal_accuracy(y_test, y_pred_entropy)
    
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

# def main_202105XX()()://
    
    

def exec_prog(): # from : 
    
    
    '''###################
        execute
    ###################'''
    main()
#     main()
    
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
