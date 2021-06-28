class MyClass:
    my_var = None

    def __init__(self, my_var):
        self.my_var = my_var

    @classmethod
    def check_my_var(cls):
        print(cls.my_var)

    @staticmethod
    def check():
        # print(self.my_var)
        print('This method does not have any object info')

    @property
    def value_of_attribute(self):
        return self.my_var

    @value_of_attribute.setter
    def set_value_of_attribute(self, value):
        self.my_var = value


my_object = MyClass('MyVar')

print('calling calls method'.center(80, "#"))
my_object.check_my_var()
# MyClass.check_my_var(MyClass)

my_object.check()
print(my_object.value_of_attribute)
my_object.set_value_of_attribute = "myNewValue"
print(my_object.value_of_attribute)
# MyClass.check_my_var(MyClass)
