label scene_5:
    window hide
    $ quick_menu = False
    show darken with dissolve
    $ nvl_mode = True
    nvl clear
    window auto show
    $ quick_menu = True
    play music warm fadein 0.5 fadeout 0.5
    play ambience fireplace fadein 0.5 fadeout 0.5
    n "I wake up and feel more rested than I have in a week."
    n "Perhaps the exertion yesterday did me good. My body is relaxed, my annoyance from being cooped up gone, and my fingers luxuriously scratch up the covers."
    n "..."
    n "My fingers now end in claws, the scales smoothing down from the knuckles into thick cartilage. I've torn a hole in Atticus's bedsheets."
    n "Both arms now. When I reach up to my shoulders, I can feel the scales slip behind and around my neck."
    nvl clear

    menu:
        "Maybe those hunters were right…":
            $ mentality = 2
            n "Part of me baulks at acknowledging those miscreants as right… but it's hard to deny."
            n "The parts of me I can see with my own eyes are no longer human. They are scaled, red and angry, ripping holes in innocent folks' bedsheets."
            n "I can't hide my arms anymore. The rot has spread too far."
            n "But… I am still human. I think with my own head and speak with my own voice."
            n "For now, at least."
            window hide
            $ nvl_mode = False
            window auto show
            hide darken
            show atticus
            with dissolve
            window auto show
            "As I ponder, I see Atticus raise his head. He had clearly slept at the table, his hair mussed and flat on one side."
            at bhappy ehappy_c @ msmile_o "You're awake. Good morning!"
            mc "Good morning, Atticus."
        "They were right - I am a monster.":
            $ mentality = 3
            stop music fadeout 0.5
            play ambience creepy fadein 0.5 fadeout 0.5
            n "I stare at my hands - my clawed and scaled hands - and know that if in some world I am still considered human, it is a fast ending one."
            n "Is this how monsters begin? Torn from the comfort, the familiarity of being a malleable human, cursed to become that which terrifies what they once were?"
            show red haze with dissolve:
                zoom 0.5 blend "multiply" alpha 0.5
            n "What if I become one? What if soon I shall tour the skies and burn down the villages I swore to protect, only to be slain by a knight who looks as I once did?"
            n "When does the mind fade? After the skin or the heart?"
            window hide
            $ nvl_mode = False
            window auto show
            hide darken
            show atticus up bangry eangry mangry 
            with dissolve
            window auto show
            at "[povname]!"
            "I feel his hands around mine, soft and padded with human fingerprints."
            play ambience fireplace fadein 0.5 fadeout 0.5
            hide red haze with dissolve
            "I snap out of whatever cursed state I was in, looking down at my clenched hands-oh."
            "I had clenched them so tight that my claws had dug into the soft flesh of my own palms, blood seeping from them."
            show atticus bsad msad_c
            mc "Atticus, I…"
            "I take in a breath. Long and slow."
            mc "My apologies. I… was lost in my head."
            show atticus mid mhappy_c
            play music warm fadein 0.5 fadeout 0.5
            "Atticus gently pried my hands open, careful to avoid the blood welling in my palms."
            at ehappy_o tloop @ mhappy_o "That's perfectly alright. Just… take a moment with me."
            at bneutral eneutral_c @ mhappy_o "In and out… that's it."
            "He's patient. Almost too patient, as if he'd been expecting me to act this way."
            "But, I comply. I take the breaths and let him dab at my new wounds with some honey salve to disinfect them."
            at bhappy eneutral_o @ mhappy_o "Are you alright?"
            mc "Yes. My apologies for startling you."
            at bshocked ehappy_c @ mhappy_o "No need to apologise. As long as you're alright."
        "I am no monster.":
            $ mentality = 1
            n "I take a breath - long and slow…"
            n "I am not a monster. My human skin may be fading, but my heart and honor has never, and will never, waver."
            n "I am a human, and more importantly, a knight who swore to protect and serve the kingdom."
            n "No scale nor claw could stop me from doing that. If the great dragon I had once slashed from the sky could not, then whatever this curse was would not either."
            window hide
            $ nvl_mode = False
            window auto show
            hide darken
            show atticus
            with dissolve
            window auto show
            "As I ponder, I see Atticus raise his head. He had clearly slept at the table, his hair mussed and flat on one side."
            at bhappy ehappy_c @ msmile_o "You're awake. Good morning!"
            mc "Good morning, Atticus."

    show atticus bhappy eneutral_o msmile_c
    "His smile was gentle, as Atticus normally tended to be, and he got to his feet."
    at bshocked @ mhappy_o "I'll be out in the garden today - just behind the house. It needs a little maintenance, so don't be too surprised if I'm out all day."
    mc "You normally are, so I'll refrain from causing a fuss."
    show atticus up ehappy twag 
    "Atticus giggled, his tail swishing in the air."
    at bshocked ehappy_c @ mhappy_o "I'm hoping there'll be plenty of crops today… including for my specialty stew, if you're interested."
    "I can barely think of the specialty stew before my stomach growls. Atticus laughs, broad and open, louder than I've ever heard him."
    mc "Ha, sorry! Yesterday must have taken a lot out of me."
    at mid eneutral_o tloop "Don't apologise! I'm glad you like my cooking. I work very hard on it."
    at bneutral ehappy_c "No stew yet, although do help yourself to anything in my pantry. Bread, honey - and the jam is fairly fresh, so… enjoy!"
    hide atticus with dissolve
    "He does a funny little tilt, his cheeks full with a smile, before collecting his basket and heading out the door."
    "Once he leaves, I do indeed help myself to bread, honey and jam, all of which taste sweet and fresh. Atticus really does know his way around food."
    $ quick_menu = False
    show darken with dissolve
    $ nvl_mode = True
    nvl clear
    window auto show
    $ quick_menu = True
    n "However, there's still very little to do, despite the fact that I can now walk around. I get the feeling that Atticus usually spends a lot of time outside, even before I got here."
    n "His shelves are packed with various trinkets and artifacts, although they are packed together so messily it's hard to know where to begin. Perhaps that's why he hasn't tidied the shelf."
    n "I do find a coin though - so weathered and worn that the silver has tarnished into black, the insignia in it smoothed over to almost flatness."
    nvl clear
    n "Despite this, I can still make it out - a unicorn stamp, the horse's head bent low with the horn proudly sprouting straight out. I had never seen any issued coin with this insignia before."
    n "Unlike the other objects here, it's not covered in dust at all. If it weren't for how old it is, this coin would be pristine."
    nvl clear

    menu:
        "Put it back.":
            n "If it has been this loved, I wouldn't want to tamper with it."
            n "All it would take is one wrong tap with these new claws to warp the metal, and that wouldn't do."
            n "I place it back on the shelf. Perhaps I can ask him about it later."
            n "I continue keeping myself busy, examining trinkets and occupying my restless mind as I wait for Atticus."
        "Dust the shelves.":
            # Atticus AFF up
            $ add_aff(1)
            n "While the coin has been loved to the point of cleanliness, there are plenty of other trinkets that have not been given the same courtesy."
            n "Luckily, there are a few rags on the lowest shelf I can use to sweep away the worst of it."
            n "It takes a while, but soon the shelf is cleaner than ever. And I don't feel like I've wasted all my time lazing around Atticus's home."

    window hide
    $ nvl_mode = False
    show layer screens:
        matrixcolor TintMatrix("#cecee2")
    scene interior night:
        zoom 0.5 
    show atticus at forest_night
    with dissolve
    window auto show
    "Atticus returns home just as the sun sets. His tunic and trousers are covered in a healthy amount of dirt, and his hands aren't faring much better."
    at "I'm home! And with plenty of vegetables."
    "Indeed, his basket is almost bursting. I think the onions are close to rolling out."
    mc "Good work! That's an amazing harvest."
    at "Isn't it? I was a little worried this year, but everything has pulled through."

    if at_aff >= 7: 
        "He chuckled, looking down at the vegetables."
        at "Who knows why! Maybe I had a lucky charm with me…"
        "He swallows and quickly sets the basket down."
        at "Anyway!"

    "Atticus starts to pile the vegetables on the counter: carrots, mushrooms, onions, potatoes…"
    "Everything needed for a damn good stew."
    mc "Can… May I help you with that?"
    "Atticus beams like the sun had risen early."
    at "Of course you can! I would—I would love the help!"
    at "You could help peel the potatoes as I prepare the onions? After that, you can move onto the carrots."
    mc "I can do that."
    "As I get to work, his tail accidentally bumps into me in excitement."
    at "Sorry."
    mc "It's alright."
    "He gets to work deftly chopping the onions, making a pile of the scraps, slicing through them with an ease that only comes from practice."
    "I take the peeler and look down at the potatoes, starting on one-"
    "The peeler slides out from my hand, my fingers unable to curl and grip as easily as before. The scales are too thick."
    "I press my lips together."
    at "Are you alright?"
    "I look over - he's stopped what he's doing and now stares at me."
    mc "I'm fine. Keep going."
    at "Okay…"
    "I swallow, and try to hold the peeler differently - holding it between two fingers, so it can't slip out from between them, the handle hooked under the knuckles."
    "But now it's too loose, my grip too weak, my claws too thick to hold it firmly. The handle touches the end of one and the sensation is so strange I drop the peeler again."
    "Can I not even peel a damn potato anymore?"
    at "May I?"
    "He's at my side before I can blink, taking the peeler from the counter and wrapping a cloth around the handle."
    at "Try now."
    "I cautiously take the peeler from him, careful not to touch his skin with my claws."
    "The cloth cushions the handle, making it thicker, and letting my knuckles bend more comfortably without the strain."
    "More importantly, it restores a sense of normalcy. A gift I once took for granted."
    "Testing it, I peel a potato - and do so much more smoothly than before."
    mc "Thank you, Atticus."
    "Atticus smiles brightly, gently patting my arm where the sleeve covers it."
    at "Happy to help!"
    mc "No, really, Atticus."
    "It's hard to control the feelings in me. But I swallow down whatever has been brewing, and try my best to smile."
    mc "Thank you."
    at "Of… of course."

    if at_aff >= 9:
        "He chuckles."
        at "I don't think I've… seen you smile properly yet. It's nice."
        "As soon as he says the words, his face bursts into a hot blush. Funny how much he does that, even at the simplest things."
        "I snort."
        mc "I'll try to do it more often."


    "It's not long until wafts of savory stew permeate the hut. My mouth waters."
    "Atticus must've noticed because he chuckles fondly."
    "Though with the way his ears are perked upwards and tail wagging side to side, he's clearly pleased as I am."

    if at_aff >= 7:
        at "Ah, that's right! I've prepared a surprise for you. Please wait right here. I'll be gone for only a moment!"
        "And then he rushes out the door."
        "I can't help but tilt my head to the side in curiosity. What could Atticus possibly have up his sleeve?"
        "Then I see his head pop from outside the door, his eyes alight with excitement."
        # show cg
        at "Behold! Your very own chair!"
        "He proudly hoists up a wooden chair. It's humble in appearance, but clearly a lot of time and effort was put into its creation."
        at "I realised with only one chair, we can't sit down and have meals together. So last night, I made this for you!"
        mc "You made this last night? You must have gotten no sleep!"
        at "It's okay! I only made the base last night and polished it off after harvesting the vegetables today."
        at "I, uh…"
        # end cg
        "In a moment, he became meek again."
        at "I hope you like it."
        "Gods, he's so cute."
        "I would have protected him no matter what. But I grow more sure every day that I am protecting a true and good soul."


    "After setting out the portions, Atticus and I sit down to eat."
    "I eat quickly, eager for food now I'm recovering enough. Eating stew while horizontal doesn't work out well most of the time."
    "Conversely, Atticus takes his time with his food, savouring every bite."
    "He's so skittish around me normally, but he looks almost peaceful right now. Eyes closed, sniffing every spoonful before eating it, not even getting the next bite ready until he swallows."
    "I slow down my own movements once I feel self-conscious enough."
    at "Are you not enjoying the stew?"
    mc "What?"
    at "I just…"
    "He swallows."
    at "I saw you slow down, so… I can always make something else if you've gone off the stew."
    mc "Oh! No, I just-"
    mc "I realised how slowly you were eating. Or, rather, how fast I was shovelling food down my throat."
    "Atticus blinks owlishly, then laughs."
    at "That's alright then! I suppose I'm just more used to the slow life."
    mc "I can't imagine a lot goes on around here… normally."
    at "No, it's… it's peaceful. I like it."
    mc "When there isn't a bleeding knight in your bed and poachers at your doorstep?"
    "We both chuckle."
    at "Yes, normally."
    mc "How long have you lived like this?"
    "Atticus pauses, tapping his spoon against the side of the bowl."
    at "Uh… most of my life? It's quite hard blending in with humans given- well…"
    "His ears twitch, and he taps the horn atop his head."
    mc "I see."
    at "So, I just… started wandering. Found my way to this forest, slept under the stars for a few nights, and then found this abandoned hut."
    at "I worked for months fixing it up, learning how to reset the walls and make the roof so no rain dripped on me… but I got there."
    at "And now, here I am!"
    mc "Wait, you fixed all this up by yourself?"
    at "I did indeed!"
    at "It's not the best work, I know. But I've lived here for years now and it's held up, so… at least it's home."

    menu:
        "You've done a beautiful job.":
            "Atticus shifts in his seat, failing to hide his smile."
            at "Thank you! I'm quite proud of it myself."
        "I'm sorry you've been alone.":
            # Atticus AFF up
            $ add_aff(1)
            "His eyes widen."
            mc "Sorry, I don't mean to overstep."
            mc "But… all this time? Am I the first guest, so to speak?"
            at "Um, well…"
            at "Yes, actually. Well, the first speaking guest."
            at "I had an injured sparrow stay with me while I fixed its wing, but it wasn't much for conversation."
            "He looks down, hands in his lap."
            mc "I'm so sorry."
            at "It's, um…"
            "He laughs softly, like he's scared to."
            at "Thank you."


    mc "Are there other unicorns out there? I know that they're quite reclusive, but even I had doubted if they were real until I met you."
    at "Oh, yes! Other unicorns exist."
    "He trails off, very obviously looking away from me."
    mc "Where are they? If you don't mind me asking."
    "Atticus sighs, his shoulders falling."
    at "Out there. I don't know where exactly."
    at "I, um… stay by myself. Given that I don't exactly fit in with humans or unicorns, it's safer to be alone so the poachers don't find me."
    mc "Atticus…"

    if at_aff >= 8:
        at "It's okay, really. And besides - I'm not alone anymore, am I?"
        "His face heats up again."
        at "I know you haven't been here for too long - or for the best reasons."
        at "But… I can't tell you how nice it's been to have someone else around! And to cook for, and to talk to…"
        mc "I can't imagine the bodyguard duties hurt either."
        "He breaks into a surprised laugh."
        at "They don't, ha!"
        at "But… I do really like the companionship. So… thank you for sticking around."
        "His tail knocks against the table leg, and the bowls jump a little."
        at "Sorry."
        mc "It's okay. Thank you for healing me."


    "Atticus smiles."
    at "But enough about me! You're a knight, aren't you?"
    mc "Well…"
    mc "Technically."
    "..."
    at "And… how do you 'technically' be a knight?"
    mc "I was once a knight. I saved the king's city from a red dragon, one that ate livestock by the dozen and tore through buildings like parchment…"
    mc "And after that, he placed me on a 'permanent sabbatical' and bid me goodbye."
    at "What's a permanent sabbatical?"
    "I grumble."
    mc "Early, unwanted retirement. I've been wandering around ever since, keeping the border safe. I don't like sitting still."
    "Atticus laughs."
    at "Maybe the slow life will do you some good!"
    mc "I'm much more used to fighting off ne'er-do-wells than gardening, Atticus. Plainly speaking, yesterday's fight was the most alive I've felt in a while."
    "Atticus tilts his head, an eager smile on his lips."
    at "But… you must have so many stories then!"
    mc "I… suppose I do."
    "What followed was the most excited interrogation of my life."
    at "How does one become a knight, then? Is it an application or are you discovered in the crowd?"
    at "Did you meet the king? Did he knight you with a sword and a vow? How many other knights were there alongside you?"
    at "Is it true that the castle's banquet table is longer than the span of this entire forest?"
    mc "Alright, alright! Let me start at the beginning…"
    # fade out
    # fade in
    mc "... and that is how I single-handedly fought off a direwolf with a chicken bone and my wits."
    "Atticus applauds, wriggling in his seat like an excited child."
    at "Oh, that's incredible! You truly are a most honorable knight."
    mc "Ah, that was years ago. Now I'm just a… faded legend wandering around the border."
    at "I…"
    "He swallows - and then straightens in his seat, looking at me with more confidence than I've ever seen him wear."
    at "I don't think that's true at all. I think you're a brave warrior who doesn't need the title of 'knight' to be one at heart."
    at "You took that vow and still live by it. That's worth more than any castle to me."
    "As I'm still stumbling over my speechlessness, he places one hand on his heart, the other brazenly taking my hand, skin to scale."
    at "So, I'm going to make one now! I vow to work out how to break your curse. I vow to not stop trying until we have answers."
    mc "Atticus-"
    at "In fact, I'm going to start now! I still need to study that dagger we found."
    "Before I can blink, he rushes away out the door, out to whatever workspace he has out the back."
    "..."
    "Well, full points for devotion. A true knight couldn't manage much better than that."
    "Still… he hadn't finished his dinner. There's half a portion of stew left in his bowl, growing colder by the second."

    menu:
        "Eat his portion.":
            # Atticus AFF down
            $ sub_aff(1)
            "Well, it would be a waste - he had spent so long harvesting the vegetables for it."
            "I switch our bowls and finish his serving, making sure nothing goes to waste."
            "Damn, he's a good cook."
        "Save his dinner for later.":
            # Atticus AFF up
            $ add_aff(1)
            "Bless him, he will probably be starving by the time he comes back from studying. He'll need something easier to eat."
            "I take a cloth from the side and rest it over the top, protecting it from any insects who may make their way inside the house."


    "I do wait up for him, but it becomes quickly apparent that Atticus won't be returning before the morning."
    "Still… he'll be needing the bed. My side is almost back to normal now, if a little stiff."
    "I find a spare blanket and find a corner to sleep in, the good food soon lulling me down into slumber."
    jump scene_6
