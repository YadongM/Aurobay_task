# Coding for the Aurobay interview 
# Coding start 14-Jun-2022

from utils import *

# Question 1
csvPath =  r"C:\\Users\\M\\Project\\Aurobay_task\\data\\datatset.csv"
data = read_csv_content(csvPath)

# Question 2
deptSalary = getCategoryAverage(data['Dept'],data['salary'])
for dept in deptSalary:
    print("{} department has average salary {:.2f}.".format(dept, deptSalary[dept]))
print('\n')

# Question 3
deptReward = getCategorySum(data['Dept'],data['awards'])
for dept in deptReward:
    print("{} department have total {:.0f} reaward.".format(dept, deptReward[dept]))
print('\n')

# Question 4
levelDeptAveSalary = getTwoCategoryAverage(data['job_level'], data['Dept'], data['salary'])

# Question 4.a
depts = [dept for dept in levelDeptAveSalary['5']]
salarys = [levelDeptAveSalary['5'][dept] for dept in levelDeptAveSalary['5']]
maxSalary = max(salarys)
maxSalaryDept = depts[salarys.index(maxSalary)]
print("The highest salary department is {}, and the salarys is {:.2f}.".format(maxSalaryDept, maxSalary))
