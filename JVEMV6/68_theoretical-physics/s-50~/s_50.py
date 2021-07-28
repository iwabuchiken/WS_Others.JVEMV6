# -*- coding: utf-8 -*-
'''
file          : 
started at    : 20210707_174437

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\s-45~\
python s_50.py


pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\68_theoretical-physics\s-50~\
echo.>> log_s_50.log && echo ============================ >> log_s_50.log && python s_50.py >> log_s_50.log


echo.>> log_s_50.log
echo ============================ >> log_s_50.log
python s_50.py >> log_s_50.log




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



'''###################
    import : others
###################'''
# from shutil import copyfile
# 
# import pydotplus, math, time


###############################################


'''###################
    tsp()
    at : 20210728_131222
###################'''
def tsp(_aryOf_Numbers, _pointOf_Tsp):
    
    '''###################
        step : 1
            validate
    ###################'''
    #code:20210728_132355
    if _pointOf_Tsp < 1 : #if _pointOf_Tsp < 1
        
        print ("[%s:%d] ****** ERROR *****" % (
                    os.path.basename(os.path.basename(libs.thisfile()))
                    , libs.linenum()
                    )
        )
        
        print ("[%s:%d] _pointOf_Tsp < 1 : %d" % (
                    os.path.basename(os.path.basename(libs.thisfile()))
                    , libs.linenum()
                    , _pointOf_Tsp
                    )
        )
    
        print()
        
        return _aryOf_Numbers
        
    
    #/if _pointOf_Tsp < 1

    
    '''###################
        step : 2
            tsp
    ###################'''
    '''###################
        step : 2 : 1
            show : elements
    ###################'''
    element_1   = _aryOf_Numbers[_pointOf_Tsp - 1]
    element_2   = _aryOf_Numbers[_pointOf_Tsp]

    
    print ("[%s:%d] element_1 = %d, element_2 = %d" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , element_1, element_2
                )
    )

    print()
    
    '''###################
        step : 2 : 2
            tsp
    ###################'''
    _aryOf_Numbers[_pointOf_Tsp - 1]    = element_2
    _aryOf_Numbers[_pointOf_Tsp]        = element_1
    
    '''###################
        step : 3
            return
    ###################'''
    valOf_Ret   = _aryOf_Numbers
    
    return  valOf_Ret
    
    
    #code:20210728_132935
    
#/ def tsp()


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
    aryOf_Numbers   = [1,2,3,4,5]
    
    print()
    
    print ("[%s:%d] aryOf_Numbers =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print(aryOf_Numbers)
    print()
    
    '''###################
        step : 3
            transposition
    ###################'''
    #code:20210728_132436
#     pointOf_Tsp     = 0
    pointOf_Tsp     = 3

    print ("[%s:%d] pointOf_Tsp => %d" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                , pointOf_Tsp
                )
    )
    
    print ("[%s:%d] calling ... => tsp()" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print()
    
    #code:20210728_132743
    aryOf_Numbers   = tsp(aryOf_Numbers, pointOf_Tsp)
#     tsp(aryOf_Numbers, pointOf_Tsp)
    
    print ("[%s:%d] tsp() => complete" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print ("[%s:%d] aryOf_Numbers is now ... =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print(aryOf_Numbers)
    print()
    
# def test_1()://

'''###################
    test_2()
    at : 20210728_131213
###################'''
def test_2_Multiple_Tsp():

    strOf_FuncName = "test_2_Multiple_Tsp"

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
    aryOf_Numbers__Orig   = [1,2,3,4,5]
    
    #ref https://www.geeksforgeeks.org/array-copying-in-python/
    aryOf_Numbers__Copy   = aryOf_Numbers__Orig.copy()
#     aryOf_Numbers__Copy   = aryOf_Numbers__Orig
    
    print()
    
    print ("[%s:%d] aryOf_Numbers__Orig =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print(aryOf_Numbers__Orig)
    print()
    
    '''###################
        step : 3
            transposition
    ###################'''
    #code:20210728_132436
#     pointOf_Tsp     = 0
    pointsOf_Tsp     = [3,1,4,1]
#     pointsOf_Tsp     = [1,3,4,1]
#     pointsOf_Tsp     = [1,1,3,4]
#     pointsOf_Tsp     = [1,3,1,4]
#     pointOf_Tsp     = 3

    print ("[%s:%d] pointsOf_Tsp =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print(pointsOf_Tsp)
    print()
    
    cntr    = 0
    
    for pointOf_Tsp in pointsOf_Tsp:

        '''###################
            counter        
        ###################'''
        cntr    += 1

        print ("[%s:%d] ----------------- for : %d" % (
                    os.path.basename(os.path.basename(libs.thisfile()))
                    , libs.linenum()
                    , cntr
                    )
        )
        
        print()

        print ("[%s:%d] calling ... => tsp()" % (
                    os.path.basename(os.path.basename(libs.thisfile()))
                    , libs.linenum()
                    )
        )
        
        print()
        
        #code:20210728_132743
        aryOf_Numbers__Copy   = tsp(aryOf_Numbers__Copy, pointOf_Tsp)
#         aryOf_Numbers   = tsp(aryOf_Numbers, pointOf_Tsp)
    #     tsp(aryOf_Numbers, pointOf_Tsp)
        
        print ("[%s:%d] tsp() => complete" % (
                    os.path.basename(os.path.basename(libs.thisfile()))
                    , libs.linenum()
                    )
        )
        
        print ("[%s:%d] aryOf_Numbers__Copy is now ... =>" % (
                    os.path.basename(os.path.basename(libs.thisfile()))
                    , libs.linenum()
                    )
        )
        
        print(aryOf_Numbers__Copy)
        print()
                    
    #/for pointOf_Tsp in pointsOf_Tsp:
    
    print ("[%s:%d] aryOf_Numbers : compare =>" % (
                os.path.basename(os.path.basename(libs.thisfile()))
                , libs.linenum()
                )
    )
    
    print("orig / tsp / pointsOf_Tsp")
    
    print(aryOf_Numbers__Orig)
    print(aryOf_Numbers__Copy)
    print(pointsOf_Tsp)
    
#     print("orig :")
#     print(aryOf_Numbers__Orig)
#     
#     print("copy :")
#     print(aryOf_Numbers__Copy)
#     
    
# def test_2_Multiple_Tsp()://

def exec_prog(): # from : 
    
    
    '''###################
        execute
    ###################'''
    test_2_Multiple_Tsp()
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
