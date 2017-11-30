from __future__ import print_function

from itertools import islice


# ========== HW09 SOLUTION [Python2/3] ========== #

# ========== 1 ========== #

def write_areas(areas):
    with open('TenBarModArea.inp', 'r') as proc_template, open('TenBarArea.inp', 'w') as proc_output:
        data = proc_template.read()
        for i in range(10):
            data = data.replace('area{:02d}'.format(i + 1),
                                str(areas[i]))
        proc_output.write(data)

write_areas((0.5, 0.5, 0.5, 0.6, 0.7, 0.25, 0.25, 0.4, 0.3, 0.7))

# ========== 2 ========== #

def read_stress_values(filename):
    with open(filename, 'r') as out:
        #   the stress values always start at line 753
        #   and will always be 10 lines long
        stress = []
        for line in islice(out, 752, 762):
            a = line.split(' ')
            stress.append(float(a[-1]))
        return stress

stress = read_stress_values('TenBarArea.dat')

# optionally, impement your function as a generator.
# read more: https://stackoverflow.com/q/231767/4410590

def read_stress_values(filename):
    with open(filename, 'r') as out:
        #   the stress values always start at line 753
        #   and will always be 10 lines long
        for line in islice(out, 752, 762):
            a = line.split(' ')
            yield float(a[-1])

stress = list(read_stress_values('TenBarArea.dat'))

print(stress)
