suc  = False
for i in range (1,4):
    print('yes')
    if suc:
        print('Done')
        break
else:
    print('not done')

for x in range (1,3):
    for y in range (1,4):
        print (f" ({x}, {y})")



com = ''
#while com.lower() != 'quit':
    #com = input('<< ')
    #print('echo: ' ,com)

def mult (*nums):
    total = 1
    for num in nums:
        total  *= num
    return total


print(mult(3,4))

def multinput (**user):
    return(user, user['name'])


print(multinput(id = 23, name = 'angor', sex = 'male'))



def fizz_buzz (input):

    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    elif input % 3 == 0 :
        return 'Fizz'
    elif input % 5 == 0:
        return 'Buzz'

    return input


print(fizz_buzz(30))



numbers = [3,4,1,2]
a, b, *c = numbers
print(a, b, c)



#sorting items

prod_list = [
    ('prod1', 30),
    ('prod4', 17),
    ('prod0', 12)
]

#learning lambda

prod_list.sort(key = lambda item: item[0])
print(prod_list)


#learninig map function map( takes in a function , and an iterable)
price = list (map ( lambda item : item [1], prod_list))
print(price)


# using filtered filter (function, iterable)

filtered = dict (filter (lambda item : item[1] > 12, prod_list ))
print (filtered)

s = [1, 2, 3]
ss = [22, 11, 33]
print (list (zip ('abcd', s, ss)))

#tuple
asp = (3,5)
#print (asp + (5,5))

#arrays
from array import array

nu = array ('I', [3,4,5])
print(nu)

zu = {asp, 2}
print(zu)
# learning generators
from sys import getsizeof

vaal_l = [x for x in range(1)]
vaal_g = (x for x in range(1))
vaal_d = {x for x in range(1)}

print('list: ', getsizeof(vaal_l))
print('gen: ', getsizeof(vaal_g))
print('set: ', getsizeof(vaal_d))

# unpcking opertor
print (*ss)
print(*range(5))


#finding the most repeted alphabet in a sentence

sn = 'ade goes to school today'
print(list (sn))
ans = list(sn)
#{ co: item for item in ans if item}
