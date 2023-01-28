screen flower_camp():

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
            hovered SetVariable("focus_location", "Village")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Forest Wall")
        text "Village" xpos 0.5 xanchor 0.5 ypos 0.95 color "#fff"

label flower_camp:
    menu:
        "Colect flowers":
            "collect flowers"
        "Colect herbs":
            "collect herbs"
        "Explore the Field":
            "explore field"
    # jump flower_camp
    window hide
    return

label flower_camp_check:
        if flowers_cap_first == True:
            $ enter_label_event = "flower_camp_first"
