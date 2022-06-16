# Coding for the Aurobay interview 
# Coding start 14-Jun-2022

def read_csv(filePath: str, column: bool = True, anormalCheck: bool = False) -> list[list[str]]:
    """Read csv file and return peer column

    Args:
        filePath (str): Path of csv file.
        column_name (bool, optional): Determine whether the returned list contains headers.
                                      If Ture, the frist factor of sublist is heaer.
                                      Default Ture.
        anormalCheck (bool, optional): Check if there abnormal value: Nan, Null , Blank.
                                       Default False.

    Returns:
        list[list]: Secondary list, each sublist contains a column in the csv.
                    The factor of sublist is str.
    """
    
    with open(filePath) as csv_file:
        columnName = csv_file.readline().split(',')
        numColumn = len(columnName)

        data = [list() for _ in range(numColumn)]
        if column:
            # Add header to the list
            for idx in range(numColumn):
                data[idx].append(columnName[idx].replace('\n', ''))
                
        # Add contain to list
        for rowNum, line in enumerate(csv_file):
            line = line.split(',')
            for idx in range(numColumn):
                
                # Check wether there is any anomal value
                if anormalCheck:
                    if line[idx] == 'Nan' or line[idx] == 'Null' or len( line[idx].replace('\n', '') ) ==  0:
                        print("Please check value at Column {} Row {}!".format(columnName[idx], rowNum) )

                # Add contain to sublist
                data[idx].append(line[idx].replace('\n', ''))
    
    return data


def dataSort(categories: list, vals: list) -> dict:
    """Sort two list in the list1 index

    Args:
        categories (list): The categories list to find index
        vals (list): The value list to get value by categories list index

    Returns:
        dict: A dictory of result
              key: Different categories, 
              value: a list context the value belong to this category
    """
    if len(categories) != len(vals):
        return "Please check input"

    # Get the name of all department
    diffCategory = list(set(categories))
    categoryIndex = [list() for _ in range(len(diffCategory))]

    # Get the index of different department
    for idx, cat in enumerate(categories):
        categoryIndex[diffCategory.index(cat)].append(idx)

    # Sort data in different category
    categoryValues = dict()
    for idx, cat in enumerate(diffCategory):
        # Put all salarys of one department in a list
        _tmp = [vals[i] for i in categoryIndex[idx]]
        categoryValues[cat] = _tmp

    return categoryValues

def calDeptAverageSalary(depts: list, salary: list) -> dict:
    """Calculate the average of differernt department

    Args:
        depts (list): The list of department, have corresponding relationship with salary list 
        salary (list): The list of salary, have corresponding relationship with department list 

    Returns:
        dict: A dictory of result
              key: Different department, 
              value: The average salary of this department
    """
    # Sort the data in different category
    deptSalary = dataSort(depts, salary)

    # Store the average result
    deptAverage = dict()
    for dept in deptSalary:
        # data type conversion
        tmp = [float(i) for i in deptSalary[dept]]
        deptAverage[dept] = sum( tmp )/len( tmp )
    return deptAverage



def findTotalReward(depts: list, awards: list) -> dict :
    """Calculate the most reward of differernt department

    Args:
        depts (list): The list of department, have corresponding relationship with reward list 
        salary (list): The list of reward, have corresponding relationship with department list 

    Returns:
        dict: A dictory of result
              key: Different department, 
              value: The total reward of this department
    """
    # Sort the data in different category
    deptAwards = dataSort(depts, awards)

    # Store the average result
    deptTotalAward = dict()
    for dept in deptAwards:
        # data type conversion
        tmp = [int(i) for i in deptAwards[dept]]
        deptTotalAward[dept] = sum( tmp )
    return deptTotalAward

