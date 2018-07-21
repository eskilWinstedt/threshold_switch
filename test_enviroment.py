import time
import threshold_switch as ts

Button1 = ts.ThresholdActivator(500, 400) 
while True:
    Button1.updateThreshold(int(input()))
    print(Button1.mode)