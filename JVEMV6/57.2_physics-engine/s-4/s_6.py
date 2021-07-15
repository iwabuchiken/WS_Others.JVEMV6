# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20210707_174437

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57.2_physics-engine\s-4\
python s_6.py


pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\57.2_physics-engine\s-4\
echo.>> log_s_6.log && echo ============================ >> log_s_6.log && python s_6.py >> log_s_6.log


echo.>> log_s_6.log
echo ============================ >> log_s_6.log
python s_6.py >> log_s_6.log

##


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

# C:\WORKS_2\Programs\panda3d\Panda3D-1.10.9-x64
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
    import : math
###################'''
from math import pi, sin, cos

'''###################
    import : panda3d
###################'''
# from direct.showbase.ShowBase import ShowBase
# from direct.task import Task
# from direct.actor.Actor import Actor
# 
# print()
# 
# print ("[%s:%d] 'direct.actor.Actor import Actor' ==> comp." % (
#             os.path.basename(os.path.basename(libs.thisfile()))
#             , libs.linenum()
#             )
# )


'''###################
    import : bulllet
    https://docs.panda3d.org/1.10/python/programming/physics/bullet/hello-world
###################'''
import direct.directbase.DirectStart
from panda3d.core import Vec3
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape

print()

print ("[%s:%d] 'panda3d.bullet' a.o. ==> comp." % (
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
    task_1_PyBullet_Hello_World()
    at : 20210708_155754
###################'''
def task_1_PyBullet_Hello_World():

    strOf_FuncName = "task_1_PyBullet_Hello_World"

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
    
    '''###################
        step : 3
    ###################'''
    
# def task_1_PyBullet_Hello_World()://

def exec_prog(): # from : 
    
    
    '''###################
        execute
    ###################'''
    #mark:20210709_160406
#     task_1_PyBullet_Hello_World()
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
