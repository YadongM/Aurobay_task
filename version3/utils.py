# Coding for the Aurobay interview 
# Coding start 17-Jun-2022
# More elegant method through function

def read_csv(filePath: str, issplit: bool = True) -> list:
    """Read csv file by line

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


def read_csv_content(filePath: str, haveHeader: bool = True, delNewline: bool = True, anormalCheck: bool = False) -> list:
    """Read csv file and return peer column.

    Args:
        filePath (str): Path of csv file.
        delNewline (bool, optional): Determine whether delete '\n'.
                                      Default Ture.
        anormalCheck (bool, optional): Check if there abnormal value: Nan, Null , Blank.
                                       Default False.

    Returns:
        dict[list]: Include dictorys, every dictory is an employee information
                    key: The header of csv file, if header is null will be replace to category and index.
                    value: The information of this information in this inforamtion category
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


    data = list()
            
    # Add contain to list
    for rowNum, line in enumerate(inputStream):
        tmpDict = dict()
        for idx, column in enumerate(columnName):
            # Check wether there is any anomal value
            if anormalCheck:
                if line[idx] == 'Nan' or line[idx] == 'Null' or len( line[idx].replace('\n', '') ) ==  0:
                    print("Please check value at Column {} Row {}!".format(columnName[idx], rowNum) )

            # Check wether need to delete "\n"
            if delNewline:
                line[idx] = line[idx].replace('\n', '')

            tmpDict[column] = line[idx]
        # Add this line to data
        data.append(tmpDict)

    return data

def sortCategory(category: list, tmpEmployeeSet: list, catEmployeeSet: dict = dict()) -> dict: 
    """The number of categories of the input is adaptive, 
        and all categories of the input are classified in turn through DFS method.

    Args:
        category (list): All categories need to be classified.
        tmpEmployeeSet (list, optional): Used as a list as the final classification result, the element is the class. 
                                            Defaults to [].
        catEmployeeSet (dict, optional): The dictory to store current Category Results. 
                                            Defaults to dict().

    Returns:
        dict: A  nested dictory.
                Key: All categories of the first element of category
                Value: A nested dictory.
                    Key: All categories of the second element of category
                    ......
                    value: A list of employee class meet all key conditions
    """
    # Get all element of first category
    cats = [i[category[0]] for i in tmpEmployeeSet]
    # Remove duplicates
    diffcats = list( set( cats ) )

    # Bulid the dictory of first category
    catEmployeeSet = dict()
    for cat in diffcats:
        catEmployeeSet[cat] = list()

    # Add employee satisfied this cat
    for idx, cat in enumerate(cats):
        catEmployeeSet[cat].append(tmpEmployeeSet[idx])

    # For every cat, iteratively filter the next level of category
    for cat in catEmployeeSet:
        if len(category[1:]) == 0:
            continue
        catEmployeeSet[cat] = sortCategory(category[1:], catEmployeeSet[cat], catEmployeeSet[cat])

    return catEmployeeSet






def getCategoryAverage(category: list, value: str, data: list, dataType: str = 'float') -> dict:
    """Get the average values satisfy all categories in category list
        Using DFS method

    Args:
        category (list): All the categories need to satisfy
        value (str): The name of column to calculate average  
        data (list): A list include the dictory, every dictory include one employee information.
        dataType (str): The expect datatype of value. Defaults to 'float.

    Returns:
        dict: A dictory of average values satisfy all categories
                key: cats of the first category
                value: A dictory of subcategory
                    key: cats of the second category
                    ...
                    value: The average value satisfy all the keys
    """
    def calCategoryAverage(catsEmployeeSet: dict, value: str, averageValue: dict = dict(), dataType: str = 'float'):
        """Used to iterate to the last layer and calculate the average

        Args:
            catsEmployeeSet (dict): A classified dictionary with employee
            value (str): The name of column to calculate average 
            averageValue (dict, optional): Dictionary for storing results. Defaults to dict().
            dataType (str): The expect datatype of value. Defaults to 'float.

        Returns:
            _type_:Dictionary for storing iterative results.
        """
        # Iterate to the last layer through DFS method
        for cat in catsEmployeeSet:
            averageValue[cat] = dict()

            # If it is the last layer, start the calculate average
            if type(catsEmployeeSet[cat]) == list:
                tmp = [float(i[value]) for i in catsEmployeeSet[cat]]
                averageValue[cat] = sum(tmp) / len(tmp)
                if dataType == "int":
                    tmp = [int(i[value]) for i in catsEmployeeSet[cat]]
                    averageValue[cat] = int( sum(tmp) / len(tmp) )
                continue

            # If not the last layer continue to iterate the next layer
            averageValue[cat] = calCategoryAverage(catsEmployeeSet[cat], value, averageValue = dict(), dataType = dataType)
        return averageValue
        
    # Get a sorted dictory
    catsEmployeeSet = sortCategory(category, data)
    averageValue = calCategoryAverage(catsEmployeeSet, value, dataType = dataType)
    return averageValue




def getCategorySum(category: list, value: str, data: list, dataType: str = 'float'):
    """Get the sum values satisfy all categories in category list
        Using DFS method

    Args:
        category (list): All the categories need to satisfy.
        value (str): The name of column to calculate sum.
        data (list): A list include the dictory, every dictory include one employee information.
        dataType (str): The expect datatype of value. Defaults to 'float.

    Returns:
        dict: A dictory of sum values satisfy all categories
                key: cats of the first category
                value: A dictory of subcategory
                    key: cats of the second category
                    ...
                    value: The average value satisfy all the keys
    """

    def calCategoryAverage(catsEmployeeSet, value, sumValue = dict(), dataType: str = 'float'):
        """Used to iterate to the last layer and calculate the sum

        Args:
            catsEmployeeSet (dict): A classified dictionary with employee
            value (str): The name of column to calculate sum 
            sumValue (dict, optional): Dictionary for storing results. Defaults to dict().
            dataType (str): The expect datatype of value. Defaults to 'float.

        Returns:
            _type_: Dictionary for storing iterative results.
        """
        # Iterate to the last layer through DFS method
        for cat in catsEmployeeSet:
            sumValue[cat] = dict()
            # If it is the last layer, start the calculate sum
            if type(catsEmployeeSet[cat]) == list:
                tmp = [float(i[value]) for i in catsEmployeeSet[cat]]
                sumValue[cat] = sum(tmp)
                if dataType == "int":
                    tmp = [int(i[value]) for i in catsEmployeeSet[cat]]
                    sumValue[cat] = sum(tmp)
                continue

            # If not the last layer continue to iterate the next layer
            sumValue[cat] = calCategoryAverage(catsEmployeeSet[cat], value, sumValue = dict(), dataType = dataType)
        return sumValue

    # Get a sorted dictory
    catsEmployeeSet = sortCategory(category, data)
    sumValue = calCategoryAverage(catsEmployeeSet, value, dataType = dataType)
    return sumValue