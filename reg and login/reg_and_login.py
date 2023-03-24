import string
import random
from tkinter import *
import subprocess

users = {}

aken = Tk()
aken.geometry('550x400')
aken.title('Kasutaja registreerimine ja autoriseerimine')
aken.resizable(False,False)

with open('DataBase.txt', 'r') as i:
    for line in i:
        user, password = line.strip().split(':')
        users[user] = password

def open_file():
    k = Tk()
    k.title("Küsimus")
    k.geometry('1920x1080')
    k.configure(background='#8c8c8c')
    label = Label(k, text="Kas jätkata diskriminant kalkulaatoris?",font='Arial 70',bg='#8c8c8c')
    label.pack()
    def y():
        k.destroy()
        filename2 = "Calc.py"
        subprocess.call(['python', filename2])
    def n():
        k.destroy()

    btn_y = Button(k, text="Jah!", font='Arial 180',bg='lightgreen', command=y)
    btn_y.pack(side="left", padx=90)

    btn_n = Button(k, text="Ei",font='Arial 180',width='5',bg='red',command=n)
    btn_n.pack(side="right", padx=90)

    k.mainloop()

def open_file2():
    k2 = Tk()
    k2.title("Küsimus")
    k2.geometry('1920x1080')
    k2.configure(background='#8c8c8c')
    label = Label(k2, text="Tahad visilica mängida?",font='Arial 70',bg='#8c8c8c')
    label.pack()

    def y2():
        k2.destroy()
        filename = "Visilica.py"
        subprocess.call(['python', filename])
    def n2():
        k2.destroy()

    btn_y = Button(k2, text="Jah!", font='Arial 180',bg='lightgreen', command=y2)
    btn_y.pack(side="left", padx=90)

    btn_n = Button(k2, text="Ei",font='Arial 180',width='5',bg='red',command=n2)
    btn_n.pack(side="right", padx=90)

    k2.mainloop()

def validate_input():
    user = entry_username.get()
    passw = entry_passw.get()
    if not user:
        lbl_status.config(text='Kasutajanimi ei tohi olla tühi.')
        return False
    elif not passw:
        lbl_status.config(text='Salasõna ei tohi olla tühi.')
        return False
    elif len(passw) < 8:
        lbl_status.config(text='Salasõna peab olema vähemalt 8 tähemärki pikk.')
        return False
    elif not any(c.isupper() for c in passw):
        lbl_status.config(text='Salasõna peab sisaldama vähemalt ühte suurtähte.')
        return False
    elif not any(c.islower() for c in passw):
        lbl_status.config(text='Salasõna peab sisaldama vähemalt ühte väiketähte.')
        return False
    elif not any(c.isdigit() for c in passw):
        lbl_status.config(text='Salasõna peab sisaldama vähemalt ühte numbrit.')
        return False
    elif not any(c in string.punctuation for c in passw):
        lbl_status.config(text='Salasõna peab sisaldama vähemalt ühte erimärki.')
        return False
    else:
        lbl_status.config(text='')
        return True

def register():
    if not validate_input():
        return
    user = entry_username.get()
    passw = entry_passw.get()
    if user in users:
        lbl_status.config(text='Kasutajanimi on juba võetud.')
    else:
        users[user] = passw
        with open('DataBase.txt', 'a') as f:
            f.write(f'{user}:{passw}\n')
        lbl_status.config(text='Kasutaja registreerimine õnnestus.')

def login():
    if not validate_input():
        return
    user = entry_username.get()
    passw = entry_passw.get()
    if user not in users:
        lbl_status.config(text='Kasutajanime ei leitud.')
    elif users[user] != passw:
        lbl_status.config(text='Vale salasõna.')
    else:
        lbl_status.config(text='Sisselogimine õnnestus.')
        if user == "max":
            open_file2()
            lbl_status.config(text='Sisselogimine õnnestus.')
        else:
            open_file()
            lbl_status.config(text='Sisselogimine õnnestus.')

def generate_password():
    while True:
        length = 12
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        if (any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in string.punctuation for char in password)):
            entry_passw.delete(0, END)
            entry_passw.insert(0, password)
            break

def recover_password():
    user = entry_username.get()
    if user not in users:
        lbl_status.config(text='Kasutajanime ei leitud.')
    else:
        password = users[user]
        lbl_status.config(text=f'Sinu salasõna on {password}.')

def change_password():
    user = entry_username.get()
    old_passw = entry_passw.get()
    new_passw = entry_passw.get()

    if user not in users:
        lbl_status.config(text='Kasutajanime ei leitud.')
    else:
        users[user] = new_passw
        with open('DataBase.txt', 'w') as f:
            for user, password in users.items():
                f.write(f'{user}:{password}\n')
        lbl_status.config(text='Salasõna muutmine õnnestus.')

lbl_username = Label(aken, text='Kasutajanimi:', font='Arial 14')
lbl_username.pack(pady=8)
entry_username = Entry(aken, font='Arial 14', bg='#cccccc')
entry_username.pack()

lbl_pass = Label(aken, text='Salasõna:', font='Arial 14')
lbl_pass.pack(pady=8)
entry_passw = Entry(aken, show='*', font='Arial 14', bg='#cccccc')
entry_passw.pack()

btn_reg = Button(aken, text='Registreeri', command=register, font='Arial 14')
btn_reg.place(x=160,y=180)
btn_login = Button(aken, text='Logi sisse', command=login, font='Arial 14')
btn_login.place(x=290,y=180)

lbl_status = Label(aken, text='', font='Arial 14', bg='#8c8c8c')
lbl_status.pack(pady=10)

btn_generate = Button(aken, text='Loo parool', command=generate_password, font='Arial 14')
btn_generate.place(x=85,y=250)

btn_recover = Button(aken, text='Taasta parool', command=recover_password, font='Arial 14')
btn_recover.place(x=205,y=250)

btn_change = Button(aken, text='Muuda salasõna', command=change_password, font='Arial 14')
btn_change.place(x=345,y=250)

aken.config(bg='#8c8c8c')
aken.mainloop()
