## insert script here
label start:
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
            
    show layer screens:
        matrixcolor TintMatrix("#cecee2")
        
    show screen flower_frame()
    scene forest night with dissolve:
        zoom 0.5
    stop music fadeout 0.5
    show rain
    play ambience storm fadein 0.5 
    $ nvl_mode = True
    n "Every knight dreams of a glorious victory. A life and death battle won through sheer grit and strength of will, justice brought to all, and a grand feast to celebrate your triumph…"
    n "I was the same, ever since my squire days. I dreamed of saving the people from injustice, of defeating foes far greater than I with nothing but my blade and skill."
    n "Yet, I never once considered what would happen after the fight of my dreams."
    n "The king offered me a reward, as thanks for saving him and his people from a cruel dragon." 
    n "Yet, instead of offering me a hero's title, or perhaps the gold with which to forge my blade and armour anew… He tells me to hang up my sword."
    nvl clear
    n "'You have earned a hero's greatest reward: the peace you have earned with your own hands'... and what am I to do with peace? Frolic in the fields with the sheep and the dogs? Let myself grow rust in placidity?"
    n "I think not. I am a knight before I am a king's citizen. As treasonous as this may be, I will not obey his decree."
    n "I spend my days training still, honing my edge to protect the people. A cutpurse here, a scoundrel there, a tyrant here."
    n "I wander wherever I please, doing what good I can for the people I encounter."
    n "While I prefer my freedom, I will admit, sometimes I do miss the amenities of proper knighthood."
    nvl clear
    n "Now, especially, I miss the luxury of a proper shelter with a warm hearth and food I don't have to bleed myself dry to attain."
    n "My makeshift shelter does little to shield me from the torrential rain. Still, the wet wood blocks out some of the storm."
    n "I shall endure. A dragon slayer will not yield to a mere drizzle. A few hours more, and the rain will end."
    scene blackout with dissolve
    window auto hide
    $ nvl_mode = False
    window auto show
    
    "I close my eyes, attempting to sleep. It's essential to conserve my energy so I can continue my trek to the next town."
    play sound shake volume 0.5
    "Hm…? What is that? An animal…?"
    play sound shake volume 0.7
    "It is… rather energetic, isn't it?"
    play sound shake 
    "I crack an eye open, taking a peek at the sound."
    scene forest night with dissolve:
        zoom 0.8 yalign 0.5
        ease 2 yalign 0.2 
    show rain
    "Up above, hanging from the branches of another tree, there's a figure thrashing about in a hunter's trap."
    "A boar, perhaps? But, it seems much too large for that… Don't tell me, is it a person…? Or some sort of beast?"
    "If it is a person, I'm obligated to lend my aid. But, if it were a beast, or some lucky family's dinner, setting it free would be a terrible offense…"

    "What should I do?"

    menu:
        "Set them free":
            $ add_aff(1)
            $ helped_atticus = True
            "It is surely the right thing to do. If I am wrong, then I shall make amends afterwards. Forgiveness, not permission, especially when something is in distress."
            scene forest night with dissolve:
                zoom 0.5
            show rain
            "I emerge from my shelter, examining the figure and the trap. It seems that the net is held aloft by a rope weighed down by rocks…"
            "A simple system, one that's easily undone with a bit of strength. I displace the pile of stones, steadily lowering the net to the ground."
            "The figure inside doesn't flee like a frightened animal. Nor do they instantly attack."
            "Instead, they attempt to emerge from the net.{w}.. and immediately fall over."
            "A very human voice curses as the figure wrestles with the rope, their fight made so much more difficult with the slippery mud and falling rain."
            mc "Do you require aid?"
            "At the sound of my voice, the figure freezes. They stare at me, their eyes wide."
            window auto hide
            hide screen flower_frame
            scene cg1 scared with dissolve:
                zoom 0.8
                align (0.6, 0.8)
            window auto show
            "They appear to be human at first glance - although their snow white hair fades into white, fluffy ears, scared and flattened against their head."
            "From underneath them, a long, thin tail with a tuft of white hair at the end, whips nervously against the grass."
            show cg1 scared:
                ease 3 zoom 0.53 align (0.5, 0.5)
            "And from their forehead, a horn protrudes, a large kink in the middle."
            "I see I was too hasty, saying this person was unlike a frightened animal before. Now, there is no description more apt."
            "They regard me as prey watches a hunter. If not for the net, I imagine they would have already fled."
            "I attempt to comfort them, but before I can say a word-"
        "Refrain":

            "It's better to err on the side of caution, lest I accidentally release some sort of fae, or perhaps a particularly large boar."
            "I continue to wait out the storm, ignoring the insistent thrashing above."
            "After what may be hours, or mere minutes, I hear something snap, then a large weight crashes upon the ground."
            window auto hide
            hide screen flower_frame
            scene cg1 angry with dissolve:
                zoom 0.8
                align (0.6, 0.8)
            window auto show
            "When I peek at the figure, I see something that looks almost like a human."
            "They certainly have the body of one - but with fluffy white ears against the side of his head, and long, tufted tail."
            show cg1 angry:
                ease 3 zoom 0.53 align (0.5, 0.5)
            "And, more surprisingly, a misshapen horn sprouting from atop their head."
            "Perhaps not the game I had been expecting to see in the net. Although it looks up at me with such animalistic fear - but also human helplessness."
            "Before I can attempt to speak, or hide myself further, I hear-"

    scene forest night with dissolve:
        zoom 0.5
    show screen flower_frame()
    show rain
    "???" "Hey! The hell are you doing with our catch!?" with vpunch
    "The trapped figure jolts, attempting to free themself with renewed vigor."
    "They do not manage to escape before the newcomer joins us."
    "She is a formidable woman - tall, broad, dressed in leathers and patched up clothes. Clearly someone who wasn't afraid to get her hands dirty."
    "I hoped not though, catching the glint of a large hunting knife in her belt. The metal is as red as blood, and shines wickedly in the limited light of the forest."
    "She looks at me with sharp, beady eyes, even as the figure still tangled in the net trembles."

    if helped_atticus:

        mc "Upon finding an unfortunate person caught in a spot of trouble, I lent my aid as any good citizen would…"
    else:

        mc "I have committed no crime. Though, I do have to wonder, what are your intentions towards this person?"


    "???" "Person? You ought to get your eyes checked, knightie! That there's a fortune on legs!"
    "???" "A unicorn, in the flesh! When we sell his horn, we'll be raking it in for the rest of our lives!"
    "A unicorn…?"
    "I had expected unicorns to look less… human. More horse-like. Although it is hard to ignore the ears, tail and horn."
    "Unlike the archetypical unicorn though, his horn is uneven and warped, discoloured at the point."
    "I wonder, do most unicorns possess similar horns?"
    "Perhaps the storybook illustrators took some liberties with their artwork to save themselves the trouble."
    "They've clearly left out the part where unicorns can take the form of horned humans."
    "But, when the woman takes a closer look at the unicorn, her celebration ceases."
    "???" "Argh, no… That horn's shit! We won't get nearly as much out of it, but…"
    "???" "Whatever, people will still pay for healing tools, no matter how mediocre they are."
    "The unicorn's breath hitches, before he turns his head."
    "He looks directly at me, vivid violet eyes burning with an emotion I can't name."
    "Is he… asking for my help?"

    "As a knight, I had sworn to protect and help the people of this kingdom… although that role was now no longer mine. Would my vow apply to a unicorn?"

    menu:
        "Withdraw":

            "What right do I have to part a desperate woman and her meagre gold? What wrong should I commit next, steal the chicken from a family's dinner?"
            "As unsavoury as it might appear, given the unicorn's human skin, this woman is a hunter. Her actions are no different from snaring rabbits or shooting deer."
            "Hunter" "Hey, wait a tick, that sword you've got… Isn't that a knight's sword?"
            mc "Yes."
            "Hunter" "So, basically, you're loaded, right?"
            mc "The king has granted me a fair sum of gold, yes."
            "Hunter" "Sweet! Then, why not join us at our market stall? I'll give you a special discount on this horn!"
            mc "I may peruse some of your wares, then."
            "Hunter" "Ha, you'd be more than welcome… but for now, I think you'd best get home. It'll be a day or two for me to get the wares in order."
            "I look at the unicorn, trembling against the ground. His eyes keep switching from mine to the hunter's."
            "My vow was made to protect the people of this kingdom… the people. There is an argument to be made that I am under no responsibility to help the animal."
            "Still. I stay nearby and watch as the hunter calls in more of her colleagues. They move the unicorn away with efficiency and ropes."
            "She finds me as the haul him away with a smile."
            "Hunter" "I knew you knights were alright. I'll make sure my men treat you right at the market."
            "Right… This is no different from a hunter selling rabbit's feet, or deer bone…"

            if helped_atticus:

                "But why does the unicorn's gaze feel so… betrayed?"
            else:

                "No matter how much it feels like the unicorn is glaring at me…"


            "It wasn't my place to intervene. I was 'retired' supposedly. A boon."
            "..."
            "Even later, when the creature and net are gone, I feel no honor in my actions."
            hide screen flower_frame
            $ quick_menu = False
            scene blackout with dissolve
            pause 1.3
            return

        "Protect him.":
            $ add_aff(1)
            "What foolishness am I even considering? Even if it is a unicorn, I can't turn a blind eye to this."
            mc "Pardon me."
            $ glasses = False
            show forest night:
                easein .5 xoffset 40
            pause .2
            show atticus bshocked eshocked mshocked tloop at forest_night with dissolve:
                yoffset 30
                pause .3
                linear .1 yoffset -30 
                linear .1 yoffset 0 
            "Unicorn" "A-ah…? Yes…?"
            "Hm, so he is capable of speech. That makes this much easier."
            mc "Do you wish to hand over your horn to this individual?"
            show atticus bsad 
            "Unicorn" "Huh?! No!"
            mc "I see. Thank you for answering."
            hide atticus with dissolve
            "???" "Oi, what are you doing, talking to the merchandise?"
            show forest night:
                easein .5 xoffset 0
            mc "I was simply ascertaining a few things."
            "???" "Well, cut it out! I hunted that freak, far and square! That means his horn is mine!"
            mc "I see. Then, answer me this:"
            mc "If I defeat you now, may I have your heart?"
            "Poacher" "Huh…?!"
            play music battle fadein 0.5 
            "I draw my blade. Its familiar weight is a reassuring companion as I advance."
            "My first strike falls short, my movements weighed down by wet clothes and slowed by wind. The poacher is surprised only for a moment, before she roars in rage."
            show forest night:
                linear 0.3 zoom 0.54 align (0.5, 0.5)
            "Drawing the knife from her belt, she rushes towards me."
            "Our blades clang together, metal scraping against metal in a horrid screech. I grit my teeth as she leans in closer."
            "Poacher" "I don't normally gut humans… but hey, there's always a first for everything!"
            "She kicks my foot back and I stumble, but manage to duck under her next sweep." with vpunch
            mc "Last chance to run. Leave the unicorn be, and I'll spare your life."
            "Poacher" "No chance, knightie."
            "Her bravado leaves her open. I jerk forwards, aiming for the gap between her leathers and the blade finds purchase–"
            "Just as the poacher's dagger finds its way between my ribs."
            mc "Ngh!" with vpunch
            "Poacher" "You little…!"
            "We both stumble back from each other… her belly is already stained dark red, but I can feel the warmth seep from my side."
            "I fall to my knees as the poacher falls onto her back. Her dagger sits in my ribs - and my sword is right at my side."

            menu:
                "Let the poacher bleed out.":

                    "She was going to die anyway. There was no point in expending any more of my limited strength."
                    "Not that I was going to be doing much more anyway…"
                    "The poacher lifts her head to look at me. Her smile is pained, but her eyes are still as sharp as the knife she stuck in my ribs."
                    "Poacher" "Oh, what an honorable knight, slaughtering an innocent woman... hope you can handle a little payback."
                    "Her laughter soon fades away."
                "End her misery now.":
                    # Atticus AFF up
                    $ add_aff(1)
                    "Stumbling to my knees - ignoring the hot, red pain spiking through my side - I take my sword once more."
                    "The poacher lays on her back, teeth bared at me like an animal."
                    "Poacher" "Bloody knightie… couldn't let a malformed creature go?"
                    mc "No. And I won't let you go either."
                    "I make quick work, pushing my sword through her chest. A quick end, if not an honorable one."
                    "She groans, looking up at me with quickly fading eyes."
                    "Poacher" "I thought knights were meant to be honorable… hope you can handle a little payback."
                    "If the last thing I were to do was take one more poacher from this world, then that would be enough."


            show blackout with dissolve:
                alpha 0.5 blend "multiply"

            "I fall onto my back, the pain somehow subsiding. Funny, how the senses dull so quickly."
            "There's a faint pulse against my side. My fingers numb and my vision darkens as I taste copper and fire at the back of my throat."
            "How disappointing… A mighty knight, a dragonslayer, meeting [their] end at the hand of a mere knave…"
            "The last I see is my own blood seeping into the ground, the darkness swallowing me as the heat in my side fades away from my grasp."
            stop music fadeout 0.5
            stop ambience fadeout 0.5
            jump scene_2
