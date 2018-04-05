#!/usr/bin/python

class Employee:
   count = 0

   @staticmethod
   def f():
      Employee.count = Employee.count + 1
      print('Class member function - static' , Employee.count)
   
   def __init__(self, name, title, dept, company):
      print ('Employee - constructor')
      self.setProfileDetails(name, title, dept, company)

   def setProfileDetails(self, name, title, dept, company):
      self.name = name 
      self.title = title 
      self.dept = dept 
      self.company = company 

   def printProfileDetails(self):
	print ('Name       : ' + self.name)
        print ('Title      : ' + self.title)
        print ('Department : ' + self.dept ) 
        print ('Company    : ' + self.company )

if __name__ == "__main__":
    sriram = Employee('Sriram', 'Architect', 'R&D', 'Verizon')
    sriram.printProfileDetails()

    nitesh = Employee('Nitesh', 'Data Scientist', 'R&D', 'Verizon')
    nitesh.printProfileDetails()
   
    nitesh.f()
    sriram.f()

