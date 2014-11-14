import random

print('Welcome to the Magic Eight Ball!')

print('please type your question for me.')

while True:
    question = input('> ')

    answers = ['Yes.','No.','Maybe.','Definetly.','very posible','likey',
               'sorry I cant answer that','reply hazy try again',
               'most likely','my sources say no','go away','cannot tell',
              'why are you asking me?','if you want to','of course','dont be mean'
               
               ]

    answer = random.choice(answers)

    print(answer)

