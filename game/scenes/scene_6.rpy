label scene_6:
    "I barely see Atticus during the next day - he spends as many hours of the day and night studying the dagger as possible."
    "But in the night, I am shaken awake."
    at "[povname]!"
    mc "What is it?"
    "His eyes are glassy from lack of sleep, purple bags deep underneath them. His hair is frizzier than ever, mussed from lack of sleep."
    at "Dragon claw."
    "I cautiously raise my hand."
    mc "These?"
    "Atticus sighs."
    at "Sorry. I'm very tired."
    at "The dagger is a dragon claw dagger. It took me a while to find the notes on it, but I think I'm right."
    mc "Okay… what does that mean?"
    at "Dragon claw daggers are very rare, mostly because they take so long to make correctly. That, and they're banned due to how dangerous and… and cruel they are."
    at "Dragon claw daggers are used to inflict a curse onto their victim. They will slowly transform into a dragon - and, once that happens, the poachers return to harvest their scales and claws."
    "That's… unnerving."
    mc "You mean… they're making their own prey from innocent people?"
    at "I- yes."
    "His ears fall to fit his frown."
    at "But now we know what it is, I can find a potential cure much quicker. I can't promise it immediately, but…"
    "He trails off."
    at "I'm sorry."
    mc "It's… it's okay."
    "So I really am turning into a red dragon. The very one I had once protected the kingdom against."
    "Atticus is still watching me. I try to smile."
    mc "Could I… just have a moment alone? To process."
    "Atticus nods."
    at "Of course! Of course, I…"
    at "I'll be out the back if you need me. I know we don't have a lot, but I'll give you what space I can."
    mc "Thank you."
    "He lingers for a moment more, but soon turns away and leaves the cottage."
    "I sigh and sit up, hunched over. The skin on my legs itches and pulls oddly with the movement."
    "..."
    "The scales have spread, circling my chest, not quite meeting in the middle but spreading down my thighs. My feet are entirely covered, and my feet bend awkwardly."
    "There are claws poking out my socks, the fabric ripped." 
    "The sun is barely up. The sky outside is pink from what I can see through the window."
    "After a few more moments, I can hear the movements of Atticus out the back. Some soft thuds, as though he was moving items around, before the familiar grind of a pestle and mortar."

    if mentality == 1:
        "The sound is soothing. The familiarity and domesticity of it."
        "It's hard to ignore the changes - how the new skin itches and the implications that I now know."
        "Turning into a dragon… that was the sort of thing that happened in stories."
        "Well, I had said I was the stuff of legends."
        "There will be a solution. I have enough faith in Atticus to push through - I should have faith in myself to hold onto what remains human."
    elif mentality == 2:
        "The sound is soothing. The familiarity and domesticity of it."
        "It's hard to ignore the changes - how the new skin itches and the implications that I now know."
        "Turning into a dragon… that was the sort of thing that happened in stories."
        "If what Atticus says is true, I will be nothing but a story soon. Not human, not knight, but the antithesis."
        "Who would I become if I could not protect, if I could not serve? My life is built around honor… is there any honor to find in a dragon?"
    elif mentality == 3:
        "It annoys me. A sound I once found soothing now grates on my nerves, between my teeth, unrelenting."
        "I will turn into a dragon. A red dragon, one that soars over skylines and destroys everything until the world is ash below it."
        "I cannot stomach the feeling. My heartbeat sits in my throat until I choke on it."
        "Am I even still human anymore? I am not currently a dragon, but if what Atticus says is true, it's only a matter of time until I am stripped of all that I once knew."
        "It takes everything in me not to collapse into melancholy. A part of me wonders if I should anyway."


    "There's time. I have to remember that. I am not yet the dragon I swore to slay."
    "Atticus will find a solution. Until then, I must remain strong."
    "..."
    "I can't stand sitting here any longer."
    "I stand up on my new feet, working out how to walk after a few stumbles, and leave the cottage."
    "Following the sounds of work, I soon find Atticus. As he catches sight of me, his eyebrows shoot up his forehead."
    at "Are you okay?"
    mc "Yes, I'm fine. I just… can I help? I feel terrible sitting inside all day while you work away."
    "His worry quickly fades away, and he pushes a basket into my hands."
    at "I'd love the help! Could you pick some of the flowers by that bush?"
    "I nod and walk over, taking a stem into my hands- "
    at "Not that one! Sorry. The small green ones. The flower you're holding will make you sneeze uncontrollably."
    mc "Oh, got it."
    mc "Why do you have that flower? The one that makes you sneeze?"
    at "When diluted, it can provide relief for colds. But if you use too much, it just makes you sneeze out all of the illness. Effective, but… a little painful."
    mc "Any chance we can get me to sneeze out a curse?"
    "Atticus chuckles, but his ears twitch just enough for me to notice."
    at "I am actually working on a potion right now to do just that! No sneezing required."
    mc "Really?"
    at "Yep! I can't promise it will break the curse, but my hope is that it will slow the transformation until I have time to find a proper cure."
    mc "That's very thoughtful. And a good idea - if we can do anything to stop me from turning any more than I already have…"
    "Atticus pauses to look over at me, his smile confident and reassuring, eyes slightly crinkled."
    at "We'll find a way. Don't worry."
    at "Now - the small green flowers, please. And the angel's bloom after that."
    "It's simple work, but Atticus gives me clear instructions and I can follow them. It's just enough for my mind to focus, to think of anything other than the scratch of my scales against my clothes."
    "I am uneducated in medicine myself, merely trusting the magic of the palace healers when needed. No human can cast magic normally, although their salves and tinctures always worked wonders."
    "That being said, I have seen magic many times before. Either through the thick potions and hexes woven from magical plants, to the cursed weapons those poachers held. I know of its power - if not of its intricacies."
    "For something close enough to a human, Atticus is incredibly adept. He flicks through two books - a green, fabric-bound one filled with diagrams and notes, and a smaller notebook that he occasionally scribbles in."
    "He is concentrating… but I am intrigued by this garden."

    menu:
        "Ask him about his garden.":
            # Atticus AFF up
            $ add_aff(1)
            $ talked_garden = True
            mc "How did you cultivate this garden? It's got such a variety of plants, I'd hardly know where to begin."
            "Atticus laughs, setting down the flower he had been seeding."
            at "Well, mine was quite simple at first! I didn't have quite the spread you see before you until a couple of years into my work."
            at "I began with just vegetables. All the standard things you can forage for, just enough to make meals with…"
            "He began to smile brighter, as if he wasn't quite aware he was doing it."
            at "One day, there was a traveller coming through the woods. He didn't see me - I was far too scared for that. But he set up camp a few minutes away."
            at "I kept coming back to watch him. He would examine every leaf, every berry, every blade of grass he saw and dissect it for his notebook."
            "Atticus picked up the green book and held it aloft."
            at "It just so happened that he left it behind. Completely forgotten."
            mc "Did he not come back and look for it?"
            at "I'm fairly certain he made several notes - this one was only half-filled. But, it meant I knew a lot more about the forest than before."
            at "So, I gave myself a mission: to find and grow every plant he had written about for my garden and find as many uses for them as possible!"
            at "Food, medicine, salves - even just decoration. It's been a lot of trial and error."
            mc "Such as the flowers that make you sneeze?"
            "Atticus turns bright red, rubbing his nose in painful memory."
            at "Such as the puffing petal, yes."
            "We both chuckle as he returns to preparing the ingredients."
        "Stay quiet.":
            "We are both working - and the last thing I want is to startle Atticus so badly he ruins the potion."
            "He's so skittish and jumpy normally, I hate to think what would happen around a cauldron…"
            "Nevertheless, we are both content to work away. I harvest flowers and herbs he asks for as he prepares the ingredients."
            "He never stops smiling, even when focussed. I must be making an alright impression, even if the first one was a little unfortunate."


    "When my basket is full, Atticus checks through it with a smile."
    at "I… think that's everything! Now it's time to brew it."
    "We go back inside, Atticus setting the basket on the side and setting out every ingredient."
    "I have no idea what everything is for, but I trust him enough."
    "He takes a moment to look through his shelves, pulling a few books from them."
    at "I know there's one here… one curses and hexes… aha!"
    "He pulls a purple cover from the shelf."
    at "Would you mind starting the fire? We'll need a rolling boil for this one!"
    mc "On it."
    "As he reads through, I prepare the cauldron. I look back at the shelves, curious."
    mc "If you don't mind me asking, where did you find all of these books?"

    if talked_garden:
        mc "I know you found this book when it was left behind, but surely not every book was found the same?"


    "Atticus laughs, surprised."
    at "Why do you ask?"
    mc "Well, simply put, I would like my own copy of a curse-breaker book from whatever trade or market you got it from!"
    "At my words, his face falls, and he busies himself in the book."
    at "No trades nor markets, unfortunately. I, um… can't go anywhere humans are, remember?"
    "He taps the end of his horn."
    mc "Oh… yes, I'm sorry."
    mc "I suppose… I had just- well, forgotten that part of you. In the sense that it no longer matters to me."
    "Atticus pauses before laughing brightly."
    at "I'm honestly quite happy to hear that. I can't remember the last time I was treated… normally. Without any special notice either of fear or malice."
    at "Thank you!"
    mc "Ha, no problem."
    "With the fire boiling, Atticus ushers me away to sit in the chair as he works on the potion. He's calm and meticulous, always referring back to the litany of notes by his side."

    menu:
        "\"Doesn't it get lonely here?\"":
            # Atticus AFF down
            $ sub_aff(1)
            "He freezes for a moment, then drops a few berries into the cauldron."
            at "Well… yes."
            at "But it's either be lonely or be in danger at every moment, so…"
            "He swallows thickly, blinking rapidly as he reads through the book."
        "\"If you could go anywhere, where would you go?\"":
            $ ask_trip = True
            # Atticus AFF up
            "Atticus thinks in silence for a moment, dropping a few berries into the cauldron."
            at "I… I don't know."
            at "I haven't really known anywhere except this forest for quite some time…"
            mc "Come on. Anywhere in the kingdom - no, anywhere in the world."
            "Atticus chuckles, smoothing a hand over the page in the book."
            at "Maybe… maybe the mountains."
            mc "Why the mountains?"
            at "I'm always surrounded by foliage. I'd love to be able to be up high, still feeling the air on my skin, but really seeing the world all around me…"
            at "I can't imagine what cities look like from above. Or forests, or lakes, seeing the rivers cut through the world…"
            "He smiles and shakes his head."
            at "It's a nice thought."

            if (at_aff >=11) and (mentality != 3):
                mc "I see no reason why it's not a possibility."
                mc "I mean… I am a fantastic knight. By my side, you could go anywhere in the world and I'll be able to protect you."
                mc "I could even show you the palace, if you want. I have some words for the king that warrant a visit, after all…"
                "Atticus bursts into laughter, stepping away from the cauldron to avoid knocking into it."
                at "My own knight in shining armor! That would, uh…"
                at "Certainly be interesting."
                else:
                mc "It is a nice thought."
                "I have travelled all over the kingdom, seen great beasts and defeated them, all the while he has been scared of people like me…"
                "One day, Atticus."
                "He smiles sadly back at me, bowing his head."
                at "It is."





    "Atticus drops in a final ingredient - and the cauldron bubbles, turning a thick purple colour. Even the fire underneath roars more viciously."
    at "Okay… I think it's done!"
    mc "Just like that?"
    at "I think!"
    mc "Please stop saying that you just 'think', I am about to ingest this."
    at "Sorry."
    "He takes a ladle and fills a bottle with the liquid, holding it out to me."
    at "Blow on it first. I don't want you to scald yourself."
    "I do as he says. A thick, pungent smell wafts up from the bottle…"
    at "It… won't taste very good. But with any luck, it should slow down the curse's progression!"
    "His smile doesn't quite reach his eyes."

    menu:
        "Hesitate. Is he sure about this?":
            # Atticus AFF 
            $ sub_aff(1)
            "He catches my hesitation and smiles awkwardly."
            at "Don't worry. There's no worm tails or goatvenom in there."
            "Do goats even have venom?"
            "I still laugh, a little appeased, despite how unappetising the potion remains to be."
            mc "Alright…"
            "I take a sip."
            "..."
            "It tastes worse than it smells, and it already smells terrible."
            at "You may want to just… chug the rest."
            "Ugh. I know he's right. It doesn't mean I'm happy about it."
            "With a final prayer to whatever divinity was still looking out for me, I swallow it all down."
        "Bottoms up!":
            # Atticus AFF up
            $ add_aff(1)
            "Well, there was no point in delaying the inevitable."
            "I pinch my nose, tilt my head back, and swallow it in one go."
            at "Impressive!"
            "As soon as it's done though, I fight to keep it down my throat."
            mc "That… did not taste good."
            at "I'm not surprised. Sorry!"
            "He doesn't sound too sorry."


    "After a few moments, I glance at Atticus."
    mc "So… how long should this take?"
    at "Not too long. Should be…"
    # show cg
    at "... soon."
    at "That's… not supposed to happen. I'm so sorry!"
    "In a split second, all of the scales on my body had changed from their blood red, to shining, iridescent colours."
    mc "This… is new."
    "Atticus, mortified, holds his hands over his face."
    at "I'm so sorry! I was confident that the potion would affect the scales, but I thought I was going to slow down the curse, not…"
    at "This!"

    menu:
        "\"Well… no harm done.\"":
            mc "I mean… it's not exactly what I was hoping for."
            at "No! No, nor I! Oh, I'm so sorry."
            mc "It's alright, Atticus. Really."
            "He reaches up to fiddle with his glasses, his tail swooping around like a whip."
            at "I'll cook stew for tonight to make up for this."
            at "I… I think it will fade soon?"
        "\"This is so funny.\"":
            # Atticus AFF up
            $ add_aff(1)
            "I can't help but think this way. Sure, it's nowhere near the desired reaction."
            "But all of that build-up, all of that worry…"
            "Just for me to spontaneously change colors."

    if mentality == 1:
        "I start laughing, looking down at my multi-colored arms."
        mc "Look! It's like an artist's attic exploded!"
        "Atticus freezes, eyes locked onto me - and then starts laughing with me, relief flooding his face."
    elif mentality == 2:
        "I chuckle, running my hands over the scales. They change color with my touch."
        mc "See? It's not so bad. At the very least, a temporary party trick."
        "Atticus rubs the back of his neck, although chuckles along with me."
    elif mentality == 3:
        "Despite my constant worries about the curse, it's hard not to crack a smile in the moment."
        mc "See? This is almost pretty."
        "Atticus sighs, smiling back at me."


    "Even if I wasn't yet cured, at least I was having fun with it."


    "Still, Atticus looks back at the cauldron, still with the remains of the potion simmering at the bottom."
    at "It's just a matter of tweaking ratios… I'm not giving up though!"

    if mentality == 1:
        mc "It's alright! I'm not either."
        mc "We at least know we're on the right track. Every mistake is a step forwards, right?"
    elif mentality == 2:
        mc "It's okay, Atticus, really."
        mc "This was just the first try, right? We'll get there."
    elif mentality == 3:
        "I take in a deep breath."
        mc "It's okay, Atticus. We'll… we'll get there."
        "This is just the first step. I'll make it. I have to."


    at "R-Right!"
    "He scratches the back of his head."
    at "Do you- um…"
    mc "You can ask me, Atticus. You can ask me anything."
    "He smiles gratefully, but still turns away to head back to the books and cauldron."
    at "Could… do you think you'll be okay if I can't…"
    "He mumbles to himself. I pause."
    mc "What… do you mean?"
    at "I-I mean- if…"
    "He swallows, then looks at me with a bright smile."
    at "What's your favourite colour? If the next potion doesn't work, I can at least try to make your scales turn the way you'd prefer!"
    mc "Well… I would prefer you to focus on curing them rather than changing them. But…"

    # PLAYER INPUT
    # What's your favourite color?
    python:
        fav_color = renpy.input("What's your favourite color?", default = "", length=10,)

        fav_color = povname.strip()

    mc "If you can't do it straight away, [fav_color] is my favourite."
    "Atticus nods eagerly."
    at "I'll see what I can do!"
    "He works over the books for the rest of the day, even as my scales turn back to the normal red."
    "Since there's nothing much for me to do, I relax in the chair and let him ramble about plants and magic as he needs to."
    "He's always been dedicated - whether to his garden or me - but now, he focuses with an intensity I've never seen before."
    "He's never wavered in his kindness to me, even when I was little more than an ill-trusting, sick patient who could still do damage with a sword."
    "Even if he was awkward at first."
    "..."

    menu:
        "He's grown on me.":
            # platonic route
            "I had never thought I would befriend a unicorn - well, up until a few days ago, I didn't know if unicorns truly existed."
            "But Atticus isn't just a unicorn; he's a damn good man, and someone worthy of a knight's protection."
            "He is effortlessly kind, intensely passionate when called for - and maybe a little too shy at times."
            "But I wouldn't want him to be any other way than himself."
        "I think I might be catching feelings for him...…":
            $ mc_crush = True
            "If you had asked me a mere few days ago whether or not I would feel this way, I would have laughed it off."
            "A lonely unicorn in the middle of the woods, and a retired knight still lurking at the borders of [their] kingdom…"
            "Perhaps it's a more cliché pair than I would have admitted. But I can't deny how I feel."
            "He is effortlessly kind, intensely passionate when called for - and maybe a little too shy at times."
            "But I wouldn't want him to be any other way than himself."
            "..."
            "Also, he is ridiculously pretty. I will assume it is from the unicorn genetics until proven otherwise."


    "He reaches up to push his glasses up his nose for the fourth time and I can't help but smile."
    "I don't know what my curse holds in store for me."

    if mentality == 1:
        "But if Atticus lets me stick around, I think I'll be alright."
    elif mentality == 2:
        "But Atticus is determined to heal me. And, as nervous as I am, I believe him."
        "Sometimes, I can't stand the feeling of my new claws. But being around Atticus makes it all bearable."
    elif mentality == 3:
        "I don't know what I'm going to do if I turn into… what we think I will."
        "I don't know what to do about Atticus. If I leave, I shall be alone forevermore. If I stay, he will come to resent my new form."
        "We'd better heal me quickly."


    "For now, Atticus works diligently away. And I believe in our efforts more than anything else."

    jump scene_7
