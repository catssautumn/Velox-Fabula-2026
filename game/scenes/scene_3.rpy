label scene_3:
    show blackout with dissolve:
            alpha 0.5 blend "multiply"
    nvl clear
    n "I stayed in that bed for three days, watching the sun rise and fall from the windows."
    n "Every single morning, Atticus would mix a new salve and soothe it over my ribs, as concentrating and quiet as ever."
    n "He would leave food for me on the bedside table before heading out into the woods, returning when the sun was low to make stew for the both of us."
    n "He would treat my wounds once more before the night fell, curling up by the front door like I had seen the guard dogs at the palace do once upon a time."
    nvl clear
    n "I scratch my arm as I watch him fall asleep, funny little sighs - not quite snores - escaping from him as he rests."
    n "He hardly talks when he's around me. I occasionally catch him muttered to himself when cooking or concocting, but nothing that I can fully hear."
    n "He reminds me of a skittish deer."
    n "Or, in this case, a skittish unicorn."
    nvl clear
    n "At the very least, Atticus seems content here, if lonely. I haven't seen or heard any other being other than him, but he returns with a basket full of flora and a soft smile."
    n "I wonder what everything is used for. He hasn't told me anything yet, but it's clear he knows what he's doing."
    n "On the fourth day, he heads out again."

    window hide
    $ nvl_mode = False
    $ quick_menu = False
    scene interior day:
        zoom 0.5
    show atticus
    with dissolve
    window auto show
    $ quick_menu = True
    at "You should be well enough to walk in a couple days! One week of bedrest, then you can start doing easy movement again."
    mc "I'll take your word for it."
    show atticus bsad tloop
    "He cocks his head with that awkward smile and leaves."
    hide atticus with dissolve
    "I scratch my arm again, staring at the ceiling. I would love to go outside, feel the bare sun on my skin and the wind on my cheek."
    "We're clearly still in the forest given the abundance of herbs he often comes home with. I wonder how peaceful it is, to be so far away from everything else…"
    stop music fadeout 0.5
    "..."
    "My arm is really itchy."
    $ nvl_mode = True
    nvl clear
    n "I pull up my sleeve, just able to reach my other arm over my chest."
    n "The skin…"
    n "Am I growing scales?"
    n "All over my arm are tiny, hard red scales, the skin pink and sore around them from my scratching. But as I pick at one, it feels just like the scale from a fish, or maybe a salamander, or…"
    n "Just like a red dragon."

menu:
    "I think I'm going to throw up.":
        $ mentality = 2
        nvl clear
        n "This can't be real… right?"
        n "I'm a human - humans don't grow scales. And certainly not spontaneously scattered all up their arm."
        n "I pick at one again - and it flakes off. I can feel the pull from underneath my skin."
        n "It's hard not to gag, but I brush the scale away and off the bed."
        n "I pull my sleeve back over them. What I don't see can't hurt me."
        window hide
        $ nvl_mode = False
        $ quick_menu = False
        show atticus with dissolve
        window auto show
        "And thank goodness I do, because Atticus arrives just at that moment, his basket filled with bright berries."
        at "[povname]. How's the pain?"
        mc "It's alright. I still haven't moved."
        "His smile comes back - soft and small. He's still so nervous around me."
        at "That's alright."

        if at_aff >= 3: 

            "Atticus opens his mouth as if he's about to ask me a question, or say anything just beyond the bare minimum—"


        "He swallows and turns away, back to the counter to set his basket down."
        "My arm still feels hot under my sleeve."
        mc "Atticus…?"
        "He jumps - literally - before spinning sharply around to look at me."
        at "Oh! Um, yes?"

        menu:
            "Ask about the scales.":

                mc "Uh… I think something's wrong with me."
                "Atticus frowns."
                at "How so? Is it your wound? Are the bandages too tight?"
                mc "No, no, uh…"
                "Part of me wants to keep my arms hidden - but it's a bit too late for that now."
                "I peel my sleeves up as Atticus comes closer."
                mc "I don't know how long they've been, uh, growing, but… I've got scales."

                jump ask_atticus
            "Stay quiet about the scales.":
                "I think about asking him…"
                "But given he still can barely look at me without that blush on his face, I don't want to ask him anything more personal than he can handle."
                mc "What did you find today?"
                "He blinks a few times - then cocks his head. Somehow, his eyes feel piercing on me."
                at "Just some moose's nettle. And some bearberries."
                "He stares at me a moment more before turning away."
                "Same old, same old."

                jump scene_4



    "Well, this is new.":
        $ mentality = 1
        nvl clear
        n "It's hard not to stare at them, all clustered on my arm. It's sort of like a constellation - if I can look past how odd this all is."
        n "..."
        n "Never mind, I can't look past how weird this is."
        n "Could this be a disease? Perhaps staying in the same vicinity as a creature caused an adverse reaction."
        n "Still, there was no point in panicking. I take a deep breath and cover my arm with my sleeve again."
        window hide
        $ nvl_mode = False
        $ quick_menu = False
        show atticus with dissolve
        window auto show
        "And thank goodness I do, because Atticus arrives just at that moment, his basket filled with bright berries."
        at "[povname]. How's the pain?"
        mc "It's alright. I still haven't moved."
        "His smile comes back - soft and small. He's still so nervous around me."
        at "That's alright."

        if at_aff >= 3: 

            "Atticus opens his mouth as if he's about to ask me a question, or say anything just beyond the bare minimum—"


        "He swallows and turns away, back to the counter to set his basket down."
        "My arm still feels hot under my sleeve."
        mc "Atticus…?"
        "He jumps - literally."
        at "Oh! Um, yes?"

        menu:
            "Ask about the scales.":

                "I pull up my sleeve once more, raising my arm as much as my position allows."
                mc "I don't suppose one of the side effects of that salve is 'may grow scales', is it?"
                "Atticus's eyebrows raise, and he comes over to the bed."
                at "Not… that I know of. You're growing scales?"
                mc "Yep. Just on my arms, as far as I can tell."

                jump ask_atticus
            "Stay quiet about the scales.":
                "I think about asking him…"
                "But given he still can barely look at me without that blush on his face, I don't want to ask him anything more personal than he can handle."
                mc "What did you find today?"
                "He blinks a few times - then cocks his head. Somehow, his eyes feel piercing on me."
                at "Just some moose's nettle. And some bearberries."
                "He stares at me a moment more before turning away."
                "Same old, same old."

                jump scene_4



    "Get them off.":
        $ mentality = 3

        n "It's just like skinning a fish. You just have to keep going until they come off."
        n "I feel panic, hot and horrible in my chest the more I stare at the blotches."
        n "With my fingernails, I scratch more fervently. I see blood starting to well around the scales, adding to the red stretching across my skin."
        n "One flakes off. I feel the pull from underneath my skin, like it grows from the bone. I bite back a noise of pain - no, fear - no, pain. It's hard to tell anything right now."
        n "I just have to get these scales off my body-"
        window hide
        $ nvl_mode = False
        $ quick_menu = False
        show atticus with dissolve
        window auto show
        "The door opens and Atticus is there, basket full."
        at "[povname], I'm back-"
        at bshocked eshocked up msad_o "Are you alright?"
        "Tears build in my throat. Everything feels hot, like a fire is cooking me from the inside out."
        mc "There's—my arms—"
        "Atticus throws the basket to the side, rushing over to me."
        at "Hey, hey! I need you to just breathe right now."
        mc "There's scales-!"
        at "And I'll examine them as soon as you take a moment. Please."
        "I manage some breaths, long and deep. Atticus breathes with me, his eyes wide and watching me intensely."
        "They're so purple… so strange…"
        "But soon, although I still can hardly bear to look at my arm, I calm down."
        at "There you are. Now, tell me what's going on?"
        "I take one more deep breath. A pit sits in my stomach."
        mc "They-I'm growing {i}scales{/i}. All up my arms."
        mc "I don't know when they started but-but I'm covered in scales!"

        jump ask_atticus


label ask_atticus:
    $ add_aff(1)
    $ at_knows = True
    # Atticus aff UP
    # Atticus knows about curse

    "Atticus sat down on the bed, taking my arm in his hands."

    if at_aff >= 4: 

        "His thumb, almost absent-mindedly, rubs soothing circles just above my elbow."
        "I can't say I mind it."


    "His brow furrows and he takes his time. Just as when he applies the salve to my side, his ears twitch in concentration."
    "His hand ghosts from my nails to my shoulder, touching each scale and the skin around it, examining the visible veins under my wrist, touching each fingertip."
    mc "Um, Atticus?"
    at "One moment, please."
    "He continues to examine the skin, gently squeezing around every single knuckle. I have no idea what he's looking for."
    "..."
    "Did he do this?"
    "I hadn't spent so long in the vicinity of any non-human creature before. Perhaps there was some latent reaction, biology or chemistry or…"
    "Was this a reaction from Atticus's medicines? I had no idea what was in any of the concoctions he made except from the stews - and even then, some of the mushrooms he named went over my head."
    "..."
    "Maybe it was something more intentional. A way of keeping me here, an odd revenge against the humans who had once trapped him."
    "..."
    "Maybe."

    menu:
        "Voice these thoughts to Atticus.":
            # Atticus AFF down  
            $ sub_aff(1)
            mc "Atticus… do you think you…"
            mc "Did you cause this?"
            "Atticus's head shoots up to look at me - and he looks almost heartbroken."
            "His ears flatten against his head and, just for a moment, his hands tighten around my arm."
            at "No. No, I… I would never do this to anyone. Let alone you."
            "He ducks his head back down again, unable to look me in the eye."
            "Gods, he looked like he was the one who had been stabbed. Of course he hadn't done this to me intentionally."
        "Stay silent and let him work.":
            # Atticus AFF up
            $ add_aff(1)
            "These were thoughts caused by fear. Irrational, but I wouldn't let them control me."
            "I keep quiet as he examines my nail beds. I'm sure he has a reason to."


    "After a couple minutes, he sets my arm down and looks at me with a forlorn expression."
    at "I'm sorry, but… this looks like a curse to me."
    "..."
    mc "A curse?"
    "Atticus nods, his teeth chewing his bottom lip."
    at "That's what it looks like to me - a transformation of this specificity doesn't seem like a reaction to a potion or anything."
    at "But, then again, I haven't seen this before. In all honesty, I don't know how to stop this."
    "I sigh, falling back against the bed."
    at "But… I won't stop trying to figure out how to help."
    mc "... really?"
    "Atticus nods, his expression entirely serious. He pushes his glasses up his nose."
    at "I may not be a master curse-breaker. But you saved me from those hunters, and if the least I can do is try my best to help…"
    at "Well, that's just what I'll do!"
    "A blush spreads all over his face and he looks away from me… but I can't help but believe him."
    "Truly, I don't know if he can help me. He may be knowledgeable on plants, but I doubt that eating my five-a-day will save me from whatever this curse wants to do with me."
    "But… he promised to help. He's been sleeping on the floor while I heal, and he has never done anything to make me uncomfortable."
    "Maybe once my side is healed, I can find a magician in town. But for now, I'm happy to accept Atticus's help."
    jump scene_4