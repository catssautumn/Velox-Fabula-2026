label scene_2:
    scene blackout with dissolve
    nvl clear
    $ nvl_mode = True
    n "..."
    n "There's heat on all sides."
    n "I open my eyes and see it - the great red dragon I once saved the kingdom from, alive and bellowing once more."
    n "Its wings fill the sky, whatever sunlight that once streamed onto the streets below now blotted out in terrifying shadow."
    nvl clear
    n "It roars - and the ground shakes. The villagers cry, sprinting from their homes, holding onto their children and running for their lives."
    n "A great spout of fire flies from its mouth and the nearby houses are burned to cinders in a matter of moments. It circles the sky, wretched eyes circling for another catastrophe to cause."
    $ nvl_mode = False
    menu:
        "Protect the kingdom.":
            pass

    $ nvl_mode = True
    nvl clear 
    n "I have faced this once before. I will face it again, as many times as needed to keep the people safe."
    n "As a burning, boiling hatred crawls up my throat, I reach for my sword by my side-"
    n "And find nothing but the fabric of my tunic."
    n "I look down - there is no trusty blade to be seen. I look around for any glint, any weapon, any sign for it. The anger turns to a white hot fear."
    n "As I look up once more-"
    n "There is no more village. No more buildings or families, no cries. I am in empty space, facing down the dragon."
    n "It ceases its destruction. It bends its head down, a low breath warming the air."
    n "Its eyes are watching me without any sense of attack. Is it… intrigued? Playing a game?"
    n "No, it's waiting for what I'll do next…"
    $ nvl_mode = False
    nvl clear
    "..."
    "I wake up on a cot."
    "Well, it certainly feels like one. Soft underneath my back, a far cry from the grass."
    hide window
    show layer screens:
        matrixcolor None
    scene interior day with dissolve:
        zoom 0.5 align (0.5, 0.5)
    play ambience fireplace fadein 0.5
    window auto show
    "..."
    "I open my eyes to see that I am in a home I do not recognise. It is far cozier than my meagre shelter - walls, a table and chair, shelves with various trinkets…"
    "It even smells good - like fresh flowers from the river banks."
    "My belongings - my pack and my sword - are at the end of the bed, resting upon a small table."
    "With their back to me, a figure works by the hearth. They are dreadfully quiet, the knock of a spoon against a bowl barely audible."

    menu:
        "Reach for my sword.":
            # Atticus affection down    
            $ sub_aff(1)
            "Whether or not they have good intentions with me, it is better to be wary of any stranger."
            "It is only at the foot of the bed. If I am calm and quick enough, I can prepare myself-"
            mc "Ah!" with hpunch
            "As I attempt to sit up, a pain slices through my side, hot and sudden."
            "I fall back onto the bedsheets as the figure snaps their head over."
            show atticus bshocked up eshocked msad_o with dissolve
            play music main_theme fadein 0.5 
            "Unicorn" "Oh, please be careful!"
            "They couldn't help but notice my hand, still stretched out for my sword, and stood a distance away from me. Their eyes watched me cautiously."
        "Try to stand up.":
            # Atticus affection up
            $ add_aff(1)
            "I try to stand, but as I do-"
            mc "Ah!" with hpunch
            "A great pain slices through my side, hot and sudden."
            "I fall back onto the bedsheets as the figure snaps their head over."
            show atticus bshocked up eshocked msad_o with dissolve
            play music main_theme fadein 0.5 
            "Unicorn" "Oh, please be careful!"
            "They stand up and start to come towards me, eyes big and worried."

    "Their eyes…"
    show atticus eneutral_o mid
    "Such a bright purple, almost piercing. And his ears - large and soft like a deer's, the same fluffy white as his mane of hair."
    "The tail, thin and tufted with that same white at the end, wrapping around his thigh almost nervously…"
    "And that horn! It's crooked, almost as if it were as shy as the man himself, but it looks so sharp."
    "It must be the same man - no, unicorn - who I saw earlier in the trap."
    "Aside from the obvious features though, he looks like an entirely different person from the poor creature in the net."
    "His hair is bright and fluffy, no longer frazzled from fear. His eyes no longer have that animalistic fear in them, but a keen kindness that is still visible behind the glint of his glasses."
    "He tilts his head as he looks at me. His fingers drum against a small wooden bowl in his hands."
    show atticus bsad msmile_o
    "Unicorn" "Um… hi!"
    "Unicorn" "How are you feeling?"
    mc "Uh…{w} rough."
    "He laughs - very prettily. Delicate, much like his stature."
    show atticus bneutral msmile_c with dissolve:
        zoom 1.1 yalign 0.4
    "He moves closer, sitting at the edge of the bed."
    "Unicorn" "I'm just going to apply this salve to your side, I won't be a moment…"

    menu:
        "\"You're really pretty.\"":
            $ add_aff(1)
            $ blush_heavy = True
            show atticus bshocked up eshocked mshocked:
                linear .1 yoffset 20
                linear .1 yoffset -20
                linear .1 yoffset 0 
            "He starts - his back straightens, his ears suddenly pointing straight out. I must have surprised him."
            "To be fair, I don't think I'm totally in my right mind. I'll blame the pain."
            mc "I'm so sorry, I didn't-"
            $ blush_heavy = False
            $ blush_light = True
            show atticus bsad eneutral_o msmile_o tloop
            "Unicorn" "Ah, no! You're, um - haha, you're fine!"
            show atticus eneutral_la
            "Unicorn" "It's just not every day that a stranger you took into your bed tells you you're pretty."
            $ blush_heavy = True
            $ blush_light = False
            show atticus bshocked eshocked msad_o tneutral
            "His face turns bright red, and his tail thumps against the bedsheets."
            show atticus bsad esad down
            "Unicorn" "Oh, goodness, that sounds completely inappropriate. I just took you in so you could heal-"
            mc "I understand. This is an… unusual circumstance."
            at bsad ehappy_c msmile_c "I'm Atticus! I really ought to have begun with that."
            mc "I'm [povname]."
            at "Lovely to meet you! Well… lovely to know your name."

        "\"Who are you?\"":
            "He pauses, then abruptly laughs."
            "Unicorn" "I forgot we haven't made introductions! My sincere apologies for doing things in an unusual order."
            mc "It's understandable. Neither of us were in a particularly usual state when we met."
            at "I am Atticus. And you?"
            mc "[povname]."
            at "A pleasure to finally know your name, [povname]!"

        "Pull back from his touch.":
            $ sub_aff(1)
            "I can't help it. I am in pain and in a house that is not my own - I would much rather know my situation before accepting any stranger's help."
            "His ears flatten against his head, and his face falls."
            "Unicorn" "My apologies, I… this is a poultice to help with the wound. I don't want it getting infected."
            "He holds the bowl out to me and lets me take a sniff."
            "It certainly smells medicinal. I sigh."
            mc "My apologies…"
            mc "I don't know your name."
            "His frown melts into a small smile."
            at "I am Atticus. And… who are you?"
            mc "I am [povname], a knight."
            at "[povname]. Lovely to meet you. May I now apply the salve?"
            mc "Yes."
            at "Thank you."

    "Atticus dips his hands into the bowl, coating his fingers in a thick, amber salve."
    "His hands are gentle as they soothe the tincture against my wound, although I still occasionally hiss in pain."
    "I want to ask Atticus so many questions - how he was caught, how he escaped, how he brought me here…"
    "What the deal is with his horn, ears and tail."
    "But his ears twitch in concentration, his tail flicking side to side in a steady routine. Given that he is currently disinfecting my wound, I would rather not distract him."
    "..."
    "Once he finishes, he bandages my ribs up tightly and gives me a quick, nervous smile."
    at "All done!"
    "I wait for him to say something more: an explanation of what happened, perhaps. Or maybe just where exactly I am."
    "Instead, he goes over to the tables at the far end of the room, sets the bowl down and picks up another."
    at "I made some vegetable stew for you. Try and eat as much as you can - you took a nasty wound, and I want to make sure you recover well."
    mc "Thank you, Atticus."

    if at_aff >= 3: 
        "He smiles softly at me, his cheeks turning tawny."

    at "I…"
    "He glances down at my ribs for just a moment."
    at "I won't keep you here. But you ought to stay here for the next few days at least, just until you recover."
    at "It may be weeks before you'll be back to normal."
    "Well, there were worse places to be. In my rainy shelter, alone and in pain… with the poacher's mocking and jeering laughter…"
    "Hanging in a net."
    mc "That's alright. I'll… I'll stay."
    "Atticus lets out a long sigh, his shoulders finally relaxing. He opens his mouth as if to say something-"
    "And then turns away, picking up a basket from the table."
    at "I'll be out until nightfall. But don't worry - you'll be perfectly safe here."
    mc "Wait, Atticus-?"
    "The door closes behind him and I am left alone in his cottage."
    "..."
    "What was I meant to do now?"
    "I can see the whole space from the bed, although when I try once more to stand and look around-"
    mc "Ngh!"
    "I collapse back down onto my bed, breathing in as hard as I can against the bandages."
    "I don't really know what I was expecting."
    "The room is at least cozy. There are few decorations, although every space and item clearly has a purpose."
    "The sun shines pleasantly through one of the windows. Atticus left it slightly open, a breeze keeping the cottage from getting too stuffy from the medicinal scents."
    "..."
    "There has to be something I can do. I'm not used to sitting still."
    "I look to my sides, seeing a small table by the bed. There are two books there, both with well-worn spines and curled at the edges."
    "One has a green fabric cover, the corners completely dog-eared. There are tabs and loose papers packed into it. Perhaps some kind of research book?"
    "The other is bound in a brown leather, more robust than the other book. There is a bookmark near the end. If my instinct is correct, some kind of journal or diary."
    "Surely Atticus wouldn't have to know, either way…?"

    menu:
        "Read the research book.":
            # Atticus AFF up
            $ add_aff(1)
            "I take the green book and open it - only for one of the loose papers to immediately fall out."
            mc "Damn it."
            "It's a sketch of a mushroom - broad and flat with pretty ribbing. While it's clearly rushed given the charcoal thumb-prints on the paper, it's very detailed."
            "Atticus has written some notes around it - properties, where he found it, how many in a cluster…"
            "But there is also another set of handwriting, much shorter and messier than Atticus's."
            "All the other pages are similar. Fungi, herbs, leaves, updated entries on all the salves and potions he's used them in and the reaction they gave."
            "If my head wasn't swimming from the pain, I could probably learn a lot from this."
        "Snoop through Atticus's diary.":
            # Atticus AFF down
            $ sub_aff(1)

            "I take the brown journal and flick to the bookmark. He's written in the date, but nothing more yet."
            "I can't blame him though. Taking care of a dying ex-knight does take a lot of focus."
            "As I flick through the journal though, a lot of the days are fairly bland. Some are just bullet points of things he did that day."
            "Last week - he saw a new fish in the river."
            "The week before - he went on a walk and twisted his ankle."
            "The week before that - he tried a new fruit and didn't like it."
            "..."
            "No mention of other people."

    "..."
    "Maybe I should stop reading and try and get some more sleep. My ribs burn and ache, despite the salve."
    "As I put the book back, I see the stew and my stomach rumbles."
    "Funny, I didn't feel that hungry."
    "..."
    "At least Atticus makes a good stew, even if he doesn't talk to me."
    jump scene_3
