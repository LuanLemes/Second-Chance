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
            hovered SetVariable("focus_location", "Bathroom")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Bedroom 1")

        imagebutton auto "overlays/door2_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Bathroom")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Bedroom 2")

        imagebutton auto "overlays/door3_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Bathroom")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "bathroom")

        imagebutton auto "overlays/door4_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Bathroom")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Bedroom 3")

        imagebutton auto "overlays/door5_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Bathroom")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Bedroom 4")

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


label hallway:
    return

label hallway_check:
    # if big_sister_prologue == True:
    #     call ashley_prologue
    return
