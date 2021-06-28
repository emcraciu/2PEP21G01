class MyClass():
    my_var = None

    def __init__(self, my_var):
        self.my_var = my_var

    @classmethod
    def check_my_var(cls):
        print(cls.my_var)

    @staticmethod
    def check():
        #print(self.my_var)
        print('This method does not have any object info')

    @property
    def value_of_attribute(self):
        return self.my_var

    @value_of_attribute.setter()
    def set_value_of_attribute(self):
        self.my_var



my_object = MyClass('MyVar')

my_object.check_my_var()
my_object.check()
print(my_object.value_of_attribute)
my_object.set_value_of_attribute = "myNewValue"
#MyClass.check_my_var(MyClass)
