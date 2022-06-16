# Coding for the Aurobay interview 
# Coding start 14-Jun-2022

from utils import *

csvPath =  r"C:\\Users\\M\\Project\\Aurobay_task\\data\\datatset.csv"
data = read_csv(csvPath, False)


deptSalary = calDeptAverageSalary(data[3],data[12])
for dept in deptSalary:
    print("{} department has average salary {:.2f}.".format(dept, deptSalary[dept]))


deptReward = findTotalReward(data[3],data[10])
for dept in deptReward:
    print("{} department have total {:.0f} reaward.".format(dept, deptReward[dept]))
