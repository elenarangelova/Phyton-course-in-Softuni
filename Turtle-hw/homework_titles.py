#По въведени имена с input() искаме програмата да покаже как това име ще се съкрати до инициали.
#Пример как трябва да изглежда програмата:
#Въведете име:  Борис Червенков
#Инициали: Б.Ч.

input_name = input('Please enter your name:')

input_name_split = input_name.split()
result = ''
for name in input_name_split:
    result += (name[0] + '.')

print(result)