# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    show screen flower_frame()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene forest day
    show atticus 

    # These display lines of dialogue.

    python:
        povname = renpy.input("What is your name?", default = "Rowan", length=9,)

        povname = povname.strip()

        if not povname:
            povname = "Rowan"

    menu:
        "What are your pronouns?"
        "They/them":
            $ pronoun = "they/them"
        "She/her":
            $ pronoun = "she/her"
        "He/him":
            $ pronoun = "he/him"

    "Autumn" "[povname] shined brightly in [their] last movie, {i}Indiana Bones{/i}. But compared to Valen, I wonder if [they_re] falling behind?"

    return
