class A:
    def __init__(self):
        print("it is init of a")
    
    def feature1(self):
        print("it is working")

    def feature2(self):
            print("it is not working")



class B(A):
    def __init__(self):
        print("it is init of b")
        super().__init__()


        
    def feature3(self):
        print("it is working")

    def feature4(self):
        print("it is not working")




b1=B()

