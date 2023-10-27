def count_letters(str1):
    str1 = str1.lower()
    vocab = dict()
    count = 0
    for i in str1:
        for j in str1:
            if i.isalpha() and i == j:
                count += 1
        if i not in vocab and i.isalpha():
            vocab[i] = count
        count = 0
    return vocab


def calculate_frequency(vocab_fr, amount):
    for key, value in vocab_fr.items():
        vocab_fr[key] = round(value / amount, 2)
    return vocab_fr


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
length = 0
for letter in main_str:
    if letter.isalpha():
        length += 1
my_vocab = calculate_frequency(count_letters(main_str), length)
for key, value in my_vocab.items():
    if value == 0:
        print(f"{key:.2}: 0.00")
    else:
        print("{:.2}: {:.2}".format(key, value))

