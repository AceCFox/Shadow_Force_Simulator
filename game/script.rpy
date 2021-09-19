# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kam")
define unknown = Character("???")
define dr = Character ("Dr. Iliac", color="#7d4900")
define ol = Character ("Oliver", color = "#3e702f")
define o = Character ("Onyx", color = "#2b2b2a")
define s = Character ("Shadow Master", color = "#a64788")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hovership

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show doodle_kam_transparent_bg:
    #     xalign 0.85

    # These display lines of dialogue.

    "I was surrounded by Supervillains"

    show xander_1:
        xalign 0.25
        #linear 0.3 xpos 0.95
    show oliver_1:
        xalign 0.75
    with Pause(1)

    hide xander_1
    with dissolve
    hide oliver_1
    with dissolve

    show alex_1:
        xalign 0.25
    show annabelle_1:
        xalign 0.75
    with Pause(1)

    hide alex_1
    with dissolve
    hide annabelle_1
    with dissolve

    "In the past, the word ‘supervillain’ didn’t really mean much to me. I stole stuff sometimes, like food or wallets. And I also happen to have superpowers. So the news reports seemed to think I'm a supervillain too."
    "But everyone else here, on this mission, is utterly terrifying."

    show dr_illiac_1:
        xalign 0.25

    unknown "Well I guess we can call that a successful mission. Good work, team!"

    hide dr_illiac_1
    show oliver_1:
        xalign 0.75

    unknown "Oh, yes, I would definitiely consider that successful. My favorite part was when you tinkered with that dimensional actuator or whatever and destroyed the entire island! Absolutely brilliant."

    hide oliver_1
    show oliver_2:
        xalign 0.75
        linear 0.2 xpos 0.5

    unknown "An especially auspicious debut for the return of the notorious {b}Dr. Iliac.{/b} Presumed dead by the world, only to mark those fools wrong with such glorious destruction. I can hardly think of a better comeback!"


    hide oliver_2
    show xander_2:
        xpos 0.25

    dr "I, uh, well. I'm not sure about {i}that{/i}, but..."

    hide xander_2
    show xander_clear_throat:
        xpos 0.25

    dr "It was {b}Oliver{/b}, right? For your own part you were certainly very..."

    hide xander_clear_throat
    with Pause(0.3)
    show alex_scowling:
        xpos 0.75

    unknown "Messy? In case you forgot, this was supposed to be a {i}quiet{/i} mission. Get in, shut the place down, get out. What part of that do you think required turning into a giant monster and tearing everything to bits?"

    hide alex_scowling
    show oliver_grinning:
        xpos 0.25

    ol "Ah. but {b}Onyx{/b}. What else was I supposed to do once they started shooting at us? While getting riddled with holes won't kill {i}me{/i}, it will kill this body, and that would be very unfortunate, yes? Besides I believe you were the one who was supposed to disable the defenses?"

    hide oliver_grinning
    with Pause(0.2)

    show alex_shouting:
        xpos 0.2

    show annabelle_annoyed:
        xpos 0.65

    o "I disabled everything perfectly! Whatever went wrong happened when {b}Shadow Master{/b} used her-- "

    s "Magic doesn't always play well with technology. Besides, who cares? I healed up Dr. Iliac's wounds, everyone's fine, we won. What's the big deal?"

    hide alex_shouting
    show alex_gritted_teeth:
        xpos 0.2

    o "It matters because it's about competence, and doing a good job, and doing it right the first time."

    hide alex_gritted_teeth
    show xander_grimace:
        xpos 0.25
    show annabelle_glower:
        xpos 0.65

    dr "Believe me, I definitely appreciate the whole not dying thing. But yes, Shadow Master is right. We accomplish our goals and the mission was a success. Maybe it wasn't perfect, but it's worth counting as a victory either way."

    hide xander_grimace
    show oliver_shrug:
        xpos 0.2

    ol "A success indeed. It could have used a bit more... panache, a bit more style. Hmm. Perhaps a bit more monologueing on your part, Dr. Iliac. I bet you'd be fantastic at it."

    hide oliver_shrug
    hide annabelle_glower
    show annabelle_raise_eyebrow:
        xpos 0.65

    s "That uh, whirlwind thing you did was pretty stylish. What did you say your name was again? {b}Confetti?{/b}"

    "The chatter died down around me, and the sound of the chopper seemed louder in its absence."

    hide annabelle_raise_eyebrow

    "With a start, I realized that she was talking to me, and everyone was waiting for my answer"

    menu:

        "Look, I don't know where that came from. My powers got caught on camera once, so that's what the news started calling me for some reason. I didn't pick it myself.":

            jump notme

        "...Yeah, that's me.":

            jump me


    label notme:
        show oliver_grinning:
            xpos 0.2
        ol "Well, that’s a classic villain mistake right there. You should never let the media decide who you are. You should declare yourself, boldly and confidently. Make your name something that they tremble to hear."

        show annabelle_nod_emphatically:
            xpos 0.65
        s "He’s right. Image is very important. There’s a reason I chose the name Shadow Master."

        ol "And a fine name that is. You may still be at the start of your journey, but I’m sure your reputation will grow quite fearsome over time."

        hide oliver_grinning
        hide annabelle_nod_emphatically

        show xander_grumpy:
            xpos 0.25

        dr "I don’t know about that. Getting a lot of attention isn’t all it’s cracked up to be, sometimes."

        show alex_grumpy:
            xpos 0.65
        o "It's a liability."

        hide xander_grumpy
        hide alex_grumpy

        jump land

    label me:

        show annabelle_thoughtful:
            xpos 0.65

        s "Huh. Well, I guess it fits. You were certainly very colorful. I’ve never seen anything like it."

        show oliver_grinning:
            xpos 0.25
        ol "An absolute whirlwind of beautiful destruction."

        hide annabelle_thoughtful
        hide oliver_grinning

        show alex_neutral:
            xpos 0.65

        o "That trick where you slipped under the door was pretty useful."

        hide alex_neutral

        show xander_SCIENCE:
            xpos 0.25
        dr "It’s certainly quite fascinating. Tell me, what does it feel like when you use your powers? Can you actually see like that? If one piece gets destroyed, is it missing when you reform? How far can your pieces stretch away from each other?"

        "I felt bile rise in my throat at his questions. There was no way I was going to answer any of that."

        hide xander_SCIENCE
        show xander_sheepish:
            xpos 0.25

        "I stared at him until he trailed off and shut up."

        hide xander_sheepish

        jump land

    label land:

        "The chopper lurched and we began to descend, before finally landing"

        "Good. The job was over, I could get paid, and never have to see any of these dangerous people ever again."

        show xander_sigh:
            xpos 0.5

        dr "Listen. Before we all go our separate ways, I’ve been thinking."

        "Uh oh."

        show xander_serious:
            xpos 0.5

        dr "None of us knew each other before we got hired for this job. We’ve never worked together before this. But together, we just pulled off something incredibly challenging and incredibly dangerous, and escaped without a scratch."

        show xander_grimace:
            xpos 0.5

        dr "Mostly."

        show xander_sigh:
            xpos 0.5

        dr "There’s power in teamwork. In having someone there to watch your back. It’s a big part of why superheroes are so successful. Just look at {b}Team 5{/b}. All of the greatest achievements of civilization have been achieved by people working together. Just…"

        show xander_frown:
            xpos 0.5

        dr "What I’m trying to say is that, maybe we should do this again sometime. Pool our resources and talents. Not to take another contract job, but to accomplish our own goals and ambitions. Help each other out."

        show oliver_thoughtful:
            xpos 0.05

        ol "An interesting proposal, Doctor. Consider me intrigued. You know, I work at a lovely little place called {b}Ambrosia{/b}. How about we get coffee sometime, and discuss it further?"

        show annabelle_thoughtful:
            xpos 0.75

        show alex_thoughtful:
            xpos 0.3

        "What?"

        "Was he serious?"

        "Are the others actually considering this?"

        "No way in hell."

        "Without a further word, I stood up and left the helicopter, and the supervillains on it behind."

        return
