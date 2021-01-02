# -*- coding: utf-8 -*-
'''
file          : C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\1_start\1_1.py
started at    : 2020/12/28 17:29:33

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\1_start
python 1_1.py

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
'''


import sys
# from sympy.solvers.tests.test_constantsimp import C2

import os

sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

from libs import libs
# from libs import libfx

from libs import cons

# from libs_D_7 import cons_D_7
# from libs_31 import libmt

import getopt
import os
import inspect

# import math as math

# import struct

from shutil import copyfile

# import xml.etree.ElementTree as ET

#ref https://qiita.com/okakatsuo/items/f2e79fc501ed9f799734 20201228_173042
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import math

###############################################
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import math

#triangle = [(x1,y1),(x2,y2),(x3,y3)]

#入力triangle内にある三角形の座標を出力する
def return_triangle(triangle):
    x1 = (triangle[0][0] + triangle[1][0])/2
    y1 = (triangle[0][1] + triangle[1][1])/2
    x2 = (triangle[1][0] + triangle[2][0])/2
    y2 = (triangle[1][1] + triangle[2][1])/2
    x3 = (triangle[2][0] + triangle[0][0])/2
    y3 = (triangle[2][1] + triangle[0][1])/2
    new_triangle = [(x1,y1),(x2,y2),(x3,y3)]
    return new_triangle

#2点間の距離を出力する
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

#点pとtriangleの内の点で点pに最も近い２点から構成される三角形を出力
def select_neighbor_points(p, triangle):
    distance1 = distance(p, triangle[0])
    distance2 = distance(p, triangle[1])
    distance3 = distance(p, triangle[2])
    if distance1 > distance2:
        if distance1 > distance3:
            return [p, triangle[1], triangle[2]]
        else:
            return [p, triangle[0], triangle[1]]
    else:
        if distance2 > distance3:
            return(p, triangle[0],triangle[2])
        else:
            return(p, triangle[0],triangle[1])

#fractal図形を生成する。iteration数が大きいほど複雑になる
def produce_fractal1(triangle, iteration):
    if iteration == 0: return 0
    p1 = triangle[0]
    p2 = triangle[1]
    p3 = triangle[2]
    new_triangle = return_triangle(triangle)
    p = pat.Polygon(xy = new_triangle,fc = "white", ec = "black")
    
    ax.add_patch(p)
    
    produce_fractal1(select_neighbor_points(p1,new_triangle), iteration-1)
    produce_fractal1(select_neighbor_points(p2,new_triangle), iteration-1)
    produce_fractal1(select_neighbor_points(p3,new_triangle), iteration-1)

# triangle = [(0.2, 0.2), (0.8, 0.2), (0.5, 0.8)] #初期三角形の座標
# fig = plt.figure(figsize=(5, 5))
# ax = fig.add_subplot(1,1,1)
# p = pat.Polygon(xy = triangle,fc = "white", ec = "black")
# ax.add_patch(p)
# produce_fractal1(triangle,6)
# fig.savefig("./fractal.png") #画像の保存




def exec_prog(): # from : 
    
#     triangle = [(0.2, 0.2), (0.8, 0.2), (0.5, 0.8)] #初期三角形の座標
#     fig = plt.figure(figsize=(5, 5))
#     
#     ax = fig.add_subplot(1,1,1)
#     
#     p = pat.Polygon(xy = triangle,fc = "white", ec = "black")
#     ax.add_patch(p)
#     produce_fractal1(triangle,6)
#     fig.savefig("./fractal.png") #画像の保存
    
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
    triangle = [(0.2, 0.2), (0.8, 0.2), (0.5, 0.8)] #初期三角形の座標
    fig = plt.figure(figsize=(5, 5))
    
    ax = fig.add_subplot(1,1,1)
    
    p = pat.Polygon(xy = triangle,fc = "white", ec = "black")
    ax.add_patch(p)
    produce_fractal1(triangle,6)
    
    fname_Out = "./fractal." + libs.get_TimeLabel_Now() + ".png"
    
    fig.savefig(fname_Out) #画像の保存
#     fig.savefig("./fractal.png") #画像の保存
    
    '''###################
        Report        
    ###################'''
    print ("[%s:%d] file gen-ed => %s" 
           % (os.path.basename(os.path.basename(libs.thisfile()))
              , libs.linenum()
              , fname_Out))
    
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

