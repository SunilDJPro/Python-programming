class MyClass:
    class_variable = "Hello, I am a class variable"
    
    @classmethod
    def class_method(cls):
        return cls.class_variable
    
    def static_method(string1):
        return string1



  

# Calling the class method
print(MyClass.class_method())

# Calling the static method
print(MyClass.static_method("I am Static"))  

