# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kam")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hovership

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show doodle_kam_transparent_bg

    # These display lines of dialogue.

    k "Hi I'm Kam and this is a mockup."

    k "{i}mockingly{/i} ...Stick em up!"

    show doodle_kam_transparent_bg:
        xalign 0.5
        linear 0.5 xpos 0.85

    menu:

        "{i}...shit...{/i}"

        "{i}(Surrender your valuables){/i}":

            jump surrender

        "{b}{i}(Fight!){/i}{/b}":

            jump lose


    label surrender:

        k "Thank you for your donation to my clothing startup!"

        scene black

        return

    label lose:

        k "You're going to regret this!"

        scene black

        return
