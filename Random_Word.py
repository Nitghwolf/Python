from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Угадай слово")
root.geometry("450x200+700+200")

def check():
    """ Проверяет загаданое программой слово с тем, что ввёл пользователь. """
    if str(textinput.get()) == str(word):
        master = Tk()
        master.geometry("200x100+700+200")
        message = Message(master, text = "Вы угадали!!!")
        message.pack()
        master.mainloop()
    else:
        master = Tk()
        master.geometry("200x100+700+200")
        message = Message(master, text=("Вы не угадали((("))
        message.pack()

        master.mainloop()



def random_word(L):
    """Создаёт список слов и выбирает одно рандомно """
    random.shuffle(L)
    randomWord = str(random.choice(L))
    return randomWord


label_01 = Label(root, text = "Программа загадала одно слова из списка:", font = ("Courier", 14, "bold italic"))
label_01.grid(row = 0, column = 0, sticky = W, columnspan = 10)

L = ["Дом", "Кровать", "Сон", "Гора", "Престиж", "Корова", "Пить", "Снег", "Весна", "Мир"]

word = random_word(L)
print(word)

label_words = Label(root, text = L)
label_words.grid(row = 1, column = 0, sticky = W, columnspan = 10)


label_entry = Label(root, text = "Ответ: ", font = 12)
label_entry.grid(row = 2, column = 0, sticky = W)
textinput = StringVar()
textinput.set("0")
entry = Entry(root, width = 30, textvariable = textinput)
entry.grid(row = 2, column = 1, sticky = W, columnspan = 15)


button = Button(root, text = "Проверить", width = 20, font = 14, command = check)
button.grid(row = 4, column = 1, sticky = W, columnspan = 4)


root.mainloop()
