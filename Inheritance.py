class dad:
    def football(self):
        print("Dad likes watching football")



class mom:
    def cooking(self):
        print("Mom likes cooking")



class boy(dad):
    def studying(self):
        print("The boy likes studying")
my_boy = boy()
my_boy.studying()
my_boy.football()


class girl(mom):
    def washing(self):
        print("The girl likes washing clothes")
my_girl = girl()
my_girl.washing()
my_girl.cooking()

