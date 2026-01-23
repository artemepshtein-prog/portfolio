translations = {
    'cat': 'кот',
    'dog': 'пёс',
    'fish': 'рыба'
}

print("Введите слово на английском, которое хотите перевести")

word = input()

if word == "cat":
    print(translations[word])
if word == "dog":
    print(translations[word])
if word == "fish":
    print(translations[word])
else:
    print("Извините, такого слова нет в словаре")

# TODO:
#  Написать программу, которая будет работать так
#  > Введите слово на английском, которое хотите перевести
#  < cat
#  > Это слово переводится как "кот"