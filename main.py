class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("config is ",self.cpu,self.ram)

comp1=computer('i5',16)
comp2=computer('ryzen 3',8)


comp2.config()
comp1.config()