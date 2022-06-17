# Aurobay_task

This is the task Aurobay interview.

Wish me luck!


	
> 1. Implement a solution that reads the dataset file
	
> 2. Implement a solution that scans the content of the text file and checks the average salary in each department.
	
> 3. Implement a solution that checks which department that has received most awards. The solution shall return the number of awards from each department.
	
> 4.  For each job level, find the average salary for each department.

	
> * 4a. Compare which department pays on average highest for job level 5.

## Version1
Base column method, function

### Function
* read_csv() : Read csv file by line.

* read_csv_content() : Read csv file and return peer processed column.

* getCategoryIndex() : Get the list index in different category.

* getCategoryAverage() : Calculate the average value of differernt category.

* getCategorySum() : Calculate the sum value of differernt category.

* getTwoCategoryIndex() : Get list index of category 2 under category 1.

* getTwoCategoryAverage() : Calculate the average value of category 2 under category 1.


## Version2
* Base row, adaptive method, class

### Function
read_csv : Read csv file by line.


### Class
Employee : Class of employee, include all data property

* All data property


Survey : Class of this survey.

* Survey.header : List include all column name.

* Survey.employeeSet : List include all emploee class.

* Survey.sortCategory() : All categories of the input are classified in turn through DFS method, the number of categories of the input is adaptive.

* Survey.getCategoryAverage() : Get the average values satisfy all categories in category list, using DFS method, the number of categories of the input is adaptive.

* Survey.getCategorySum() : Get the sum values satisfy all categories in category list, using DFS method, the number of categories of the input is adaptive.




## Version3
Base row, adaptive method, function

### Function

* read_csv() : Read csv file by line.

* read_csv_content() : Read csv file and return peer processed row.

* sortCategory() : All categories of the input are classified in turn through DFS method, the number of categories of the input is adaptive.

* getCategoryAverage() : Get the average values satisfy all categories in category list, using DFS method, the number of categories of the input is adaptive.

* getCategorySum() : Get the sum values satisfy all categories in category list, using DFS method, the number of categories of the input is adaptive.