import unittest
import utilsv1
from utils import *


FILEPATH =  r"C:\\Users\\M\\Project\\Aurobay_task\\data\\datatset.csv"
DATA = read_csv_content(FILEPATH)

class TestFunction(unittest.TestCase):
    # def setUP(self):
    #     print("Start Test...")
        
    # test read_csv function
    def testReadCsv_Linenumber(self):
        self.allData = read_csv(FILEPATH)
        with open(FILEPATH) as file:
            count=len(file.readlines())
        self.assertEqual(count, len(self.allData), msg  = "Read file have problem.")
    
    def testReadCsv_LineContent(self):
        self.allData = read_csv(FILEPATH)
        with open(FILEPATH) as file:
            for idx, line in enumerate(file.readlines()):
                self.assertEqual(line.split(','), self.allData[idx], msg  = 'Row {} have problem.'.format(idx))

    # test read_csv_content function
    def testReadCsvContent_LineNumber(self):
        self.allDataContent = read_csv_content(FILEPATH, haveHeader= True, delNewline = False, anormalCheck = False)
        with open(FILEPATH) as file:
            count = len(file.readlines())
        self.assertEqual(count-1, len(self.allDataContent), msg  = 'read_csv_content function line number have problem')

        self.allDataContent = read_csv_content(FILEPATH, haveHeader= False, delNewline = False, anormalCheck = False)
        with open(FILEPATH) as file:
            count = len(file.readlines())
        self.assertEqual(count, len(self.allDataContent), msg  = 'read_csv_content function line number have problem')


    def testReadCsvContent_Header(self):
        self.allDataContent = read_csv_content(FILEPATH, haveHeader= False, delNewline = False, anormalCheck = False)
        for employeeDict in self.allDataContent:
            for idx, headerName in enumerate(list(employeeDict.keys())):
                self.assertEqual(headerName, 'category'+str(idx), msg  = 'read_csv_content function haveHeader parameter have problem')

        self.allDataContent = read_csv_content(FILEPATH, haveHeader= True, delNewline = False, anormalCheck = False)
        with open(FILEPATH) as file:
            headNames = file.readline().split(',')
            headNames = [headername.replace('\n', '') if '\n' in headername else headername for headername in headNames]
            headNames = ['category'+str(idx) if headername == '' else headername for idx, headername in enumerate(headNames)]
        for employeeDict in self.allDataContent:
            for idx, headerName in enumerate(list(employeeDict.keys())):
                self.assertEqual(headerName, headNames[idx], msg  = 'read_csv_content function haveHeader have problem')

    def testReadCsvContent_Newline(self):
        self.allDataContent = read_csv_content(FILEPATH, haveHeader= True, delNewline = True, anormalCheck = False)
        for employeeDict in self.allDataContent:
            for headerName in employeeDict:
                self.assertNotIn('\n', headerName, msg  = 'read_csv_content function delNewline have problem')
                self.assertNotIn('\n', employeeDict[headerName], msg  = 'read_csv_content function delNewline have problem')
    
    def testReadCsvContent_Anormal(self):
        self.allDataContent = read_csv_content(FILEPATH, haveHeader= True, delNewline = True, anormalCheck = True)
        for employeeDict in self.allDataContent:
            for headerName in employeeDict:
                self.assertIsNotNone(headerName, msg  = 'read_csv_content function delNewline have problem')
                self.assertIsNotNone(employeeDict[headerName], msg  = 'read_csv_content function delNewline have problem')
    
    # test sortCategory function
    def testSortCategory_LineNumber(self):
        self.allDataContent = read_csv_content(FILEPATH, haveHeader= True, delNewline = True, anormalCheck = True)
        with open(FILEPATH) as file:
            count = len(file.readlines()) - 1
        for category in self.allDataContent[0]:
            tmpCount = 0
            tmpSortRes = sortCategory([category], DATA)
            for cat in tmpSortRes:
                tmpCount += len(tmpSortRes[cat])
            self.assertEqual(count, tmpCount, msg  = 'SortCategory function have problem')

        for category1 in self.allDataContent[0]:
            for category2 in self.allDataContent[0]:
                tmpCount = 0
                tmpSortRes = sortCategory([category1, category2], DATA)
                for cat1 in tmpSortRes:
                    for cat2 in tmpSortRes[cat1]:
                        tmpCount += len(tmpSortRes[cat1][cat2])
                self.assertEqual(count, tmpCount, msg  = 'SortCategory function have problem')

    def testSortCategory_SortResult(self):
        self.allDataContent = read_csv_content(FILEPATH, haveHeader= True, delNewline = True, anormalCheck = True)
        for category in self.allDataContent[0]:
            tmpSortRes = sortCategory([category], DATA)
            for cat in tmpSortRes:
                for employeeInfo in tmpSortRes[cat]:
                    self.assertEqual(employeeInfo[category], cat, msg  = 'SortCategory function have problem')
        
        for category1 in self.allDataContent[0]:
            for category2 in self.allDataContent[0]:
                tmpSortRes = sortCategory([category1, category2], DATA)
                for cat1 in tmpSortRes:
                    for cat2 in tmpSortRes[cat1]:
                        for employeeInfo in tmpSortRes[cat1][cat2]:
                            self.assertEqual(employeeInfo[category1], cat1, msg  = 'SortCategory function have problem')
                            self.assertEqual(employeeInfo[category2], cat2, msg  = 'SortCategory function have problem')

    # test getCategoryAverage function
    def testgetCategoryAverage(self):
        self.allDataContent = read_csv_content(FILEPATH, haveHeader= True, delNewline = True, anormalCheck = True)
        tmpData = utilsv1.read_csv_content(FILEPATH)
        for category in ['Dept','education','job_level']:
            for value in ['salary', 'awards']:
                ave1 = getCategoryAverage([category], value, DATA)
                ave2 = utilsv1.getCategoryAverage(tmpData[category], tmpData[value])
                self.assertEqual(ave1, ave2, msg  = 'getCategoryAverage function have problem')

        for category1 in ['Dept','education','job_level']:
            for category2 in ['Dept','education','job_level']:
                for value in ['salary', 'awards']:
                    ave1 = getCategoryAverage([category1, category2], value, DATA)
                    ave2 = utilsv1.getTwoCategoryAverage(tmpData[category1], tmpData[category2], tmpData[value])
                    self.assertEqual(ave1, ave2, msg  = 'getCategoryAverage function have problem')

    # test getCategorySum function
    def testgetCategorySum(self):
        self.allDataContent = read_csv_content(FILEPATH, haveHeader= True, delNewline = True, anormalCheck = True)
        tmpData = utilsv1.read_csv_content(FILEPATH)
        for category in ['Dept','education','job_level']:
            for value in ['salary', 'awards']:
                ave1 = getCategorySum([category], value, DATA)
                ave2 = utilsv1.getCategorySum(tmpData[category], tmpData[value])
                self.assertEqual(ave1, ave2, msg  = 'getCategorySum function have problem')

        for category1 in ['Dept','education','job_level']:
            for category2 in ['Dept','education','job_level']:
                for value in ['salary', 'awards']:
                    ave1 = getCategorySum([category1, category2], value, DATA)
                    ave2 = utilsv1.getTwoCategorySum(tmpData[category1], tmpData[category2], tmpData[value])
                    self.assertEqual(ave1, ave2, msg  = 'getCategorySum function have problem')

if __name__ == '__main__':
    unittest.main()


