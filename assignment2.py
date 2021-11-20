from __future__ import print_function
import time
from sr.robot import *

a_th = 2.0
""" float: Threshold for the control of the orientation"""

d_th = 0.4
""" float: Threshold for the control of the linear distance"""

d_min = 1.2
""" float: Threshold for the minimum distance from the golden token"""

#dist2 =0.0 
"""Float: distance to compare"""

#dist3=0.0 
"""Float: distance to compare"""

angl2 = 0.0
"""Float: angolaxion to compare"""

angl3=0.0 
"""Float: angolaxion to compare"""

R = Robot()
""" instance of the class Robot"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity

    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
def grab_release(code):
    """
    function that bring in entrance the token identified in tha main and go grab it
    """    
    dist= 10
    for token2 in R.see():
        if token2.info.marker_type is MARKER_TOKEN_SILVER and token2.dist<dist:
            dist = token2.dist
            angl = token2.rot_y       
    if -a_th < angl < a_th:
        print ("in vista")
        if dist< d_th:
            R.grab()
            print ("preso")
            turn(13,4)
            R.release()
            turn(-13,4)
            print("pronto")
            drive(20,0.5)
        else:
            print ("mo arrivo")
            drive(20, 0.5)
            grab_release(token2.info.code)
    elif angl > a_th:
        print ("mi giro a destra")
        turn (5,0.3)
        grab_release(token2.info.code)
    elif angl < -a_th:
        print ("mi giro a sinistra")
        turn (-5,0.3)
        grab_release(token2.info.code)

def scelta():
    """
    function to turn in the rigth way when it is at the corner
    """
    dist2 =0.0
    dist3 =0.0
    for token3 in R.see():
        if 88 < token3.rot_y < 92:
            dist2=token3.dist
            print("preso primo dato")            
        else:
            print("nope1")           
            
    for token2 in R.see():
        if -92 < token2.rot_y < -88:
            dist3=token2.dist
            print ("preso dato 2")
        else:
            print("nope 2")
            
    if dist2 > dist3:
        print ("da questa parte")
        turn (12,2)
    else:
        print ("invece da questa parte")
        turn(-12,2)

def distance(token):
    """
    function that bring in entrance the token identified in the main and turn to not hit it 
    """
    dist = token.dist
    angl = token.rot_y
    if -10 < angl < 10:
        if dist<= d_min:
            if angl >= a_th+1 :
                print("a sinistra")
                turn(-15,1.3)
                #drive(10,1)
            elif angl <= -a_th-1 :
                print("a destra")
                turn(15,1.3)
                #drive(10,1)
            elif -a_th-1 < angl < a_th+1:
                print("sono indeciso")
                scelta()
        elif dist> d_min:
            print("ancora lontano")
    elif -135 < angl < -45 or 45 < angl < 135:
        if dist <= 0.5:
            if angl < 0:
                turn (5, 0.1)
            elif angl > 0:
                turn (-5, 0.1)
    else:
        print("per ora no")
 
       
#the main
drive (20,5)
while 1:
    drive(20,0.5)
    #silver = []
    #i=0
    for token in R.see():
        if token.info.marker_type is MARKER_TOKEN_GOLD:
            if token.dist<=d_min:
                distance(token)
        elif token.info.marker_type is MARKER_TOKEN_SILVER and token.dist<1.2 and -45 < token.rot_y < 45:
            #silver.append(token.info.code)                       
            #if silver[i] not in silver:
            code=token.info.code
            print("vediamo")
            grab_release(code)
            #i=i+1
        #else:
            #print("andata")
    #drive(0,0.5)
           
"""                   
for token in R.see():
    if token.info.marker_type is MARKER_TOKEN_SILVER:
        print(" dist %d  angl %d" %(token.dist, token.rot_y))  
"""   
    
    
    
    
    
    
    
    
        
    
    
    
    
