label scene_6:
    "I barely see Atticus during the next day - he spends as many hours of the day and night studying the dagger as possible."
    "But in the night, I am shaken awake."
    stop music fadeout 0.5 
    hide darken
    show atticus eshocked at forest_night
    with dissolve
    at "[povname]!"
    mc "What is it?"
    "His eyes are glassy from lack of sleep, purple bags deep underneath them. His hair is frizzier than ever, mussed from lack of sleep."
    at "Dragon claw."
    "I cautiously raise my hand."
    mc "These?"
    "Atticus sighs."
    at esad msad_c "Sorry. I'm very tired."
    at eneutral_o msad_o "The dagger is a dragon claw dagger. It took me a while to find the notes on it, but I think I'm right."
    mc "Okay… what does that mean?"
    play music sad fadein 1.0
    at esad msad_c "Dragon claw daggers are very rare, mostly because they take so long to make correctly. That, and they're banned due to how dangerous and… and cruel they are."
    at "Dragon claw daggers are used to inflict a curse onto their victim. They will slowly transform into a dragon - and, once that happens, the poachers return to harvest their scales and claws."
    "That's… unnerving."
    mc "You mean… they're making their own prey from innocent people?"
    at esad_la msad_o "I-"
    show atticus esad msad_c
    extend "yes."
    "His ears fall to fit his frown."
    at eangry "But now we know what it is, I can find a potential cure much quicker. I can't promise it immediately, but…"
    "He trails off."
    at esad msad_c "I'm sorry."
    mc "It's… it's okay."
    "So I really am turning into a red dragon. The very one I had once protected the kingdom against."
    "Atticus is still watching me. I try to smile."
    mc "Could I… just have a moment alone? To process."
    "Atticus nods."
    at eshocked mshocked "Of course! Of course, I…"
    at esad msad_o "I'll be out the back if you need me. I know we don't have a lot, but I'll give you what space I can."
    mc "Thank you."
    hide atticus with dissolve
    "He lingers for a moment more, but soon turns away and leaves the cottage."
    window hide
    $ quick_menu = False
    show darken with dissolve
    $ nvl_mode = True
    nvl clear
    window auto show
    $ quick_menu = True
    n "I sigh and sit up, hunched over. The skin on my legs itches and pulls oddly with the movement."
    n "..."
    n "The scales have spread, circling my chest, not quite meeting in the middle but spreading down my thighs. My feet are entirely covered, and my feet bend awkwardly."
    n "There are claws poking out my socks, the fabric ripped." 
    nvl clear
    n "The sun is barely up. The sky outside is pink from what I can see through the window."
    n "After a few more moments, I can hear the movements of Atticus out the back. Some soft thuds, as though he was moving items around, before the familiar grind of a pestle and mortar."
    nvl clear

    if mentality == 1:
        n "The sound is soothing. The familiarity and domesticity of it."
        n "It's hard to ignore the changes - how the new skin itches and the implications that I now know."
        n "Turning into a dragon… that was the sort of thing that happened in stories."
        nvl clear
        n "Well, I had said I was the stuff of legends."
        n "There will be a solution. I have enough faith in Atticus to push through - I should have faith in myself to hold onto what remains human."
        nvl clear
    elif mentality == 2:
        n "The sound is soothing. The familiarity and domesticity of it."
        n "It's hard to ignore the changes - how the new skin itches and the implications that I now know."
        n "Turning into a dragon… that was the sort of thing that happened in stories."
        nvl clear
        n "If what Atticus says is true, I will be nothing but a story soon. Not human, not knight, but the antithesis."
        n "Who would I become if I could not protect, if I could not serve? My life is built around honor… is there any honor to find in a dragon?"
    elif mentality == 3:
        n "It annoys me. A sound I once found soothing now grates on my nerves, between my teeth, unrelenting."
        n "I will turn into a dragon. A red dragon, one that soars over skylines and destroys everything until the world is ash below it."
        n "I cannot stomach the feeling. My heartbeat sits in my throat until I choke on it."
        nvl clear
        n "Am I even still human anymore? I am not currently a dragon, but if what Atticus says is true, it's only a matter of time until I am stripped of all that I once knew."
        n "It takes everything in me not to collapse into melancholy. A part of me wonders if I should anyway."

    nvl clear
    n "There's time. I have to remember that. I am not yet the dragon I swore to slay."
    n "Atticus will find a solution. Until then, I must remain strong."
    n "..."
    n "I can't stand sitting here any longer."
    n "I stand up on my new feet, working out how to walk after a few stumbles, and leave the cottage."

    window hide
    $ quick_menu = False
    scene outside:
        zoom 0.5
    $ nvl_mode = False
    nvl clear
    show layer screens:
        matrixcolor None
    window auto show
    $ quick_menu = True
    play music warm fadein 0.5 fadeout 0.5
    "Following the sounds of work, I soon find Atticus. As he catches sight of me, his eyebrows shoot up his forehead."
    show atticus eshocked mshocked with dissolve
    at  "Are you okay?"
    mc "Yes, I'm fine. I just… can I help? I feel terrible sitting inside all day while you work away."
    "His worry quickly fades away, and he pushes a basket into my hands."
    at ehappy_c mhappy_o "I'd love the help! Could you pick some of the flowers by that bush?"
    "I nod and walk over, taking a stem into my hands- "
    at eshocked mshocked "Not that one! Sorry. The small green ones. The flower you're holding will make you sneeze uncontrollably."
    mc "Oh, got it."
    mc "Why do you have that flower? The one that makes you sneeze?"
    at ehappy mhappy_c "When diluted, it can provide relief for colds. But if you use too much, it just makes you sneeze out all of the illness. Effective, but… a little painful."
    mc "Any chance we can get me to sneeze out a curse?"
    "Atticus chuckles, but his ears twitch just enough for me to notice."
    at ehappy_c mhappy_c "I am actually working on a potion right now to do just that! No sneezing required."
    mc "Really?"
    at mhappy_o "Yep! I can't promise it will break the curse, but my hope is that it will slow the transformation until I have time to find a proper cure."
    mc "That's very thoughtful. And a good idea - if we can do anything to stop me from turning any more than I already have…"
    "Atticus pauses to look over at me, his smile confident and reassuring, eyes slightly crinkled."
    at eangry mhappy_c "We'll find a way. Don't worry."
    at ehappy "Now - the small green flowers, please. And the angel's bloom after that."
    window hide
    $ quick_menu = False
    show darken with dissolve
    $ nvl_mode = True
    nvl clear
    window auto show
    $ quick_menu = True
    n "It's simple work, but Atticus gives me clear instructions and I can follow them."
    n "It's just enough for my mind to focus, to think of anything other than the scratch of my scales against my clothes."
    n "I am uneducated in medicine myself, merely trusting the magic of the palace healers when needed. No human can cast magic normally, although their salves and tinctures always worked wonders."
    nvl clear
    n "That being said, I have seen magic many times before. Either through the thick potions and hexes woven from magical plants, to the cursed weapons those poachers held. I know of its power - if not of its intricacies."
    n "For something close enough to a human, Atticus is incredibly adept. He flicks through two books - a green, fabric-bound one filled with diagrams and notes, and a smaller notebook that he occasionally scribbles in."
    n "He is concentrating… but I am intrigued by this garden."
    nvl clear

    menu:
        "Ask him about his garden.":
            # Atticus AFF up
            $ add_aff(1)
            $ talked_garden = True
            window hide
            $ quick_menu = False
            hide darken 
            show atticus mshocked eneutral_o 
            with dissolve
            $ nvl_mode = False
            $ quick_menu = True
            window auto show
            mc "How did you cultivate this garden? It's got such a variety of plants, I'd hardly know where to begin."
            show atticus mhappy_c
            "Atticus laughs, setting down the flower he had been seeding."
            at bsad mhappy_o tloop "Well, mine was quite simple at first! I didn't have quite the spread you see before you until a couple of years into my work."
            at bhappy eneutral_la mshocked up "I began with just vegetables. All the standard things you can forage for, just enough to make meals with…"
            "He began to smile brighter, as if he wasn't quite aware he was doing it."
            at mhappy_o "One day, there was a traveller coming through the woods. He didn't see me - I was far too scared for that. But he set up camp a few minutes away."
            at eneutral_o mshocked "I kept coming back to watch him. He would examine every leaf, every berry, every blade of grass he saw and dissect it for his notebook."
            show atticus eneutral_la
            "Atticus picked up the green book and held it aloft."
            at ehappy_c  mhappy_o "It just so happened that he left it behind. Completely forgotten."
            mc "Did he not come back and look for it?"
            at ehappy mhappy_o "I'm fairly certain he made several notes - this one was only half-filled. But, it meant I knew a lot more about the forest than before."
            at bangry tneutral "So, I gave myself a mission: to find and grow every plant he had written about for my garden and find as many uses for them as possible!"
            at ehappy_c mhappy_o "Food, medicine, salves - even just decoration. It's been a lot of trial and error."
            mc "Such as the flowers that make you sneeze?"
            "Atticus turns bright red, rubbing his nose in painful memory."
            $ blush_light = True
            at esad_la mhappy_c "Such as the puffing petal, yes."
            "We both chuckle as he returns to preparing the ingredients."
            $ blush_light = False
        "Stay quiet.":
            n "We are both working - and the last thing I want is to startle Atticus so badly he ruins the potion."
            n "He's so skittish and jumpy normally, I hate to think what would happen around a cauldron…"
            n "Nevertheless, we are both content to work away. I harvest flowers and herbs he asks for as he prepares the ingredients."
            n "He never stops smiling, even when focussed. I must be making an alright impression, even if the first one was a little unfortunate."
            window hide
            $ quick_menu = False
            hide darken with dissolve
            $ nvl_mode = False
            $ quick_menu = True
            window auto show
            nvl clear


    "When my basket is full, Atticus checks through it with a smile."
    at bhappy ehappy_c mhappy_o "I… think that's everything! Now it's time to brew it."
    scene interior day with dissolve:
        zoom 0.5
    "We go back inside, Atticus setting the basket on the side and setting out every ingredient."
    "I have no idea what everything is for, but I trust him enough."
    "He takes a moment to look through his shelves, pulling a few books from them."
    show atticus bangry eneutral_la mpout tloop with dissolve
    at "I know there's one here… one curses and hexes… aha!"
    show atticus msmile_c
    "He pulls a purple cover from the shelf."
    at ehappy @ mhappy_o "Would you mind starting the fire? We'll need a rolling boil for this one!"
    mc "On it."
    show atticus bneutral eneutral_la
    "As he reads through, I prepare the cauldron. I look back at the shelves, curious."
    mc "If you don't mind me asking, where did you find all of these books?"

    if talked_garden:
        mc "I know you found this book when it was left behind, but surely not every book was found the same?"

    show atticus eshocked mhappy_c
    "Atticus laughs, surprised."
    at eneutral_o mhappy_o tneutral "Why do you ask?"
    mc "Well, simply put, I would like my own copy of a curse-breaker book from whatever trade or market you got it from!"
    show atticus bsad down eneutral_la tloop msad_c
    "At my words, his face falls, and he busies himself in the book."
    at esad @ msad_o "No trades nor markets, unfortunately. I, um… can't go anywhere humans are, remember?"
    "He taps the end of his horn."
    mc "Oh… yes, I'm sorry."
    mc "I suppose… I had just- well, forgotten that part of you. In the sense that it no longer matters to me."
    show atticus bshocked eshocked mshocked 
    "Atticus pauses before laughing brightly."
    at ehappy_c mhappy_o tneutral "I'm honestly quite happy to hear that. I can't remember the last time I was treated… normally. Without any special notice either of fear or malice."
    at ehappy mid "Thank you!"
    mc "Ha, no problem."
    hide atticus with dissolve
    "With the fire boiling, Atticus ushers me away to sit in the chair as he works on the potion. He's calm and meticulous, always referring back to the litany of notes by his side."

    menu:
        "\"Doesn't it get lonely here?\"":
            # Atticus AFF down
            $ sub_aff(1)
            "He freezes for a moment, then drops a few berries into the cauldron."
            show atticus down bsad eneutral_la msad_c with dissolve
            at @ msad_o "Well… yes."
            at esad @ msad_o "But it's either be lonely or be in danger at every moment, so…"
            show atticus eneutral_la tloop
            "He swallows thickly, blinking rapidly as he reads through the book."
        "\"If you could go anywhere, where would you go?\"":
            $ ask_trip = True
            # Atticus AFF up
            "Atticus thinks in silence for a moment, dropping a few berries into the cauldron."
            show atticus down econfused msad_o
            at "I… I don't know."
            at bsad @ mshocked "I haven't really known anywhere except this forest for quite some time…"
            show atticus msad_c
            mc "Come on. Anywhere in the kingdom - no, anywhere in the world."
            show atticus mid mhappy_c
            "Atticus chuckles, smoothing a hand over the page in the book."
            at esad_la @ mhappy_o "Maybe… maybe the mountains."
            mc "Why the mountains?"
            at ehappy @ mhappy_o "I'm always surrounded by foliage. I'd love to be able to be up high, still feeling the air on my skin, but really seeing the world all around me…"
            at bsad esad_la @ mhappy_o"I can't imagine what cities look like from above. Or forests, or lakes, seeing the rivers cut through the world…"
            "He smiles and shakes his head."
            at mhappy_c "It's a nice thought."

            if (at_aff >=11) and (mentality != 3):
                mc "I see no reason why it's not a possibility."
                mc "I mean… I am a fantastic knight. By my side, you could go anywhere in the world and I'll be able to protect you."
                mc "I could even show you the palace, if you want. I have some words for the king that warrant a visit, after all…"
                "Atticus bursts into laughter, stepping away from the cauldron to avoid knocking into it."
                at eshocked mshocked "My own knight in shining armor! That would, uh…"
                at ehappy mhappy_o "Certainly be interesting."
            else:
                mc "It is a nice thought."
                "I have travelled all over the kingdom, seen great beasts and defeated them, all the while he has been scared of people like me…"
                "One day, Atticus."
                "He smiles sadly back at me, bowing his head."
                at esad_la mhappy_c "It is."

    play music light fadein 0.5 fadeout 0.5
    "Atticus drops in a final ingredient - and the cauldron bubbles, turning a thick purple colour. Even the fire underneath roars more viciously."
    at bhappy ehappy mhappy_o tneutral "Okay… I think it's done!"
    mc "Just like that?"
    at eneutral_o "I think!"
    mc "Please stop saying that you just 'think', I am about to ingest this."
    at esad msad_c down tloop "Sorry."
    show atticus eneutral_la
    "He takes a ladle and fills a bottle with the liquid, holding it out to me."
    at eneutral_o mhappy_o "Blow on it first. I don't want you to scald yourself."
    show atticus mhappy_c
    "I do as he says. A thick, pungent smell wafts up from the bottle…"
    at esad @ mhappy_o "It… won't taste very good. But with any luck, it should slow down the curse's progression!"
    "His smile doesn't quite reach his eyes."

    menu:
        "Hesitate. Is he sure about this?":
            # Atticus AFF 
            $ sub_aff(1)
            "He catches my hesitation and smiles awkwardly."
            at @ mhappy_o "Don't worry. There's no worm tails or goatvenom in there."
            "Do goats even have venom?"
            "I still laugh, a little appeased, despite how unappetising the potion remains to be."
            mc "Alright…"
            "I take a sip."
            "..."
            "It tastes worse than it smells, and it already smells terrible."
            at bsad eneutral_o @ msad_o "You may want to just… chug the rest."
            show atticus msmile_c
            "Ugh. I know he's right. It doesn't mean I'm happy about it."
            "With a final prayer to whatever divinity was still looking out for me, I swallow it all down."
        "Bottoms up!":
            # Atticus AFF up
            $ add_aff(1)
            "Well, there was no point in delaying the inevitable."
            "I pinch my nose, tilt my head back, and swallow it in one go."
            at bshocked eshocked mshocked "Impressive!"
            "As soon as it's done though, I fight to keep it down my throat."
            mc "That… did not taste good."
            at bhappy eneutral_o mhappy_c msmile_o "I'm not surprised. Sorry!"
            show atticus msmile_c
            "He doesn't sound too sorry."


    "After a few moments, I glance at Atticus."
    mc "So… how long should this take?"
    at eneutral_c msad_o "Not too long. Should be…"
    show darken
    show cg3 
    with dissolve
    at "... soon."
    at "That's… not supposed to happen. I'm so sorry!"
    "In a split second, all of the scales on my body had changed from their blood red, to shining, iridescent colours."
    mc "This… is new."
    "Atticus, mortified, holds his hands over his face."
    at "I'm so sorry! I was confident that the potion would affect the scales, but I thought I was going to slow down the curse, not…"
    at "This!"
    hide cg3 
    hide darken
    show atticus bsad eshocked mshocked tloop
    with dissolve
    menu:
        "\"Well… no harm done.\"":
            mc "I mean… it's not exactly what I was hoping for."
            at eangry mshocked "No! No, nor I! Oh, I'm so sorry."
            mc "It's alright, Atticus. Really."
            "He reaches up to fiddle with his glasses, his tail swooping around like a whip."
            at esad_la msad_c twag "I'll cook stew for tonight to make up for this."
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
                show atticus eshocked msad_c
                "Atticus freezes, eyes locked onto me -"
                show atticus ehappy_c mhappy_o
                extend "and then starts laughing with me, relief flooding his face."
            elif mentality == 2:
                "I chuckle, running my hands over the scales. They change color with my touch."
                mc "See? It's not so bad. At the very least, a temporary party trick."
                show atticus esad mhappy_c
                "Atticus rubs the back of his neck, although chuckles along with me."
            elif mentality == 3:
                "Despite my constant worries about the curse, it's hard not to crack a smile in the moment."
                mc "See? This is almost pretty."
                "Atticus sighs, smiling back at me."
                show atticus esad mhappy_c


            "Even if I wasn't yet cured, at least I was having fun with it."

    play music main_theme fadein 0.5 fadeout 0.5
    "Still, Atticus looks back at the cauldron, still with the remains of the potion simmering at the bottom."
    at eangry mhappy_c tneutral "It's just a matter of tweaking ratios… I'm not giving up though!"

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


    at mhappy_o "R-Right!"
    "He scratches the back of his head."
    at esad_la mhappy_c"Do you- um…"
    mc "You can ask me, Atticus. You can ask me anything."
    "He smiles gratefully, but still turns away to head back to the books and cauldron."
    at esad "Could… do you think you'll be okay if I can't…"
    "He mumbles to himself. I pause."
    mc "What… do you mean?"
    at bsad eneutral_la msad_o "I-I mean- if…"
    show atticus eneutral_o mhappy_c
    "He swallows, then looks at me with a bright smile."
    at bshocked @ mhappy_o "What's your favourite colour? If the next potion doesn't work, I can at least try to make your scales turn the way you'd prefer!"
    mc "Well… I would prefer you to focus on curing them rather than changing them. But…"

    # PLAYER INPUT
    # What's your favourite color?
    python:
        fav_color = renpy.input("What's your favourite color?", default = "", length=10,)

        fav_color = fav_color.strip()

    mc "If you can't do it straight away, [fav_color!l] is my favourite."
    "Atticus nods eagerly."
    at ehappy_c mhappy_o "I'll see what I can do!"
    hide atticus with dissolve
    "He works over the books for the rest of the day, even as my scales turn back to the normal red."
    window hide
    $ quick_menu = False
    show darken with dissolve
    $ nvl_mode = True
    nvl clear
    window auto show
    $ quick_menu = True
    n "Since there's nothing much for me to do, I relax in the chair and let him ramble about plants and magic as he needs to."
    n "He's always been dedicated - whether to his garden or me - but now, he focuses with an intensity I've never seen before."
    n "He's never wavered in his kindness to me, even when I was little more than an ill-trusting, sick patient who could still do damage with a sword."
    n "Even if he was awkward at first."
    nvl clear

    menu:
        "He's grown on me.":
            # platonic route
            n "I had never thought I would befriend a unicorn - well, up until a few days ago, I didn't know if unicorns truly existed."
            n "But Atticus isn't just a unicorn; he's a damn good man, and someone worthy of a knight's protection."
            n "He is effortlessly kind, intensely passionate when called for - and maybe a little too shy at times."
            n "But I wouldn't want him to be any other way than himself."
        "I think I might be catching feelings for him...…":
            $ mc_crush = True
            n "If you had asked me a mere few days ago whether or not I would feel this way, I would have laughed it off."
            n "A lonely unicorn in the middle of the woods, and a retired knight still lurking at the borders of [their] kingdom…"
            n "Perhaps it's a more cliché pair than I would have admitted. But I can't deny how I feel."
            nvl clear
            n "He is effortlessly kind, intensely passionate when called for - and maybe a little too shy at times."
            n "But I wouldn't want him to be any other way than himself."
            n "..."
            n "Also, he is ridiculously pretty. I will assume it is from the unicorn genetics until proven otherwise."


    nvl clear
    n "He reaches up to push his glasses up his nose for the fourth time and I can't help but smile."
    n "I don't know what my curse holds in store for me."

    if mentality == 1:
        n "But if Atticus lets me stick around, I think I'll be alright."
    elif mentality == 2:
        n "But Atticus is determined to heal me. And, as nervous as I am, I believe him."
        n "Sometimes, I can't stand the feeling of my new claws. But being around Atticus makes it all bearable."
    elif mentality == 3:
        n "I don't know what I'm going to do if I turn into… what we think I will."
        nvl clear
        n "I don't know what to do about Atticus. If I leave, I shall be alone forevermore. If I stay, he will come to resent my new form."
        n "We'd better heal me quickly."


    n "For now, Atticus works diligently away. And I believe in our efforts more than anything else."
    nvl clear

    jump scene_7
