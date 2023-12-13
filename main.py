def bmi_calculator(weight, height):
    '''Эта фнкция отвечает за калькуляцую BMI'''
    
    return weight / height**2



weight = float(input("Введите ваш вес: "))
height = float(input("Введите ваш рост: "))


bmi = bmi_calculator(weight,height)

if bmi < 18.5:
    print("У вас недовес.")
elif bmi > 18.5 and bmi < 24.9:
    print("Все нормально")
else:
    print("Bad")