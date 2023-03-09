screen your_room():
    zorder -10
    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton:
            xpos 0.5
            xanchor 0.5
            ypos 0.95
            hover im.Scale("gui/idle.png", 340, 47)
            idle im.Scale("gui/hover.png", 340, 47)
            hovered SetVariable("focus_location", "Hallway")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Hallway")


        text "Hallway" xpos 0.5 xanchor 0.5 ypos 0.955 color "#fff"

        if school_prepare == True:
            default name_of_the_image = ""
            default range_of_buttons = 9
            for i in range (range_of_buttons):
                $ name_of_the_image = "overlays/your_room_door" + str(i+1) + "_%s.webp"
                if list_of_school_prepare_buttons[i+1] != -1 :
                    imagebutton auto name_of_the_image:
                        focus_mask True
                        xpos -5
                        ypos -5
                        action SetDict(list_of_school_prepare_buttons, i+1, -1,), Call("school_prepare_button_clicked",)
                else:
                    pass
    use top_screen
    

label your_room:
    if mandy_first == True:
        mc "Man..I have to go to the bathroom! (@EVO I think there should be a  line somehow like this here)"
        $ map_dissolve_black_default = 0.0
        $ map_dissolve_time_default = 0.0
        $ map_black_pause_time_default = 0.0
        $ map_dissolve_black= 0.0
        $ map_dissolve_time = 0.0
        $ map_black_pause_time = 0.0
        call change_location_to("hallway")
        return

    if school_prepare == True:
        default list_of_school_prepare_buttons = []
        python: 
            list_of_school_prepare_buttons.clear()
            for i in range (11):
                list_of_school_prepare_buttons.append(i)

        $ school_prepare_phrases = [ "not there...", "I'm going to get late..", "found it.", "Ok, Now just need to find my bag.", "money", "nope", "Got it." ]
        # jump school_prepare_button_clicked
        mc "Now where are my things?"
        return
    return

label school_prepare_button_clicked:
    if len(school_prepare_phrases) > 0:
        if school_prepare_phrases[0] == "money":
            mc_thought "(Oh hey {color=#0051ffff}20 bucks{/color} nice.)"
            $ player.money += 20
        else:
            mc_thought"([school_prepare_phrases[0]])"
        $del(school_prepare_phrases[0])



    if len(school_prepare_phrases) <= 0:
        $ school_prepare = False
        python:
            for button in list_of_school_prepare_buttons:
                button = -1
        $ exit_dialog = renpy.random.choice(school_quest_complete_phrases)
        mc "[exit_dialog]"
    return

label your_room_on_exit:
    if school_prepare:
        mc_thought"(I cant leave now, I have to get ready for school first.)"
        return False
