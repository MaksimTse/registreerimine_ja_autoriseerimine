from tkinter import *
import random

mang = Tk()
mang.title('Arva ära Sõna!')

animals = ['tiiger', 'lõvi', 'kaelkirjak', 'elevant', 'ahv', 'zeebra']
drinks = ['kohv', 'tee', 'mahl', 'soda', 'vesi', 'limonaad']
food = ['pitsa', 'hamburger', 'sushi', 'pasta', 'salat', 'võileib']
prog = ['programmeerimine', 'python', 'toimetaja', 'arvuti', 'terminal']
country = ['hispaania', 'hiina', 'eesti', 'saksamaa', 'nigeeria', 'tšili']

word = ''
guesses = ''
mis = 0
max_mis = 5
image_list = []

def close():
    k = Tk()
    k.title("Küsimus")
    k.geometry('1920x1080')
    k.configure(background='#8c8c8c')
    label = Label(k, text="Kas oled kindel, et tahad mängu sulgeda?",font='Arial 60',bg='#8c8c8c')
    label.pack()
    def y():
        k.destroy()
        mang.destroy()
    def n():
        k.destroy()

    btn_y = Button(k, text="Jah!", font='Arial 180',bg='lightgreen', command=y)
    btn_y.pack(side="left", padx=90)

    btn_n = Button(k, text="Ei",font='Arial 180',width='5',bg='red',command=n)
    btn_n.pack(side="right", padx=90)

    k.mainloop()

def choose_animals():
    global word_list
    global word

    new()
        
    word_list = [animals]
    word = random.choice(word_list[0])
    disp_word = ''
    for letter in word:
        disp_word += '_ '
    word_lbl.config(text=disp_word)
        
def choose_drinks():
    global word_list
    global word

    new()
        
    word_list = [drinks]
    word = random.choice(word_list[0])
    disp_word = ''
    for letter in word:
        disp_word += '_ '
    word_lbl.config(text=disp_word)
        
def choose_food():
    global word_list
    global word

    new()
        
    word_list = [food]
    word = random.choice(word_list[0])
    disp_word = ''
    for letter in word:
        disp_word += '_ '
    word_lbl.config(text=disp_word)

def choose_prog():
    global word_list
    global word

    new()
        
    word_list = [prog]
    word = random.choice(word_list[0])
    disp_word = ''
    for letter in word:
        disp_word += '_ '
    word_lbl.config(text=disp_word)

def choose_country():
    global word_list
    global word
        
    new()

    word_list = [country]
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
    mis_lbl.config(text=f'Vead: {mis}/{max_mis}',fg='green')

    guess_entry.delete(0, END)
    result_lbl.config(text='')
    
    tahvel = Canvas(mang, width=300, height=300)
    tahvel.create_image(2, 2, image=image_list[mis], anchor=NW)
    tahvel.grid(row=0, column=2)

def check_guess():
    global word
    global guesses
    global mis
    
    guess = guess_entry.get().lower()
    
    guess_entry.delete(0, END)
    
    if len(guess) != 1:
        result_lbl.config(text='Palun sisestage üks täht.')
    if guess in guesses:
        result_lbl.config(text='Sa juba arvasid seda kirja.') 
    guesses += guess
    
    if guess in word:
        display_word = ''
        for letter in word:
            if letter in guesses:
                display_word += letter + ' '
            else:
                display_word += '_ '
        word_lbl.config(text=display_word)
        
        if '_' not in display_word:
            result_lbl.config(text='Palju õnne! Sa arvasid sõna.',font='Arial 25')
            mis_lbl.config(text=f'Vead: {mis}/{max_mis}',fg='green')
            tahvel = Canvas(mang, width=300, height=300)
            tahvel.create_image(2, 2, image=image_list[mis], anchor=NW)
            tahvel.grid(row=0, column=2)
            
    else:
        mis += 1
        mis_lbl.config(text=f'Vead: {mis}/{max_mis}',fg='red')

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
            result_lbl.config(text=f'Mäng läbi. Sõna oli {word}!.',font='Arial 25')
            mis = 0
            mis_lbl.config(text=f'Vead: {mis}/{max_mis}',fg='red')

f=Frame(mang,bg='#8c8c8c')
f2=Frame(mang,bg='#8c8c8c')

choice_lbl = Label(f2, text='Vali teema!',font='Arial 15',bg='#8c8c8c', fg='#404040')
choice_lbl.pack(pady=10,padx=40)

animals_btn = Button(f2, text='Loomad',bg='#333333',fg='red', command=choose_animals)
animals_btn.pack(pady=10,padx=40)
    
drinks_btn = Button(f2, text='Joogid',bg='#333333',fg='orange', command=choose_drinks)
drinks_btn.pack(pady=10,padx=40)
    
food_btn = Button(f2, text='Toidud',bg='#333333',fg='yellow', command=choose_food)
food_btn.pack(pady=10,padx=40)

drinks_btn = Button(f2, text='Programmeerimine',bg='#333333',fg='lightgreen', command=choose_prog)
drinks_btn.pack(pady=10,padx=40)
    
food_btn = Button(f2, text='Riigid',bg='#333333',fg='lightblue', command=choose_country)
food_btn.pack(pady=10,padx=40)

instructions_lbl = Label(f, text='Arva ära sõna!',font='Arial 24',bg='#8c8c8c', fg='#404040')
instructions_lbl.pack(pady=10)

word_lbl = Label(f, text='',bg='#8c8c8c',font='Arial 18')
word_lbl.pack(pady=10)

guess_entry = Entry(f, width=1,font='Arial 30')
guess_entry.pack(pady=10)

check_btn = Button(f, text='Kontrollima', bg='#d7f7ed',width='18',font='Arial 16',command=check_guess)
check_btn.pack(pady=10)

result_lbl = Label(f, text='',bg='#8c8c8c')
result_lbl.pack(pady=8)

mis_lbl = Label(f, text=f'Vaed: {mis}/{max_mis}',fg='#00bf13',bg='#d4d6d5',width='18',font='Arial 16')
mis_lbl.pack(pady=8)

new_btn = Label(f, bg='#8c8c8c',width='70')
new_btn.pack(pady=5)

check_btn = Button(f2, text='Sule', bg='red',font='Arial 8',command=close)
check_btn.pack(pady=60,padx=30)

f.grid(row=0,column=1)
f2.grid(row=0,column=0)

new()
mang.resizable(False,False)
mang.geometry('1070x400')
mang.configure(background='#8c8c8c')
mang.mainloop()
