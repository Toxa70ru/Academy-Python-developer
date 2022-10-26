print("Введите длину коврика")
height = int(input())
width = height * 3

for stick_count in range(1, height, 2):
    print(('.|.' * stick_count).center(width, '-'))

print('WELCOME'.center(width, '-'))

for stick_count in range(height-2, 0, -2):
    print(('.|.' * stick_count).center(width, '-'))