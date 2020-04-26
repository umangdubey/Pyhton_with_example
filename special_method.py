class human:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("config is",self.cpu,self.ram)


hum=human("i5",16)  #making object
hum1=human("amd",16)
hum.config()
hum1.config()

