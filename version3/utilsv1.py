# Coding for the Aurobay interview 
# Coding start 14-Jun-2022

def read_csv(filePath: str, issplit: bool = True) -> list:
    """Read csv file by line.

    Args:
        filePath (str): Path of csv file.
        issplit (bool, optional): Determine whether split line by ','
                                  Default True.

    Returns:
        list: A list of csv content, every factor is one line split by ','
    """
    inputStream = list()
    with open(filePath) as csv_file:
        for line in csv_file:
            tmp = line.split(',') if issplit else line
            inputStream.append( tmp )
            
    return inputStream


def read_csv_content(filePath: str, haveHeader: bool = True, delNewline: bool = True, anormalCheck: bool = False) -> list[list[str]]:
    """Read csv file and return peer column.

    Args:
        filePath (str): Path of csv file.
        delNewline (bool, optional): Determine whether delete '\n'.
                                      Default Ture.
        anormalCheck (bool, optional): Check if there abnormal value: Nan, Null , Blank.
                                       Default False.

    Returns:
        dict[list]: A dictory of all data
                    key: The header of csv file, if header is null will be replace to category and index.
                    value: The column of this header
    """
    inputStream = read_csv(filePath)

    if haveHeader:
        columnName = inputStream.pop(0)
        for idx, column in enumerate(columnName):
            if column == '':
                columnName[idx] = 'category'+str(idx)
            if '\n' in column:
                columnName[idx] = column.replace('\n', '')
    else:
        columnName = ['category'+str(i) for i in range(len(inputStream[0]))]


    data = dict()
    for idx, column in enumerate(columnName):
        data[column] = list()
            
    # Add contain to list
    for rowNum, line in enumerate(inputStream):
        line = line
        for idx, column in enumerate(columnName):

            # Check wether there is any anomal value
            if anormalCheck:
                if line[idx] == 'Nan' or line[idx] == 'Null' or len( line[idx].replace('\n', '') ) ==  0:
                    print("Please check value at Column {} Row {}!".format(columnName[idx], rowNum) )

            # Check wether need to delete "\n"
            tmp = line[idx].replace('\n', '') if delNewline else line[idx]
            
            data[column].append(tmp)

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


def getCategoryAverage(category: list, values: list, dataType: str = 'float') -> dict :
    """Calculate the average value of differernt category.
    Args:
        category (list): Category list
        values (list): Value list
        dataType (str, optional): The values data type. Defaults to 'float'.
    Returns:
        dict: A dictory of result
              key: Different category, 
              value: The average value of this category
    """

    # Sort the data in different category
    catIndex = getCategoryIndex(category)

    # Store the average result
    catAverage = dict()
    for cat in catIndex:
        # Get corresponding value and convert data type
        if dataType == 'int':
            tmp = [int(values[i]) for i in catIndex[cat]]
            catAverage[cat] = int(sum( tmp )/len( tmp ))
        else:
            tmp = [float(values[i]) for i in catIndex[cat]]
            catAverage[cat] = sum( tmp )/len( tmp )
    return catAverage


def getCategorySum(depts: list, values: list, dataType: str = 'float') -> dict :
    """Calculate the sum value of differernt category.
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
        tmp = [float(values[i]) for i in catIndex[cat]]
        if dataType == 'int':
            tmp = [int(values[i]) for i in catIndex[cat]]
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
                catAverage[cat1][cat2] = int(sum( tmp )/len( tmp ))
            else:
                tmp = [float(values[i]) for i in catsIndex[cat1][cat2]]
                catAverage[cat1][cat2] = sum( tmp )/len( tmp )

    return catAverage

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
                catAverage[cat1][cat2] = int(sum( tmp )/len( tmp ))
            else:
                tmp = [float(values[i]) for i in catsIndex[cat1][cat2]]
                catAverage[cat1][cat2] = sum( tmp )/len( tmp )

    return catAverage

def getTwoCategorySum(cats1: list, cats2: list, values: list, dataType: str = 'float') -> dict :
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
                    value: The sum of this subcategory.
    """

    # Sort the data in different category
    catsIndex = getTwoCategoryIndex(cats1, cats2)

    # Store the sum result
    catSum = dict()
    for cat1 in catsIndex:
        catSum[cat1] = dict()
        for cat2 in catsIndex[cat1]:
        # Get corresponding value and convert data type
            if dataType == 'int':
                tmp = [int(values[i]) for i in catsIndex[cat1][cat2]]
                catSum[cat1][cat2] = sum( tmp )
            else:
                tmp = [float(values[i]) for i in catsIndex[cat1][cat2]]
                catSum[cat1][cat2] = sum( tmp )

    return catSum