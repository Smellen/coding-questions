def is_unique(word):
    print('Checking if \'' + word + '\' contains unique characters. ')
    found = []
    for letter in word:
        if letter not in found:
            found.append(letter)
        else:
            print('The letter ' + letter + ' has already appeared.')
            return

    print('The word \'' + word + '\' is unique')


is_unique('ellen')
is_unique('abcdefg')
is_unique('Adm Jenso')
