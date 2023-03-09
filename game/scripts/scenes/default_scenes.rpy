label reset_camera:
    camera:
        pos (0, 0) xzoom 1.0 zoom 1.0 
    return

label age_check:
    menu:
        "Are You 18 or Older?"
        "Yes":
            return True
        "No":
            "Maybe in a few years then"
            return False

label input_player_name:
    $ player.name = renpy.input("What is your name?", length = 21, default = "Marcel" )
    $ mc = Character("[player.name]")
    $ mc_shout = Character("[player.name]", what_size = 37,)
    $ mc_thought = Character("[player.name]", what_color = "#98969E")
    menu:
        mc "My name is [player.name]."
        "Confirm":
            jump start_3
        "Change name":
            jump input_player_name



label start_3:
    call start_time_variables
    # show screen top_screen
    call enter_map
return
