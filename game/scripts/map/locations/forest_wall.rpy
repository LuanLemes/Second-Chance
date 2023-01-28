screen forest_wall():
    $ show_subtitle = False
    text "thats the map babe"

    frame:
        # xalign 0.0
        # yalign 0.0
        xpos 0.0
        ypos 0.0
        xsize 1920
        ysize 1080

        background (str(map_image))
        # background "maps/"+location +".webp"
        # background "maps/forest wall.webp"
        # background Solid("0000")
        # background "maps/forest wall/webp"

        for place in places:
            if place.is_active == True and place.map_to_show == 1:
                $ hover_name = place.avatar
                $ hover_name = hover_name.replace(".png", " hover.png")
                vbox:
                    xpos place.x
                    ypos place.y
                    imagebutton:
                        focus_mask True
                        hover im.Scale(hover_name, 100, 100)
                        hovered SetVariable("focus_location", place.name)
                        unhovered SetVariable("focus_location", location_object.name)
                        idle im.Scale(place.avatar, 100, 100)
                        action Call("change_location_to", place.name)

label forest_wall:
    return
