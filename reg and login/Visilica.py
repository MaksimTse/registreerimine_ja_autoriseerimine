from tkinter import *
import random

mang = Tk()
mang.title('Arva ära Sõna!')

animals_est = ['tiiger', 'lõvi', 'kaelkirjak', 'elevant', 'ahv', 'zeebra']
drinks_est = ['kohv', 'tee', 'mahl', 'õlut', 'vesi', 'limonaad']
food_est = ['pitsa', 'hamburger', 'sushi', 'pasta', 'salat', 'võileib']
prog_est = ['programmeerimine', 'python', 'toimetaja', 'arvuti', 'terminal']
country_est = ['hispaania', 'hiina', 'eesti', 'saksamaa', 'nigeeria', 'tšili']

animals_rus = ['тигр', 'лев', 'жираф', 'слон', 'обезьяна', 'зебра']
drinks_rus = ['кофе', 'чай', 'сок', 'вода', 'пиво', 'лимонад']
food_rus = ['пицца', 'гамбургер', 'суши', 'макароны', 'салат', 'сэндвич']
prog_rus = ['программирование', 'питон', 'редактор', 'компьютер', 'консоль']
country_rus = ['Испания', 'Китай', 'Эстония', 'Германия', 'Нигерия', 'Чили']

words_est = [animals_est, drinks_est, food_est, prog_est, country_est]
word_list = [words_est]

word = ''
guesses = ''
mis = 0
max_mis = 5
image_list = []

def dark():
    animals_btn.config(bg='#141414')
    drinks_btn.config(bg='#141414')
    food_btn.config(bg='#141414')
    prog_btn.config(bg='#141414')
    country_btn.config(bg='#141414')
    check_btn.config(bg='#141414',fg='#FFFFFF')
    word_lbl.config(bg='#141414',fg='#FFFFFF')
    mis_lbl.config(bg='#141414')
    result_lbl.config(bg='#141414',fg='#FFFFFF')
    instructions_lbl.config(bg='#141414',fg='#FFFFFF')
    choice_lbl.config(bg='#141414',fg='#FFFFFF')
    f.config(bg='#141414')
    f2.config(bg='#141414')
    mang.config(bg='#141414')
    est_btn.config(bg='#141414',fg='#FFFFFF')
    rus_btn.config(bg='#141414',fg='#FFFFFF')
    new_btn.config(bg='#141414')

def light():
    animals_btn.config(bg='#b0b0b0')
    drinks_btn.config(bg='#b0b0b0',fg='#d95a00')
    food_btn.config(bg='#b0b0b0',fg='#d9ce00')
    prog_btn.config(bg='#b0b0b0',fg='green')
    country_btn.config(bg='#b0b0b0',fg='blue')
    check_btn.config(bg='#e3e3e3',fg='#121212')
    word_lbl.config(bg='#e3e3e3',fg='#121212')
    mis_lbl.config(bg='#e3e3e3')
    result_lbl.config(bg='#e3e3e3',fg='#121212')
    instructions_lbl.config(bg='#e3e3e3',fg='#121212')
    choice_lbl.config(bg='#e3e3e3',fg='#121212')
    f.config(bg='#e3e3e3')
    f2.config(bg='#e3e3e3')
    mang.config(bg='#e3e3e3')
    est_btn.config(bg='#e3e3e3',fg='#121212')
    rus_btn.config(bg='#e3e3e3',fg='#121212')
    new_btn.config(bg='#e3e3e3')

def set_language_estonian():
    global word
    global word_list
    global mis
    global max_mis

    new()

    word_list = [animals_est, drinks_est, food_est, prog_est, country_est]
    animals_btn.config(text="Loomad")
    drinks_btn.config(text="Joogid")
    food_btn.config(text="Toit")
    prog_btn.config(text="Programmeerimine")
    country_btn.config(text="Riigid")
    check_btn.config(text="Kontrolli")
    word_lbl.config(text="_ " * len(word))
    mis_lbl.config(text=f'Vead: {mis}/{max_mis}')
    result_lbl.config(text="")
    instructions_lbl.config(text='Arva ära sõna!')
    mang.title('Arva ära Sõna!')
    close_btn.config(text='Sule')
    choice_lbl.config(text='Vali teema!')
    dark_btn.config(text='Tume')
    light_btn.config(text='hele')
    word_list = [words_est]

def set_language_russian():
    global word
    global word_list
    global mis
    global max_mis

    new()

    word_list = [animals_rus, drinks_rus, food_rus, prog_rus, country_rus]
    animals_btn.config(text="Животные")
    drinks_btn.config(text="Напитки")
    food_btn.config(text="Еда")
    prog_btn.config(text="Программирование")
    country_btn.config(text="Страны")
    check_btn.config(text="Проверить")
    word_lbl.config(text="_ " * len(word))
    mis_lbl.config(text=f'Ошибки: {mis}/{max_mis}')
    result_lbl.config(text="")
    instructions_lbl.config(text='Угадай Слово!')
    close_btn.config(text='Закрыть')
    choice_lbl.config(text='Выбери тему!')
    mang.title('Угадай Слово!')
    dark_btn.config(text='Тёмная')
    light_btn.config(text='Светлая')

def close():
    k = Tk()
    k.title("Küsimus")
    k.geometry('1920x1080')
    k.configure(background='#141414')
    if word_list == [words_est]:
        lbl = Label(k, text="Kas oled kindel, et tahad mängu sulgeda?",font='Arial 60',bg='#8c8c8c')
    else:
        lbl = Label(k, text="Вы уверены, что хотите закрыть игру?",font='Arial 60',bg='#8c8c8c')
    lbl.pack()
    def y():
        k.destroy()
        mang.destroy()
    def n():
        k.destroy()

    if word_list == [words_est]:
        btn_y = Button(k, text="Jah", font='Arial 180',bg='lightgreen', command=y)
    else:
        btn_y = Button(k, text="Да", font='Arial 180',bg='lightgreen', command=y)
    btn_y.pack(side="left", padx=90)
    if word_list == [words_est]:
        btn_n = Button(k, text="Ei",font='Arial 180',width='5',bg='red',command=n)
    else:
        btn_n = Button(k, text="Нет",font='Arial 180',width='5',bg='red',command=n)
    btn_n.pack(side="right", padx=90)

    k.mainloop()

def choose_animals():
    global word_list
    global word
    global words_est
    global words_rus

    new()
        
    if word_list == [words_est]:
        word_list = [animals_est]
    else:
        word_list = [animals_rus]

    word = random.choice(word_list[0])
    disp_word = ''
    for letter in word:
        disp_word += '_ '
    word_lbl.config(text=disp_word)
        
def choose_drinks():
    global word_list
    global word
    global words_est
    global words_rus

    new()
        
    if word_list == [words_est]:
        word_list = [drinks_est]
    else:
        word_list = [drinks_rus]

    word = random.choice(word_list[0])
    disp_word = ''
    for letter in word:
        disp_word += '_ '
    word_lbl.config(text=disp_word)
        
def choose_food():
    global word_list
    global word
    global words_est
    global words_rus

    new()
        
    if word_list == [words_est]:
        word_list = [food_est]
    else:
        word_list = [food_rus]
        
    word = random.choice(word_list[0])
    disp_word = ''
    for letter in word:
        disp_word += '_ '
    word_lbl.config(text=disp_word)

def choose_prog():
    global word_list
    global word
    global words_est
    global words_rus

    new()
        
    if word_list == [words_est]:
        word_list = [prog_est]
    else:
        word_list = [prog_rus]

    word = random.choice(word_list[0])
    disp_word = ''
    for letter in word:
        disp_word += '_ '
    word_lbl.config(text=disp_word)

def choose_country():
    global word_list
    global word
    global words_est
    global words_rus

    new()
        
    if word_list == [words_est]:
        word_list = [country_est]
    else:
        word_list = [country_rus]

    word = random.choice(word_list[0])
    disp_word = ''
    for letter in word:
        disp_word += '_ '
    word_lbl.config(text=disp_word)

for img_file in ['vis6.png','vis1.png', 'vis2.png', 'vis3.png', 'vis4.png', 'vis5.png']:
    img = PhotoImage(file=img_file)
    image_list.append(img)

def new():
    global word
    global guesses
    global mis
    global word_list

    word = ''
    guesses = ''
    mis = 0
    if word_list == [words_est]:
            mis_lbl.config(text=f'Vead: {mis}/{max_mis}',fg='green')
    else:
        mis_lbl.config(text=f'Ошибки: {mis}/{max_mis}',fg='green')

    guess_entry.delete(0, END)
    result_lbl.config(text='')
    
    tahvel = Canvas(mang, width=300, height=300)
    tahvel.create_image(2, 2, image=image_list[mis], anchor=NW)
    tahvel.grid(row=0, column=2)

def check_guess():
    global word
    global guesses
    global mis
    global word_list
    
    guess = guess_entry.get().lower()
    
    guess_entry.delete(0, END)
    
    result_lbl.config(text='')

    if len(guess) != 1:
        if word_list == [words_est]:
            result_lbl.config(text='Palun sisestage üks täht.')
        else:
            result_lbl.config(text='Пожалуйста, введите одну букву.')
    else:
        if guess in guesses:
            if word_list == [words_est]:
                result_lbl.config(text='Sa juba sisenenud seda täht.')
            else:
                result_lbl.config(text='Вы уже вводили эту букву.')
        else:
            guesses += guess
            if guess not in word:
                if word_list == [words_est]:
                    result_lbl.config(text='See täht ei ole sõnas.')
                else:
                    result_lbl.config(text='Эта буква не в слове.')
    
    if guess in word:
        display_word = ''
        for letter in word:
            if letter in guesses:
                display_word += letter + ' '
            else:
                display_word += '_ '
        word_lbl.config(text=display_word)
        
        if '_' not in display_word:
            if word_list == [words_est]:
                result_lbl.config(text='Palju õnne! Sa arvasid sõna.',font='Arial 25')
            else:
                result_lbl.config(text='Поздравляем! Вы угадали слово.',font='Arial 22')
            if word_list == [words_est]:
                mis_lbl.config(text=f'Vead: {mis}/{max_mis}',fg='green')
            else:
                mis_lbl.config(text=f'Ошибки: {mis}/{max_mis}',fg='green')
            tahvel = Canvas(mang, width=300, height=300)
            tahvel.create_image(2, 2, image=image_list[mis], anchor=NW)
            tahvel.grid(row=0, column=2)
            
    else:
        mis += 1
        if word_list == [words_est]:
            mis_lbl.config(text=f'Vead: {mis}/{max_mis}',fg='red')
        else:
            mis_lbl.config(text=f'Ошибки: {mis}/{max_mis}',fg='red')

        if mis == 1:
            tahvel = Canvas(mang, width=300, height=300)
            tahvel.create_image(2, 2, image=image_list[mis], anchor=NW)
            tahvel.grid(row=0, column=2)
        elif mis == 2:
            tahvel = Canvas(mang, width=300, height=300)
            tahvel.create_image(2, 2, image=image_list[mis], anchor=NW)
            tahvel.grid(row=0, column=2)
        elif mis == 3:
            tahvel = Canvas(mang, width=300, height=300)
            tahvel.create_image(2, 2, image=image_list[mis], anchor=NW)
            tahvel.grid(row=0, column=2)
        elif mis == 4:
            tahvel = Canvas(mang, width=300, height=300)
            tahvel.create_image(2, 2, image=image_list[mis], anchor=NW)
            tahvel.grid(row=0, column=2)
        elif mis == 5:
            tahvel = Canvas(mang, width=300, height=300)
            tahvel.create_image(2, 2, image=image_list[mis], anchor=NW)
            tahvel.grid(row=0, column=2)
        
        if mis >= max_mis:
            if word_list == [words_est]:
                result_lbl.config(text=f'Mäng läbi. Sõna oli {word}!.',font='Arial 25')
            else:
                result_lbl.config(text=f'Игра закончена. Слово было {word}!.',font='Arial 22')
            mis = 0
            if word_list == [words_est]:
                mis_lbl.config(text=f'Vead: {mis}/{max_mis}',fg='red')
            else:
                mis_lbl.config(text=f'Ошибки: {mis}/{max_mis}',fg='red')

f=Frame(mang,bg='#141414')
f2=Frame(mang,bg='#141414')

choice_lbl = Label(f2, text='Vali teema!',font='Arial 15',bg='#141414', fg='#FFFFFF')
choice_lbl.pack(pady=10,padx=40)

animals_btn = Button(f2, text='Loomad',bg='#141414',fg='red', command=choose_animals)
animals_btn.pack(pady=10,padx=40)
    
drinks_btn = Button(f2, text='Joogid',bg='#141414',fg='orange', command=choose_drinks)
drinks_btn.pack(pady=10,padx=40)
    
food_btn = Button(f2, text='Toit',bg='#141414',fg='yellow', command=choose_food)
food_btn.pack(pady=10,padx=40)

prog_btn = Button(f2, text='Programmeerimine',bg='#141414',fg='lightgreen', command=choose_prog)
prog_btn.pack(pady=10,padx=40)
    
country_btn = Button(f2, text='Riigid',bg='#141414',fg='lightblue', command=choose_country)
country_btn.pack(pady=10,padx=40)

instructions_lbl = Label(f, text='Arva ära sõna!',font='Arial 24',bg='#141414', fg='#FFFFFF')
instructions_lbl.pack(pady=32)

word_lbl = Label(f, text='',bg='#141414',fg='#FFFFFF',font='Arial 18')
word_lbl.pack(pady=10)

guess_entry = Entry(f, width=1,font='Arial 30')
guess_entry.pack(pady=10)

check_btn = Button(f, text='Kontrolli',bg='#141414',fg='#FFFFFF',width='18',font='Arial 16',command=check_guess)
check_btn.pack(pady=10)

result_lbl = Label(f, text='',bg='#141414', fg='#FFFFFF')
result_lbl.pack(pady=8)

mis_lbl = Label(f, text=f'Vaed: {mis}/{max_mis}',bg='#141414', fg='#FFFFFF',width='18',font='Arial 16')
mis_lbl.pack(pady=8)

new_btn = Label(f, bg="#141414",width='70')
new_btn.pack(pady=5)

close_btn = Button(f2, text='Sule', bg='red',font='Arial 8',command=close)
close_btn.pack(pady=60,padx=25)

light_btn = Button(f2, text="Hele",bg='#e3e3e3',fg='#121212',command=light)
light_btn.place(y=290, x=34)

dark_btn = Button(f2, text="Tume",bg='#141414',fg='#FFFFFF',command=dark)
dark_btn.place(y=290, x=125)

rus_btn = Button(f, text="На русском",bg='#141414',fg='#FFFFFF',command=set_language_russian)
rus_btn.place(x=160)

est_btn = Button(f, text="Eesti keeles",bg='#141414',fg='#FFFFFF',command=set_language_estonian)
est_btn.place(x=270)

f.grid(row=0,column=1)
f2.grid(row=0,column=0)

new()
mang.resizable(False,False)
mang.geometry('1070x400')
mang.configure(background='#141414')
mang.mainloop()
