#Python Class and Object 
class Student:

    # class attribute
    name = ""
    age = 0
    def eat(self):
        print( "I can eat!")
    
    def sleep(self):
        print("I can sleep!")

# create parrot1 object
p1 = Student()
p1.name = "Ali"
p1.age = 17

# create another object parrot2
p2 = Student()
p2.name = "Khan"
p2.age = 18

# access attributes
print(p1.name)
print(f"{p2.name} is {p2.age} years old")
p1.eat()
p2.eat()