# TODO  Напишите функцию count_letters
def count_letters(str):
    str = str.lower()
    dict = {}

    for char in str:
        if char.isalpha():
            if char not in dict:
                dict[char] = 0

            dict[char] += 1

    return dict

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict):
    total_letter_amount = 0

    for value in dict:
        total_letter_amount += dict[value]

    for value in dict:
        dict[value] = round(dict[value] / total_letter_amount, 2)

    return dict

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

# TODO Распечатайте в столбик букву и её частоту в тексте
letters_amount = count_letters(main_str)
letters_freq = calculate_frequency(letters_amount)

for key, value in letters_freq.items():
    value = f'{value:.2f}'
    print(f'{key}:', value)
