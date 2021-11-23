def ввод():
    кнопка_начать.pack_forget()
    группа_ввода.pack()
    кнопка_готово.pack()

def проверка():
    try:
        float(ввод_веса.get())
        float(ввод_роста.get())
        вывод()
        return True
    except ValueError:
        messagebox.showinfo('Fatal ERROR', 'Число?')
        return False

def вывод():
    имт = float(ввод_веса.get())/float(ввод_роста.get())**2
    if имт < 18.5:
        вывод = "Недостаток веса"
    elif  18.5 < имт < 25:
        вывод = "Нормальный вес"
    elif 25 < имт < 30:
        вывод = "Избыточный вес"
    elif 30 < имт < 35:
        вывод = "Ожирение 1-й степени"
    elif 35 < имт < 40:
        вывод = "Ожирение 2-й степени"
    elif имт > 40:
        вывод = "Ожирение 3-й степени"
    else:
        вывод = "Неопределённый вывод. Я без понятия как такое вышло"
    вывод = Label(окно, bg="black", fg="white", text="Поздравляю! У вас:\n" + вывод + ".")
    вывод.pack()

from tkinter import *
from tkinter import messagebox
from datetime import *
now = date.today()

окно = Tk()
окно["bg"] = "black"
предупреждение = Label(окно, bg="black", fg="white", text="Чтобы закрыть окно нажмите комбинацию клавишь Alt + F4")
предупреждение.pack()
тд = Label(окно, bg="black", fg="white", text="Текущая дата:")
тд.pack()
дмгчм = Label(окно, bg="black", fg="white", text=now.today())
дмгчм.pack()
кнопка_начать = Button(окно, text="Начать", bg="black", fg="white", command=ввод)
кнопка_начать.pack(expand=True, fill=BOTH)

группа_ввода = Frame(relief=SUNKEN, bg="black")
группа_ввода.pack_forget()

требование_веса = Label(master=группа_ввода, bg="black", fg="white", text="Вес (кг):")
требование_веса.grid(row=0, column=0, sticky="e")
ввод_веса = Entry(master=группа_ввода)
ввод_веса.grid(row=0, column=1, columnspan=3)
требование_роста = Label(master=группа_ввода, bg="black", fg="white", text="Рост (м):")
требование_роста.grid(row=1, column=0, sticky="e")
ввод_роста = Entry(master=группа_ввода)
ввод_роста.grid(row=1, column=1, columnspan=3)



кнопка_готово = Button(окно, text="Готово", bg="black", fg="white", command=проверка)
кнопка_готово.pack_forget()

окно.mainloop()