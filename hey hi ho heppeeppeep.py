import random

print('What is your name?')
name = input('>').strip().title()
print('Hello',name)
print('welcome to my magic 8 ball')
answers=['Yes.',
         'No.',
         'Really? mm hmmmmmm.',
         'yes no maybeso'
         'never','nope','uh no']
print('please type your question')
while True:  
    question= input('> ')
    answer=random.choice(answers)
    print(answer)
