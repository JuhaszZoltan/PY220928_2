nev = input('írd be a neved: ')
print(f'Hello {nev}!')
print(f'Milyen szép név az, hogy {nev}!')
print(f'Szerintem már most Beléd vagyok zúgva {nev}! uwu <3')

valasz = input(f'{nev}, szeretsz programozni? ')
if valasz.lower() in {'igen', 'ja', 'yes', 'y'}:
    print('Akkor még itt sokra viheted!')
else:
    print('Remélem majd megszereted... :(')

szam = int(input('Hányszor írjam ki a neved? '))
for x in range(szam):
    print(f'{nev}', end=' ')

print('\nRendben, mára végeztünk!')
print(f'Köszönj el szépen {nev}!')

while input() not in {'Szia!', 'Viszlát!', 'Viszont látásra!'}:
    print('Hát ez nem jött össze, próbáld újra!')

print(f'Viszlát {nev}, legyen szép napod! :)')