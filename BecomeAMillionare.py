from colorama import Fore, Back, Style
import random
import time
print(Fore.BLUE + 'Здравей!')
time.sleep(2)
print('Добре дошъл в Стани богат!')
time.sleep(2)
print('Нека да започваме.Ето и първият въпрос:')
print(Style.RESET_ALL)
questions_counter = 0
answered_questions = []

questions_between_1_to_3 = ["Най-високият връх в Стара планина?", "В кой град се произвежда бира с марка Алмус?", "Кой град се счита за столицата на Розовата долина?"]
questions_between_4_to_5 = ["Кой е авторът на стихотворението 'Опълченците на Шипка'?", "През коя година избухва Априлското въстание?"]
for _ in range(1,100):
    if questions_counter <= 3:
        computer_question = random.choice(questions_between_1_to_3)
        if computer_question not in answered_questions:
            answered_questions.append(computer_question)
            print(computer_question)
            if computer_question == "Най-високият връх в Стара планина?":
                answer = input('Вашият отговор е: ')
                if answer == 'връх Ботев' or answer == "Ботев":
                    print("Верен отговор!Ето и следващият въпрос:\n")
                    questions_counter += 1
                else:
                    print("Грешен отговор!Хващай пътя!")
                    exit()
            elif computer_question == "В кой град се произвежда бира с марка Алмус?":
                answer = input('Вашият отговор е: ')
                if answer == 'Лом' or answer == 'град Лом':
                    print("Верен отговор!Ето и следващият въпрос:\n")
                    questions_counter += 1
                else:
                    print("Грешен отговор!Хващай пътя!")
                    exit()
            elif computer_question == "Кой град се счита за столицата на Розовата долина?":
                answer = input('Вашият отговор е: ')
                if answer == 'Казанлък' or answer == 'град Казанлък':
                    print("Верен отговор!Ето и следващият въпрос:\n")
                    questions_counter += 1
                else:
                    print("Грешен отговор!Хващай пътя!")
                    exit()
        else:
            continue
if questions_counter == 3:
    print(Back.BLUE + Fore.BLACK + 'ЧЕСТИТО! СПЕЧЕЛИХТЕ ПОЧЕРПКА БИРА! ЖЕЛАЕТЕ ЛИ ДА ПРОДЪЛЖИТЕ НАПРЕД ?')
    print(Style.RESET_ALL)
    answer = input()
    if answer == 'да':
        for _ in range(1, 100):
            computer_question = random.choice(questions_between_4_to_5)
            if computer_question not in answered_questions:
                answered_questions.append(computer_question)
                print(computer_question)
                if computer_question == "Кой е авторът на стихотворението 'Опълченците на Шипка'?":
                    answer = input("Вашият отговор е: ")
                    if answer == 'Иван Вазов' or answer == 'Вазов':
                        questions_counter += 1
                        if questions_counter == 5:
                            print(Back.BLUE + Fore.BLACK + 'ЧЕСТИТО! СПЕЧЕЛИХТЕ КАСА БИРА!')
                            print(Style.RESET_ALL)
                        else:
                            print("Верен отговор!Ето и следващият въпрос:\n")
                    else:
                        print("Грешен отговор!Хващай пътя!")
                elif computer_question == "През коя година избухва Априлското въстание?":
                    answer = input("Вашият отговор е: ")
                    if answer == '1876':
                        questions_counter += 1
                        if questions_counter == 5:
                            print(Back.BLUE + Fore.BLACK + 'ЧЕСТИТО! СПЕЧЕЛИХТЕ ПОЧЕРПКА КАСА БИРА!')
                            print(Style.RESET_ALL)
                        else:
                            print("Верен отговор!Ето и следващият въпрос:\n")

                    else:
                        print("Грешен отговор!Хващай пътя!")
            else:
                continue















