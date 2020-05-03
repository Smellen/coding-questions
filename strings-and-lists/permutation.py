def is_permutation(one, two):
    one = one.replace(' ', '')
    two = two.replace(' ', '')

    if (len(one) != len(two)):
        print('Not a permutation.')
        return

    for letter in one:
        if letter in two:
            two = two.replace(letter, '', 1)
        else:
            print('Not a permutation.')
            return

    if len(two) == 0:
        print('Permutation found.')
    else:
        print('Not a permutation.')
            


print('Checking permutations')
is_permutation('ellen', 'ellen')
is_permutation('hello', 'world')
is_permutation('dog     ', 'god')

