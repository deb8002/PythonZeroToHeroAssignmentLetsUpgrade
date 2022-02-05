list_1=[6,15,35,9,10,24,40,12,20,18,25]
lambda y: y%3==0
lambda z: z%5==0
number_3= list(filter(lambda y: (y%3==0),list_1))
number_5= list(filter(lambda z: (z%5==0),list_1))
print("Numbers that are divisible by 3 are",number_3,"and numbers that are divisible by 5 are",number_5)