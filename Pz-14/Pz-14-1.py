# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
# «произведение».

import re

with open('writer.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'\b([А-ЯЁ][а-яё]+)\s[А-Я]\.[А-Я]\.'
surnames = re.findall(pattern, text)
file_surnames = sorted(set(surnames))
# Запись фамилий в отдельный файл
with open('surnames.txt', 'w', encoding='utf-8') as f:
    for surname in file_surnames:
        f.write(surname + '\n')

# Замена слова "роман" на "произведение"
update_text = re.sub(r'\bроман\b', 'произведение', text, flags=re.IGNORECASE)

with open('updated.txt', 'w', encoding='utf-8') as f:
    f.write(update_text)

print(f"Извлечено {len(file_surnames)} фамилий. Файл 'surnames.txt' создан.")
print("Файл с заменами сохранён как 'updated.txt'.")
