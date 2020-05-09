# [3, 4, 9, 6, 1]
# Count the number of smaller elements to the right should return 
# [1, 1, 2, 1, 0]

def number_smaller_elements_right(values):
    print(values)

    if not values or len(values) == 1:
        return

    result = []
    
    for i in range(len(values)):
        count = 0
        
        for j in range(i, len(values)):
            if(values[j] < values[i]):
                count = count+1

        result.append(count)

    print(result)
    print()


number_smaller_elements_right([3, 4, 9, 6, 1])#1,1,2,1,0
number_smaller_elements_right([1, 1, 1, 1, 1])#0,0,0,0,0
number_smaller_elements_right([9, 8, 7, 6, 5])#4,3,2,1,0