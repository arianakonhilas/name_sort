#All My Cats 2
#A program that prints cat names in alphabetical order
#Ariana Konhilas

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are:')
for name in sorted(catNames):
    print(' ' + name)
