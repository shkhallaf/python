# mario pyramid
# num = input("Enter number : ")
# while not num.isdigit():
#     num = input("Enter number : ")
# num = int (num)

# using nested 

# for i in range (num):
#     for space in range ((i+1),num):
#         print (" " , end="")
#     for star in range (i+1):
#         print ("*",end="")
#     print()

# using string interpolation

# for i in range (num):
#     print ("  "*(num-(i+1)) + "* " * (i+1))


# array elements 

# num = input("Enter number : ")
# while not num.isdigit():
#     num = input("Enter number : ")
# num = int (num)
# l =[]
# for i in range (num):
#     ele = input (f"Enter element number {i+1} : ")
#     while not ele.isdigit():
#         ele = input(f"Enter element number {i+1} : ")
#     ele = int (ele)
#     l.append(ele)
# print (l)


# multiplication table
# num = input("Enter number : ")
# while not num.isdigit():
#     num = input("Enter number : ")
# num = int (num)
# final = []
# for i in range (1,num+1):
#     small =[]
#     for j in range (1,i+1):
#         small.append(i*j)
#     final.append(small)
# print(final)


# str ="shimaa"
# print (str.replace("s" , "S") )# Shimaa
# print(str)
# l =[]
# l = list ([])
# t = ()
# print(type(t))
# print(len(t))
# t = tuple([])
# t= (1,2,"shimaa" , [1,2,2] , [[],[]])
# print(len(t))
# print(t[0])
# t[3][0]="test"
# t = list(t)
# print (type (t))
# print(t.pop())
# t = tuple(t)
# print(t)
# print(type(t))
# del t 
# print (t)
# l =[1,1,(1,12,3)]
# l[2][1]=0
# print(l)
# t= (1,2,"shimaa" , [1,2,2] , [[],[]])
# t2 = (1,2,3)
# t3=t+t2
# print(t3)
# t=()
# t=(1,2,3,)
# print("shimaa" in t)
# for ele in t:
#     print (ele)
# unit = (1,)
# print(type(unit))
# print(len(unit))

# t= (1,2,"shimaa" , [1,2,2] , [[],[]] )
# print (type(t[3][0]))
# result = t[3][0]+10
# print(result)

# s = {10,9,9,15,1,2,3,4,5,6,6,5,4}
# print(s)
# l=[3,2,1,2,2,(1,2),(1,2),(1,2),(2,1),(1,4), (3,4) , "shimaa"]
# l = set(l)
# print(l)
# # l.pop() # remove from the begginig 
# # l.pop(5) # not allowed 
# # l.remove(2)
# l.add("try")
# l.add(10)
# print("-----------------")
# print(l)
# print("-----------------")

# print(l.update(l,{"test","try"}))
# print(l)
# details = ["shimaa" , 23 , "iti staff"]

# details = {"name":"shimaa" , "age":23 , "courses":["css" , "python"] , 1 : 1999 , (1,2):["html","css"]}
# print(details[1])
# d = dict([("name","shimaa"),(1,1999),("age" , 23) , (1,1000)])
# print(d.items())
# d.pop(1)
# d.update({"name" : "mona" , "salary" : 20000})
# for key , value  in d.items():
#     if key==1:
#         continue
#     print(f"{key} = {value}")

# d.clear()
# print(d)
# print (d.keys())
# l = list(d.values())
# print(l)
# for ele in l :
#     print(d[ele])
# print("---------------------------")
# for ele in d:
#     print(f"{ele} => {d[ele]}")
# print(l)
# print (d[1])
# d[1]=2000
# print (d[1])
# print (d)
# print("_________________________")
# d["test"] ="test"
# print (d)
# print("_________________________")
# d["name"] ="ahmed"
# print (d)
# s = {1,1,2,2,} # {1:1 , 2:2}
# a,b=(1,2)
# print(a)
# print(b)
# l = ["ibraam","shimaa" , "ahmed" , "mohammed" , "shimaa"]
# passed =[]
# for ele in l :
#     if ele =="shimaa":
#         break
#     passed.append(ele)
# print(passed)




# for i in range(10):
#     if i == 4:
#         break
#     print(i)
# else:
#     print("loop ended")

# str = input ("enter str : ")
# print (str)

def myrange(end,start=0,step=1):
    #start = 0 step = 1
    #end = 1 , start = 0 , step = 1 (1)
    #end = 1 , start = 2 , step = 1 (1,2)
    # end = 1  start = 2 step = 3 (1,2,3)
    return end+start+step
# print(myrange())
# print(myrange())
# print(myrange(1))
# print(myrange(1,2))
# print(myrange(1,2,3))

# adding()
# adding()


# sum (1,2)
# not supported in python
# def sum(int n,int n1):
# def sum(int n,int n1 , int n3):
# def sum (float n , float n1):
# def sum (string n , string n1 ):
# def sum(int n,str n1, float x):
# def sum(float n,str n1, float x):




# n = input ("enter number : ")
# n1 = input("enter number : ")
# r = n +n1
# print (r)
# n = input ("enter number : ")
# n1 = input("enter number : ")
# r = n +n1
# print (r)
# n = input ("enter number : ")
# n1 = input("enter number : ")
# r = n +n1
# print (r)



def myrange(x=0,y=0,z=0,a=0,s=0):
    if type(x)==type(0):
        print("integer")
    return x+y+z+a+s
# print(myrange(1))
# print(myrange(1,2))
# print(myrange(1,2,3))
# print(myrange("a","b","c","d","e" , "l")) error

# print (type(1)==type(2))
# print(isinstance("1",int))
# print(type(1))


# def funWithUlimitedArgs(*hazlqomm):
#     sum = 0
#     for ele in hazlqomm:
#         sum +=ele
#     print(sum)
# funWithUlimitedArgs()
# funWithUlimitedArgs(1)
# funWithUlimitedArgs(1,2)
# funWithUlimitedArgs(1,2,3)



def funWithnamesandcountofargs(**hazlqomm):
    for key , value in hazlqomm.items():
        print (f"{key}  =  {value}")
    print("------------------")
funWithnamesandcountofargs(name = "shimaa")
funWithnamesandcountofargs(name = "ahmed"  , age =23)
