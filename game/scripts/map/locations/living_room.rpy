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
            hovered SetVariable("focus_location", "Front Door")
            unhovered SetVariable("focus_location", location_object.name)

            action Call("change_location_to", "Front Door")

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

        imagebutton auto "overlays/living_to_kitchen_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Hallway")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("kitchen_click")

        imagebutton auto "overlays/living_room_living_room_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Hallway")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("living_room_click")
    use top_screen


label living_room:
    return

label living_room_check:
    # if prologue_to_living_room == True:
    #     $ only_location = "Kitchen"
    #     $ only_location_message = "I have to see Monica (She is on the Kitchen)"
    #     $ prologue_to_living_room = False
    return

label kitchen_click:
    $ phrase = renpy.random.choice(kitchen_click_phrases)
    mc_thought "([phrase])"
    return


label living_room_click:
    $ phrase = renpy.random.choice(living_click_phrases)
    mc_thought "([phrase])"
    return