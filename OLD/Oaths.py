RAINBOW = "\n Red \n Orange \n Yellow \n Green \n Blue \n Indigo \n Violet"
SPECTRUM = "\n Rage \n Greed \n Fear \n Will \n Hope \n Compassion \n Love \n Death \n Life"

def get_input(prompt):
    return input(prompt).strip().lower()

def print_lantern_oath(data, keyword):
    print(data.get(keyword, "Invalid choice. Try again."))

def main():
    name = get_input("What is your name?\n")
    choice_type = get_input(f"\nWould you like to start by choosing a color or an emotion, {name.capitalize()}?\n\n")

    data = {
        "rage": """Red Lanterns: Rage
                    "With blood and rage of crimson red, 
                    Ripped from a corpse so freshly dead, 
                    Together with our hellish hate, 
                    We’ll burn you all–That is your fate! """,
        
        "greed": """Orange Lantern: Avarice
                    "What’s mine is mine and mine and mine. 
                    And mine and mine and mine! 
                    Not yours! """,

        "fear": """Sinestro Corps: Fear
                    "In blackest day, in brightest night, 
                    Beware your fears made into light, 
                    Let those who try to stop what’s right, 
                    Burn like my power!… Sinestro’s might!""",

        "will": """Green Lantern: Willpower
                   "In brightest day, in blackest night, 
                    No evil shall escape my sight,
                    Let those who worship evil’s might, 
                    Beware my power… Green Lantern’s Light! """,

        "hope": """Blue Lantern: Hope
                    "In fearful day, in raging night, 
                    With strong hearts full, our souls ignite, 
                    When all seems lost in the War of Light, 
                    Look to the stars– For hope burns bright!""",
       
        "compassion": """Indigo Tribe: Compassion
                    "Tor lorek san, bor nakka mur, 
                    Natromo faan tornek wot ur, 
                    Ter lantern ker lo Abin Sur, 
                    Taan lek lek nok — Formorrow Sur! """,
        
        "love": """Star Sapphires: Love
                    "For hearts long lost and full of fright, 
                    For those alone in blackest night, 
                    Accept our ring and join our fight, 
                    Love conquers all– With violet light!""",
        
        "death": """Black Lanterns: Death
                    "The Blackest Night falls from the skies, 
                    The darkness grows as all light dies, 
                    We crave your hearts and your demise, 
                    By my black hand–The dead shall rise! """,
        
        "life": """White Lantern: Life
                    "LIVE. """
    }

    prompt = f"Ok, so what's the strongest emotion you are feeling today, {name.capitalize()}?"
    if choice_type == "emotion":
        keyword = get_input(f"{prompt} \n{SPECTRUM}\n")
    elif choice_type == "color":
        keyword = get_input(f"\nOk then, please choose a color from the emotional spectrum below \n{RAINBOW}")
    else:
        print("Invalid choice. Try again.")
        return

    print_lantern_oath(data, keyword)

if __name__ == '__main__':
    main()
