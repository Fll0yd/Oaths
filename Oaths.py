from tkinter import *
from tkinter import messagebox

RAINBOW = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
SPECTRUM = ["Rage", "Greed", "Fear", "Will", "Hope", "Compassion", "Love", "Death", "Life"]

data = {
    "rage": "Red Lanterns: Rage\n[With blood and rage of crimson red, ripped from a corpse so freshly dead, together with our hellish hate, we’ll burn you all–That is your fate!]",
    "greed": "Orange Lantern: Avarice\n[What’s mine is mine and mine and mine. And mine and mine and mine! Not yours!]",
    "fear": "Sinestro Corps: Fear\n[In blackest day, in brightest night, beware your fears made into light, let those who try to stop what’s right, burn like my power!… Sinestro’s might!]",
    "will": "Green Lantern: Willpower\n[In brightest day, in blackest night, no evil shall escape my sight, let those who worship evil’s might, beware my power… Green Lantern’s Light!]",
    "hope": "Blue Lantern: Hope\n[In fearful day, in raging night, with strong hearts full, our souls ignite, when all seems lost in the War of Light, look to the stars– For hope burns bright!]",
    "compassion": "Indigo Tribe: Compassion\n[Tor lorek san, bor nakka mur, natromo faan tornek wot ur, ter lantern ker lo Abin Sur, taan lek lek nok — Formorrow Sur!]",
    "love": "Star Sapphires: Love\n[For hearts long lost and full of fright, for those alone in blackest night, accept our ring and join our fight, love conquers all– With violet light!]",
    "death": "Black Lanterns: Death\n[The Blackest Night falls from the skies, the darkness grows as all light dies, we crave your hearts and your demise, by my black hand–The dead shall rise!]",
    "life": "White Lantern: Life\n[LIVE!]"
}

def print_lantern_oath():
    choice_type = choice_var.get()
    keyword = keyword_var.get().lower()

    if keyword:
        message = data.get(keyword, "Invalid choice. Try again.")
        messagebox.showinfo("Lantern Oath", message)

# Initialize Tkinter
root = Tk()
root.title("Lantern Oath")

# Name Entry
Label(root, text="Enter your name:").grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

# Choice Type
choice_var = StringVar()
choice_var.set("emotion")
Label(root, text="Choose color or emotion:").grid(row=1, column=0)
Radiobutton(root, text="Color", variable=choice_var, value="color").grid(row=1, column=1)
Radiobutton(root, text="Emotion", variable=choice_var, value="emotion").grid(row=1, column=2)

# Keyword Entry
keyword_var = StringVar()
keyword_var.set(RAINBOW[0])  # default
Label(root, text="Choose a keyword:").grid(row=2, column=0)
OptionMenu(root, keyword_var, *(RAINBOW + SPECTRUM)).grid(row=2, column=1)

# Submit button
Button(root, text="Submit", command=print_lantern_oath).grid(row=3, columnspan=2)

root.mainloop()
