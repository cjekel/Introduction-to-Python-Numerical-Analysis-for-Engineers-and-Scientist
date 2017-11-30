import numpy as np
from itertools import islice
import os
import cPickle as pickle

def getStressValues(fileName):
    with open(fileName,'r') as out:
        #   the stress values always start at line 753
        for line in islice(out, 752):
            pass
        count = 0
        stress = []
        for line in out:
            a = line.split(' ')
            stress.append(float(a[-1]))
            count +=1
            if count == 10:
                break
        #   the stress returned is in psi
        return stress

def writeAreas(areas):
    with open('TenBarModArea.inp', 'r') as procTemplate, open('TenBarArea.inp', 'w') as procOutput:
        data = procTemplate.read()
        changeVar  = data.replace('area01', str(areas[0])).replace('area02', str(areas[1])).replace('area03', str(areas[2])).replace('area04', str(areas[3])).replace('area05', str(areas[4])).replace('area06', str(areas[5])).replace('area07', str(areas[6])).replace('area08', str(areas[7])).replace('area09', str(areas[8])).replace('area10', str(areas[9]))
        data = changeVar
        procOutput.write(data)

def myFunction(var):
    areas = var

    #   write file
    writeAreas(areas)
    
    #   force loop to re run if stress values empty
    stressValues = []
    while len(stressValues) < 10:
        #   run input file
        os.system('abaqus job=TenBarArea ask_delete=NO interactive > /dev/null')
        
        #   pull the stress values
        stressValues = getStressValues('TenBarArea.dat')
    
    #   max allowable stress values
    maxStress = np.array([25e3, 25e3, 25e3, 25e3, 25e3, 25e3, 25e3, 25e3, 75e3, 25e3])
    sf = 1.0
    
    #   compute the constraints
    cons = (np.abs(stressValues)*sf)-maxStress
    
    #   compute the new area
    aNew = np.abs((stressValues/maxStress))*areas
    
    lengths = np.ones(10)*360.0
    lengths[6] = 509.11688245431424
    lengths[7] = 509.11688245431424
    lengths[8] = 509.11688245431424
    lengths[9] = 509.11688245431424
    
    #   calculate the weight
    weights = 0.1*lengths*areas
    return sum(weights), cons, aNew

area = np.ones(10)
runs = []
for i in range(0, 100):
    #   evaluate the function
    obj, cons, aNew = myFunction(area)
    runs.append([obj, cons, area, aNew])
    
    print 'Objective ', obj
    print 'Constraints ', cons
    
    #   save the run
    pickle.dump( runs, open( 'runs00.p', 'wb'))
    
    #   set the new variables
    area = aNew.copy()
    
    #   check to make sure that each item is above 0.1 if not change it
    for j, k in enumerate(area):
        if k < 0.1:
            area[j] = 0.1
    print 'Area ', area
    print ' *** new run ***'
