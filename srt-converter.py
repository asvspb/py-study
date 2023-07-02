with open('ru.txt', 'r') as file:
    text = file.read()

# Разделение текста на абзацы
paragraphs = text.split('\n\n')

# Новая нумерация для абзацев
new_number = 12657

# Замена нумерации для каждого абзаца
for i in range(len(paragraphs)):
    paragraph = paragraphs[i]
    lines = paragraph.split('\n')

    # Обновление первой строки абзаца с новым номером
    lines[0] = str(new_number)
    new_number += 1

    paragraphs[i] = '\n'.join(lines)

# Обновленный текст
new_text = '\n\n'.join(paragraphs)

# Запись обновленного текста в файл
with open('ru_updated.txt', 'w') as file:
    file.write(new_text)
