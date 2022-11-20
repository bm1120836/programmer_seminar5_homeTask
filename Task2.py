
# Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

my_text = '«АБВГДе́йка» — советская и российская абв детская образовательная \ 
    телевизионная программа для дошкольников и младших школьников абвгдейка'

def del_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_words(my_text)
print(my_text)
