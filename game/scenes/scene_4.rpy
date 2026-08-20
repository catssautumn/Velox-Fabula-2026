label scene_4:
    "Three days later - a whole week after I was first stabbed - I am finally able to stand once more."
    "Atticus, as per his usual routine, leaves after giving me food, basket on his arm."
    "However, given I can see the sunlight through the window - and my side finally doesn't feel like it's burning from the inside out - after an hour or so, I tail after him."
    "I pat my trusty sword, once more faithfully by my side. I'm not dressed in my full armour, but I feel more like myself with every step into the forest."
    "I feel a scale from my palm catch on my sword hilt."
    "They've been growing every day - inch by inch, creeping from my arm to my hand, curling around my shoulder. It's only a matter of time before they reach my chest."

    if mentality == 1:

        "At least it's taking a while to spread. The more time I have to uncover what's happening, the better."
    elif mentality == 2:

        "I hold my hand by my side. I pulled my sleeves all the way down before leaving."
        "If I can't see it, it can't hurt me…"
    elif mentality == 3

        "I swallow down a wave of fear that catches in my throat."
        "I can't panic right now - as long as I focus, Atticus and I can figure out what's going on."


    "I don't plan on going too far from the hut. After all, my side isn't completely healed - and I don't actually know where I am within the forest."
    "No. This is a small hike to get used to movement again, not some grand escape plan."

    if at_aff >= 4: 

        "And besides - I couldn't leave Atticus without at least saying goodbye and thank you for all he had done for me."


    "The forest is beautiful around Atticus's cottage - bushes of bright berries cluster underneath towering trees, dappled sunlight hitting their leaves."
    "Flowers bloom all along the rich green grass - yellows and pinks and blues, all different shapes and curves. Further away, I see a small stretch of heather-like herbs winding a path between the trees."
    "No wonder he comes home with something new every day - he's not exactly starved for choice around here."
    "As I walk around, I soon hear voices coming from a nearby grove."
    "None of them sound like Atticus - his voice is too delicate compared to these murmurs."
    "I keep a hand on my sword, ducking low into the foliage and sneaking towards the conversation. I soon see the perpetrators: a group of four cloaked figures, an array of shining weapons at their sides."
    "I keep behind a tree, but press my back to the bark to listen into their discussion."
    "Hunter 1" "It was around here, I swear! I know what I saw."
    "Hunter 2" "I believe you. I've seen that unicorn around this area too, slipping between the trees."
    "They must be talking about Atticus."
    "Hunter 3" "We can't let it go again. Not after what it did to Maggie."
    "Hunter 1" "Agreed. We find it and drag it back to the base. Easy."
    "Hunter 4" "With these new weapons? Never been easier."
    "They laugh together, low and sinister. Do they know how malevolent they sound?"
    "But they are far too close to the hut. Two minutes in the wrong direction and Atticus's home would be more than compromised - it would be ruined."
    "I slowly rise from the ground, trying to get a good vantage point. Even in my injured state, I knew my training from battle - if I were quick, I could take down a couple, fend off the others and send them running."
    "Just as I was about to circle them though, I heard footprints to my right."
    at "[povname]? What are you doing out here?"
    mc "Atticus!"
    at "You're supposed to be rest-AH!"
    "Catching sight of us, the hunters started calling out, rushing towards us."
    mc "Atticus, get back!"
    "I backed away, the hunters soon entering the clearing. Atticus quickly ducked behind me, quivering against my back."
    "Hunter 3" "What do we have here? The very unicorn we've been looking for!"
    mc "I'd advise you to leave this place immediately - lest you face the same fate as your friend."
    "The hunters' faces darkened."
    "Hunter 1" "You're the one who killed her?"
    mc "She thought to kill an innocent creature. As a knight of the realm, I am bound to protect this place from people like her."
    "The hunter who was speaking to me grit his teeth and turned his head away."
    "Hunter 1" "Just hand over the unicorn and no one else has to get hurt, alright? Honor-bound as you are, we too are bound by our job."
    mc "To injure and maim a peaceful man? I think not."
    "The hunter laughs. Another steps up, a wicked dagger already in her hand."
    "Hunter 2" "Why do you protect this one? Its horn is all bent and useless - there's no point in holding onto a malformed creature!"

    menu:
        "\"He is not malformed!\"":
            # Atticus AFF up
            $ add_aff(1)
            "The outburst escapes me before I can help it. How horrid, to dismiss anyone by a perceived 'deformity'?"
            "He was alive. That was the only factor that mattered."
            "While the hunter who asked the question looks almost taken aback, the others laugh mockingly."
            "I feel Atticus press closer to my back, his ears trembling against my shoulder."
        "\"I could say the same thing.\"":

            mc "I could ask you the very same thing. Why do you keep your sights set on something you perceive as 'malformed' if it isn't worthy?"
            "The hunter rolls her eyes."


    "Hunter 2" "Be that as it may, any horn is worth a good price, no matter how mutated it is."
    mc "Then you shall have to cut me down to get it."
    "I draw my sword. Despite the time spent away from it, it still fits so nicely into my hand."
    "The hunters glance at each other… and then take up their own weapons."
    "Hunter 1" "Job done, then."
    "They lunge for me. I parry one easily and kick another in the stomach, sending him sprawling."
    mc "Atticus, stay back!"
    at "Yep! I'm okay with that!"
    "The hunters are fierce - but clearly lack the experience in fighting that I do. Their movements are rushed and eager, but lack the finesse needed to take down someone of my calibre."
    "I catch one on the elbow and another in the neck with one move of my arm, winding one and injuring the other."
    "Hunter 1" "Get [them]!"
    "They are certainly trying - although I'm not worried. I've been needing a workout after spending so much time cooped up in bed."
    "Still - I need to focus. Atticus is behind me and watching my every move… although perhaps I can provide a little of a show, as thanks for saving me."

    menu:
        "Show off a little.":
            # Atticus AFF up
            $ add_aff(1)
            "There is a little part of me - that grand knight who once saved the kingdom - who feels honored by Atticus keeping so close to me."
            "So, why not repay that feeling?"
            "I laugh and gesture for the hunters to come closer."
            mc "Is that all you can give me? I've barely broken a sweat!"
            "They come at me again, although I've already given a good few enough scars to remember me by. I bat them away easily, adding a little flourish to my sword as the hilt catches one in the temple."
            "Hunter 4" "Stop that!"
            mc "Why should I? I'm having quite a bit of fun!"
            "I hear Atticus laugh behind me as I spin, sweeping the legs out from two of them in one movement."
            "It's the sort of thing my sword instructor would have scolded me for, perhaps with a knock on the head to get some sense into me."
            "But I was retired and he wasn't here, so I was going to have some fun."
            "And besides, if Atticus was enjoying the show, I wasn't going to stop now."
        "Ask Atticus to back up.":
            # Atticus AFF down
            $ sub_aff(1)
            "I was glad I could keep him safe - although it had been a while since my last true fight against a crowd, and I didn't want to risk anything."
            mc "Atticus! Back up, I don't want you to get in the way!"
            "I heard Atticus squeal and felt him leave my back."
            at "Sorry!"
            "I had to focus. I grit my teeth, batting one dagger away and ducking under another, sending the two combatants falling into each other."
            "It was almost comedic how they floundered around me - but now I had the space to concentrate, I could ensure none of them would be chasing us down again."
        "Focus on the fight.":

            "Now was not the time to be distracted. I tightened my grip on my sword, eyes tracking every movement."
            "As one hunter lunged, I moved back. As another swung, I ducked. As the third reached to grab me, I swung my sword up and sliced at their forearm, sending them away."
            "Swordfighting was a dance. Where they were ungraceful, I was a master of performance."
            "Atticus remained close to my back, never far enough away for anyone to make a sudden lunge for him. It took a minimal change, just making sure my arm or chest blocked him from an easy grab, to keep him safe."
            "I had trained this way for years. These hunters were barely catching up to me."


    "I raise my sword once more, high and proud-"
    "Hunter 2" "Look at that! A freak protecting a freak!"
    "I freeze and glance up - my sleeve has rolled down, just revealing the latest, long stretch of scales from wrist to elbow."
    "They glimmer like rubies in the sun. A vaguely sick feeling overcomes me, fueled by adrenaline and shame."
    "Hunter 3" "I didn't know we were fighting two monsters, men!"
    "Hunter 4" "Could fetch a good price for both of them!"
    "Hunter 1" "Monsters, both of them!"

    if at_knows == False:

        "In the corner of my vision, I see Atticus staring at me with wide, sorry eyes."


    "I swallow, my heartbeat loud in my ears."

    if mentality == 1:

        "But I take one breath - just one, just a moment - and concentrate again."
        "Their jeers and calls are only words. And I still hold a sword in my hand."
        "Before they've finished laughing, I'm swooping again, knocking them off their feet and spilling their blood."
        mc "Leave this place! And if you dare come back, I shall make sure you never leave again!"
        "Their inexperience weakens them more than any taunts could ever weaken me. They can barely lift their sword, exhausted and thoroughly beaten by a true knight."
        "As they groan and rally around me, their leader backs away into the trees."
        "Hunter 1" "We'll be back! We won't rest until we've got horns and scales in our market!"
        "Despite their sore loss, they cackle as they flee, their laughter soon fading among the plants."
        "I huff, feeling the exhaustion hit me. My side flares in pain, although nothing compared to what it was a few days ago."
        "I turn to catch Atticus's eye."
        mc "Are you alright?"
        at "I'm perfectly fine. A little shaken, but…"
    elif mentality == 2:

        "I tighten my grip on my sword. The adrenaline pumps stronger through my body, and I lower my sleeve until it covers my arm once more."
        mc "I am no monster. I am a proud knight, and it is my duty to protect people from the likes of you!"
        "I jerk forwards, aiming for the throat. The hunter dodges just in time, but all four snap out of whatever had amused them so and renew their attacks."
        "Unfortunately for them, I'm a little too practiced, and they're a little too slow."
        "As they groan and rally around me, their leader backs away into the trees."
        "Hunter 1" "We'll be back! We won't rest until we've got horns and scales in our market!"
        "Despite their sore loss, they cackle as they flee, their laughter soon fading among the plants."
        "I huff, feeling the exhaustion hit me. My side flares in pain, although nothing compared to what it was a few days ago."
        "I turn to catch Atticus's eye."
        mc "Are you alright?"
        at "I'm perfectly fine. A little shaken, but…"
    elif mentality == 3:

        "Fear floods through me, my grip shaking around my sword. I can't help it - I shake and tremble, and my voice comes out loud and hoarse."
        mc "I am not a monster! I am not, and will never be, a monster!"
        "I sprint forwards, swinging my sword too quickly for them. I slash one through their arm, watching the blood run out as they back away in fear."
        "It's not enough though. I need to move, need to get all of this out."
        "I spin around and catch another, stabbing straight through their leg to make sure they cannot run away. They scream, pushing themselves away from me. They can't run away from this."
        "I can't run away from this."
        mc "{i}I'm not a monster!{/i}" #screenshake
        "A couple respond with blows of their own - but I'm too fast, too vicious for them. Their leader backs away, pulling another with them."
        "Hunter 1" "Retreat! Retreat!"
        "They lean on each other, one carrying another, sprinting off into the forest. I start towards them, tears blinding my vision, my sword red."
        mc "Get back here! I'll kill you all!"
        at "[povname]!"
        "I stop still as Atticus calls for me."
        "My hand still trembles. There is blood splattered all along the forest floor, trailing after the hunters."
        "I take a deep breath…"
        "..."
        mc "I'm… I'm sorry, Atticus."
        "Atticus hovers by the tree line - and then walks towards me."
        at "It's okay. I'm… I'm sorry they called you that. And…"


    at "Thank you, so much, for protecting me."
    at "I truly don't know how I can repay you. This is the second time you've saved my life."
    mc "You're already repaying me, Atticus."
    "He bows his head."
    at "I'll find more ways."
    "I turn away from him, looking at the path the hunters escaped down. They would surely be back, especially after knowing both Atticus and I were posted nearby."
    "However, a glimmer on the ground catches my eye:"
    "A dagger made with blood red metal, laying on the ground."
    "I pick it up and hold it to the sunlight, watching the metal shine. It's hard to name, but there's a coldness to the handle, a chill that wouldn't make sense if someone were just holding it in battle…"
    "I recognise it. It's perhaps not the exact same dagger, but it is remarkably similar to the one I was stabbed with a week ago."
    at "What have you found?"
    "I show the dagger to Atticus."
    mc "Take care not to nick yourself with it - I fear it's quite dangerous."
    "His ears flatten against his head as he inspects the blade."
    at "Is it…?"
    mc "I think it is of the same make. At the very least, that group knew the hunter I… dispatched."
    "Atticus swallowed. He rubs the back of his head, adjusting his glasses and looking more and more like the skittish unicorn I had grown accustomed to."

    if at_knows == False:

        at "[povname], if you don't mind me asking…"
        mc "Yes?"
        at "What… was that on your arm? And why did they call you a monster?"
        "I swallow… and hitch the dagger into my belt. I'd rather not hold it while having such a vulnerable conversation."

        if mentality == 1:

            "I roll back my sleeve, revealing the patches of scales travelling from my hand upwards."
            mc "About three days ago, I spotted this. They've been growing more every day - they started just around my elbow, now they're from my fingernails to my shoulder."
            at "Do… do they hurt?"
            mc "No. They itch a lot though… and I'm not meant to grow scales, Atticus."
            "Atticus flushes."
            at "Oh! Yes, sorry."
        elif mentality == 2:

            "It takes me a second to compose myself, but I roll back my sleeve, revealing the patches of scales travelling from my hand upwards."
            mc "I'm… growing scales. I tried to ignore them - could have been a weird reaction to the medicine or… or something."
            mc "But they've been growing more and more. They started just around my elbow and now my whole arm is covered."
            mc "I… I don't know what to do."
            "Atticus looks at me, his big eyes filled with so much sympathy, it makes me shy away from him."


        at "May I… take a look?"
        "I hold out my arm and he cautiously holds it, dragging his fingers hesitantly over the scales."
        "They've grown to great patches, spreading like a rash up my arm. Still, Atticus doesn't flinch at the sight, but treats them with gentleness and care that makes them itch even more."
        at "I'm sorry, but… this looks like a curse to me."
        "..."
        mc "A curse?"
        "Atticus nods, his teeth chewing his bottom lip."
        at "That's what it looks like to me - a transformation of this specificity doesn't seem like a reaction to a potion or anything."
        mc "Agreed. If this were a reaction to the salve, it would be concentrated around my ribs and you would have noticed long before I did."


    "His eyes dropped to the dagger."
    at "Do you… do you think the dagger may have caused your curse?"
    "It wasn't too far out of the question. It had stabbed me pretty good - and so far, it was one of the few reasonable explanations."
    mc "I think it's a possibility."
    at "I'd like to study it, if that's alright with you. Even if it doesn't hold the clue to breaking your curse, any more information about it is good."
    at "And besides… I want to help you."
    "Gods, his face is so earnest. He looks at me with such innocence, like he couldn't bear not helping me."
    mc "Thank you, Atticus."
    "I hand him the dagger. He sighs and bows his head."
    at "Thank you, [povname]! I won't let you down."
    "I laugh, although it soon turns into a long sigh as exhaustion floods through me."
    mc "I'm sure you won't… although I could do with a long rest. I haven't fought that much in quite a long time…"
    at "Of course! Here, let me help you back. You weren't hurt again, were you?"
    "I can hardly call it confidence, although I've never seen Atticus quite so animated about something. I laugh again, and Atticus's ears twitch as he giggles along with me."
    at "Sorry. I just… want to help you."
    mc "I'm alright to walk, but thank you. Perhaps you can guide us back?"
    at "Yes! Absolutely!"
    "He immediately starts trotting, taking a much slower pace to allow me to keep up."
    "As he walks us back towards the cottage, he turns to me."
    at "I, um…"
    mc "Yes, Atticus?"
    at "I just… uh…"
    "He turns his face away, but I can still see his bright red cheeks."
    at "I just want to say that I don't think you're a monster. Or a freak."
    at "No matter what those hunters said."

    menu: 
        "Thank him.":
            # Atticus AFF up
            $ add_aff(1)
            mc "Thank you, Atticus."
            mc "I… I needed to hear that."
            "He looked up at me again, his expression soft and worried."
            at "You'll never be a monster. Not as long as you've got that honor."
            "We continue down the path in silence."
        "Shrug it off.":
            # Atticus AFF down
            $ sub_aff(1)
            "I turn away, looking straight ahead. There was nothing to say in response."
            "After a few moments, I hear Atticus sigh and quicken his pace."


    "We soon reach the cottage once more. I set my sword to the side and collapse onto the bed, falling asleep in a matter of moments as Atticus busies himself around the house."
    jump scene_5