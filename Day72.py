class parentclass:
    def parent_method(self):
        print("this is parent class !!")

class childclass(parentclass):
     def parent_method(self):
        print("hii i am piyush !!")
        super().parent_method()
     def child_method(self):
        print("this is child class !!")
        super().parent_method()

child_object = childclass()
child_object.child_method()
child_object.parent_method()