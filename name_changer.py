import smartpy as sp

class Value_Changer(sp.Contract):
    def __init__(self):
        self.init(
            name = "name",
            place= "location",
            age = 22,
        )
    @sp.entry_point
    def name_changer(self,new_name):
        self.data.name = new_name

    @sp.entry_point
    def place_changer(self, new_place):
        self.data.place = new_place

    @sp.entry_point
    def age_changer(self, new_age):
        self.data.age = new_age

@sp.add_test(name = "value changer")
def test():
    scenario = sp.test_scenario()
    scenario.h1("Value changer / Name changer")
    vc_obj = Value_Changer()
    scenario+=vc_obj 
    admin = sp.test_account("admin")
    simar = sp.test_account("simar")

    vc_obj.name_changer("simar").run(sender = simar)
    vc_obj.name_changer(input("Enter your name")).run(sender = admin)
    vc_obj.place_changer(input("Enter your place")).run(sender = simar)
    vc_obj.age_changer(int(input("Enter your place"))).run(sender = simar)
    
    

