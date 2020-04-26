
class Pycharm:
    def execute(self):
        print("compilling")
        print("executing")



class mycharm:
    def execute(self):
        print("compilling")
        print("executing")
        print("spell check")

class  laptop:


    def code(self,ide):
        ide.execute()




#ide = Pycharm()       #this called duck typing in duck typing it is not what class object you are
                                    #passing it only important it have same method 

ide=mycharm()


lap=laptop()
lap.code(ide)
