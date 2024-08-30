def single_root_words(root_word, *other_words):
    same_words = []
    root_word_ = root_word.lower()
    for i in other_words:
        other_words_ = i.lower()
        if root_word_ in other_words_ or other_words_ in root_word_:
            same_words.append(i)  # Если да, добавляем в список

    return same_words
# Примеры использования
result = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result)  # Ожидаемый вывод: ['richiest', 'orichalcum', 'richies']

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)  # Ожидаемый вывод: ['Able', 'Disable']