a = [0]
for i in a:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    operation = input("Выберите операцию: \n \n( + ); ( - ); ( * ); ( / ); ( ** ); ( // )")

    if operation == "+":
        print("Вы выбрали сложение: " + str(num1) + " + " + str(num2) + " = " + str(num1 + num2) + "\n")
    elif operation == "-":
        print("Вы выбрали вычитание: " + str(num1) + " - " + str(num2) + " = " + str(num1 - num2) + "\n")
    elif operation == "*":
        print("Вы выбрали умножение: " + str(num1) + " * " + str(num2) + " = " + str(num1 * num2) + "\n")
    elif operation == "/":
        print("Вы выбрали деление: " + str(num1) + " / " + str(num2) + " = " + str(num1 / num2) + "\n")
    elif operation == "%":
        print("Вы выбрали остаток от деление: " + str(num1) + " % " + str(num2) + " = " + str(num1 % num2) + "\n")
    elif operation == "//":
        print("Вы выбрали целочисленное деление: " + str(num1) + " // " + str(num2) + " = " + str(
            num1 // num2) + "\n")
    elif operation == "**":
        print(
            "Вы выбрали возведение в степень: " + str(num1) + " ** " + str(num2) + " = " + str(num1 ** num2) + "\n")
    else:
        print("Выберите одну из выше перечисленных операций!")

    question = input("Продолжить?\nДа: Нажмите на любую кнопку кроме n и N\nНет: Нажмите n или N\n")
    if question == "n" or question == "N":
        print(f"Вы использовали мой калькулятор {len(a)} раз(-а)")
        break
    else:
        a.append(len(a))