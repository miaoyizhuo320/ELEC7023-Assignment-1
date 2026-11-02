# Name: Yizhuo(Steven) Miao
# Assignment One

import turtle

# Part A: Turtle Drawing
colors = ['red', 'orange', 'green', 'blue', 'purple']
turtle.speed(0)

for i in range(30):
    turtle.color(colors[i % 5])
    for j in range(4):
        turtle.forward(40 + i * 4)
        turtle.right(90)
    turtle.right(12)

turtle.done()

# Part B: QA Bot
print('Question Answering Bot (type bye to exit)')
while True:
    question = input('Ask me something: ').lower()
    if question == 'bye':
        print('Bot: Goodbye!')
        break
    elif 'hku' in question:
        print('Bot: HKU is the University of Hong Kong.')
    elif 'robot' in question:
        print('Bot: A robot is a machine that can perform tasks.')
    elif 'jetson' in question:
        print('Bot: Jetson is a small computer for AI applications.')
    elif 'ai' in question:
        print('Bot: AI means artificial intelligence.')
    elif 'human' in question:
        print('Bot: Humans can think, learn, and create.')
    else:
        print("Bot: Sorry, I don't understand.")
