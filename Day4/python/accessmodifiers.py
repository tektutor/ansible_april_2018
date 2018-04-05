#!/usr/bin/python

class MyClass:

    def __init__(self):
	print ('MyClass constructor')

    def publicMethod(self):
        print ('publicMethod invoked')

    def _protectedMethod(self):
	print ('protectedMethod invoked')

    def __privateMethod(self):
	print ('privateMethod invoked')

class Child(MyClass):

     def __init__(self):
         MyClass.__init__(self)
         print ('Child constructor')

     def childMethod(self):
         self.publicMethod()
         self._protectedMethod()
#        self.__privateMethod() - Compilation error expected

if __name__ == "__main__":
   myClassObj = MyClass()
   myClassObj.publicMethod()
   myClassObj._protectedMethod()
#  myClassObj.__privateMethod() - Compilatio error expected 

   childObj = Child()
   childObj.childMethod()
