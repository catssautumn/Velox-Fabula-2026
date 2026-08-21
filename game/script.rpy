# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define n = Character(kind=nvl)
default mc = Character("[povname]")
define at = Character("Atticus", image ="atticus")

default nvl_mode = False

default name_ypos = -0.5


## Story variables
default at_aff = 0
default mentality = 0
default at_knows = False
default helped_atticus = False


label testing:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ nvl_mode = True
    n "Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
    n "Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
    n "Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
    n "Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
    n "Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
    n "Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
    n "Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
    $ nvl_mode = False

    scene forest day
    show atticus eneutral_c 


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

    scene cg1_scared with dissolve:
        zoom 0.5
    at "woah"


    return
