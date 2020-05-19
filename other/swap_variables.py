def number_swap(a, b):
    print('Before swapped values')
    print('a = ' + str(a))
    print('b = ' + str(b))
    
    a = a+b
    b = a-b
    a = a-b
    
    print('Swapped values')
    print('a = ' + str(a))
    print('b = ' + str(b))


def built_in_swap(a, b):
    print('Before swapped values')
    print('a = ' + str(a))
    print('b = ' + str(b))
    
    a,b = b,a

    print('Swapped values')
    print('a = ' + str(a))
    print('b = ' + str(b))


def xor_swap(a, b):
    print('Before swapped values')
    print('a = ' + str(a))
    print('b = ' + str(b))
    
    a = a^b
    b = a^b
    a = a^b
    
    print('Swapped values')
    print('a = ' + str(a))
    print('b = ' + str(b))


number_swap(1, 2)
print()
number_swap(3, 4)
print()
number_swap(5, 8)
print
built_in_swap('ellen', 'dotnet')
print
built_in_swap(10, 15)
print
built_in_swap([1, 2, 3], [5, 6, 7])
print
built_in_swap(1.2, 5.8)
print
built_in_swap(True, False)
print
xor_swap(1, 2)
