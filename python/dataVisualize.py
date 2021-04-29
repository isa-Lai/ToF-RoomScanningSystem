#yuyint lai 400268588 
import serial
import math
import numpy as np
import open3d as o3d

#Modify the following line with your own serial port details
#   Currently set COM3 as serial port at 115.2kbps 8N1
#   Refer to PySerial API for other options.  One option to consider is
#   the "timeout" - allowing the program to proceed if after a defined
#   timeout period.  The default = 0, which means wait forever.

s = serial.Serial("COM7", 115200)

print("Opening: " + s.name)

#  modify the file path here
#  please use the path you want to write file
file = open('D:\\dx_lab\\Project\\python\\tof_radar.xyz','w');

s.write(b'1')           #This program will send a '1' or 0x31 

#   perameter
#   numTestPerRotation means the number of measument for one rotation
#   numtest is the total test counted in this python
numTestPerRotation = 64;
numTest=0;
x =0;
dataIsIn=False

while(True):
    data = s.readline()        # read one byte
    i = numTest%numTestPerRotation
    angle = i*2.0*math.pi/numTestPerRotation
    distanceStr = data.decode()     # convert byte type to str
    distanceStr = distanceStr[:-1] #remove \n
    if(distanceStr.isdigit() == True): #only get digital value
        print("distance is "+distanceStr)
        dataIsIn = True
        distance = int(distanceStr)
        y = distance*math.cos(angle) # Calculate x
        z = distance*math.sin(angle) # Calcualte y
        point_cor = str(x)+' '+str(y)+' '+str(z)+'\n' #convert into xyz format
        print(point_cor)
        file.write(point_cor)
        numTest+=1
    # x displacement 30cm
    if(numTest%numTestPerRotation==0):
        x+=150 #modify here fore your x displacement
    #end if the program end
    if((distanceStr.isdigit()==False) and (dataIsIn == True)): 
        break

print("Closing: " + s.name)
file.close()
s.close();


# 3d plot start
if __name__ == "__main__":
    
    # please modify the path here the same as line 19 in last section
    pointdata = o3d.io.read_point_cloud('D:\\dx_lab\\Project\\python\\tof_radar.xyz', format='xyz')
    
    numpoints = len(pointdata.points)

    vector = []

    level = numTest//numTestPerRotation
    print("total level "+str(level))
    for i in range(level):
        vector.append([0+i*numTestPerRotation,numTestPerRotation-1+i*numTestPerRotation]) #connect the head and tail
        #connect every adjacent point
        for x in range(numTestPerRotation-1):
            #print("connet "+str(x+i*numTestPerRotation)+" "+str(x+1+i*numTestPerRotation))
            vector.append([x+i*numTestPerRotation,x+1+i*numTestPerRotation])
        
    #connect between each level
    i=0
    for i in range(level-1):
        #connect every 22.5 degree 
        #modify the angle here if you needed 
        vectorAngle = 22.5
        point = 0;
        shiftPoint = int(vectorAngle/360*numTestPerRotation ) 
        while (point<numTestPerRotation):
            vector.append([point+i*numTestPerRotation,point+(i+1)*numTestPerRotation])
            point+=shiftPoint

        
    

    line_set = o3d.geometry.LineSet(points=o3d.utility.Vector3dVector(np.asarray(pointdata.points)), lines=o3d.utility.Vector2iVector(vector))
    o3d.visualization.draw_geometries([line_set])