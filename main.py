from tkinter import * 
import random


def submit():
    guess = entry.get().strip()
    if guess.lower() == random_word.lower():
        result_label.config(text="Lol nice")
    else:
        result_label.config(text="Bruh you suck, the word is: " + random_word)
        
def next_word():
    global random_word, sorted_string
    random_word = random.choice(easy_words)
    sorted_string = "".join(sorted(random_word))
    rand_word.config(text=sorted_string)
    entry.delete(0, END)
    result_label.config(text="")
    entry.focus_set()


THEMES = {
    "Peach Coffee": {
        "bg": "#FFE584",
        "fg": "#4B3832",
        "accent": "#7E5A55",
        "entry_bg": "#FFF8E1",
        "button_bg": "#FFDAB9"
    },
    "Mint Meadow": {
        "bg": "#E7F8EE",     # pale mint
        "fg": "#2E4D43",     # forest green text
        "accent": "#569E8A",
        "entry_bg": "#FFFFFF",
        "button_bg": "#C6EDE0"
    },
    "Midnight Lavender": {
        "bg": "#2E2B47",     # deep purple-blue
        "fg": "#EDE9FF",     # soft lavender text
        "accent": "#B59FFF",
        "entry_bg": "#3C385D",
        "button_bg": "#6C5DD3"
    },
    "Sunset Ember": {
        "bg": "#FCE8D4",      # warm sand
        "fg": "#5A2D1C",      # deep ember brown
        "accent": "#D67A36",
        "entry_bg": "#FFF3E6",
        "button_bg": "#F5B67A"
    },
    "Ocean Breeze": {
        "bg": "#DFF6FF",      # pale water blue
        "fg": "#1B3A4B",      # deep navy text
        "accent": "#4A90A4",
        "entry_bg": "#FFFFFF",
        "button_bg": "#B9E6F2"
    },
    "Sleek Monochrome": {
        "bg": "#F2F2F2",      # light grey
        "fg": "#1B1B1B",      # near-black text
        "accent": "#555555",
        "entry_bg": "#FFFFFF",
        "button_bg": "#DDDDDD"
    },
    "Cozy Cabin": {
        "bg": "#F6EFE7",      # cream beige
        "fg": "#3D2B1F",      # deep wood brown
        "accent": "#8C5F3F",
        "entry_bg": "#FFF9F0",
        "button_bg": "#E3C9A6"
    },
    "Cyber Terminal": {
        "bg": "#0A0A0A",      # black
        "fg": "#00FF9F",      # neon mint text
        "accent": "#00B36E",
        "entry_bg": "#1B1B1B",
        "button_bg": "#003B2E"
    },
    "Pastel Sakura": {
        "bg": "#FFEAF4",      # soft cherry blossom pink
        "fg": "#3A2D33",      # plum-brown text
        "accent": "#C06387",
        "entry_bg": "#FFFFFF",
        "button_bg": "#FFD1E3"
    }
}

current_theme = "Peach Coffee"  # default

def apply_theme(theme_name: str):
    """Apply colors to the window and all widgets."""
    global current_theme
    theme = THEMES[theme_name]
    current_theme = theme_name

    window.config(bg=theme["bg"])

    
    for lbl in (title_label, guess_word_label, rand_word, result_label):
        lbl.config(bg=theme["bg"], fg=theme["fg"])

    
    entry.config(bg=theme["entry_bg"], fg=theme["fg"], insertbackground=theme["fg"])

    
    for btn in (submit_button, next_button, change_color):
        btn.config(bg=theme["button_bg"], fg=theme["fg"], activebackground=theme["accent"])



def change_theme():
    """Open a small popup with radio buttons to pick a theme."""
    top = Toplevel(window)
    top.title("Choose Theme")
    # style the popup to match current theme
    theme = THEMES[current_theme]
    top.config(bg=theme["bg"])

    Label(top, text="Select a theme:", bg=theme["bg"], fg=theme["fg"]).pack(padx=12, pady=(12, 6), anchor="w")

    choice = StringVar(value=current_theme)

    # list themes as radio buttons
    radio_frame = Frame(top, bg=theme["bg"])
    radio_frame.pack(padx=12, pady=6, fill="both")
    for name in THEMES.keys():
        Radiobutton(
            radio_frame,
            text=name,
            variable=choice,
            value=name,
            bg=theme["bg"],
            fg=theme["fg"],
            selectcolor=theme["button_bg"],
            activebackground=theme["accent"],
            anchor="w",
            padx=6
        ).pack(fill="x")

    
    btn_row = Frame(top, bg=theme["bg"])
    btn_row.pack(padx=12, pady=(10, 12), fill="x")

    def on_apply():
        apply_theme(choice.get())
        entry.focus_set()
        top.destroy()

    Button(btn_row, text="Apply", command=on_apply, bg=theme["button_bg"], fg=theme["fg"], activebackground=theme["accent"]).pack(side="right", padx=6)
    Button(btn_row, text="Cancel", command=top.destroy, bg=theme["button_bg"], fg=theme["fg"], activebackground=theme["accent"]).pack(side="right")

    # center the popup roughly
    top.geometry("+%d+%d" % (window.winfo_rootx()+60, window.winfo_rooty()+60))
    top.transient(window)   
    top.grab_set()          
    top.focus_force()




window = Tk()
window.title("WORD GUESSR")
window.geometry("600x600")
window.config(background="#FFE5B4")  # will be overridden by apply_theme

with open("words.txt", "r") as f:
    exec(f.read())  

random_word = random.choice(easy_words)
sorted_string = "".join(sorted(random_word))




title_label = Label(window, text="Word Guessr", font=("Segoe Script Bold", 24, "bold"), bg="#FFE5B4", fg="#4B3832")
title_label.pack(pady=20)

guess_word_label = Label(window, text="Guess the word:", font=("Palatino Linotype Bold Italic", 16), bg="#FFE5B4", fg="#4B3832")
guess_word_label.pack(pady=21)

rand_word = Label(window, text=sorted_string, font=("Palatino Linotype Bold Italic", 12), bg="#FFE5B4", fg="#4B3832")
rand_word.pack()

entry = Entry(window, font=("Palatino Linotype Bold Italic", 14), fg="#4B3832", bg="#FFF8E1")
entry.place(relx=0.5, rely=0.7, anchor="center")
entry.focus_set()

result_label = Label(window, text="", bg="#FFE5B4", fg="#4B3832", font=("Palatino Linotype Bold Italic", 14))
result_label.pack(pady=8)

submit_button = Button(window, text="Enter", bg="#FFDAB9", fg="#4B3832", command=submit)
submit_button.place(relx=0.3, rely=0.9, anchor="center")

next_button = Button(window, text="Next Word", bg="#FFDAB9", fg="#4B3832", command=next_word)
next_button.place(relx=0.7, rely=0.9, anchor="center")

change_color = Button(window, text="Change Theme", bg="#FFDA89", fg="#4B3832", command=change_theme)
change_color.place(relx=0.5, rely=0.9, anchor="center")


# apply default theme once so all hard-coded colors get normalized
apply_theme(current_theme)

window.bind("<Return>", lambda e: submit())
window.mainloop()
