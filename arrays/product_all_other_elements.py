def divide(product, value):
    return product/value

def product_all_other_elements(values):
    print('Getting the product of all other elements.')
    print(values)

    if not values:
        print('No values passed in.')
        return

    product = 1
    for value in values:
        product = product * value

    result = [product//x for x in values]

    print(result)


product_all_other_elements([1,2,3])
product_all_other_elements([3,2,1])
product_all_other_elements([1,2,3,4,5,6])
product_all_other_elements([10,20,30,45])
product_all_other_elements([1,2])
product_all_other_elements([])