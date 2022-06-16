# Coding for the Aurobay interview 
# Coding start 16-Jun-2022
# More elegant method

from utils import *

# Question 1
csvPath =  r"C:\\Users\\M\\Project\\Aurobay_task\\data\\datatset.csv"
inputStream = read_csv(csvPath)

# Question 2
survey = Survey( read_csv(csvPath) )
deptAverageSalary = survey.getCategoryAverage(['Dept'], 'salary')
for dept in deptAverageSalary:
    print("{} department has average salary {:.2f}.".format(dept, deptAverageSalary[dept]))
print('\n')

# Question 3
deptSumAward = survey.getCategorySum(['Dept'], 'awards')
for dept in deptSumAward:
    print("{} department have total {:.0f} reaward.".format(dept, deptSumAward[dept]))
print('\n')

# Question 4
levelDeptAveSalary = survey.getCategoryAverage(['job_level', 'Dept'], 'salary')
depts = [dept for dept in levelDeptAveSalary['5']]
salarys = [levelDeptAveSalary['5'][dept] for dept in levelDeptAveSalary['5']]
maxSalary = max(salarys)
maxSalaryDept = depts[salarys.index(maxSalary)]
print("The highest salary department is {}, and the salarys is {:.2f}.".format(maxSalaryDept, maxSalary))