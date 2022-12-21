# # # # # # # user = "shimaa"
# # # # # # # age = 23
# # # # # # # print(user) #shimaa
# # # # # # # def printuser():
# # # # # # #     #creates it's own variable 
# # # # # # #     user = "ahmed"
# # # # # # #     age = 25
# # # # # # #     print(user) # ahmed
    
# # # # # # # printuser()
# # # # # # # print(user) #shimaa

# # # # # # # # using global keyword changes the variable in the global scope 

# # # # # # # user = "shimaa"
# # # # # # # age =23
# # # # # # # print(user) #shimaa
# # # # # # # print(age) #23
# # # # # # # def printuser():
# # # # # # #     global user , age
# # # # # # #     user = "ahmed"
# # # # # # #     age = 30
# # # # # # #     print(user) # ahmed
    
# # # # # # # printuser()
# # # # # # # print(user) #ahmed
# # # # # # # print(age) #30



# # # # # # # user = "shimaa"
# # # # # # # age =23
# # # # # # # print(user) #shimaa
# # # # # # # print(age) #23
# # # # # # # def printuser():
# # # # # # #     global user 
# # # # # # #     user = "ahmed"
# # # # # # #     age = 30
# # # # # # #     print(user) # ahmed
# # # # # # #     print(age) # 30
    
# # # # # # # printuser()
# # # # # # # print(user) #ahmed
# # # # # # # print(age) #23


# # # # # # # user = "shimaa"
# # # # # # # def outer ():
# # # # # # #     print (user) #shimaa
# # # # # # #     def inner():
# # # # # # #         print(user) #shimaa
# # # # # # #     inner()
# # # # # # # outer() 



# # # # # # user = "remon"
# # # # # # print(user) #remon 
# # # # # # def outer ():
# # # # # #     user = "ahmed"
# # # # # #     def inner():
# # # # # #         global user
# # # # # #         user ="khalid"
# # # # # #         print(user) #khalid
# # # # # #     inner()
# # # # # #     def secondinner():
# # # # # #         print(user) #ahmed
# # # # # #     secondinner()
# # # # # #     print (user) #ahmed

# # # # # # outer() 
# # # # # # print(user) #khalid

# # # # # user = "shimaa"
# # # # # def outer ():
# # # # #     global user 
# # # # #     user = "remon"
# # # # #     print(user) #remon
# # # # #     def inner():
# # # # #         nonlocal user  #error
# # # # #         user = "hussein"
# # # # #         print(user) #hussein
# # # # #     inner()
# # # # #     print(user) #hussein
# # # # # outer()
# # # # # import day2
# # # # # day2.funWithUlimitedArgs(1)
# # # # # day2.funWithUlimitedArgs(1,2)
# # # # # from day2 import funWithUlimitedArgs, user
# # # # # funWithUlimitedArgs(1)
# # # # # funWithUlimitedArgs(1,3)
# # # # # print(user) 

# # # # from folder.d.day1 import x , y , sum
# # # # print(x , y , sum)

# # # # # import folder.d.day1  as day1 
# # # # # print (day1.x)


# # # num = input ("enter number : ")

# # # try:
# # #     num = int(num)
# # #     print(1/0)
# # # except Exception as e:
# # #     print(e)
# # #     print("can't be casted")
# # # else :

# # #     print("the string is casted to number")
# # # finally:
# # #     print("print in the tcases")
# # # print(num)
# # # print("after error")

# # # # rising exceptions

# # # # num = input ("enter number : ")
# # # # if num =="done":
# # # #     raise Exception("exception message")
# # # # print("after error")
# # # # print(num)



# # #dealing with files  reading from file 
# # # file =open("some_file.txt" , "r")
# # # # print(file)
# # # data = file.readline()
# # # print(data)
# # # data = file.readline()
# # # print(data)
# # # data = file.readline()
# # # print(data)
# # # # for line in data:
# # # #     print (line)
# # # print (type (data))
# # # file.close()

# # file =open("somefile.txt" , "w")
# # # print(type(khalid))
# # # for line in khalid:
# # #     print(line)
# # file.write("line 1 ")
# # file.write("line 2 ")
# # # file.close()
# # file.seek(8)
# # # file =open("somefile.txt" , "w")
# # file.write("te")
# # # file.write("line 4 ")
# # # file.writelines(['line  5 ','line 6 ','line 7 '])
# # file.close()




# # a,*b,c = [1,2,3,4]
# # print(a , b , c)




# # l = [x**2 for x in range (10) if x%2==0]
# # print(l)
# # # they are equivilant 
# # l=[]
# # for x in range (10):
# #     if x%2==0:
# #         l.append(x**2)
# # print(l)
# # class Mammel:
# #     pass
# # m = Mammel()

# class Person:
#     count = 0
#     def __init__(self, name="ahmed" , age=25):
#         self.name= name
#         self.age=age
#         Person.count+=1
    
#     def walk(self): #insttance method
#         print(f"{self.name} is walking now")
#     def __str__(self):
#         return f"{self.name} is printed "
#     def __len__(self):
#         return len(self.__dict__)







#     @classmethod
#     def personwithoneargument(cls,name ):
#         pass 
#     @classmethod
#     def personwithtwoargument(cls,name , age):
#         pass












#     @staticmethod
#     def netSalry(sal):
#         print(sal*0.9)
# user = Person()
# # print(user)
# # print(len(user))
# newpersn = user.iti()
# # print(user.__dict__)
# # shrouk = Person("shrouk" , 23)
# # print(Person.count) #1
# # print(shrouk.name)
# divina = Person("divina" , 23)
# divina.salary = 10000
# # print(len(divina))
# # print(Person.count) #2
# # print(divina.name)
# # print(divina.count) #2
# # print(shrouk.count) #2


# # divina.netSalry(5000)
# # divina.netSalry(divina.salary)
# # Person.netSalry(5000)
# # Person.netSalry(divina.salary)

# # shrouk = Person("shrouk" , 23)
# # print(Person.count) #1
# # print(shrouk.name)
# # divina = Person("divina" , 23)
# # print(Person.count) #2
# # print(divina.name)
# # divina.count= 0
# # print(divina.count) #0
# # print(shrouk.count) #2
# # print(Person.count) #2
# # shrouk = Person("shrouk" , 23)
# # print(Person.count) #1
# # print(shrouk.name)
# # divina = Person("divina" , 23)
# # divina.salary = 10000
# # print (divina.__dict__)
# # print (shrouk.__dict__)
# # divina.walk()
# # shrouk.walk()
# # print(divina)
# # print(shrouk)
# # print(Person.count) #2
# # print(divina.name)
# # Person.count= 0
# # print(divina.count) #0
# # print(shrouk.count) #0
# # print(Person.count) #0
# # print(divina.salary)