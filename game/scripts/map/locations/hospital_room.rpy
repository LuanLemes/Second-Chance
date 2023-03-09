screen hospital_room():
    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton auto "overlays/living_room_living_room_%s.webp":
            focus_mask True
            action Call ("watch_hospital_tv")
    use top_screen

label hospital_room:
    if hospital_first == True:
        scene black
        if developer_checkpoints == True:
            menu:
                "hospital room":
                    pass
        $ ui_show_foward_time = True
        $ hospital_first = False
        jump hospital_first
    window hide
    return

label hospital_room_reload:
    if calendar.current_week_day == 3 and calendar.current_day_time == 1:
        "Today is Wednesday, Thats a visit day"
        if wednesday_visit_who == "None":
            mc_thought "But I asked to be alone so no one came."
            return
        menu:
            "Today is [wednesday_visit_who] day of visit"
            "Accept the visit":
                call wednesday_visit
            "Skip the visit":
                return

    if calendar.current_week_day == 5 and calendar.current_day_time == 1:
        "Today is Friday, Thats a visit day"
        if friday_visit_who == "":
            mc_thought "But I asked to be alone so no one came."
            return
        menu:
            "Today is [friday_visit_who] day of visit"
            "Accept the visit":
                call friday_visit
            "Skip the visit":
                return
    return

label wednesday_visit:
    $ this_visit = ""
    $ this_visit = str(wednesday_visit_who + "_visit")
    call expression this_visit
    return

label friday_visit:
    $ this_visit = ""
    $ this_visit = str(friday_visit_who + "_visit")
    call expression this_visit
    return

label visit_day:
    menu: 
        "Well...."
        "Finally a visit, someone to talk to.":
            pass
        "Im not willing to take any visits today":
            return
    if visit_count == 0:
        call martha_visit

label martha_visit:
    if martha_visit_count > 0:
        "Martha came to visit you."
        "You spent the afternoon together."   
        return
    mar "Hey kid, how are you holding up ?"
    menu:
        "I'm holding up":
            mar "That's good to hear. Any news from the medics ?"
            mc "Nope still same stuff,meds are tiring."
            mar "Oh sweetie you push throught this the worst part is already over."
            mc "hope so."
            "You spent the afternoon talking to Martha."
            if im_holding_up == True:
                $ im_holding_up = False
                notif "Relationship up."
                $ martha_relationship += 1
            return
        "Can't wait to go home":
            mar "I wish this was all a bad dream too [mc]."
            mar "so you could go home with me already."
            mc "..."
            mar "any updates on your condition."
            mc "Nope. The meds are pretty tiring tho."
            mar "Oh sweetie you push get used to then, the worst part is already over."
            mc "hope so."
            "You spent the afternoon talking with martha" 
            if can_wait_to_go_home == True:
                $ can_wait_to_go_home = False
                notif "Relationship up."
                $ martha_relationship += 1
                #Relationship up.
            return
        "Would be better if you where here with me.":
        #fails stat check this is the dialog that shows if you choose that option
            if courage < 3.5:
                "You wanted to say that, but you didn't have enough courage."
                call martha_visit
                return
            mar "Oh...I wish I could stay here with you but, I really can't I'm sorry." #redfaced
            mc "Hmm...Figured as much."
            mc "Can anyone be here with me ?"
            mar "I'm afraid not."
            mar "But do you want then to visit you."
            mc "well they promiced they would..."
            mar "Oh I'm so sorry, I'm just hogged you all to myself but if you want I'll let then come next time."
            mar "Is there anyone you want to talk too ?"
                #this dialog if player wants to change the girls to trigger this messages again
            menu:
                "hey, could you tell..."
                "Mandy to come visit." if mandy_visit_count == 0:
                    call ask_mandy_visit
                    return
                "Caroline to come visit."if caroline_visit_count == 0:
                    call ask_caroline_visit
                    return
                "Ana to come visit." if ana_visit_count == 0:
                    call ask_ana_visit
                    return
                "Agatha to come visit." if agatha_visit_count == 0:
                    call ask_atatha_visit
                    return
                "I want to be alone.":
                    mar "Oh uhm... Ok."
                    mar "I guess you need some space, Just tell the nurse if you want to see us again ok ?"
                    mc "Will do."
                    "You spent the afternoon with Martha."
                    return
                "Mandy to come visit again." if mandy_visit_count > 0:
                    call ask_mandy_visit
                    return
                "Caroline to come visit again."if caroline_visit_count > 0:
                    call ask_caroline_visit
                    return
                "Ana to come visit again." if ana_visit_count > 0:
                    call ask_ana_visit
                    return
                "Agatha to come visit again." if agatha_visit_count > 0:
                    call ask_atatha_visit
                    return
    call martha_visit
    return

label ana_visit:
    "Ana didn't show up."
    "You spent the afternoon waiting for her."
    return

label agatha_visit:
    #agatha
    aga "Hello can i come in ?"
    mc "Come on in don't just stand there."
    agatha" Ok..." 
    agathat "mom said you wanted to talk with me. d-did I do something ?!"
    mc "No agatha relax."
    mc "Is it that hard to believe I want to hang out with you?"
    #dialog based on what girl MC sees more
        #mandy
    $ max_visits_count = max(mandy_visit_count, caroline_visit_count, martha_visit_count, agatha_visit_count, ana_visit_count)
    if mandy_visit_count == max_visits_count:
        aga "You say that but, You keep drooling over Mandy."
        mc "What?! Agatha where did you get that Idea Mandy just felt guilty because of what happened."
        agathat "I-I also felt guilty b-because I went to Uni so early I was so anxious I coulden't wait anymore, If I was there Mandy would have waited for you and..."
        mc "AGATHA!! Snap out of it!"
        aga "I'm sorry" #almost crying face."
        mc "Can't cry over the spilled milk ok, what is done is done."
        mc "Now i'll just recover and move on girl relax."
        agatha"Hmm..."
    if ana_visit_count = max_visits_count:
        #Ana
        aga "Well you asked to See Ana first and not me."
        aga "You know I was worried suck waiting for  my turn and you ask for her..."
        mc "Agatha Mom never told me you were so worried."
        aga "..."
    if caroline_visit_count = max_visits_count:
        #Caroline
        aga "You been hanging out with auntie a lot huh ?"
        mc "Yeah why ?"
        agathat "Did she get you with that self-help speech she always gives."#angry
        mc "..."
        mc "Agatha what's wrong ?"
        aga "I was Worried SICK!! And I even fainted because of you, did you not remember me at all?!!"
        mc "Agathat I'm sorry ok."
        aga "..."
    if martha_visit_count = max_visits_count:
    #martha
        aga "I was really surprised that mom let go of you so I could finally visit."
        mc "Well I did ask her tho."
        aga "YOU DID ?!?!" #redface.
        aga "I mean of course haha, you were worried that I fainted the other day because you scared me."
        mc "Hahaha."
        aga "It's not funny stop lauging at me..."
        mc "It's a little funny, Did you think I was zombie or something."
        aga "SHUT UP!!!"
    if agatha = max_visits_count:
        #Agatha is the first visit after mom.
        aga "I'm sorry..."
        aga "It's just, that things have been pretty heavy around the house now that you are here."
        mc "Why is that ?"
        aga "I'm running my mouth I'm sorry I shoulden't worry you with this kind of stuff."
        if route == "dom":
            mc "Agatha! Tell me what is going on."
            aga "AH! O-ok..."
            "You feel Agatha's submission grow."
            aga "B-becase of your accident, Mom is having some financial trouble."
            mc "WHAT?!!"
            agatha"T-The bill it's p-pretty expensive, we are going to be a bit short on money now."
            aga "I'm Looking for a part time job, to help and So is Mandy, Mom  has started looking for a job too."
            mc "Shit... What about that pension she was getting ?"
            aga "It won't be anywhere near enough I'm afraid, she might even have to sell the car."
            mc "for fucks sake..."
            mc "I need to get out of here."
            aga "WAIT! PLEASE!!"
            aga "Please don't worry [mc] We will figure everything out, please just rest and get well soon."
            mc "I..."
            mc "I'm sorry, I'll do my best For you..."#she gets really red
            mc "For the family We will get trought this together."
            "You spent the afternoon with Agatha."#end day with her here if dom stat
            return
    mc "What do you mean by that Agatha."
    aga "Ah... Well You know we thought you were dead."
    mc "Guess I was for a bit."
    mc "But you all Need to relax a bit,I'll be out of here soon."
    aga "Not sure we can..."#looks sad/tired
    "You Don't quite get what is getting Agatha so worried."
    "You spent the afternoon with Agatha."
    return

label caroline_visit:
    if caroline_visit_count > 0:
        "Caroline came to visit you."
        "You spent the afternoon together."
        return
    Kim "There he is. How are you doing kid."
    mc "How is it going Carol."
    Kim"Oh you know, Ana is a handfull, and your girls have been worried sick."
    mc "Guess they are missing their trust Stallion around the house huh?"#Charisma/courage icreases relationship with kim quite  abit
    Kim "Ahahaha."
    Kim "That's the Spirit [mc], You'll be out of here in no time."
    Kim " Here I promiced i Would bring you something to read didn't I."
    Mc "Opening your third Eye, A spiritual journey to enlightment."#Boosts meditation after reading it takes 4 readings but gives double arcane on meditation.
    mc "Wow,a spiritual jorney huh."#courage and chrarimas high."
    mc "I'm more of a physical guy to be honest."
    Kim "You must be really bored here if you are flirting with me."
    mc "I mean...You are pretty hot this place is very lacking on the visual department, sorry if I got a little worked up."
    Kim "Oh...Hahaha, Stop making fun of me [mc] A boy like you would never want an old woman like me."
    mc "Trust me Carol, I would love to have my way with an experienced woman,it must be the best experience a man can have."#needs max courage."
    Kim"..."#she is red faced/horny. increaces her relationship quit a bit."
    Kim "Oh hoho, you silvertongued fox."
    Kim "Quit playing ahaha..."
    mc "hahaha"
    "You laugh with her to make her feel less awkward."
    "You spent the afternoon together."
    Kim "I doubt that there is a lot for you do do here."
    Kim "Might as well read a book meditate."
    Kim "It's good for your mental health [mc], it's not just our bodies that need healing our minds and soul too."
    mc "I Think you're right Carol, This is not such a bad idea."
    Kim "Give it a go, You'll love it I'm sure."
    "You spent the afternoon with Caroline."
    return

label mandy_visit:
    if mandy_visit_count > 0:
        "Mandy came to visit you."
        "You spent the afternoon together."
        return
    "Mandy came to visit you today."
    man "Hey..."
    mc "Hey, so how are you doing ?"
    man "Well... You know like always." #she looks sad/embarrased."
    if courage >= 4:
        mc "Oh cmon cheer up Mandy. That frown doesn't look good on you." #Needs courage. lots of it. if he fails continues bellow until he has enough coruage or not
        mc "Althought you do look really cute right now."
        man "Oh shut the fuck up you...IDIOT!"
        mc "Hahaha Ouch! fuck Ahh."
        man "[mc]!!!!"
        mc "Oi calm down Aaah, shit I'm sorry It hurts when I laugh."
        man"..."
        mc "Guess college is just as boring as highschool huh."
        man "That's... You could say so yes."
        mc "Don't be so down I'll make it up to you once I'm out of here."
        man"..."
        man "It's Ok no need to do that I'll handle it."
        mc "Mandy!"
        #she looks surprised.
        man "WHAT!!!"
        mc "This is not like you, ya know."
        man "I..."
        mc "LandLady told me that you were blaming yourself over what happened to me."
        #angy mandy
        man " SHE DID FUCKING WHAT!!"
        mc "Hey don't Yell they will kick you out."
        man "SHUT THE FUCK UP SHE SHOULDEN'T HAVE SAID THAT SHE..."
        "That's the Mandy you remember."
        "You spent the afternoon together."
        return
    #failed check
    "Mandy was coy the entire visit."
    "You spent the afternoon together."
    return

label no_visit:
    call set_next_visit("")
    #No visit dialog."
    "Nobody came to visit you Today."
    return

label ask_ana_visit:
    call set_next_visit("ana")
    #she will dip on the MC never comign to visit waste of time.
    mc "can Ana visit me this time?"
    mar "Oh [mc] my dear, I'll try to talk to her."
    mar "She is so busy with college, and to be fair..."
    mar "She is very cold towards me, I doubt she would come."
    mc "..."
    "You spent the afternoon with Martha"
    return

label ask_agatha_visit:
    if agatha_visit_count > 0:    
        "Agatha came to visit you."
        "You spent the afternoon together."
        return
    call set_next_visit("agatha")
    mar "Of course, I'll tell her."
    mar "It would be good for her."
    mc "Why is that ?"
    mar "She was a little shocked after your miraculous awakening."
    mc "Oh."
    mc "You spent the afternoon with Martha."
    return

label ask_caroline_visit:
    call set_next_visit("caroline")
    mar "Of course, I'll tell her."
    mar "It would be good for her."
    mc "Why is that ?"
    mar "She was a little shocked after your miraculous awakening."
    mc "Oh."
    mc "You spent the afternoon with Martha."
    return

label ask_mandy_visit:
    call set_next_visit("mandy")
    mar "Oh she wanted to come first."
    mc "Really ?!"
    mar "Yea... Take it easy on her ok ?"
    mc "Huh !? Why ?"
    mar "She blames herself for your accident just so you know."
    mc "oh..."
    mc "tell her to come visit next time."
    mar "Ok."
    "You spent the afternoon with martha."
    return

label hospital_first:
    if developer_checkpoints == True:
        menu:
            "hospital":
                pass    
    man "B-but he can't be dead!"
    mar "Doctor isn't there something we can do?!"
    medic "I'm afraid not ma'am,he has sustained numerous injuries and fractures,the emergency cirgury saved his life"
    medic "But a few hours ago I got confirmation that his brain activities have stoped,that means he will not regain consciousness or be able to breathe without support."
    kim "That...Martha."
    mar "My poor boy..."
    medic "I'll leave you alone to take your decision, but please take into consideration donating his organs, there is still a lot of good that can be done."
    medic "Despite your tragic lost, and the bill will be at the front desk, my condolences."
    aga "I-i can't believe he is gone..."
    man_shout "FUCK! WHY WHY WHY DIDN'T I WAIT FOR HIM THIS WOULD HAVE NEVER HAPPNED!"
    mar "Mandy my dear, It's not your fault please."
    man "Mc you fucking IDIOT!!"
    if team_notes == True:
        menu:
            "we need a sprite of mandy crying over here":
                dev "so im using a placeholder sprite, but lets pretend this is mandy crying."
                
                pass
    scene hospital room morning
    show mandy sad:
            xpos 355 
    show agata sad:
            xpos 1290 
    show martha sad:
            xpos 871 
    show kim sad:
            xpos -18 
    show eyes overlay2
    show blacked
    window hide
    show eyes overlay2:
        subpixel True 
        alpha 1.0 
        linear 3.01 alpha 0.0 
    show blacked:
        subpixel True 
        alpha 1.0 
        linear 1.50 alpha 0.38 
        linear 1.51 alpha 0.0 
    with Pause(3.11)
    show eyes overlay2:
        alpha 0.0 
    show blacked:
        alpha 0.0 
    pause 0.5
# agatha animation scare
    show agata shocked:
        subpixel True 
        pos (1210, 0) 
        linear 0.13 pos (1227, -48) 
        linear 0.09 pos (1175, -35) 
        linear 0.07 pos (1135, -1) 
    with Pause(0.39)
    show agata shocked:
        pos (1135, -1) 
    window show


    aga_shout "m-m-m...h-h-he!!"
    
    mar "Whaat's wrong dear?"
    show agata shocked:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.54)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    with dissolve
    aga_shout "m-m-m...h-h-heeeeeeeeeee!!"
    show agata shocked:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.34)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    with dissolve
    aga "I think Im gonna..."
    window hide
    show agata shocked:
        subpixel True 
        pos (1135, -1) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
        linear 0.28 pos (1130, 304) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 68.0) 
    with Pause(0.38)
    show agata shocked:
        pos (1130, 304) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 68.0) 
    kim "I think she fainted."
    window show
    #have agatha faint

    show martha shocked
    show mandy shocked
    show kim shocked
    with dissolve
    everybody "...!"
    mc "ugh my head..."
    show martha excited
    show mandy happy
    show kim happy
    everybody "YOU'RE ALIVE !!!!" with vpunch
    mc "agh stop screaming so much what happened ?!"

    window hide
    show mandy default:
        subpixel True 
        parallel:
            pos (355, 0) 
            linear 0.08 pos (390, -46) 
            linear 0.07 pos (338, 45) 
            linear 0.09 pos (355, 0) 
        parallel:
            zoom 1.0 
            linear 0.15 zoom 1.04 
            linear 0.09 zoom 1.0 
    with Pause(0.34)
    show mandy default:
        pos (355, 0) zoom 1.0 
    window show

    man "YOU FUCKING BASTARD"
    show mandy angry
    camera:
        pos (906, 63) xzoom 1.0 zoom 2.6 


    man "I'LL FUCKING KILL YOU!!!!" 
    show martha disappointed
    camera:
            xpos 1462 
    mar "Mandy NO!!"
    # call reset_camera
    camera:
            xpos 11 xzoom 1.0 
    kim "I'll go call the doctor" 
    show mandy default
    call reset_camera
    kim "hold here."
    hide kim with moveoutleft
    mc "What's going on ?!"
    camera:
            xpos 464 zoom 1.54 
    camera reset_camera
    mar "Oh dear god, you were hit by a truck on your way to college."
    man "Y-you were supposed to be fucking dead right now."
    mc "so that's what happened... Do you know when I can get out ?"
    aga "ugh"
    call reset_camera
    aga "I think..."
    hide agata
    show agata default:
        pos (1210, -1) 
    with dissolve
    aga "I think I hit my head..."
    aga "I imagined that [mc] was alive and he was opening his eyes."
    #have her easeinbottom
    aga "and..."
    menu:
        "Talk to her":
            mc "Hi Agatha."
        "Say Hey":
            mc "Hey."
    show agata shocked:
        subpixel True 
        pos (1210, 0) 
        linear 0.13 pos (1227, -48) 
        linear 0.09 pos (1175, -35) 
        linear 0.07 pos (1135, -1) 
    with Pause(0.39)
    show agata shocked:
        pos (1135, -1) 
    window show
    aga "..."
    everybody "..." 
    window hide
    show agata shocked:
        subpixel True 
        pos (1135, -1) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
        linear 0.28 pos (1130, 304) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 68.0) 
    with Pause(0.38)
    show agata shocked:
        pos (1130, 304) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 68.0) 
    #she blacks out again.
    window hide
    show mandy default:
        subpixel True 
        xpos 355 
        linear 0.34 xpos 734 
    show martha disappointed:
        subpixel True 
        xpos 871 
        linear 0.34 xpos 1256 
    with Pause(0.35)
    show mandy tired
    everybody "Agatha!"with vpunch  #everyone with vpunch
    kim "I Swear look at him"
    #kim comes back with the medic"
    medic "It's not posiible ma'am he is..."

    show kim default:
        xpos -609 
    show doc norm:
        pos (-855, -29) zoom 1.37 crop (0.0, 0.0, 1.0, 1.0) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -150.0, 0.0) 
    with dissolve
    
    window hide
    show kim default:
        subpixel True 
        xpos -609 
        linear 0.37 xpos 395 
    show doc norm:
        subpixel True 
        xpos -855 
        linear 0.37 xpos -138 
    with Pause(0.37)
    show kim default:
        xpos 395 
    show doc norm:
        xpos -138 
    show doc surp:
        subpixel True 
        parallel:
            pos (-138, 0) 
            linear 0.04 pos (-104, -29) 
            linear 0.04 pos (-161, 17) 
            linear 0.05 pos (-138, 0) 
            pos (-138, 0) 
            linear 0.04 pos (-104, -29) 
            linear 0.04 pos (-161, 17) 
            linear 0.05 pos (-138, 0) 
            pos (-138, 0) 
            linear 0.04 pos (-104, -29) 
            linear 0.04 pos (-161, 17) 
            linear 0.05 pos (-138, 0) 
        parallel:
            zoom 1.5
            linear 0.04 zoom 1.4 
            zoom 1.5
            linear 0.04 zoom 1.4 

        parallel:
            zoom 1.5
            linear 0.04 zoom 1.4 
    with Pause(0.26)
    show doc surp:
        pos (-138, 0) zoom 1.4 
    window show


    medic "Sweet mother of jesus."
    medic "He is fucking alive!"
    show kim one eye blink
    kim "Told ya"
    show kim happy

    #visible confusion
    mc "Hey Doc when can I get home?"
    medic "..."

    show martha happy:
        subpixel True zoom 1.03 
    # show martha happy
    with dissolve
    mar "It's a Miracle Doctor my boy woke up!"
    show martha happy:
        subpixel True zoom 1.0
    show doc norm
    medic "I..."
    medic "I have no words."
    medic "Please I will have to ask all of you to leave the room."
    show kim angry
    show martha sad
    show kim:
        zoom 1.03
    kim"What why ?!"
    show kim:
        zoom 1.0
    show doc norm:
        zoom 1.45
    medic "Clearly we need to make some more exams on him,and acess the situation there must be an explanation for this..."
    show doc norm:
        zoom 1.40
    show martha angry
    window hide
    show martha disappointed:
        subpixel True 
        pos (1256, 0) 
        linear 0.05 pos (1296, 22) 
        linear 0.05 pos (1273, -23) 
        linear 0.03 pos (1256, 0) 
    with Pause(0.23)
    show martha disappointed:
        pos (1256, 0) 
    window show


    mar "wow geez Doc you barely sound excited he is alive."
    show mandy sad
    man "Yeah what the fuck is wrong with you?"
    medic "Lisen ma'am with all due respect leave the room now, and take that girl to infirmary."
    window hide
    show martha:
        zoom 1.03
    mar "I'm not leaving my Boy here with you I want him home."
    #menu choices here depend if the mc is submissive or not.
    #full sub
    show martha:
        zoom 1.0
    if route == "sub":
        mc "Land Lady It's ok"
        mar "Are you sure ?"
        mc "Yes I'm feeling well, just my body that hurts a lot"
        mar "Ok but... if you need anything call us ok ?"
        mc "Will do"
        medic "alright let's acess this situation"
    #dominant
    if route == "dom":
        mc "Let then Stay."
        show doc:
            zoom 1.4
        medic "They can't stay it's against medical protocol."
        show doc:
            zoom 1.35
        show kim:
            zoom 1.03
        kim "Protocol be dammed doc can't you see this is a miracle."
        show kim:
            zoom 1.0
        show martha:
            zoom 1.03
        mar "Yes! we need to be here with him."
        show martha:
            zoom 1.0
        show doc:
            zoom 1.4
        medic "ALRIGHT! I understand."
        everybody "..."
        show doc:
            zoom 1.35
        medic "Let's take you trought some exams again young man."
        mc "Alright."
    #switch
    if route == "swi":
        mc "I want Martha to Stay."
        medic "Nobody can stay It's against protocol."
        mc "Oh C'mon doc Let her Stay I need her."
        mar "Please doc I won't get in your way."
        medic "I... tsk  Right but the rest of you get out now!"
        medic "I'll call in the nurses we need to run you thorught some tests."
        
    " A few hours later."

    mc "So doc how does it look?"
    medic" Well, your recovery is miraculous young man."
    medic "Someone up there must really like you."
    mc_thought "somehow I doubt that..."
    mc "so how long until I'm up and kicking again?"
    medic "8 Weeks give or take."
    mc "2 MONTHS ?!"
    medic "That's what I said..."
    medic "Ayway I'll leave you too it."
    mc "Wait!"
    mc_thought "He left."
    mc "motherfucker..."
    if developer_checkpoints:
        menu:
            "checkpoint":
                pass
    if route == "sub":
        # if sub route fade to black.
        #dream sequence with licue."
        jump licue_dream
        return
    if route == "swi":
        jump hospital_switch_route
    if route == "dom":
        jump hospital_dominant_route

label hospital_nurse:
    #morning hospital machine going beep beep as sfx
    #mc slowly opens eyes. medic and nurse are there in front of him
    medic "Good morning kid."
    medic " how are you holding up ?"
    mc " Ugh..."
    mc "I'm fine I guess."
    medic " Alrightm this is Nurse Kelly."
    nur "Hello mc "
    medic "she will be responsable for taking care of you, so be nice to each other."
    mc "..."
    nur "Don't worry mc, you will be out of here in no time."
    medic "Alright, I'll get going now you take care of him."
    nur " Doc check don't forget to check the patient on room 404, he had some complications last night."
    medic "Alright I'll head there now."
    #he leaves.
    nur "Can you swallow ?"

    #menu need to talk about what this things will give as far as stats go.
    menu:
        "S-swallow!?":
            nur "The medications silly"
            mc "oh...haha."
        "can you ?":
            nur "Woke up full of energy I see."
            nur " But I'm talking about your medication, and breakfast."
            mc "oh."
        "yes.":
            nur "alright good."

    #swalloing sound.
    nur "Alright good."
    nur "Just so you are aware,of your routine."
    nur " Every morning and night I'll come to your room,bring you your medicine."
    nur "During Days you can receive visits."
    nur "or just watch the TV over there,sometimes the Doc will come here check on you."
    nur " And you might need to make a few exams so we know how you are progressing."

    #menu once u choose one make the other dissapear
    menu:
        "Can I get out of my room ?" if can_get_out == False:
            $ can_get_out = True
            nur "No."
            mc "And if I do ?"
            nur "We will tie you to your bed. And you will be slapped with a Fine."
            mc "..."
        "So Hey..." if so_hey == False:
            $so_hey = True
            mc "Wasn't I supposed to have someone here with me as a companion."
            nur "Yes, but you are pretty well considering your accident, so administration is evaluating the situation."
            nur "I'll give you an update once their decision has been made."
            mc "Oh ok but what you think they are gonna say."
            nur "Probably not necessary, since its only mandatory for people who require constant care."
        "What about showers ?" if what_about_showers == False:
            $ what_about_showers = True
            nur "We will take care of that for you, since in your state you have no condition of doing it yourself."
            mc "You people are going to shower me ?!"
            nur "Mostly me since i'm the one taking you into my care."
            mc "I see..."
            nur "well that's if for now, do you require anything else ?"
            mc "No I'll be fine."
    nur "Ok, if you need anything press the button next to your bed, there is the TV remote, see you later mc."

        #make this a text to the player."
    show blacked with dissolve
    centered "You´ve been hospitalized and are recovering from your wounds. \n Spend your time wisely..."
    hide blacked with dissolve
    #fade to black.

    #maybe have the day be announced tuesday. gonna lay down some generic dialog

    #meds
    "You've taken your medication you feel Tired"
    "You woke up in the afternoon."
    #repeat the 2 above for 3/5 days dependinf if submissive or dom,dom gets recovered faster."
    "You've gotten used to your meds, you can now do something during the morning."

    #morning."
    " You Now can Do thing During the morning, but your body is still not fully recovered."
    "Some activities might make you sleep during the afternoon."
    "What will you do?"
    window hide

    #not sure if should be a menu or image button either way here you go dialogs
    #TV
    # the x plus a number means the times a dialog should repeat before it changes.
    return

label watch_hospital_tv:    

    #Fist dialog
    if watch_tv_first == True:
        $ watch_tv_first = False
        "Watch TV ?"
        mc "Looks like they have a few streaming platforms here."
        mc "I could binge a show, I bet time would fly if I did that."
    
    menu: 
        "What will you watch ?"
        "Horror show.":
            if tv_horror_count == 0:
                $ tv_horror_count = 1
                mc "Let's see if there is anything good."#first watch
                "The show was too scary, you coulden't finish it." #raise courage notif at the end of this lines
                notif "You're courage has increased slitly."
                $ courage += 0.5
            elif tv_horror_count == 1:
                $ tv_horror_count = 2
                mc "Ok, This time I'll definitly finish it."
                "You Rewatched it, and almost made it to the end before a jump scare got you."
                notif "You're courage as increased slitly."
                $ courage += 0.5
                
            elif tv_horror_count == 2:
                $ tv_horror_count = 3
                mc"Fuck off, I Literally came back from the dead this shit won't scare me!!"
                "You watched the Horror show again."
                "This time you finished it."
                notif "You're courage has increased."#bonus
                $ courage += 1
            elif tv_horror_count == 3:
                $ tv_horror_count = 4
                mc "I Want to watch,something scary lets see what they got."
                "You watched a horror Movie"
                #no courage increace."
            elif tv_horror_count == 4:
                $ tv_horror_count = 5
                mc"In the mood for something scary, lets see."
                "You watched a ghost story special."
                "The ending said based on real events, you got a shivver on your spine."
                notif "You're courage has increased slitly."
                $ courage += 0.5

            elif tv_horror_count == 5:
                $ tv_horror_count = 6
                mc"Feel like a need a good scare to get the blood pumping."
                "You watched another season of the scary show you first saw."
                "It wasn't as good as first season"
                    #no stat.
            elif tv_horror_count == 6:
                "You watched a Horror story."

        "Action show.": 
            if tv_action_count == 0:
                $tv_action_count = 1
                mc "Oh man, They must have some good action movies here right."
                mc "I was looking foward to Slaughterhouse warriors 5, that Actor everyone hypes will be on it." #First watch.
                "You watched An action movie."
                "It was way better then you expected."

            elif tv_action_count == 1:
                $tv_action_count = 2
                mc"I need some action to get this boredon out of my mind lets see."
                "A new show caught your eye."
                "You decide to watch it."

            elif tv_action_count == 2:
                $tv_action_count = 3
                mc"I wonder if a new Episode is out alredy."
                "You decided to watch that action show again."

            elif tv_action_count == 3:
                $tv_action_count = 4
                mc "Fuck, It's just living rent free in my mind now, I have to see it."
                show blacked with dissolve
                centered "3 days passed \n You Binged the action show. "
                call time_days_next(3)
            
            elif tv_action_count == 4:
                "you watched an action show."

            elif tv_action_count == 6:
                $tv_action_count = 7
                mc "Oh man..."
                mc "Ludwig Von Lust, what a chad, what a crazy journey."
                mc" I doubt there is going to be anything that comes close to Peniless and unwise season 1, but I have an itch."
                "You decided to search for action shows to watch."
                "You didn't find anything."

            elif tv_action_count == 7:
                $tv_action_count = 8
                mc "Ok Maybe today I'll find something."
                "You decided to search for action shows to watch."
                "One caught you eye, But you dropped after 2 eps."
                mc "no luck lately..."
                mc "Maybe today."
                "You decided to search for action shows again."
                "You found a movie you enjoyed."
            #generic."
            elif tv_action_count == 8:
                $ tv_action_count = 9
                "You watched an action movie."
            elif tv_action_count == 9:
                $ tv_action_count = 10
                "You watched a super hero movie."
            elif tv_action_count == 10:
                $ tv_action_count = 8
                "You watched a Drama."

        "Documentaries.":#Raises Knowledge:
            if tv_documentaries_count == 0:
                $ tv_documentaries_count = 1
                mc "Documentaries, oh man haven't watched these in a long time."
                mc "Let's see if they changed at all."
            #two lines above first time only.
                "You watched a documentary about the Dragon of Komodo Flesh melting venom."
                #nothing on the first try.
            elif tv_documentaries_count == 1:
                $ tv_documentaries_count = 2
                mc "That was pretty interesting, I wonder if i can learn something new again."
                "You decied to watch a documentary again."
                "You watched Two brothers make a Banana Foster Liquor from scrach."
                "Your mouth waters for a drink..."
                notif "Knowledge increased."
                $ knowledge += 0.5
            elif tv_documentaries_count == 2:
                $ tv_documentaries_count = 3
                mc"What other stuff will they have today."
                "You decided to watch another documentary."
                "You learned about the legend of a car that had won a race every single day, for years."
                "You feel inspired..."
                notif "You're knowledge has increased."
                $ knowledge += 0.5
            elif tv_documentaries_count == 3:
                $ tv_documentaries_count = 4
                mc "Why not."
                "You decided to watch a documentary again."
                "You learned about Rome and its people."
                notif"You're knowledge has increased."
                $ knowledge += 0.5
            elif tv_documentaries_count == 5:
                $ tv_documentaries_count = 6
                mc "Let's see."
                "You decided to watch a documentary again."
                "You Learned about Electronic music, and its evolution."
                notif "You're knowledge has increased."
                $ knowledge += 0.5
            #generic line
            elif tv_documentaries_count == 6:
                $ tv_documentaries_count = 7
                "You watched a documentary."
                #no reward. x3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ASK EVO 
            elif tv_documentaries_count == 7:
                $ tv_documentaries_count = 8
                "You watched a documentary."
                #no reward. x3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ASK EVO 
            elif tv_documentaries_count == 8:
                $ tv_documentaries_count = 9
                "You watched a documentary."
                #no reward. x3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ASK EVO 
                notif"You're knowledge has increased."
                $ knowledge += 1
            elif tv_documentaries_count == 9:
                "You watched a documentary."
                #no reward. x3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ASK EVO 


        "Serial Killer Stories.": #Raises courage a lot
            if tv_serial_killer_count == 0 and courage < 2:
                $ tv_serial_killer_count = 1
                "You tried to watch a serial killer documentary."
                "you didn't have enough courage to do it." #unlock the dialogs bellow when his corage has reached the max on the horror movies
            elif tv_serial_killer_count == 0 and courage > 2:
                $ tv_serial_killer_count = 2
                mc_thought "Oh boy,they have these."
                mc_thought "It won't hurt giving it a try right ?"
                "You watched a Serial Killer Documentary."
                "You learned about the methods of the killer and his victims."
                "You spend the day thinking about it."
                "Later that night you coulden't sleep..."
                notif"You're courage has increassed."
                $ courage += 1
                 #Maybe keep it a secret that increases a lot if horror is 1 point this is 2 kekw. <<<<<<<<<<<<<< ask evo<<<<<<<<<<<<<<<<<<<<
            elif tv_serial_killer_count == 2:
                $ tv_serial_killer_count = 3
                "You decided to watch a Serial Killer documentary."
                mc "Wow..."
                mc "If he didn't get cocky he would never been caught."
                notif"You're courage has increased Siginificantly."
                $ courage += 1.5
            elif tv_serial_killer_count == 3:
                #generic
                "You watched a Serial killer documentary."
                #no reward."
        
        "reality show.": #Raises Charisma, Lowers Knowledge.:
            if tv_reality_show_count == 0:
                $ tv_reality_show_count = 1
                mc "Oh man... Reality shows it's been a long time since i've seen one of those."
                mc "That title its absurd."
                mc "I have to watch."
                "You decided to watch A absurd reality show"
            #lines above are first dialog only
            elif tv_reality_show_count == 1:
                $ tv_reality_show_count = 2
                mc "Oh boy. My favorite show got a new EP let's see sharons shenanigans."
                "You decided to watch ther reality show again."
                "You learned a thing or two with Sharon."
                notif "You're charisma has increased."
                $ carism += 0.5
                "You decided to watch the reality show again."
            elif tv_reality_show_count == 2:
                $ tv_reality_show_count = 3
                mc "OH MY GOD."
                mc "She has to win right?! no fucking way she did that."
                "You enjoyed the show Your favorite girl made it to the semifinals."
                notif "You're charisma has increased."
                $ carism += 0.5
            elif tv_reality_show_count == 3:
                $ tv_reality_show_count = 4
                mc "Things are heating up I wonder what is going to happen!"
                "You decided to watch the reality TV show again."
                "Sharon made it to the Final."
                "You were so happy that your broken bones hurt from moving around."
                notif "You're charisma has increased."
                $ carism += 0.5
            elif tv_reality_show_count == 4:
                $ tv_reality_show_count = 5
                mc "this is it. The final showdown, C'mon Sharon you can WIN THIS!!!"
                "You watched the Final episode of the Reality show."
                "It was a long and arduous battle but in the end..."
                "Sharon came out on top!"
                notif "You're charisma has increased Siginificantly."
                $ carism += 1.5
                call time_skip_to_night
                #skip to night."
            elif tv_reality_show_count >= 5 and  tv_reality_show_count <= 7:
                $tv_reality_show_count += 1
                "You decided to watch a reality TV show."
                "Nothing caught your attention." #x3
            elif tv_reality_show_count == 8:
                $ tv_reality_show_count = 9
                "You decided to watch a reality TV show."
                "You had a good time with a cooking show."
                notif "You're charisma has increased."
                $ carism += 1
            elif tv_reality_show_count == 10:
                "You decided to watch a reality TV show.yep"
                "You had a good time with a cooking show."
        
        "Local TV.": #Raises Understanding
                if tv_local_count == 0:
                    $ tv_local_count = 1
                    "You decided to watch the local News."
                    "There was a report about you."
                #first dialog.
                elif tv_local_count == 1:
                    $ tv_local_count = 2
                    "You decide to watch the local news again."
                    "You learned about a tourment taking place in your college soon."
                elif tv_local_count == 2:
                    $ tv_local_count = 3
                    "You decided to watch the local news."
                    notif "You're understanding has increased."
                    $ understanding += 1
                #repeat 3 times with understanding gain and after that no gains.
                #Generic
                elif tv_local_count == 2 :
                    $ tv_local_count = 3
                    "You decided to watch the local news."
                    notif "You're understanding has increased."
                    $ understanding += 1
                elif tv_local_count == 3:
                    $ tv_local_count = 4
                    "YOu watched the local news."
                    "nothing interesting happened."
                elif tv_local_count == 4:
                    $ tv_local_count = 5
                    "You watched the local news."
                    "You are up to date on the town."
                elif tv_local_count == 5 :
                    $ tv_local_count = 3
                    "You decided to watch the local news."
    return

label set_next_visit(who):
    "this is who [who]"
    if calendar.current_week_day == 3:
        $ friday_visit_who = who
        return
    if calendar.current_week_day == 5:
        $ wednesday_visit_who = who
        return
    return


label arcana:
    if arcana_count == 0:
        "You think about what Licue told you, her precise words."
        "What were they ?"
        menu:
            "Coatlick I call you on  a tree give me your strengh":
                "You uttered the words..."
                "Nothing happened."
                "You decided to try again another time."
                call time_next
                return
                #if he fails to pick the right one can only try tomorrow, either skip the afternoon or make him unable to medita again

            "Coatlicue I call Upon you Give me your strenght!":
                "You uttered the words..."
                "You feel something inside of you..."
                "But nothing happened."
                "You decided to try again another time."
                call time_next
                return

            "Coatlicue I call Upon thee give me thy strengh.":
                "You uttered those words."
                "You feel something Inside of you."
                "It's a burning feeling on your chest..."
                "An overwhealming power."
                "You faint...." #skip to next day
                call time_days_next(1)
        mc "Huh?!"
        nurse "Oh you're awake, great I got your medication here."
        mc "What happened ?!"
        nurse "You're blood pressure was really low, it seens you fainted."
        nurse "But you should be fine now everything has stabalized."
        nurse "the electrocardiogram didn't show anything abnormal nor did the blood exams."
        nurse "Shoulden't be anything serious."
        nurse "Anyway see you later." # she leaves the room
        mc "Shit..."
        mc "I need to be more careful."
        mc "I should try to focus on that feeling without calling on her power."
        $ arcana_first = False
        $ arcana_count == 1
        return
if arcana_count == 1:
    $ arcana_count = 2
    #generic dialog
    "You decided to meditate and focus on that feeling..."
    "Just as you saw in countless animes..."
    "You learned nothing."
    return

if arcana_count == 2:
    $arcana_count =3
    "You decided to meditate and focus on that feeling..."
    "You started thinking about [girl with most visits]..."#if possible make the girl with most visits name show
    "And got an erection."
    "You learned nothing."
    return

if arcana_count == 3:
    $arcana_count = 4
    "You decided to meditate and focus on that feeling..."
    "You feel something inside of you."
    "It burns as before, but you manage to bear it."
    "You feel really tired."#gains arcana bonus if u read the book auntie gave u
    return

if arcana_count == 4:
    $arcana_count = 5
    "You decided to meditate and focus on that feeling..."
    "You feel something inside of you."
    "It burns, but you can withstand it."
    "You don't feel as tired, but it's already late."#gains
    return

if arcana_count == 5:
    $arcana_count = 6
    "You decided to meditate and focus on that feeling..."
    "You feel something inside of you."
    "You can almost grasp it..."
    "It seens you are beggining to understand Licue's power."
    "you decided to rest." #gains
    return

if arcana_count == 6:
    $arcana_count = 7
    "You decided to meditate and focus on that feeling..."
    "You feel something inside of you."
    "It burns,you feel it flowing trought your whole body dancing inside of you."
    "It's such an Intence feeling."
    "You are Erect during all of it on the edge of orgasm..."
    "As you calm down from the experience, you feel as you got edged for hours..."
    " and your hospital gowl is definitly stained with precum."
    "But now you Understand how to not faint, it might be time to try it on someone."#gains end
    return


if arcana_count == 7:
    $arcana_count = 8
    "You decided to meditate and focus on that feeling..."
    "You feel something inside of you."
    "You focus on what you've read on the book Carol Gave you."
    "You feel that burning energy coursing trought your body."
    "It's almost too much to bear, but you push trought it."
    "You can feel your member start to rise, and stand in full attention..."
    "You keep your mental fortitude, despite feeling like you are being molested by Licue from beyond the realm of the living."
    "Your Heart beats a faster and faster, Your mind goes completely blank blocking out everything else."
    "The sound of the hospital machines,people outside your room, your own thoughts."
    "You feel One with this borning fire you can feel it pulsating bellow your waist."
    "A burning passion."
    return

    menu:
        "Embrace it.":
            "You embrace the flames, Immersinging yourself in the Fire, It burns off all your inibitions, you feel free, the flame..."
            "Fills you with passion and desire,you feel it going deeper and deeper..."
            "Until It all come crashing down." #cum sounds/screen flashing white
            "It all Leaves you as soon as it entered your body, All of it Its spurting out of you."
            "Your thoughts,worries,friends family, all is forgotten as you keep cumming."
            "Your last shred of resistance is squashed as on last rope of cum shoots out of your cock."
            "You start to lose consciousness and fade into the abyss..."
            #black screen,into the eye opening transition.
            mc "...where am I ?"
            nurse "Look at you."
            nurse "Was the sleep good ?"
            mc "Huh?"
            nurse "Guess you don't remember huh."
            nurse "Oh well, it was quite the site when we got in thinking you were having a heart attack..."
            nurse "Just to see you moaning like an animal and Shooting ropes of cum."
            mc "I...?!!"
            nurse "Ahahaha."
            nurse "Don't worry Kid I've seen weirder stuff."
            nurse "But you did almost had  a heart attack after you were done making a mess."
            nurse "So no more jerking off."
            nurse "Doctors orders."
            #she goes out the room.
            "You are completely embarrased."
            "And don't remember anything of what happened."
            "But you might have an Idea of what that power does now."
            "You can call Upon Licue Powers."
    return