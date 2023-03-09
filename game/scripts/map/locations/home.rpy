screen front_door():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton auto "overlays/house_entrance_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Enter House")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Living Room")

label front_door:
    if isekai_quest == True:
        scene blacked
        scene front door morning
        show mc normal:
                pos (506, 178) zoom 0.62 
        mc "oh man I have like 10 minutes to get there."
        mc "It's not far but fuck."
        mc "I don't want to get there all sweaty."
        mc "What do I do?"
        # $phrase = renpy.random.choice(isekai_quest_phrases)
        menu:
            "do I run ?":
                show cross road
                with dissolve
                mc "Can't afford to get late here goes nothing."
                dev "#if he runs or not have a little CG corresponding to it."

            "It's not worth it":
                show cross road
                with dissolve
                mc "I don't want to get sweaty I'll take it slow"
                show school morning
                show school_crowd
                with dissolve
                mc "I'm sure everything will be late since is the first day."
        
        mc "almost there."
        show truck hit with vpunch
        pause 1.2
        scene black with Dissolve(1.0)
        
        scene 13 with Dissolve(1.5)
        scene black with Dissolve(1.0)

        scene 13_2 with Dissolve(1.5)
        scene black with Dissolve(1.5)

        scene 13_3 with Dissolve(1.0)
        scene black with Dissolve(2.0)
        pause 0.3
        # $ map_dissolve_time = 2.0

        call change_location_to("Licue Realm")
        # crosses the road and . BEEEEEEEEEEEEEEEEEEEEEP!
        # dissolve to the front end of a truck hpunch
        # Sounds of tire screechin
        return
    return

label front_door_on_enter:
    return
    


