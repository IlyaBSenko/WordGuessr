from tkinter import * 
import random

def submit():
    guess = entry.get().strip()
    if guess.lower() == random_word.lower():
        result_label.config(text="Lol nice", fg="black")
    else:
        result_label.config(text="Wrong, die", fg="black")
        
def next():
    global random_word
    random_word = random.choice(easy_words)
    sorted_word = sorted(random_word)
    sorted_string = "".join(sorted_word)
    rand_word.config(text=sorted_string)
    
    entry.delete(0, END)
    result_label.config(text="")
    entry.focus_set()
    
    

window = Tk()
window.title("WORD GUESSR")
window.geometry("600x600")
window.config(background="#F7DCEC")

with open("words.txt", "r") as f:
    exec(f.read()) # executive mode cmon now (Top Dogs Only)
    
random_word = random.choice(easy_words) # select a random word from the list
sorted_word = sorted(random_word)
sorted_string = "".join(sorted_word)


# GUI ELEMENTS
title_label = Label(window, text="Word Guessr", font=("Segoe Script Bold", 24, "bold"), bg="#F7DCEC", fg="black")
title_label.pack(pady=20)

guess_word_label = Label(window, text="Guess the word:", font=("Palatino Linotype Bold Italic", 16), bg="#F7DCEC", fg="black")
guess_word_label.pack(pady=21)

rand_word = Label(window, text=sorted_string, font=("Palatino Linotype Bold Italic", 12), bg="#F7DCEC", fg="black")
rand_word.pack()

entry = Entry(window, font=("Palatino Linotype Bold Italic", 14), fg="black")
entry.place(relx=0.5, rely=0.7, anchor="center") 
entry.focus_set() # clutch lets you start typing immediately without needing to click the box first

result_label = Label(window, text="", bg="#F7DCEC", fg="white", font=("Palatino Linotype Bold Italic", 14))
result_label.pack(pady=8)

submit_button = Button(window, text="Enter", command=submit)
submit_button.place(relx=0.3, rely=0.9, anchor="center")

next_button = Button(window, text="Next Word", bg="#F7DCEC", fg="black", command=next)
next_button.place(relx=0.7, rely=0.9, anchor="center")

window.bind("<Return>", lambda e: submit()) # connects keyboard enter button to submit button, clutch

window.mainloop()