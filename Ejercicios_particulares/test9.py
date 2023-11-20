lst = [1,2,3,4,5]
lst_2 = []
add = 0
for number in range (len(lst)):
    add += number #number es variable de control
    lst_2.append(add)
print (lst_2)