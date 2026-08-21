label scene_8:
    "The light is no more friendly though."
    "I awake in agony, a half-scream coming out of my mouth before my eyes are even open."
    "My back feels like it's ripping open. My shoulder blades are tense, rippling, struggling against the thin fabric of my shirt."
    "I curl up, scared to touch them and scared to move too much."
    at "I'm here."
    "I finally open my eyes, seeing Atticus hunching over me through a haze of pain-induced tears."
    mc "Atticus… what's happening?"
    "I can barely see his face. His glasses are off though, and his hands are colder than normal."
    at "You got hurt pretty badly. Try to relax if you can."
    "I feel his hands on my legs. I look down and see the scales, once glistening and red, now scorched and black in places."
    "The trap-the fire."
    "Atticus, facing the fire just to make sure I escaped…"
    "I blink, trying to focus on him. His arms are wrapped in their own bandages, a faintly herbal smell surrounding us both that reminds me of the salves he used for my ribs."
    "Not quite as bad as me, but he's still far more hurt than I ever want him to be."
    mc "You got hurt…"
    "I can now see the purplish bags under his eyes. Despite his exhaustion, he smiles at me."
    at "I got you out. That's all that matters right now."

    if mentality == 1:
        "Through all the pain and all the fear, what comes through is an immense and undying gratitude."
        "A knight can swear a vow to protect, but Atticus was a true hero, brave and sure."
    elif mentality == 2:
        "Gratitude and guilt choke me in equal amounts. My entire body aches, but I cannot imagine being here without him."
        "He risked his life for mine, and even while injured, smoothes salves and tinctures over my skin to help me. I cannot comprehend one man's kindness."
    elif mentality == 3:
        "Guilt wrecks me. He should never have been caught up in this, never had to face the poachers, never had to be so scared."
        "But more than that - he should never have been so tied up in this monstrous life. I should be dead in the woods, and he should be free from me."


    mc "Ngh!"
    "Another wave of pain shoots through my back, my spine tingling as though the fire still raged inside it. I bite my tongue, trying to keep the cries back–"
    at "[povname], stop!"
    "He gently pries my jaw open as blood drips from my mouth - new fangs pierced the flesh, large and bloody in my mouth."
    "It's hard to think through the pain. But I reach up and grasp his arm."
    mc "The Queen's promise… did you find it?"
    "He takes my hand and places it back in front of me."
    at "We can talk about it once you're through this spell-"
    mc "No! No, Atticus - did you find the flower?"
    "I can feel my body changing. My bones feel close to snapping. My back may soon split open. There is a roiling heat that is soon to explode inside of me."
    mc "I don't know if I have much longer."
    "Atticus pauses… and then his face crumbles. He shakes his head."
    at "The fire… it burned the only patch I could see. I only found the remnants as I was pulling you away from the inferno."
    "..."
    mc "Isn't there… anything we can do?"
    "Atticus chokes back a sob. He shakes his head."
    at "The fire… it was too much. They won't grow back before the transformation. I'm… I'm sorry."
    "..."
    "That's it then. I'm going to become a dragon."
    "Wings will sprout from my back. I will breathe fire and my claws will never know softness again."
    "Perhaps it is only a matter of time before the curse goes further, beyond the physical. Will my mind fall to that of a beast's too?"
    "I don't have long left. I can barely think through the pain."
    "..."
    "Atticus hand brushes over my forehead. It is blissfully cool."
    at "I… I can't promise that this will be easy."
    at "But… the pain will fade. Time will pass. You can figure out how to adapt to this new life."
    mc "Atticus…"
    "He smoothes a sweat-soaked strand of hair from my head."
    at "We may not be able to reverse it. But we don't have to let it control you."
    at "I… don't think it will be easy, learning how to live again. But… I'm here."
    "His smile is so small, so worried. But, at the same time, it is so strong that tears well in my eyes."
    at "I can help you navigate your way through it." 
    at "I know it's… an isolating experience. But you don't have to be alone. We can find ways of making this life comfortable for you again."
    mc "The humans treat you so horribly… I don't know if I can…"
    "I cringe through the pain. Atticus swallows, but takes my hand and squeezes it tight."
    at "I know. And you can - it will be hard, but you will find your way through this."
    "My back burns. I grit my teeth."
    "Maybe this is only temporary. I am scared beyond my wits, transforming into a terrible creature…"

    if at_aff >= 12:
        "But I'm not alone. Not now."
    else:
        "But I don't have to be alone."


    mc "I… I don't know…"
    at "You don't have to know now. We can figure things out. But… I believe in you."

    if at_aff >= 15:
        at "You are the bravest, strongest, most resilient person I have ever met. You have dedicated your life to making this world safer for others."
        at "If anyone can find it in them to live their life in spite of a curse, it's you."
        at "Stay with me. Let me help you."


    "He looks at me with so much belief, so much honestly. I cannot think of a more honorable man in my entire life."
    "Another wave of pain overtakes me. I duck my head, curling into myself."
    "Here was where I decided - whether I could stand to live with this, whether I could even fathom living anew."
    "Whether I would remain a knight, or fail to meet the beast within…"

    menu:
        "\"The life of a monster is no life for me.\"":
            $ mentality = 3
            if at_aff >= 12:
                jump tragic_end_2
            else:
                jump tragic_end_1
        "\"I just don't think I can do this. I'm sorry, Atticus.\"":
            $ mentality = 2
            if at_aff >= 12:
                jump tragic_end_2
            else:
                jump tragic_end_1
        "\"...Perhaps you're right. There is hope for me yet.\"":
            $ mentality = 1
            if at_aff >= 12:
                jump best_end
            else:
                jump happy_end


    # max aff == 19
