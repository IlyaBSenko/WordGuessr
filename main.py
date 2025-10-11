from tkinter import * 
import random

def submit():
    guess = entry.get().strip()
    if guess.lower() == random_word.lower():
        result_label.config(text="Lol nice", fg="#4B3832") 
    else:
        result_label.config(text="Wrong, die", fg="#4B3832")  
        
def next_word():
    global random_word
    random_word = random.choice(easy_words)
    sorted_word = sorted(random_word)
    global sorted_string 
    sorted_string = "".join(sorted_word)
    rand_word.config(text=sorted_string)
    
    entry.delete(0, END)
    result_label.config(text="")
    entry.focus_set()
    
    

window = Tk()
window.title("WORD GUESSR")
window.geometry("600x600")
window.config(background="#FFE5B4")  # light peach background

with open("words.txt", "r") as f:
    exec(f.read()) # executive mode cmon now (Top Dogs Only)
    
random_word = random.choice(easy_words) # select a random word from the list
sorted_word = sorted(random_word)
sorted_string = "".join(sorted_word)

# GUI ELEMENTS
title_label = Label(window, text="Word Guessr", font=("Segoe Script Bold", 24, "bold"), bg="#FFE5B4", fg="#4B3832")  # peach & brown palette
title_label.pack(pady=20)

guess_word_label = Label(window, text="Guess the word:", font=("Palatino Linotype Bold Italic", 16), bg="#FFE5B4", fg="#4B3832")
guess_word_label.pack(pady=21)

rand_word = Label(window, text=sorted_string, font=("Palatino Linotype Bold Italic", 12), bg="#FFE5B4", fg="#4B3832")
rand_word.pack()

entry = Entry(window, font=("Palatino Linotype Bold Italic", 14), fg="#4B3832", bg="#FFF8E1")  # brown text on soft cream background
entry.place(relx=0.5, rely=0.7, anchor="center") 
entry.focus_set() # clutch lets you start typing immediately without needing to click the box first

result_label = Label(window, text="", bg="#FFE5B4", fg="#4B3832", font=("Palatino Linotype Bold Italic", 14))
result_label.pack(pady=8)

submit_button = Button(window, text="Enter", bg="#FFDAB9", fg="#4B3832", command=submit)  # peach button
submit_button.place(relx=0.3, rely=0.9, anchor="center")

next_button = Button(window, text="Next Word", bg="#FFDAB9", fg="#4B3832", command=next_word)  # matching peach button
next_button.place(relx=0.7, rely=0.9, anchor="center")

change_color = Button(window, text="Change Theme", bg="#FFDA89", fg="#4B3832", command=change_color)
change_color.place(relx=0.5, rely=0.9, anchor="center")

window.bind("<Return>", lambda e: submit()) # connects keyboard enter button to submit button, clutch

window.mainloop()
