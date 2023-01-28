default location = "Map"
$ exit_map = False
default status_function = "x"
default map_image = ""
default can_enter = True
default not_enter_message = ""
default not_enter_label = ""
default enter_label_event = ""
default only_location = ""
default only_location_message = ""

label enter_map:
    call change_location_to("Bedroom 1")
    return

label change_location_to(new_location):
#  check if there is only possible location
    if only_location != "" and new_location != only_location and new_location != location_object.name:
        mc_thought "[only_location_message]"
        window hide
        return
# return
    if only_location == new_location:
        $ only_location_message = ""
        $ only_location = ""
#  reset global vars
    $ can_enter = True
    $ not_enter_message = ""
    $ check_label = ""
    $ enter_label_event = ""
    $ not_enter_label = ""
# check if has check method
    $ check_label = new_location
    $ check_label = str(new_location.lower())
    $ check_label = check_label.replace(" ", "_")
    $ check_label = str(str(check_label) + "_check")
    if renpy.has_label(check_label):
        call expression check_label
        if _return == False:
# check for enter message -
            if not_enter_message != "":
                mc_thought "([not_enter_message])"
                window hide
# check for not enter label
            if not_enter_label != "":
                if renpy.has_label(not_enter_label):
                    call expression not_enter_label
            window hide
            jump reload_location
            return
# update vars
    $ location = new_location
    $ low_location = str(location.lower())
    $ screen_name = low_location.replace(" ", "_")
# identify the location object
    python:
        for place in places:
            if location == place.name:
                location_object = place
# clear screen
    scene
    hide screen expression location
# update iamges
    call update_image
    call expression screen_name
    call focus_location_to(location)
# check for enter event
    if renpy.has_label(enter_label_event):
        call expression enter_label_event
        window hide
        jump reload_location
        # return
#call screen
    $ renpy.call_screen(screen_name)
# reload in case of return
    jump reload_location

label update_image:
    $ list_of_images_bool = [False, False, False, False, False]
    $ list_of_images_sufix = ["", " afternoon", " night", " dawn", " late_dawn"]

    if renpy.has_image(location.lower(), exact=True):
        $ list_of_images_bool[0] = True
        $ map_image = str("maps/" + location.lower() + ".webp")
        # "has day"

    if renpy.has_image(location.lower() + " afternoon" , exact=True):
        $ list_of_images_bool[1] = True
        # "has afternoon"

    if renpy.has_image(location.lower() + " night", exact=True):
        $ list_of_images_bool[2] = True
        # "has night"

    if renpy.has_image(location.lower() + " dawn", exact = True):
        $ list_of_images_bool[3] = True
        # "has dawn"
    if renpy.has_image(location.lower() + " late_dawn", exact = True):
        $ list_of_images_bool[4] = True
        # "has dawn"

    $ image_found = False
    $ image_to_select = -1
    $ count = -1
    while image_found == False:
        $ count = count +1
        if list_of_images_bool[calendar.current_day_time - count] == True:
            $ image_to_select = calendar.current_day_time - count
            $ map_image = str("maps/" +location + list_of_images_sufix[image_to_select] + ".webp")
            $ image_found = True
    $ map_image = str(map_image.lower())
    show expression map_image
    return

label reload_location:
    call change_location_to(location)
    return

label focus_location_to(new_value):
    $ focus_location = new_value
