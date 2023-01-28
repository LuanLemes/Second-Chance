screen map():

    text "thats the map babe"
    frame:
        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        # background Solid("0000")
        background location +".webp"

        for place in places:
            if place.is_active == True:
                vbox:
                    xpos place.x
                    ypos place.y
                    imagebutton:
                        hover place.avatar
                        idle place.avatar
                        action Call("change_location_to", place.name)
                    button:
                        xalign 0.5
                        text place.name

label map:
return
