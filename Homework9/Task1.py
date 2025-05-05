# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

import re

with open('test_file/task1_data.txt', 'r', encoding='utf-8') as infile:
    text = infile.read()

text_without_digits = re.sub(r'\d+', '', text)

with open('test_file/task1_answer.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(text_without_digits)

with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')