from __future__ import print_function
from itertools import islice

def getStressValues(fileName):
    with open(fileName,'r') as out:
        #   the stress values always start at line 753
        #   and will always be 10 lines long
        stress = []
        for line in islice(out,752,762):
            a = line.split(' ')
            stress.append(float(a[-1]))
        return stress

def write_areas(areas):
    with open('TenBarModArea.inp', 'r') as procTemplate, open('TenBarArea.inp', 'w') as procOutput:
        data = procTemplate.read()
        changeVar = data.replace('area01', str(areas[0])).replace('area02', str(areas[1])).replace('area03', str(areas[2])).replace('area04', str(areas[3])).replace('area05', str(areas[4])).replace('area06', str(areas[5])).replace('area07', str(areas[6])).replace('area08', str(areas[7])).replace('area09', str(areas[8])).replace('area10', str(areas[9]))
        procOutput.write(changeVar)
        
write_areas((0.5, 0.5, 0.5, 0.6, 0.7, 0.25, 0.25, 0.4, 0.3, 0.7))
stress = getStressValues('TenBarArea.dat')
print(stress)