from serial import Serial 
import time as t
import os as o

s = Serial('/dev/cu.usbmodem14101',9600) 
t.sleep(2) 

while 1:
    gesture = str(s.readline())
    #print (gesture)
    
    if 'Right' in gesture:
        print("### Gesture => Right ###")
        o.system("/usr/local/Cellar/shpotify/2.1/bin/spotify next")
        print('\n')

    if 'Left' in gesture:
        print("### Gesture => Left ###")
        o.system("/usr/local/Cellar/shpotify/2.1/bin/spotify prev")
        print('\n')

    if 'Up' in gesture:
        print("### Gesture => Up ###")
        o.system("/usr/local/Cellar/shpotify/2.1/bin/spotify vol up")
        print('\n')   

    if 'Down' in gesture:
        print("### Gesture => Down ###")
        o.system("/usr/local/Cellar/shpotify/2.1/bin/spotify vol down")
        print('\n')  
    
    if 'Forward' in gesture:
        print("### Gesture => Forward ###")
        o.system("/usr/local/Cellar/shpotify/2.1/bin/spotify pause")
        print('\n') 

    if 'Backward' in gesture:
        print("### Gesture => Backward ###")
        o.system("/usr/local/Cellar/shpotify/2.1/bin/spotify pause")
        print('\n') 

    if 'Clockwise' in gesture:
        print("### Gesture => Clockwise ###")
        o.system("/usr/local/Cellar/shpotify/2.1/bin/spotify replay")
        print('\n') 

    if 'anti-clockwise' in gesture:
        print("### Gesture => anti-clockwise ###")
        o.system("/usr/local/Cellar/shpotify/2.1/bin/spotify toggle shuffle")
        print('\n') 
    gesture = "";
