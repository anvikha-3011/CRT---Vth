#Single Inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")
        
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
        self.func1()  # Calling parent class function
        class_name = self.__class__.__name__
        print(f"This function is in {class_name} class.")
        