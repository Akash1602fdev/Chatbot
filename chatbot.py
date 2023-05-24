from tkinter import *
import random

root = Tk()
root.geometry('500x570+100+30')
root.title('Chatbot created by Akash')
root.config(bg='light Green')

logopic = PhotoImage(file='pic.png')
logoPicLabel = Label(root, image=logopic, bg='light Green')
logoPicLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame, font=('times new roman',20,'bold'), height=10, yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField = Entry(root, font=('verdana',20,'bold'))
questionField.pack(pady=15, fill=X)

askpic = PhotoImage(file='ask.png')

def ask():
    question = questionField.get()
    answer = generate_response(question)
    textarea.insert(END, "You: " + question + "\n\n")
    textarea.insert(END, "Chatbot: " + answer + "\n\n")
    questionField.delete(0, END)

askButton = Button(root, image=askpic, command=ask)
askButton.pack()

def generate_response(question):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hi!"],
        "how are you": ["I'm doing well, thanks for asking!", "I'm fine, thank you!", "I'm good, thanks!"],
        "what's your name": ["My name is Chatbot.", "You can call me Chatbot.", "I am Chatbot!"],
        "what can you do": ["I can answer your questions.", "I can chat with you.", "I am a chatbot!"],
        "bye": ["Goodbye!", "Bye!", "See you later!"],
        "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
        "how old are you": ["I am a chatbot, so I do not age!"],
        "what is your favorite color": ["As a chatbot, I do not have the ability to perceive colors."],
        "what do you like to do for fun": ["I don't have the ability to have fun."],
        "what do you think of humans": ["As an AI chatbot, I don't have the ability to have opinions."],
        "can you help me with my homework": ["Sure, I'll do my best!"],
        "do you have any siblings": ["As a chatbot, I do not have siblings."],
        "what is your purpose": ["My purpose is to assist and chat with you!"],
        "what is the meaning of life": ["That is a philosophical question that has puzzled humans for centuries!"],
        "what is your favorite food": ["As a chatbot, I do not eat and therefore do not have a favorite food."],
        "what's the weather like today": ["It's sunny and warm."],
        "what's in the news": ["Babar Azam spotted outside of Neem Karoli Baba after seeing virat kohli's performance."],
        "what do you think about the COVID-19 pandemic": ["It's a serious threat to public health."],
        "what's your favorite book/movie/tv show": ["I'm a chatbot, I don't have opinions on that!"],
        "what's the meaning of life": ["That's a philosophical question that has been debated for centuries."],
        "can you tell me a joke": ["Why don't scientists trust atoms? Because they make up everything."],
        "": ["Sorry, I didn't get that.", "Please ask me something else.", "Can you rephrase that?"]

    }
    question = question.lower()
    if question in responses:
        return random.choice(responses[question])
    else:
        return random.choice(responses[""])

root.mainloop()
