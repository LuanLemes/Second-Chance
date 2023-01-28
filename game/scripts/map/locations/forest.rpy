screen forest():

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
label forest:
    $ start_inventory_items()
    # $ player_inventory.list_items()
    call screen magister_store

    return
    # menu:
    #     "Are you +18 years old?"
    #     "Yes":
    #         "option 1"
    #         call bedroom
    #     "No":
    #         "option 2"
    #         return
