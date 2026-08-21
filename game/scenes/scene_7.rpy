label scene_7:
    "Over the next few days, I try several of Atticus's potions."
    "One changed my vision to make every colour the inverse. Another made my hair grow three inches in an hour. The third turned all the scales as cold as ice for the entire afternoon."
    at "We're getting closer though!"
    "Sure."
    "When I wake up this time though, there are dots of pain all over my body: namely at my temples, my shoulder blades, and down by my tailbone."
    "I roll over onto my stomach to relieve the pressure, reaching around to my back to feel for them."
    "..."
    "There's definitely something there."
    "It feels like something is growing from the bones - little nubs poke, not quite piercing the skin, but the area around it is sore."
    "When I reach up to my head, however, there is definitely something there. It twinges against my skull when I touch it, but feels almost like my claws."
    mc "Atticus?"
    "He always wakes up earlier than me. I hear him clatter something by the hearth."
    at "Yes?"
    mc "What… are these?"
    "I show him the nubs atop my head and he feels for the nubs at my shoulder blades. As per usual, he takes a moment to examine the skin, tenderly feeling around them."
    mc "So? What's the verdict, doc?"
    "Atticus hums in thought, taking off his glasses and cleaning them."
    at "I… think they may be the beginnings of the transformation."
    mc "But… the scales were the beginning."
    at "I know. But…"
    at "I'm sorry, it appears that you're growing horns. "
    at "And I think the nubs may turn into wings and a tail."
    "He sounds almost broken as he says it, trying to keep back from revealing his own panic too much."

    menu:
        "Huh. Pretty cool.":
            $ mentality = 1
            "I sigh, rolling my shoulders and feeling how the muscle has already changed."
            mc "Well… it's a bit sooner than expected."
            mc "But hey, traversing the land will be a lot easier. I can just fly over the trees instead of needing to plan paths through them."
            at "Ha, that's true! You can fly up and get all the fruit and flowers I can't reach."
            mc "See? Not too bad, is it?"
            "Still, I can see his relief at my acceptance as clear as the morning sun coming through the window."
        "We need to heal me now.":
            $ mentality = 3
            mc "So… we should get working on the cure then?"
            at "[povname]..."
            mc "No, no - if it's moving this quickly then - then we don't have time to waste, do we?"
            mc "Because if-if I've started growing wings a-and and tail, then it's only a matter of time before it gets worse-"
            mc "So we need to hurry up! I'll take all the potions you need me to, but we need to get going-"
            "Atticus places his hands on my shoulders, heavy and grounding."
            at "We'll get there. I promise, I'm trying my best."
            mc "Atticus, I'm going to turn into a monster-"
            at "No, you won't. We just have to… keep trying."
            at "I promise I am not going to leave you alone in this, alright?"
            "He motions for me to breathe. I do so, although I can't say that it makes me feel totally better."
            mc "Alright."
            at "Thank you."
        "Not ideal…":
            $ mentality = 2
            "It's hard to be too positive about this. But I try to take it on the chin."
            mc "Well… the wings will be a bit hard to disguise around humans. And I can't say I'm a huge fan of the tail - sitting down is going to be a nightmare."
            "Atticus offers me a sympathetic smile."
            at "I'm sure we can find solutions, no matter what."

    if at_aff >= 10:
        at "And hey! With the horns and tail, at least we'll be matching."
        mc "Sure…"





    at "Look… even if we're not able to stop it - which, I think we will! - there are ways of hiding yourself, if that's what you want."
    mc "Like… finding ways I can still be in civilisation?"
    at "Right! I've been thinking of ways for a very long time, I just… never felt the need to use them."

    if gave_chair:
        "He sits down at the table, and I sit on my seat beside him."
    else:
        "He sits down at the table, and I sit up properly on the bed."


    at "When I was younger, older unicorns would transform into humans so we could trade with others and keep connections outside of the herd."
    at "It takes a while to learn how to transform, so it was only ever the elders that did it. But even then, they normally wrapped up in lots of clothes just to make sure."
    mc "No chance of the ears poking out then."
    "Atticus grins, twitching his ears to prove a point."
    at "A hat can do wonders… I remember seeing so many of them. Once, we managed to trade for an entire hatter's stock and we all walked around with silly bobbles on our horns for a week…"
    "He swallows, his gaze darting away from me."

    if mentality == 1:
        "There's a definite shift in him - his normal meek but happy self suddenly looks so…"
        "Sad."
        mc "You don't have to tell me more if it's hard."
        "Atticus chuckles, although it doesn't hold much humor. He shakes his head."
        at "It's okay, I can keep going."
        mc "Just… don't say any more than you feel you can."
        at "Thank you."
    elif mentality == 2:
        "There's a definite shift in him - his normal meek but happy self suddenly looks so…"
        "Sad."
        "I frown, trying to catch his eye, but he's not looking at me at all. Instead, his fingers twist themselves into knots in his lap."
    elif mentality == 3:
        "Is that what I have to look forward to? Wrapping myself up in hats and scarves to hide every damn scale on my face?"
        "Never being able to honestly interact with another human again, lest I be screamed at or slaughtered…"


    "Atticus sighs softly, smiling down at the table."
    at "Normally, young unicorns learn how to transform into humans and back from their elders. It's a skill that's been passed down for generations."
    at "But, uh… I lost my herd before I learned from them."
    "He swallows thickly, blinking rapidly as his ears freeze against his head."
    mc "How did you lose them?"
    at "Poachers. Not the same group that were in the forest the other day, but…"
    "He clenches his hands, as if anchoring himself back down into reality."
    at "I had started learning, but… I always found it tricky. Always getting stuck halfway, never fully quite committing to the change."
    at "So, when… when my herd was attacked, my father transformed me with magic so I could run away. There was less chance of the poachers finding me if I only had two legs instead of four."
    at "I'm stuck though. I've tried to shift either way, but… I can't quite do it."
    mc "I'm so sorry, Atticus… have you made no progress?"
    "Atticus laughs, a spark appearing in his eyes."
    at "I have, actually. When my father transformed me, he, uh… forgot to give me hands."
    at "So I was fumbling around with hooves for a long time."
    "Despite the grief weighing heavily on him, Atticus grinned, miming his hands uselessly clopping around on the table."
    at "Building was terrible! Although at least I had a built-in hammer for the nails."
    at "Like the potions, everything is just… trial and error. One day I'll be able to transform fully. But, until then…"
    mc "You've got some funky ears and a funky horn."
    "Atticus smiles. There's a thud against the table."
    at "Don't forget the tail."
    "He straightens his shoulders though, pushing his glasses up his nose to look at me squarely in the eye."
    at "Still. I'm confident I'll find a way for both of us to live happily, without fear."

    if mentality == 1:
        if mc_crush:
            "It catches me by surprise, but I blush. Me, a valiant knight, blushing like a youthful maiden watching her saviour climb in through the tower window."
            "But I couldn't help it. He looks at me with such conviction and honesty, and I cannot help but believe him with all of my heart."
            "He's so determined. And beautiful, which doesn't help the blush."
        else:
            "He looks at me with such conviction and honesty, and I cannot help but believe him with all of my heart."
            "He's so determined. I feel myself nod, and know that I too would do all I could not just to help myself, but to help him too."



    elif mentality == 2:
        if mc_crush:
            "I swallow, suddenly overcome with emotion. It's hard not to feel so empowered, so indebted to someone swearing their assistance and loyalty to you."
            "I had no idea he felt so strongly about me…"
        else:
            "I swallow, suddenly overcome with emotion. I still hold onto doubts and fears of my new and changing body, but seeing him swearing his assistance so valiantly…"
            "I do not know if he will succeed in his research. But I will not doubt his efforts."



    elif mentality == 3:
        if mc_crush:
            "It's hard to hold onto the belief that I'll make it through this. But he tells me with such conviction that my heart stutters."
            "Even if I won't make it through this, I am so glad I met a being as kindhearted as Atticus."
        else:
            "I can't help but doubt his words. Not his conviction in them, but the truth of them."
            "I was already more of a dragon than a human…"
            "But I would never crush him like that."





    mc "Thank you, Atticus."
    "He bows his head, then rises to his feet."
    at "I'm going to start working again, okay?"
    mc "What are you working on today?"
    "He smiles."
    at "In one of the books, a flower called the Queen's promise was mentioned to being useful in pausing the spread of hexes and curses."
    at "They're incredibly rare and tend to only exist in small patches, so I'll be searching for it today. I think this might be the key I've been missing in all my potions."
    mc "What if you don't find it?"
    at "I will."

    if at_aff >= 12:
        if mc_crush:
            "He takes my hands in his, squeezing them gently. I still see a blush creeping up his neck."
            at "I'm not coming back until I find that flower. I promise."
            "His hands are so calloused, but they hold my scales and claws so gently, as if he doesn't want to hurt me…"
        else:
            "He grasps my shoulder, shaking it slightly so I look into his eyes."
            at "I'm not coming back until I find that flower. I promise."
            "His hands are so calloused, I can feel them scratch against my tunic. He works so hard."





    "Atticus moves away from me, picking up his basket from the side and opening the front door."
    at "There's a pot of water by the hearth. You can wash with it - the water might help alleviate your pains."
    at "Just… take it easy today."
    mc "Thank you, Atticus."
    "He bows his head and leaves the cottage."
    "Well, there's nothing much for me to do. I take the cloth from the hearth, soak it in the warm water, and run it over my shoulders."
    "It's definitely not fixing the whole 'wing' problem, but it does soothe my shoulders. After my shoulders, I move to my forehead, trying to ignore how the very tips of the horns catch against the fabric."
    "As I reach down to resoak the cloth, I notice how dirty the hearth is. It's covered in soot and charcoal, no doubt from years of cooking."
    "Without thinking, I push away some of the debris with my foot - and catch sight of a half-burned scrap of parchment."
    "It's got Atticus's handwriting."
    "..."
    "Well, he's not around to know. I wipe my damp hand on my trousers, then pick up the scrap."
    "{i}Two different books about unicorns now say the same thing: the horns are invaluable to medicine, no matter how malformed they are.{/i}"
    "{i}One story says a person's broken leg healed in a day using a salve made from powdered unicorn horn. Another says a person came from the brink of death by holding the horn against their chest.{/i}"
    "{i}It's hard to tell whether it's the horn's innate magic, or whether the magic comes from giving up the horn itself. One sacrifice for another."
    "{i}It's not ideal, but if…{/i}"
    "The scrap burns away there."
    "..."
    "If what?"
    "It's unconscionable, sure. But one sacrifice for another…"
    "It was only a horn. Atticus didn't need to be hurt."
    "..."

    if mentality == 1:
        "No. That was no way to think."
        "It wasn't just a horn. It was Atticus's horn, and no matter its power, it was despicable to consider taking it from him."
        "I would be no more a monster than I am now, knighthood or no."
        "I turn back to the pot and continue to wash myself. A clean body helps to clean the mind."
        # fade out
        jump scene_7_flower
    elif mentality == 2:
        "It's hard not to think of it. The honorable part of me recoils at the idea, repulsed that I would even consider doing something so cruel as taking what was not mine…"
        "But another part reached for it. A solution, right there. No more transforming, no more dragon."
        "Still. Guilt swirls in my stomach at the thought."
        "..."

        menu:
            "No. It isn't right.":
                jump scene_7_no_dark_ending
            "I must have his horn, no matter the cost.":
                jump dark_end



    elif mentality == 3:
        "I wouldn't need to kill Atticus for it. I would just need his horn, and then I could be free from this transformation."
        "The easy answer. No more potions, no more hoping for the best. Just certainty and freedom."
        "..."
        "But… Atticus didn't deserve this."
        "..."
        "He would be free from me too. My curse only weighs down those around me, including him."
        "This could be for the greater good."

        menu:
            "No. It isn't right.":
                jump scene_7_no_dark_ending
            "I must have his horn, no matter the cost.":
                jump dark_end

label scene_7_no_dark_ending:
    "And I should listen to the guilt. All of this fear, all of this uncertainty…"
    "None of it warranted any hardship against Atticus. He has been my one salvation in this ordeal."
    "This isn't a matter of honor anymore. This is normal, human decency, something I will never dismiss."
    "I kick the scrap away, turning back to the pot to continue washing myself. A clean body helps to clean the mind."
    # fade out
    jump scene_7_flower


label scene_7_flower:
    # fade in
    "The next day, I wake and stare at the ceiling. The cottage is empty and the basket is gone, meaning Atticus must have left already."
    "One day, I'll get used to the slow life. Today is not the day."

    if attempted_poach == True:
        "I shiver when I think of the night before, of how close I was to succumbing to something darker than I had ever imagined I could."
        "Maybe the slow life was what I needed. Something to calm down my worries, something to drag me into sensibility."


    "..."
    "He had mentioned he was looking for a rare flower - the Queen's promise. Surely two pairs of eyes were better than one?"
    "After putting out the hearth and grabbing my sword, I left the cottage."
    "However, after a few minutes of bravely walking through the forest, it becomes very clear that I am a little lost."
    "Not in the navigational sense - a knight is always aware of their surroundings, after all - but it occurs to me very quickly that I have no idea what the flower I am looking for looks like."
    "Or where it would grow."
    "Or any pertinent information about it."

    menu:
        "Look for Atticus.":
            # Atticus AFF up
            $ add_aff(1)
            "Perhaps it was a little hasty to rush out alone."
            "Atticus knew more about the plant than me - two people searching in the most likely area was far more helpful that one person uselessly walking around an unlikely area."
            "I keep my eyes to the treeline, searching for the familiar cloud of white hair."
        "Keep searching alone.":
            "He had told me to rest, after all. It would become very clear that I had ignored his advice if I rocked up to his foraging."
            "And besides, if the flowers were rare, it was best to spread out resources."
            "I keep my eyes to the trees and bushes, looking for anything that spoke to me as magically inclined."


    "I walk forwards, squinting-"
    # sfx snap?
    mc "AH!"
    "A searing pain wraps around my leg, like an animal had sunk its jaws deep into me."
    "I look down - and hidden by the leaves and flowers is a trap, now tourniqueting my leg."
    "I try to slash at the thing, but this one is made of metal and I only end up cutting the wires further into my leg."
    mc "Damnit…"
    "Every trap has a weak point though. If I breathe and take my time, I can find this one's-"
    "Hunter 1" "Well! Looks like we've got quite the catch!"
    "No…"
    "From the treeline, the four hunters I had once bravely fought off emerge, each wearing viciously victorious grins."
    "Hunter 2" "Wow, those are quite some scales… Maggie's dagger really was a cursed item then!"
    "They laugh amongst themselves, slowly removing their weapons. An axe, wicked and sharp; a sword, black and curved like a claw; and a remarkably familiar dagger, one that glimmers like blood in the sunlight."
    "Hunter 3" "Look at [them]... a knight turned dragon. And now, turned prey."
    "Hunter 4" "Think of the prices! Dragon scales sell for much more than a measly horn."
    "I hold onto my sword."
    mc "You'll regret this. Let me go, now!"
    "I slash with my sword as a warning - but the movement jostles my leg, digging the trap further into my flesh. As I yelp, the hunters' eyes gleam."
    "Hunter 1" "You know what? I don't think we {i}will{/i} regret this."
    "He raises his axe, poised like an executioner. My hand sweats around my sword and I open my mouth to scream-"
    "And a burst of flame exits my throat."
    "As the taste of coal and acid fills my mouth, choking and smothering, I can hear the screams get louder."
    "Hunter 1" "What?! How is this-{i}argh!{/i}"
    "Hunter 3" "It's everywhere! The fire's spreading!"
    "Hunter 2" "Leave it! Run away, run away!"
    "Hunter 1" "No, no - wait for me!"
    "I can't close my mouth. Heat licks all around me and I hear the hunter thud to the ground, still whimpering in pain."
    "The flames are so strong. The foliage around me has turned to ash, the pretty flowers now black and wilted."
    "Fire burns around me. I am still trapped, the metal getting hotter and hotter. Even as I force my jaw closed, the forest is burning."
    "The other three hunters have disappeared. I am left alone with the scorched body of the fourth."
    "I fall down, ducking as a branch cracks and falls above me, narrowly missing my head. I cry out in pain, but it is swallowed among the trees."

    if mentality == 1:
        "Even as my own chaos reigns around me, I cannot help but feel a sense of peace."
        "I knew I wouldn't die peacefully. A knight's life rarely does. But this hardly feels fitting for how hard I had worked throughout my life."
        "No battle, no glorious sword slays me. Just a fire of my own making, chasing inexperienced idiots who were too scared to face me honestly."
        "Maybe I should have been smarter. I should have avoided that dagger in the first place. But at least die honourable."
        "I close my eyes, feeling the heat inch closer…"
    elif mentality == 2:
        "This is how I die, isn't it? Not in a blaze of glory, tales of my heroic actions lining the path of my legend, but in a fire I caused by mistake and fear."
        "There is little honour in this. But, as the charred hunter's body is swallowed by fire, at least I know I took one of them out with me. Justice was served, even if it is tainted."
        "I close my eyes, swallowing back the bile in my throat…"
    elif mentality == 3:
        "Tears drip down my face that immediately evaporate in the smoke. This cannot be how I die - not as a knight, not as a human, but as squandered livestock."
        "I was meant to serve and protect until the end! I was meant to die a hero, not in this hellscape."
        "Damn this curse. Damn the poachers who scraped through the cracks and dare to leave me to die. Damn the kingdom for leaving me in the rubble."
        "I squeeze my eyes closed. I refuse to witness my own end, to see my body ruined more than it has been."


    at "[povname]!"
    "My eyes fly open."
    mc "Atticus? What are you doing? Get out of here!"
    "He's so nervous. His eyes are wide, hair frazzled, movements frantic."
    at "I'm going to get you out of here."
    mc "No, no - you have to save yourself-"
    "He leaps over me, bracing the fire licking against his back, hands working against the trap."

    if at_aff >= 12:
        at "You're not dying here. Not while I'm here!"


    at "Just trust me!"
    "He's focussed. He's always so focussed, even with his forest turning to ruin around him."
    mc "You can't save everyone. Just go, it's okay, save your cottage-"
    at "Got it!"
    "The trap springs open around my ankle. He immediately stands over me, grabbing my arm and hauling me up onto my weak legs."
    at "That's it, just lean on me. I'm going to get you out of here…"
    "I hadn't thought him to be so strong, but he holds me so firmly against his side, moving me through the brush with ease."
    "I can feel the heat receding. My mind reels, still flooded with panic and near-death worries…"
    "But I trust Atticus. If there's one thing in this world I can be sure of, it's him."
    "With his arm around my waist, my leg burning, my lungs and head filled with smoke, I finally let myself slip away into a darkness that moments ago, I would have never left."
    jump scene_8





