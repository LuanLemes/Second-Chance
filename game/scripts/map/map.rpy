default location_in_string = ""
default location = ""
define default_location = "Your Room"
$ exit_map = False
default status_function = "x"
default map_image = ""
default enter_label_event = ""
default only_location = ""
default only_location_message = ""
default screen_name = ""
default is_reloading = False
# start the map with fade....start the dialogue
default map_dissolve_black_default = 0.5
default map_dissolve_time_default = 0.5
default map_black_pause_time_default = 0.1
default map_dissolve_black = map_dissolve_black_default
default map_dissolve_time = map_dissolve_time_default
default map_black_pause_time = map_black_pause_time_default
default map_reload_name = ""

label enter_map:
    call change_location_to(default_location)
    return

label change_location_to(new_location):
    if new_location == location:
        $ is_reloading = True
    else:
        $ is_reloading = False
    # if screen_name == new_location.lower().replace(" ", "_"):
    # jump reload_screen
#  reset global vars
    $ map_reload_name = ""
    $ check_label = ""
    $ exit_check_label = ""
    $ enter_label_event = ""
# Check if can leave
    $ can_leave_label = ""
    $ can_leave_label = str(location_in_string.lower() + "_on_exit")
    if new_location != location:
        if renpy.has_label(can_leave_label):
            call expression can_leave_label
            if _return == False:
                # jump reload_location
                jump reload_location
                return
#  Check if there is only possible location
    if only_location != "" and is_reloading == False and new_location != only_location:
#________________________________________ randomizar mensage later
        $ this_only_location_message = renpy.random.choice(only_location_message)
        mc_thought "[this_only_location_message]"
        window hide
        jump reload_location
        return
# Can enter check (it was not inside and then it entered)
    if is_reloading == False:
        $ check_label = new_location
        $ check_label = str(new_location.lower())
        $ check_label = check_label.replace(" ", "_")
        $ check_label = str(str(check_label) + "_on_enter")
        if renpy.has_label(check_label):
            call expression check_label
            if _return == False:
                jump reload_location
# from here on the map will change no matter what
# update vars
    $ location = new_location
    $ location_in_string = new_location.replace(" ", "_")
    $ low_location = str(location.lower())
    $ screen_name = low_location.replace(" ", "_")
# identify the location object
    python:
        for place in places:
            if location == place.name:
                location_object = place
# clear screen and show black
    if map_dissolve_black != 0 or map_black_pause_time != 0 or map_dissolve_time!= 0    :
        if is_reloading == False:
            scene black with Dissolve(map_dissolve_black)
            pause(map_black_pause_time)
    else:
        scene
    $ map_dissolve_black  = map_dissolve_black_default
    $ map_black_pause_time = map_black_pause_time_default
# hide screen
    hide screen expression location
# update iamges
    call update_image
# call reload name
    $ map_reload_name = screen_name + "_reload"
    if renpy.has_label(map_reload_name):
        call expression map_reload_name
# update screen name
    call focus_location_to(location_object.show_name)
    if is_reloading == False:
        call expression screen_name
# reset_only_location_if_only_location
    if only_location == new_location:
        $ only_location_message = ""
        $ only_location = ""
#call screen
    $ renpy.call_screen(screen_name)
    window hide
# reload in case of return
    jump reload_location


label reload_screen:
    $ renpy.call_screen(screen_name)
    return


label update_image:
    $ list_of_images_bool = [False, False, False, False, False]
    $ list_of_images_sufix = [" morning", " afternoon", " night", " dawn", " late_dawn"]


    if renpy.has_image(location.lower() + " morning" , exact=True):
        $ list_of_images_bool[0] = True
        # "has afternoon"

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
    # default map_dissolve_time = 5

    show expression map_image with Dissolve(map_dissolve_time)
    $ map_dissolve_time = map_dissolve_time_default
    return


label reload_location:
    call change_location_to(location)
    return


label focus_location_to(new_value):
    $ focus_location = new_value
