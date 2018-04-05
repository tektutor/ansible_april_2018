from mobile import Mobile

class IPhone(Mobile):
    
    def __init__(self, mobileNumber):
        Mobile.__init__(self,mobileNumber)
	print('IPhone constructor')

if __name__ == "__main__":
    iPhone = IPhone(1234567890)
    iPhone.printMobile()
