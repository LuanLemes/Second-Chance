screen home():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton:
            focus_mask True
            xpos 0
            ypos 0
            hovered SetVariable("focus_location", " Enter House")
            unhovered SetVariable("focus_location", location_object.name)
            hover ("overlays/house to living room hover.webp")
            idle ("overlays/house to living room.webp")
            action Call("change_location_to", "Living Room")

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

label home_check:
    if calendar.current_day_time == 0:
        $ can_enter = False
        $ not_enter_message = "Now its morning and you cant go home."
    elif calendar.current_day_time >= -1:
        $ can_enter = False
        $ not_enter_message = "You you cant go home now."
    return can_enter


label home:
    window hide
    return