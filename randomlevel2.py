import random
my_randoms=[]
list1 = []
list2 = []

for i in range (10):
    my_randoms.append(random.randrange(1,101,1))

list1 = for elements in my_randoms:
    list1.extend([])
    if elements%5 == 0:
        print ("These numbers are divisible by 5" , elements)
list2 = for elements in my_randoms:
    list2.extend([])
    if elements%3 == 0:
        print ("These numbers are divisible by 3" , elements)
