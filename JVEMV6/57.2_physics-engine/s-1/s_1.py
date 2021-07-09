# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20210707_174437

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57.2_physics-engine\s-1\
python s_1.py


echo.>> log_s-1.log
echo ============================ >> log_s-1.log
python s_1.py >> log_s-1.log

##
pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57.2_physics-engine\s-1\
echo.>> log_s-1.log && echo ============================ >> log_s-1.log && python s_1.py >> log_s-1.log



['', 'C:\\WORKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64\\python\\pyth
on37.zip', 'C:\\WORKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64', 'C:\\
WORKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64\\python\\DLLs', 'C:\\WO
RKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64\\python\\lib', 'C:\\WORKS
_2\\Programs\\panda3d\\Panda3D-1.10.9-x64\\python', 'C:\\WORKS_2\\Prog
rams\\panda3d\\Panda3D-1.10.9-x64\\bin', 'C:\\WORKS_2\\Programs\\panda
3d\\Panda3D-1.10.9-x64\\python\\lib\\site-packages']

'''


# from sympy.solvers.tests.test_constantsimp import C2

'''###################
    import : basics
###################'''
import sys, os, getopt, inspect

os.environ["PATH"] += os.pathsep + 'C:/WORKS_2/Programs/Python/Python_3.5.1/lib_additional/'

pathOf_Python_3_5_1 = "C:\\WORKS_2\\Programs\\Python\\Python_3.5.1\\Lib\\site-packages"

#code:20210707_175722
os.environ["PATH"] += os.pathsep + pathOf_Python_3_5_1

aryOf_PathOf_Panda3D_Libs = [\
        "C:\\WORKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64\\python\\python37.zip"\
        , "C:\\WORKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64"\
        , "C:\\WORKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64\\python\\DLLs"\
        , "C:\\WORKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64\\python\\lib"\
        , "C:\\WORKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64\\python"\
        , "C:\\WORKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64\\bin"\
        , "C:\\WORKS_2\\Programs\\panda3d\\Panda3D-1.10.9-x64\\python\\lib\\site-packages"
        ]

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
    import : pandas
###################'''

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
    import : panda3d
###################'''
from direct.showbase.ShowBase import ShowBase


'''###################
    import : others
###################'''
# from shutil import copyfile
# 
# import pydotplus, math, time


###############################################

'''###################
    class MyApp(ShowBase):
    at : 20210708_155754
###################'''
# class MyApp(ShowBase):
# 
#     def __init__(self):
#         ShowBase.__init__(self)
# 
#     # Load the environment model.
#     self.scene = self.loader.loadModel("models/environment")
#     # Reparent the model to render.
#     self.scene.reparentTo(self.render)
#     # Apply scale and position transforms on the model.
#     self.scene.setScale(0.25, 0.25, 0.25)
#     self.scene.setPos(-8, 42, 0)

print()

print ("[%s:%d] 'MyApp' ==> defined" % (
            os.path.basename(os.path.basename(libs.thisfile()))
            , libs.linenum()
            )
)

'''###################
    task_1_ShowBase()
    at : 20210708_155754
###################'''
def task_1_ShowBase():

    strOf_FuncName = "task_1_ShowBase"

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
    class MyApp(ShowBase):
    
        def __init__(self):
            ShowBase.__init__(self)
            
            # Load the environment model.
            self.scene = self.loader.loadModel("models/environment")
            # Reparent the model to render.
            self.scene.reparentTo(self.render)
            # Apply scale and position transforms on the model.
            self.scene.setScale(0.25, 0.25, 0.25)
            
            #code:20210708_162726
#             valOf_Pos_X, valOf_Pos_Y, valOf_Pos_Z     = -100, 42, 0
#             valOf_Pos_X, valOf_Pos_Y, valOf_Pos_Z     = -400, 42, 0
#             valOf_Pos_X, valOf_Pos_Y, valOf_Pos_Z     = -400, 420, 0
#             valOf_Pos_X, valOf_Pos_Y, valOf_Pos_Z     = -400, 42, 100
            valOf_Pos_X, valOf_Pos_Y, valOf_Pos_Z     = -800, 42, 0
#             valOf_Pos_X     = -100
# #             valOf_Pos_X     = -50
#             valOf_Pos_Y     = 42
#             valOf_Pos_Z     = 0
            self.scene.setPos(valOf_Pos_Y, valOf_Pos_Y, valOf_Pos_Z)
#             self.scene.setPos(-8, 42, 0)
    
    '''###################
        step : 3
    ###################'''
    app = MyApp()

    print()
    
    print ("[%s:%d] 'MyApp' ==> instantiated" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )

    app.run()
    
    
# def task_1_ShowBase()://

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


    
# def test_1()://

def exec_prog(): # from : 
    
    
    '''###################
        execute
    ###################'''
    task_1_ShowBase()
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
