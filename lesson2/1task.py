#Напишете програма, която взима текст от потребителя използвайки
#input() и ограничава текста до 10 символа и добавя ... накрая

input_text = input()
if len(input_text) < 10:
    print(input_text)
else:
    print(input_text[0:10] + "...")
