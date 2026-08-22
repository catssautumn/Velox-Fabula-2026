label dark_end:
    "It's the best option for me."
    "Even if he won't understand in the moment… it's for the best."
    # fade out
    # fade in
    "Atticus comes back in the evening, no more progress made than before. It's alright though - my hopes were never high to begin with."
    "He cooks me dinner. He prepares me warm water to bathe myself. He falls asleep in his nest of blankets and cushions in the corner."
    "I stay awake. My mind is racing, unable to slow down enough for me to fall asleep."
    "The moonlight shines through, illuminating the cottage in a silvery, ghostly light. The shadows stretch across the floor."
    "I am silent as I pad along the floor. There is no wind, no creak, nothing to hint that I am not asleep right now."
    "I stand above him. He doesn't even twitch."
    "I hold a knife in my hand. One he had used to prepare the stew with. It was easy enough to sneak it from the counter."
    "I look down at it - and catch my reflection. I look hungry. Like a dragon waiting to add something shiny to their horde. My eyes narrow."
    "..."

    if mentality == 2:
        "I can't stand the sight of me."
        "This isn't me… is it? A monster who steals what is not theirs to take?"
        "It is everything I have stood against for years. For my entire career, for everything before and beyond it."
        "I know I will never recover from this."
    elif mentality == 3:
        "My eyes… they look so evil. Slitted, dangerous, a snake ready to strike."
        "The knife shakes in my hands. It's pathetic - it's all so pathetic."
        "But the answer is so close…"


    "Atticus twitches beneath me, nuzzling into his blankets. He's so peaceful, fast asleep and unaware of the world around him."
    "Of the monster with a knife less than a foot away."
    "..."
    "Now's the moment."

    menu:
        "Take his horn.":
            "I'm sorry, Atticus."
            "I lean down, taking his jaw in my hand to hold his head still. I raise my knife."
            "Atticus stirs…"
            at "[povname]...?"
            # blackout
            at "[povname]!"
            "..."
            # bg forest
            n "I walk away from the cottage. There's nothing left there anymore."
            n "My sword is heavy in my hand. My shoulders feel weighed down by something I dare not name."
            n "At my belt, I have tied the horn into the leather. When I walk, the end pokes into my thigh."
            n "The scales have already started to fade. By sunrise, I shall be human once again."
            n "Yes… human. I'm human, and always will be"
            nvl clear
            "No matter the cost."
            $ persistent.main_menu_background = "dark_end"
            return
        "Sheathe the knife.":
            $ attempted_poach = True
            "I…"
            "I can't take the moment."
            "I breathe out, letting the knife hang by my side."
            "There is no world in which I can do this and remain human. No monster, no fear, no force could ever be powerful enough for me to commit such an atrocity."
            "I back away and place the knife back on the counter. Atticus will never know how far I let myself abandon everything honorable."
            "I hear him twitch behind me."
            at "[povname]...?"
            "I turn around and smile."
            mc "Go back to sleep. I just needed to walk around."
            at "Mmm…"
            "He's back to dreaming in moments."
            "I climb back into bed. I don't sleep well."
            # fade out
            jump scene_7_flower


label tragic_end_1:
    at "[povname]..."
    "..."
    n "There is nothing else to say. I've said my piece, and Atticus has said his."
    n "He continues to patch me up, wrapping me in bandages and soothing my head with cool water from a rag."
    n "When he is content, he remains silent, before setting a bowl of stew by my bedside and tending to the hearth, his back to me."
    nvl clear

    if mentality == 2:
        n "Day in and day out he tends to me, soothing my burns and feeding me stew. But with each spoonful, the flavor I once enjoyed fades into bitterness."
        n "So, as soon as I am able to walk once more, I leave, unable to take one more sip of it."
        n "I pack my bags and head out the door. I leave Atticus behind, I leave that damned poacher camp behind."
        n "I try to leave my curse behind, but it is never too far from me."
        nvl clear
        n "No matter where I run, it follows, the shadows of great wings and a whipping tail just behind me."
    elif mentality == 3:
        n "I'm not sure how many bowls he leaves out for me. Of how many days pass by before I am sick to my stomach at its very stench."
        n "As soon as I can stumble to my feet, I leave. I don't understand how he could ever be around me for as long as he was."
        n "So I leave the hut behind with nothing but the monstrosity on my skin and sword in my clawed hand."
        nvl clear
        n "It's time to slay a dragon."

    $ persistent.main_menu_background = "tragic_end_1"
    return

label tragic_end_2:
    "Atticus looks at me, his mouth opening and closing. He's searching for words, but he knows that it's meaningless."
    mc "Can I have some time to myself, please?"
    at "I... Yes, of course. I'll be in the garden if you need me."
    # bg transition
    "That night, the dragon taunts my dreams. It shines with red scales and breathes acrid smoke into my face, daring me with slitted eyes."
    "My sword isn't in my hand, nor by my side. No armor sits on my shoulders. I am petrified with fear."
    "My only option is to flee, but there is nowhere for me to run. Everywhere is up in flames, destroying everything in its wake."
    "So, I cry out for aid. I plead to the heavens for mercy. What did I ever do to deserve this fate?"
    "..."
    "Miracoulously, it listens. A refreshing rain pours down, putting out the fires around me. The dragon takes flight, ascending to the skies until it's nothing but a speck."
    "..."
    # bg hut
    "For the first time in ages, I wake with a smile. My heart feels so light, so free."
    "That's when I notice a distinct lack of scales on my body. The pains have ceased as well. Every sign of the curse has disappeared without a trait, as if it never existed in the first place."
    "My arms are scarred from my years of battle, but it was {i}human{/i}."
    mc "It's- I can't-"
    mc "Atticus, I can't believe it! The curse is gone, I'm free-"
    # show cg
    mc "...Atticus?"
    "Where a crooked yet beautiful horn sat, lies a scar. As I rise up, I can feel its weight on a cord around my neck, the horn rested against my heart."
    "I ask him questions. I beg him to tell me what happened, what made him do this."
    "He doesn't answer me. I don't think he can. He smiles sweetly at me, as he always does. But it carries a weight and pain I can never understand."
    # blackout bg
    n "And I don't think I could ever begin to understand. Of why he made the choices he did, or what he saw in me that was worthy to make such a sacrifice."
    n "But he did. And my life returned to the way it once was."
    n "Maybe I came out of retirement and returned to my knightly duties."
    n "Or maybe I accepted the idyllic life after all. Perhaps I settled down or traversed across kingdoms to see sights never seen before."
    n "But whenever I get a quiet moment to myself, my thoughts always wander back to Atticus."
    nvl clear
    n "He may have left so I could forget him, but I never will. The unicorn... the man everyone labelled as a freak, was the most kind-hearted person I've ever had the privilege of knowing."
    n "Sometimes, I wonder what would have happened if I had listened to his words."
    n "Would I have actually been able to live with the curse? Would he have stayed? Would we have remained friends?"
    nvl clear
    n "But such thoughts are useless. The best I can do is carry him by my heart, like he did with mine."
    $ persistent.main_menu_background = "tragic_end_2"
    return

label happy_end:
    mc "I… can't promise I'll be too bearable for a while. But I promise to try."
    "He remains calm, fussing over my wounds and my back like a worried mother. But more than that - he cannot wipe the smile from his face."
    n "True to his word, he helps me through my transformation. He teaches me how to survive in the wild."
    n "Of course, I already knew how to hunt, make a fire, set up a tent..."
    n "But he taught me which herbs were useful for a burn, and which one would make me dead within a minute."
    n "How to avoid as much human interaction as possible, and where to potentially acquire supplies in case of an emergency."
    nvl clear
    n "It takes a long time to soak up every bit of his bountiful knowledge. But it was peaceful and dotted with happy moments."
    n "Life was hard, and it's still hard. My tail gets in the way, and I have to be careful not to breathe fire or else I can ruin my throat for good."
    n "Not to mention that my wings are heavy and cumbersome. And I can't even fly with them!"
    n "... Not yet, at least. I'm still working on that."
    nvl clear
    n "But there are still positives. With sufficient knowledge from Atticus, I can move out on my own."
    n "Thanks to my draconic eyesight, I can navigate even the darkest of nights. It's then that I use it as my chance to strike hidden foes and protect the kingdom I still love."
    n "People even begin to whisper about me, a mysterious and noble hero who disappeared into the shadows after being released from their post."
    # bg outside cottage
    "But here, I can take off my helm. I take the time to emerge from the unknown to pay a certain unicorn a visit. Mostly for his company but..."
    at "Ah, [povname]! Back for some stew? You're just in time, I've harvested some fresh ingredients!"
    "...The stew is pretty damn good too."
    $ persistent.main_menu_background = "happy_end"
    return

label best_end:
    "I'm not fully convinced I can do this. But with Atticus by my side, I'll sure as hell try."
    "He smiles so brightly as I answer him. He continues to work on my injuries, soothing my back with cool water and salves, day in and day out."
    "He doesn't stop. I don't think Atticus is even capable of stopping his caring. And I wouldn't want him to."
    n "The next few weeks are grueling. The curse latches to my body, sprouting large, red wings and tail. Horns weigh on my head and my eyes are slitted."
    n "But just as Atticus surmised, the pains ceased. Now it was just a matter of acclimating to my new appendages."
    n "I've accidentally broken my fair share of pitchers and vials bumping into everything. I swear they have a mind of their own, but my roommate doesn't seem to mind, thankfully."
    n "Now, the forest is slowly growing back since the fire. Signs of new life bloom and Atticus is determined to restock his supply of herbs."
    # bg forest
    "In the end, we both got carried away and wound up near the edge of the woods."
    "Not too far from us, I can see the main road that loops around to the distant town I was journeying to."
    "I would've been wary of other travelers too, but this time of year, everyone else is taking a different route into the castle walls to celebrate the king's birthday."
    "I recall last year's banquet. The streets were abuzz with laughter and the aroma of delicious food permeated the air."
    at "Do... Do you miss your old life?"
    mc "I do... But only from time to time."
    mc "But I wouldn't change my path here for anything."

    if mc_crush == True:
        mc "After all, it led me to the most kind-hearted, gentlest, and bravest unicorn in the world."
        "I look at Atticus besides me, not bothering to guise the love and affection I feel for him."
        "He blushes profusely and averts his gaze. He twiddles his thumbs while his tail thumps happily."
        "Cute."
    else:
        mc "After all, it led me to meeting you!"
        mc "And who else can say a unicorn is [their] dear and irreplaceable friend?"
        "I playfully nudge Atticus, who snorts softly."
        at "And how many can say they're friends with a dragon knight?"
        mc "Yes, yes, savour my presence for as long as you need."


    # drizzle animation + ambience
    mc "Oh, it's a sunshower!"
    at "Now that forest can flourish even more."
    # drizzle animation + ambience, show cg
    "Instinctively, I unfurl my wing and shelter Atticus underneath."

    if mc_crush == True:
        mc "Unfortunately, you're no flower, although you are as pretty as one. Take care not to catch a cold."
        at "Th-thank you..."
    else:
        mc "Unfortunately, you're no flower. Take care not to catch a cold."
        at "Thank you!"


    at "This reminds me of how we first met. It was raining then too."
    mc "Mildly put, yes, it was."
    mc "It was a fierce storm that caught me by surprise. I had to seek shelter and wound up finding you."
    at "I would've died that day if it weren't for you."
    mc "And I would've also succumbed to despair from the curse had it not been for you."
    at "Oh! You're very welcome, though anyone would've done the same."
    mc "Oh you'd be surprised by how people would leave one after an inconvenience."
    mc "You have the noble heart of a knight, Atticus, and I am grateful for it. Truly."
    at "So, ah... That makes each other's knights in shining armor and damsels in distress then?"
    "I thump my tail against Atticus' legs in jest."
    mc "I'm still a knight! I don't need the title to have all the honor of one."
    at "Haha, whatever you say."
    # hide cg
    at "..."
    at "So, what do you plan on doing now? You're well enough to stake out on your own, if you so wish."
    "He continues to look out towards the scenery ahead of us as he asks his question."
    mc "Well, obviously we're going to see the world! Climb a mountain, watch the ocean waves crash on the shore."
    mc "If we're sneaky enough, maybe we can sample the local cuisine!"
    at "Ah.. That sounds nice- Wait, \"{i}we{/i}\"?!"

    if mc_crush == True:
        mc "Yes, of course!"
        mc "You wanted to see the world, right? So that's what we'll do."
        at "I... But... Are you sure you want me to accompany you?"
        mc "Atticus, I {i}want{/i} you to be there with me. There is no one else I'd rather have by my side than you."
        mc "Just like you've helped me come to terms with my curse, allow me to help you pave the way to your dreams."
        "At this, Atticus blushes yet again. This time, though, he manages to squeak out a few words."
        at "F-forgive my forwardness, but... Are.. Are you f-flirting with me...?"
        mc "Ah! You finally notice. I have been for the past few months now, truthfully."
        mc "I'm glad it took only a few gallant words to get through to you."
        mc "Do not be mistaken, though. I do mean to take you on a grand journey across the realm, whether you reciprocate or not."
        "Atticus is silent for a few moments. I can't help but feel the nerves get to me as well, my tail swishing the damp grass beneath my feet."
        at "I... I would positively love that."
        "He smiles at me shyly before leaning in to peck me on my cheek."
        at "U-um, I shall go pack my belongings right away!" 
        "I rest a scaled palm upon my cheek as I watch him bound away."
    else:
        mc "...Yes?"
        mc "Unless you prefer to stay here. In which case is fine, I'm sure-"
        at "No, I want to go!"
        at "I... But... Are you sure you want me to accompany you?"
        mc "Well, I've no other traveling companion in mind that won't scream in terror upon taking in my visage."
        mc "So I'm afraid you're stuck with me, good friend. Haha!"
        mc "...But in truth, I do recall it being your dream to see the world."
        mc "So let's do that together?"
        at "...Yes."
        at "Yes., I would positively love that!"
        at "Let me go pack my things straight away."
        "I can't help but fondly shake my head as I watch him bound away."


    mc "I have a good feeling this is going to be quite the memorable journey."
    # $ bg half black out
    n "And what a memorable journey it was."
    n "Just as promised, I took Atticus across the lands I was familiar with and more. It wasn't easy to avoid human crowds, but we did stumble across people in similar situations to us."
    n "I admit that I've never noticed them during my time as a knight, but now that I am..."
    nvl clear
    n "We didn't hesitate to lend a helping hand. We taught them what we knew, provided aid where we could."
    n "We even built a small community of our own. People to rely on when times are tough."
    n "Now we're even honing in on ending poaching once and for all."
    nvl clear
    n "It's not all serious business, though. Atticus soon discovered the joys of candied sweets, a delicacy he strived to perfect in his own kitchen."

    if mc_crush == True:
        n "There are quiet moments that we enjoy together. I've quickly learned of the fact that Atticus loves to cuddle with my tail."
        n "Sometimes, when he lucks out on a new book, he huddles under the blankets to read, insisting I join him."
        n "I can't truly wrap my mind around whatever informative tome he reads, but it's a wonderful way to fall asleep."
    else:
        n "Life with Atticus means that there isn't a day that goes by without a laugh."
        n "It's fun to banter with him, and in turn he's been learning to play along."
        n "The other day, he even pulled a small prank on me. I'm so proud."

    nvl clear
    n "And of course, we do get attacked or ambushed every once in a while."
    n "It's nothing a strong (and admittedly clumsy) knight such as I can't handle."
    n "...But if I couldn't? A certain unicorn concocted potions that can turn anyone's skin rainbow for a {i}very{/i} long time."
    $ persistent.main_menu_background = "happy_end"
    return
