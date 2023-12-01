fruits = [
    'apples',
    'bananas',
    'grapes',
    'mangos',
    'nectarines',
    'pears',
    'watermillion',
]

# Print any sentence of your choice.   اطبع أي جملة من اختيارك
print('I Love Learning with Almdrasa')

# Make for loop, and print each name individually.  واطبع كل اسم حدة for loop قم بعمل 
for fruit in fruits:
    print(fruit)

# After that, Use while loop to print all fruits until you reach nectarines, don't print it. لا تقوم بطباعته nectarines لطباعة كل الفواكة الي ان تصل الي while loop بعد ذالك استخدم 
index = 0
while index < len(fruits):
    if fruits[index] == 'nectarines':
        break
    print(fruits[index])
    index += 1


