#Nested if-using decision tree -fitness check
age = 18
eat_pizza = False
exercise = True
if (age<30):
    if eat_pizza:
        print('unfit')
    else:
        print('fit')
else:
    if exercise:
        print('fit')
    else:
        print('unfit')
