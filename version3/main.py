# Coding for the Aurobay interview 
# Coding start 17-Jun-2022
# More elegant method through function


from utils import *

def main():
    # Question 1
    csvPath =  r"C:\\Users\\M\\Project\\Aurobay_task\\data\\datatset.csv"
    data = read_csv_content(csvPath)

    # Question 2
    deptSalary = getCategoryAverage(['Dept'], 'salary', data)
    for dept in deptSalary:
        print("{} department has average salary {:.2f}.".format(dept, deptSalary[dept]))
    print('\n')

    # Question 3
    deptReward = getCategorySum(['Dept'], 'awards', data)
    for dept in deptReward:
        print("{} department have total {:.0f} reaward.".format(dept, deptReward[dept]))
    print('\n')

    # Question 4
    levelDeptAveSalary = getCategoryAverage(['job_level', 'Dept'], 'salary', data)

    # Question 4.a
    depts = [dept for dept in levelDeptAveSalary['5']]
    salarys = [levelDeptAveSalary['5'][dept] for dept in levelDeptAveSalary['5']]
    maxSalary = max(salarys)
    maxSalaryDept = depts[salarys.index(maxSalary)]
    print("The highest salary department of level 5 is {}, and the salarys is {:.2f}.".format(maxSalaryDept, maxSalary))





if __name__ == "__main__":
    main()