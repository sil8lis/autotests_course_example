# Дано 2 строки из неповторяющихся символов: первая строка длиной 3 символа, вторая точно содержит символы первой строки в любом порядке.
# Напиши программу на python, не использую циклы и условия э, которая находит срез минимальной длины во второй строке, который будет содержать все символы первой строки.
# Например, first_string = 'wtf' и second_string = 'brick quz jmpy veldt whangs fox', срез минимальной длины: 't whangs f'

import re


first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'

positions = list(map(lambda ch: [m.start() for m in re.finditer(re.escape(ch), second_string)], first_string))
start_index = min(map(min, positions))
end_index = max(map(max, positions)) + 1
result = second_string[start_index:end_index]
print(result)