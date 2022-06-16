# Coding for the Aurobay interview 
# Coding start 14-Jun-2022

def read_csv(filePath: str, column: bool = True, anormalCheck: bool = False) -> list[list[str]]:
    """Read csv file and return peer column.

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


def getCategoryIndex(categories: list) -> dict:
    """Get the list index in different category
    Args:
        categories (list): The categories list to find index
    Returns:
        dict: A dictory of result
              key: Different categories, 
              value: The index of this category.
    """
    # Get the name of all categories
    diffCategory = list(set(categories))
    categoryIndex = dict()
    for cat in diffCategory:
        categoryIndex[cat] = list()

    # Get the index of different category
    for idx, cat in enumerate(categories):
        categoryIndex[cat].append(idx)

    return categoryIndex


def getCategoryAverage(categories: list, values: list, dataType: str = 'float') -> dict :
    """Calculate the average value of differernt categories.
    Args:
        categories (list): Category list
        values (list): Value list
        dataType (str, optional): The values data type. Defaults to 'float'.
    Returns:
        dict: A dictory of result
              key: Different category, 
              value: The average value of this category
    """

    # Sort the data in different category
    catIndex = getCategoryIndex(categories)

    # Store the average result
    catAverage = dict()
    for cat in catIndex:
        # Get corresponding value and convert data type
        if dataType == 'int':
            tmp = [int(values[i]) for i in catIndex[cat]]
        tmp = [float(values[i]) for i in catIndex[cat]]
        catAverage[cat] = sum( tmp )/len( tmp )
    return catAverage


def getCategorySum(depts: list, values: list, dataType: str = 'float') -> dict :
    """Calculate the sum value of differernt categories.
    Args:
        categories (list): Category list
        values (list): Value list
        dataType (str, optional): The values data type. Defaults to 'float'.
    Returns:
        dict: A dictory of result
              key: Different category, 
              value: The sum value of this category
    """
    # Sort the data in different category
    catIndex = getCategoryIndex(depts)

    # Store the average result
    catSum = dict()
    for cat in catIndex:
        # data type conversion
        if dataType == 'int':
            tmp = [int(values[i]) for i in catIndex[cat]]
        tmp = [float(values[i]) for i in catIndex[cat]]
        catSum[cat] = sum( tmp )
    return catSum




def getTwoCategoryIndex(cats1, cats2) -> dict:
    """Get index of category 2 under category 1.
    Args:
        cats1 (list): The categories list to find index
        cats2 (list): The sub categories list to find index
    Returns:
        dict: A dictory of result
              key: Different categories, 
              value: A dictory of result
                    key: Different subcategories, 
                    value: The index of this subcategory.
    """
    catsIndex = dict()
    tmp_index_1 = getCategoryIndex(cats1)
    for cat1 in tmp_index_1:
        catsIndex[cat1] = dict()
        tmp_Value_1 = [cats2[i] for i in tmp_index_1[cat1]]
        tmp_index_2 = getCategoryIndex(tmp_Value_1)

        for cat2 in tmp_index_2:
            tmp = [tmp_index_1[cat1][i] for i in tmp_index_2[cat2]]
            catsIndex[cat1][cat2] = tmp
                
    return catsIndex

def getTwoCategoryAverage(cats1: list, cats2: list, values: list, dataType: str = 'float') -> dict :
    """Calculate the average value of category 2 under category 1.
    Args:
        cats1 (list): Category list
        cats2 (list): Category list
        values (list): Value list
        dataType (str, optional): The values data type. Defaults to 'float'.
    Returns:
        dict: A dictory of result
              key: Different category, 
              value: A dictory of result
                    key: Different subcategories, 
                    value: The average of this subcategory.
    """

    # Sort the data in different category
    catsIndex = getTwoCategoryIndex(cats1, cats2)

    # Store the average result
    catAverage = dict()
    for cat1 in catsIndex:
        catAverage[cat1] = dict()
        for cat2 in catsIndex[cat1]:
        # Get corresponding value and convert data type
            if dataType == 'int':
                tmp = [int(values[i]) for i in catsIndex[cat1][cat2]]
            tmp = [float(values[i]) for i in catsIndex[cat1][cat2]]
            catAverage[cat1][cat2] = sum( tmp )/len( tmp )

    return catAverage