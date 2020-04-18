from tkinter import *


def main():

    languages=["Python","JavaScript", "C#","Java", "C/C++", "Swift", "PHP",
               "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go", "Lua", "Typescript", "T-SQL"]

    # удаление выделенного элемента
    def delete():
        selection=lang_listbox.curselection()
        # мы можем получить удаляемый элемент по индексу
        # selected_language = languages_listbox.get(selection[0])
        lang_listbox.delete(selection[0])


    # добавление нового элемента
    def add():
        new_language=lang_entry.get()
        lang_listbox.insert(0, new_language)

    root = Tk()
    root.title("Listbox")
    root.geometry("333x220+850+650")
    root.config(bg="#acb2a8")

    # текстовое поле и кнопка для добавления в список
    lang_entry=Entry(root, width=40)
    lang_entry.grid(column=0, row=0, padx=6, pady=6)
    add_button=Button(root, text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)

    # scrollbar=Scrollbar(root)
    # scrollbar.pack(side=RIGHT, fill=Y)

    # создаем список
    lang_listbox=Listbox(root, bg="#cceeb1", bd=2, height=8, selectbackground="#4ab0d2",
                         selectmode=EXTENDED #сколько элементов могут быть выделены
    )

    # for language in languages:
        # lang_listbox.insert(END, language)


    lang_listbox.grid(row = 1, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)
    # scrollbar.config(command=lang_listbox.yview)

    # добавляем в список начальные элементы
    lang_listbox.insert(END, "Python")
    lang_listbox.insert(END, "Java")

    delete_button=Button(root, text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)



    root.mainloop()

if __name__ == "__main__":
    main()