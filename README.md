# Aurobay_task

This is the task Aurobay interview.

Wish me luck!


	
> 1. Implement a solution that reads the dataset file
	
> 2. Implement a solution that scans the content of the text file and checks the average salary in each department.
	
> 3. Implement a solution that checks which department that has received most awards. The solution shall return the number of awards from each department.
	
> 4.  For each job level, find the average salary for each department.

	
> * 4a. Compare which department pays on average highest for job level 5.

## Version1
Base column, function

### Function
* read_csv() : Read csv file by line.

* read_csv_content() : Read csv file and return peer processed column.

* getCategoryIndex() : Get the list index in different categories.

* getCategoryAverage() : Calculate the average value of different categories.

* getCategorySum() : Calculate the sum value of different categories.

* getTwoCategoryIndex() : Get the list index of category 2 under category 1.

* getTwoCategoryAverage() : Calculate the average value of category 2 under category 1.


## Version2
* Base row, adaptive, class

### Function
read_csv : Read csv file by line.


### Class
Employee: Class of the employee, including all data property

* All data property


Survey: Class of this survey.


* Survey.header : The list includes all column names.

* Survey.employeeSet : The list includes all employee classes.

* Survey.sortCategory() : All input categories are classified in turn through DFS method. The number of categories of the input is adaptive.

* Survey.getCategoryAverage() : Get the average values that satisfy all categories in the category list. Using DFS method, the number of categories of the input is adaptive.

* Survey.getCategorySum() : Get the sum values that satisfy all categories in the category list. Using DFS method, the number of categories of the input is adaptive.




## Version3
Base row, adaptive, function

### Function

* read_csv() : Read csv file by line.

* read_csv_content() : Read csv file and return peer processed row.

* sortCategory() : All input categories are classified in turn through DFS method. The number of categories of the input is adaptive.

* getCategoryAverage() : Get the average values that satisfy all categories in the category list. Using DFS method, the number of categories of the input is adaptive.

* getCategorySum() : Get the sum values that satisfy all categories in the category list. Using DFS method, the number of categories of the input is adaptive.