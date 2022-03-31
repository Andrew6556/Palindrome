#Первый вариант решения
# print('Введите слово на проверку паллидрому')
# word = input('Введите ваше слово:\n')
# print(f'Слово {word} является паллидромом') if word == word[::-1] else print(f'Слово "{word}" не является паллидромом')

#второй вариант решения 
list(map(lambda word: print(f'Слово "{word}" является паллидромом') if word != None else print("не является паллидромом") ,list(filter(lambda word: word == word[::-1], [input()]))))
