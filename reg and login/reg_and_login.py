import string
import random
import tkinter as tk

users = {'admin': 'password'}

def change_password():
    username = entry_username.get()
    old_password = entry_password.get()
    new_password = entry_password.get()

    if username not in users:
        label_status.config(text='Kasutajanime ei leitud.')
    elif users[username] != old_password:
        label_status.config(text='Vale salasõna.')
    else:
        users[username] = new_password
        label_status.config(text='Salasõna muutmine õnnestus.')

def validate_input():
    username = entry_username.get()
    password = entry_password.get()
    if not username:
        label_status.config(text='Kasutajanimi ei tohi olla tühi.')
        return False
    elif not password:
        label_status.config(text='Parool ei tohi olla tühi.')
        return False
    else:
        label_status.config(text='')
        return True

def register():
    if not validate_input():
        return
    username = entry_username.get()
    password = entry_password.get()
    if username in users:
        label_status.config(text='Kasutajanimi on juba võetud.')
    else:
        users[username] = password
        label_status.config(text='Kasutaja registreerimine õnnestus.')

def login():
    if not validate_input():
        return
    username = entry_username.get()
    password = entry_password.get()
    if username not in users:
        label_status.config(text='Kasutajanime ei leitud.')
    elif users[username] != password:
        label_status.config(text='Vale salasõna.')
    else:
        label_status.config(text='Sisselogimine õnnestus.')

def generate_password():
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def recover_password():
    username = entry_username.get()
    if username not in users:
        label_status.config(text='Kasutajanime ei leitud.')
    else:
        password = users[username]
        label_status.config(text=f'Sinu parool on {password}.')

def change_password():

    if not validate_input():
        return
    username = entry_username.get()
    password = entry_password.get()
    if username not in users:
        label_status.config(text='Kasutajanime ei leitud.')
    else:
        users[username] = password
        label_status.config(text='Salasõna muutmine õnnestus.')


root = tk.Tk()
root.geometry('400x600')
root.title('Kasutaja registreerimine ja autoriseerimine')

label_username = tk.Label(root, text='Kasutajanimi:', font=('Arial', 14))
label_username.pack()
entry_username = tk.Entry(root, font=('Arial', 14))
entry_username.pack()

label_password = tk.Label(root, text='Salasõna:', font=('Arial', 14))
label_password.pack()
entry_password = tk.Entry(root, show='*', font=('Arial', 14))
entry_password.pack()

button_register = tk.Button(root, text='Registreeri', command=register, font=('Arial', 14))
button_register.pack(pady=10)
button_login = tk.Button(root, text='Logi sisse', command=login, font=('Arial', 14))
button_login.pack()

label_status = tk.Label(root, text='', font=('Arial', 14))
label_status.pack(pady=10)

button_generate = tk.Button(root, text='Loo parool', command=generate_password, font=('Arial', 14))
button_generate.pack(pady=10)

button_recover = tk.Button(root, text='Taasta parool', command=recover_password, font=('Arial', 14))
button_recover.pack(pady=10)

button_change = tk.Button(root, text='Muuda salasõna', command=change_password, font=('Arial', 14))
button_change.pack(pady=10)


root.mainloop()
