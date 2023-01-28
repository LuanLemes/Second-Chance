screen living_room():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))
        imagebutton auto "overlays/living_room_door1_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Exit")
            unhovered SetVariable("focus_location", location_object.name)

            action Call("change_location_to", "Exit")

        imagebutton auto "overlays/living_room_door2_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Laundry Room")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Laundry Room")


        imagebutton auto "overlays/living_room_door3_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Bathroom")
            unhovered SetVariable("focus_location", location_object.name)

            action Call("change_location_to", "Exit")

        imagebutton auto "overlays/living_room_stairs_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Hallway")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Hallway")


label living_room:
    return

label living_room_check:
    # if prologue_to_living_room == True:
    #     $ only_location = "Kitchen"
    #     $ only_location_message = "I have to see Monica (She is on the Kitchen)"
    #     $ prologue_to_living_room = False
    return
