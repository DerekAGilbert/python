# my_friends = ['ben', 'tom', 'josh']
# friend = input('Enter the name here!? of the person you might know')
#
#
# if friend in my_friends:
#     print('this is your friend {}!'.format(friend))
# else:
#     print('You do not know this man, {}!'.format(friend))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
def even():
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print(even())
