# # class Mammel:
# #     def __init__(self , gender) :
# #         self.gender = gender
# #         # print("mammel created")
# #     def walk(self):
# #         print("mammel is walking")
# # class Person:
# #     def __init__(self, name , age  ):
# #         self.name = name
# #         self.age = age 
# #         # print("new person created")
# #     # def walk(self):
# #     #     print("Person is walking")

# # class Staff(Person , Mammel):
# #     def __init__(self,gender ,name,age):
# #         # print("new staff created")
# #         super().__init__(name,age)
# #         # they are equivilant 
# #         # Person.__init__(self , name , age)
# #         Mammel.__init__(self, gender)
# #         self._protected = "protected"
# #     def walk(self):
# #         super().walk()
# #         print("staff is walking")
# #     def setSalary(self,sal):
# #         self.__salary=sal
# #     def getSalry(self):
# #         return self.__salary
# #     def __call__(self):
# #         print("staff object is collable")
# #         # return "called"

# # shimaa = Staff("female","shimaa", 23 )
# # shimaa.setSalary(10000)
# # print(shimaa.getSalry())
# # print(shimaa._protected)
# # # shimaa.walk()
# # # print(shimaa.name)
# # # print(shimaa.age)
# # # print(shimaa.salary)
# # # print(shimaa.gender)
# # # shimaa()
# # # print(shimaa())



# class Human:
#     def __init__ (self, age):
#         self.age = age
#     @property
#     def age(self):
#         return self.__age
#     @age.setter 
#     def age(self, age):
#         if age > 0:
#             self.__age = age
#         if age <= 0:
#             self.__age = 0
# man = Human(23)  #23
# print(man.age) 
# man.age = -25
# print(man.age) #0

def outer(x):
    def inner(n):
        # print(x+n)
        return(x+n)
    return inner # returns function 

print(outer(2)(3))
