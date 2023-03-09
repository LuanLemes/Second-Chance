screen hallway():

    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton auto "overlays/door1_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Martha Room")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Martha Room")

        imagebutton auto "overlays/door2_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Your Room")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Your Room")

        imagebutton auto "overlays/door3_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Bathroom")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Bathroom")

        imagebutton auto "overlays/door4_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Agatha Room")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Agatha Room")

        imagebutton auto "overlays/door5_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Mandy Room")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Mandy Room")

        imagebutton auto "overlays/door6_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Bathroom")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Bedroom 5")

        imagebutton:
            xpos 0.5
            xanchor 0.5
            ypos 0.95
            hover im.Scale("gui/idle.png", 340, 46)
            idle im.Scale("gui/hover.png", 340, 46)
            hovered SetVariable("focus_location", "Living Room")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Living Room")
        text "Living Room" xpos 0.5 xanchor 0.5 ypos 0.955 color "#fff"
    use top_screen

label hallway:
    if mandy_first == True:
        call first_mandy
    if school_prepare == True:
        mc_thought "Now I need to get dressed for school."
        $ only_location = "Your Room"
        $ only_location_message = ["I need to get dressed and find my stuff.", "I need to get dressed can't go out like this.", "Since when do I have a exibicionist fetish tsk, dammit this intrusive thoughts..."]

label hallway_before_enter:
    return

label first_mandy:
    $ mandy_first = False
    scene bump with hpunch
    pause(1.5)
    window hide
    scene hallway morning
    window hide


    show mandy angry with dissolve:
        xpos 437

    man " Hey!! Watch where you're going!!!"
    menu:
        man " Hey!! Watch where you're going!!!"

        "What time is it ?":
            show mandy angry:
                    pos (986, 1548) xzoom 0.4 yzoom 0.4 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -16.0, 0.0) yanchor 1.0
            show mc surprised:
                    pos (275, 1599) xzoom 0.4 yzoom 0.4  matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 30.0, 0.0) yanchor 1.0
            man "7:30 You are going to be late."


            window auto hide
            show mandy angry:
                subpixel True
                pos (986, 1548)
                linear 0.02 pos (949, 1536)
                linear 0.02 pos (994, 1551)
                linear 0.03 pos (986, 1548)
            with Pause(0.15)
            show mandy angry:
                pos (986, 1548)
            window auto show



            mc "Ugh,you can go I'll catch up give me like 20 minutes."
            man "Ha! as if I would wait for you,Later loser."
            hide mandy with dissolve
            # hide mc with dissolve
            mc "Ugh..."
            hide mc with dissolve

        "Just go, I'll see you there.":
            show mandy angry:
                    pos (986, 126) xzoom 0.54 yzoom 0.54 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -27.0, 0.0)

            show mc normal:
                    xpos 357 ypos 55 xzoom 0.55 yzoom 0.55 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 21.0, 0.0)
            man " The one day we need you to get there in time and you fuck up."
            man "Tipical"
            mc "Whatever..."
            show mandy tired with dissolve
            man "Quit wasting my time and get a move on loser."
            hide mandy
            hide mc
            with dissolve

        "What ? why are you in such a hurry ?":
            show mandy angry:
                    pos (986, 126) xzoom 0.56 yzoom 0.56 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -16.0, 0.0)
            show mc normal:
                    pos (275, 188) xzoom 0.49 yzoom 0.49 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 30.0, 0.0)
            man "Are you fucking kidding me ?!"
            show mc surprised
            man "Oh my god, It's not possible that you forgot It's our first day in college"
            mc "It's Today ?!"
            show mandy angry with Dissolve(0.3):
                    pos (970, 110) xzoom 0.58 yzoom 0.58 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -16.0, 0.0)
            man "Don't fuck this up [mc] everyone has been waiting for this for a long time."
            man "Even LandLady finally decided to leave the house for once to see us."
            mc "Alright ok."
            mc "just give me like 20 minutes."
            man "I'm not going to wait for you, I'm heading out good luck."
            hide mandy
            with Dissolve(0.2)
            # window auto show
            mc "Mandy wait..."
            mc_thought "(she left already...)"

    call mandy_relations
    $ only_location_message = ["I need to take a shower first."]
    $ only_location = "Bathroom"

    window hide
    return
