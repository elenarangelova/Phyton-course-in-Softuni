#Напишете код, който взима два текста от потребителя, използвайки input(),
# след което покажете първия текст, но само частта която се намира след втория текст.
#Пример:
#Първи текст: This is soo difficult, I prefer playing WoW
#Втори текст: soo
#Резултат: difficult, I preffer playing WoW


input_text1 = input('1 sentence')
input_text2 = input('Word in the text')

index_text2 = input_text1.find(input_text2)
if index_text2 == -1:
    print(input_text1)
else:
    print(input_text1[index_text2 + len(input_text2):len(input_text1)])
