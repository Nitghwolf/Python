# Упражнение 20.1
# Напишите программу, переводящую градусы по Фаренгейту в градусы по Цельсию. 

import tkinter

window = tkinter.Tk()
window.title("Конвертация температуры")
window.geometry("320x200+800+200")

def convert():
    grad_data = entry.get()
    grad_data = float(grad_data)
    grad_celc = round(5/9 *(grad_data - 32),3)
    label_celc.config(text=grad_celc)

label = tkinter.Label(window, text = "Temperature in Fahrenheit：", font = ("bold"))
label.pack()

entry = tkinter.Entry(window)
entry.pack()

label_Gr = tkinter.Label(window, text = "Temperature in Celsius：", font = ("bold"))
label_Gr.pack()

label_celc = tkinter.Label(window)
label_celc.pack()

button_convert = tkinter.Button(window, text = "Convert", command = convert)
button_convert.pack()

button_exit = tkinter.Button(window, text = "Exit", command = window.quit)
button_exit.pack()

window.mainloop()