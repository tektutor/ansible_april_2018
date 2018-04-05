class Mobile:
   
    def __init__(self, mobileNumber):
        print( 'Mobile constructor' )
	self._mobileNumber = mobileNumber

    def printMobile(self):
        print( 'Mobile No => ' + str( self._mobileNumber ) )

