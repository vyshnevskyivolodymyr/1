print("Hello world!")
# print
# print('test')
'''
 # - закоментированный текст 
 который не воспринимается
 при запуске кода
'''
# Ctrl + / -> comment или uncomment

# # escape послідовності
# # \n -> перенесение на новую строчку
print("Hello\nworld")
# # \t -> табуляция -> 4 пробела (в консоле бывает 2 или 8 пробела)
# print("Hello\n\tworld")
# # \ -> отзеркаливание – если нужно служебный символ сделать печатным
print("He\\llo\\n\\t\"world\"")
print("\\\\\\\\\\")

uah =32800
rate = 41.75 # курс доллара
usd = uah / rate
print("Сумма в долларах:", usd)

uah = float(input("Введите сумму в гривнах: "))
rate = 41.75
usd = uah / rate
print("Сумма в долларах:", round(usd, 2))


