class A:
    
    def feature1(self):
        print("it is working")

    def feature2(self):
            print("it is not working")



class B(A):
    def feature3(self):
        print("it is working")

    def feature4(self):
        print("it is not working")




b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

