#Дана строка, содержащая латинские буквы и скобки трех видов: «()», «[]», «{}». Если
#скобки расставлены правильно (то есть каждой открывающей соответствует
#закрывающая скобка того же вида), то вывести число 0. В противном случае вывести
#или номер позиции, в которой расположена первая ошибочная скобка, или, если
#закрывающих скобок не хватает, число —1.

def skobki(s):
    stack = []

    for i, c in enumerate(s):
        if c in '([{':
            stack.append((c, i))
        elif c in ')]}':
            if not stack:
                return i + 1

            last_bracket, last_index = stack.pop()
            if (c == ')' and last_bracket != '(') or \
                    (c == ']' and last_bracket != '[') or \
                    (c == '}' and last_bracket != '{'):
                return i + 1

    if stack:
        return -1

    return 0


input_string = input('Введите текст: ')
result = skobki(input_string)
print(result)