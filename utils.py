# Coding for the Aurobay interview 
# Coding start 16-Jun-2022
# More elegant method

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

class Employee(object):
    """Class of employee, include all data property

    Args:
        object (_type_): _description_
    """
    def __init__(self, value: list):
        self.index = value[0]
        self.emp_id = value[1]
        self.age = value[2]
        self.Dept = value[3]
        self.location = value[4]
        self.education = value[5]
        self.recruitment_type = value[6]
        self.job_level = value[7]
        self.rating = value[8]
        self.onsite = value[9]
        self.awards = value[10]
        self.certifications = value[11]
        self.salary = value[12]
        self.satisfied = value[13]


class Survey(object):
    """Class of this survey

    Args:
        object (_type_): _description_
    """
    def __init__(self, inputStream: list, exitHeader: bool = True, delNewline: bool = True):
        """initialize Survey class

        Args:
            inputStream (list): All the data read from csv file
            exitheader (bool, optional): Whether to include column names. 
                                         Defaults to True.
            delNewline (bool, optional): Whether to remove all newlines. 
                                         Defaults to True.
        """
        if exitHeader:
            header = inputStream.pop(0)
            if delNewline:
                header = [i.replace('\n', '') for i in header]
        else: header = ['category'+str(idx) for idx in range(len(inputStream[0]))]

        # Add column names to the class
        self.header = header

        # Add all employee as Employee class
        self.employeeSet = []
        for line in inputStream:
            line = [i.replace("\n", '') for i in line] if delNewline else line
            self.employeeSet.append(Employee(line))
    

    def sortCategory(self, category: list, tmpEmployeeSet: list = [], catEmployeeSet: dict = dict()) -> dict: 
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

        if not tmpEmployeeSet:
            tmpEmployeeSet = self.employeeSet
        
        # Get all element of first category
        cats = [getattr(i, category[0]) for i in tmpEmployeeSet]
        # Remove duplicates
        diffcats = list( set( cats ) )

        # Bulid the dictory of first category
        catEmployeeSet = dict()
        for cat in diffcats:
            catEmployeeSet[cat] = list()

        # Add employee class satisfied this cat
        for idx, cat in enumerate(cats):
            catEmployeeSet[cat].append(tmpEmployeeSet[idx])

        # For every cat, iteratively filter the next level of category
        for cat in catEmployeeSet:
            if len(category[1:]) == 0:
                continue
            catEmployeeSet[cat] = self.sortCategory(category[1:], catEmployeeSet[cat], catEmployeeSet[cat])

        return catEmployeeSet
    

    def getCategoryAverage(self, category: list, value: str) -> dict:
        """Get the average values satisfy all categories in category list
           Using DFS method

        Args:
            category (list): All the categories need to satisfy
            value (str): The name of column to calculate average  

        Returns:
            dict: A dictory of average values satisfy all categories
                  key: cats of the first category
                  value: A dictory of subcategory
                        key: cats of the second category
                        ...
                        value: The average value satisfy all the keys
        """
        def calCategoryAverage(catsEmployeeSet: dict, value: str, averageValue: dict = dict()):
            """Used to iterate to the last layer and calculate the average

            Args:
                catsEmployeeSet (dict): A classified dictionary with employee
                value (str): The name of column to calculate average 
                averageValue (dict, optional): Dictionary for storing results. Defaults to dict().

            Returns:
                _type_:Dictionary for storing iterative results.
            """
            # Iterate to the last layer through DFS method
            for cat in catsEmployeeSet:
                averageValue[cat] = dict()

                # If it is the last layer, start the calculate average
                if type(catsEmployeeSet[cat]) == list:
                    tmp = [float(getattr(i, value)) for i in catsEmployeeSet[cat]]
                    averageValue[cat] = sum(tmp) / len(tmp)
                    continue

                # If not the last layer continue to iterate the next layer
                averageValue[cat] = calCategoryAverage(catsEmployeeSet[cat], value, averageValue = dict())
            return averageValue
            
        # Get a sorted dictory
        catsEmployeeSet = self.sortCategory(category)

        averageValue = calCategoryAverage(catsEmployeeSet, value)
        return averageValue




    def getCategorySum(self, category, value):
        """Get the sum values satisfy all categories in category list
           Using DFS method

        Args:
            category (list): All the categories need to satisfy
            value (str): The name of column to calculate sum  

        Returns:
            dict: A dictory of sum values satisfy all categories
                  key: cats of the first category
                  value: A dictory of subcategory
                        key: cats of the second category
                        ...
                        value: The average value satisfy all the keys
        """

        def calCategoryAverage(catsEmployeeSet, value, sumAgeValue = dict()):
            """Used to iterate to the last layer and calculate the sum

            Args:
                catsEmployeeSet (dict): A classified dictionary with employee
                value (str): The name of column to calculate sum 
                sumAgeValue (dict, optional): Dictionary for storing results. Defaults to dict().

            Returns:
                _type_: Dictionary for storing iterative results.
            """
            # Iterate to the last layer through DFS method
            for cat in catsEmployeeSet:
                sumAgeValue[cat] = dict()
                # If it is the last layer, start the calculate sum
                if type(catsEmployeeSet[cat]) == list:
                    tmp = [float(getattr(i, value)) for i in catsEmployeeSet[cat]]
                    sumAgeValue[cat] = sum(tmp)
                    continue

                # If not the last layer continue to iterate the next layer
                sumAgeValue[cat] = calCategoryAverage(catsEmployeeSet[cat], value, sumAgeValue = dict())
            return sumAgeValue

        # Get a sorted dictory
        catsEmployeeSet = self.sortCategory(category)
        sumAgeValue = calCategoryAverage(catsEmployeeSet, value)
        return sumAgeValue