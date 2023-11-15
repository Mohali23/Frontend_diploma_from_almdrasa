
# هنا تم اضافة مسافة بين الكلمة المحجوزة و اسم الدالة 
def plant_recommendation(care):
    # تم اضافة علامة يساوي اخرى بدلاً من واحدة 
    if care == 'low':
        print('Sabar')
    elif care == 'medium':
        print('Liblab')
    # elif هنا تم تصحيح كلمة 
    elif care == 'high': # Medium --> High
        print('Orcade')

# تصحيح اسم الدالة
plant_recommendation('low')
# اضافة علامات التنصيص
plant_recommendation("medium")
plant_recommendation('high')


# في البرنامج bugs صلح ال 