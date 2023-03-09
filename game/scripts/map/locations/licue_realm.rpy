screen licue_realm():

    frame:
        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))
    use top_screen


label licue_realm:
    if licue_realm_quest == True:
        call licue_realm_quest
    return

label licue_realm_on_enter:
    return

label licue_realm_quest:
    # scene licue throne
    window hide
    show licue throne:
        subpixel True yzoom 1.0 zoom 2.73 
        pos (-682, -667) zpos 0.0 
        linear 4.7 pos (-2500, -1817) zpos -51.0 
    with Pause(4.7)
    pause 0.5
    show licue throne:
        pos (-2500, -1817) zpos -51.0 
    window show
    hide licue throne
    show licue throne with dissolve

    sci "You Mortal what brings you here?"
    #she appears before him maybe have a panning shot from head to toe of her body make her look imposing and godly on the CG.
    #btw keep notes of the stuff here that needs to be drawn so Gen knows it before hand, might need to tweek it after she does the art
    #so both writing and art better marry each other, also this why i'm not giving detailed descriptions.
    mc "I..."
    #menu have the mc talk to her and only progress after getting all his doubts out of the way, or have one to skip it.
    #if you want the mc to repeat himself after choosing a line just copy paste it

    while am_i_dead == False or who_are_you == False or what_is_this_place == False or you_said_you_dont_know == False or when_you_said == False:
        menu:
            "Am I dead ?":
                $ am_i_dead = True
                sci "It would seen so."
                mc "B-but how ?!"
                sci "Well Let's take a look"
                #she sits on the throne no matter what option you pick.
                sci "Hit by a truck, cause of death."
                mc "That's... how I go."
                sci "How original of you."
                sci "Huh?!"
                sci "Oh dear, It would seen you weren't supposed to Die."
                mc "What?!"

            "Who are you ?":
                $ who_are_you = True
                $ sci.name = "Scilla"
                sci "I'm Scilla Goddess of [redacted]" #make the Goddess of text corrupt like the mc can't understand it.
                mc "W-what?! Why am I here ?"
                sci " You are here, because your time on the realm of the living has ended."
                sci " But. That is indeed a good question Mortal."
                sci "And one that I have no answer to."

            "What is this place ?":
                $ what_is_this_place = True
                sci " This is my domain the palace of [redacted]" #again same with her title corrupted text
                mc "The what ?!"
                sci "Palace of [redacted]."
                mc "..."
                sci "Ugh, your soul is too weak I'm surprised you can even understand what I'm saying"

            "When you said you don't know Why I'm here." if who_are_you == True and what_is_this_place == True and am_i_dead == True:
                $ you_said_you_dont_know = True
                mc "what do you mean by this."
                sci " I'm a forgotten Idol mortal my power has faded across milenia."
                sci "the cult of my worship is all but forgotten."
                mc "but... Why then ? am I here?"
                sci "I see you are lost but worry not I'll think of something."

            "Of course Goddess Please think of something to help me."if you_said_you_dont_know == True:
                $ goddes_help_me = True
                mc_thought "what is wrong with me why do i keep calling her that?"
            
            "When you said I wasn't supposed to die." if goddes_help_me == True:
                $ when_you_said = True
                mc "How do you know that ?"
                sci "Quite simple I know when mortals Will expire."
                sci "I'm a goddess after all."
                mc "Then why did I die ?"
                mc "Why am I here ?!"
                sci_shout "Mortal!"
                #make her eyes glow and a pink aura evelopt the screen."
                sci "Worry not for I will give you a solution."
                mc "Yes Goddess."
                #use this line in case the player clicked the "i wasn't supposed to die option first,or right after it."
                mc_thought "W-why did I call her that, I feel so..."
                mc_thought "Relaxed"
    
    mc "What are you going to do to me ?!"
    #she gets up from her throne and descent the stairs towards the mc.

    sci "My my... Aren't you cute."

    sci "What is your name boy ?"
    #maybe this would be a good time to have the name prompt
    mc "It's [mc] G-goddess."
    sci "What an exquisite name you have my dear."
    sci "Do you want to know what I have planned for you ?"
    # scene licue throne
    scene
    show licue throne:
            pos (-469, -67) zoom 1.46 crop (0.0, 0.0, 1.0, 1.0) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(-631.0) 
    with vpunch
    pause(0.1)
    hide licue throne    
    scene licue throne


    menu:
        
        "What is this? I fell some...force trying to dominate me."
    #resist
        "resist":
            $ resist += 1
            mc "What are you going to do to me ?!"
            sci "Oh my, Aren't you resilient what a surprise."
            sci "Perhaps you will prove more Useful then i thought."
            mc "What are you talking about ?!"
            sci "Relax... my sweet child I'll tell you."
            jump after_resiste_once
    # relax from the let go
        "relax":
            $ relax += 1
            mc "Yes Goddess."
            mc "What have you got planned for me."
            hide licue throne
            show licue throne:
                    pos (-303, -80) zoom 1.53 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(9.0, 0.0, 0.0) 
            with dissolve

            sci "You will make a Fine pet for me my dear."
            $ route = "sub"
            jump full_sub
    return

label after_resiste_once:
    scene
    show licue throne:
            pos (-469, -67) zoom 1.46 crop (0.0, 0.0, 1.0, 1.0) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(-631.0) 
    with vpunch
    pause(0.1)
    hide licue throne    
    scene licue throne
    #resist again.P
    menu: 
        "AHHHHH AGAIN?"
        "Resist Again":
            $ resist += 1
            mc "I'm not a child Tell me what are you going to do with me."
            mc "You said I wasn't supposed to die so now what ?"
            sci "Hoho, You seemed so bland and weak, guess I awoken something in you huh."
            sci "Even better."
            $ route = "dom"
            jump resist_everything
        "Relax":
            $ relax += 1
            mc "Y-yes Goddess..."
            sci "Good boy."
            sci "I don't want you to be completely neutered after all, but you need to know your place."
            $ route = "swi"
            jump resist_then_relax

    return

label full_sub:

    sci "now the way I see it You only have two options."
    #full sub dialog/route
    mc "Wich one Goddess wants me to pick ?!"
    mc_thought "What am I saying !!"
    sci "My oh my."
    sci "I'll send you back to earth my dear."
    hide licue    
    show licue throne:
            pos (-700, -163) zoom 1.94 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(15.0, 0.0, 0.0) 
    with dissolve
    sci "But you will bear my mark, and will spread my influence."
    mc "Yes Goddess."
    mc "Anything for you."
    mc_thought "What!!! I-i... why Would I say that?!"
    mc_thought "It's like I'm a passanger in my own body."
    mc_thought "This Isnt good I need to resist..."
    mc_thought "Somehow..."
    sci "What a well behaved Dog you are [mc]." #remember to change this to the custom name prompt
    scene
    show licue throne:
        pos (-71, -51) zoom 1.1 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(9.0, 0.0, 0.0)
    with dissolve
    sci "Now, show me all of that devotion, let's see if you really mean it."
    scene blacked with dissolve
    pause (0.5)

    show sub_licue_suck
    with dissolve

    #fade to black have some sound effects."
    #show Licue on top of him crushing his hard cock with her feet."
    sci "That's it."
    sci_shout "Put that tongue to work slave." with vpunch
    mc "Mmmmmggnnnn!!!"
    mc_thought "She!!!WHAT!!!"
    sci "What is that ?"
    sci "You are going to have to speak up HAHAHA!"
    sci "Oh that's right you can't."
    sci "work that tongue BOY!!"
    mc "MMmgnhh!!!"
    mc_thought "Her smell."
    mc_thought "Her body.."
    mc_thought "Her taste..."
    mc_thought "she is perfect."
    mc_thought "This is bad..."
    mc_thought "I need to breath, But dead people don't need to breath right ?!!"
    mc_thought "I can just keep tasting her."
    mc_thought "The heat from her thighs, the way she is smothering my face into her pussy."
    mc_thought "Ah fuck!!"
    mc_thought "I'm so hard it hurts, she is balancing her entire weight on my cock."
    mc_thought "I've never felt so hopeless as I'm right now."
    mc_thought "It's intoxicating...."
    mc_thought "I can't think properly..."
    sci "MMMMmmmm, That's the stop."
    sci "You must have been a very well behave pet in your past life."
    sci "And oh how eagerly you tremble and twitch Under my feet."
    sci "This is where you belong pet, Worshiping me, beneath me."
    sci "Show me more of your passion!!!"
    mc "MMMMMMM!!!!"
    mc_thought "I can't resist it, I give up!!!"
    mc_thought "I surrender to you Goddess."
    sci "Look at you..."
    scilla" PATHETIC!"
    sci " WEAK!"
    mc "mmmnnghhhh"
    mc_thought "fuck..."
    mc_thought "Evertime she issults me, My heart pounds like crazy."
    mc_thought "And my head goes blank."
    mc_thought "I-is this ?!"
    mc_thought "The power of a god ?!"
    sci " HAHAHA"
    sci "How cute trying to swing your hips like a wild animal in heat."
    show licue sub1 with vpunch
    #she kicks him on his back and steps on his cock.
    mc "*huf huf*"
    mc "G-goddess I."
    sci "Whats wrong ? Don't tell me you are getting all worked up over my feet ?"
    with vpunch
    mc "I-i..."

    # make a meny with 4 options all say BEG!!!
    menu:
        "BEG!!!":
            pass
        "BEG!!!":
            pass
        "BEG!!!":
            pass
        "BEG!!!":
            pass

    mc "PLEASE LET ME CUM I BEG YOU !!"
    sci "Huh ?! Did I hear that right ?"
    sci "You are turned on by me stepping on your worthless little cock ?"

    menu:
        "YES!!":
            mc_shout "Yes!!"
        mc "Please Goddess I beg you please !!"
    scilla"Not convinced, try a little harder you masochistic dog."
    sci "come to think of it, you are of no use to me, I'll throw you out like the trash you are."
    mc "NO!!! PLEASE GODDESS I NEED YOU!"
    mc_thought "I need to Beg, for my life!!"
    mc_thought "To be her pet !!!"
    mc "Without you I'm nothing!"
    mc "Please Let me serve you for all eternity I BEG YOU!!"
    sci "And why would I need such a useless dog like you ?!!"
    mc "I-i can't live without you, I'm addicted to you, you are so amazing I..."
    mc "I'll you do anything for you so please ?!"
    sci "Anything?"
    mc "A-anything..."
    sci "Those women in your life, I want then corrupt and completely under my spell."
    mc "W-what women Goddess ?!"
    sci "Agatha, Mandy, Martha, Ana,Caroline."
    with vpunch
    sci "Did you just throb when I said their names ?!"
    mc "N-no I-i-i!"
    sci "AHAHAHAHAHAA"
    sci "Interesting..."
    sci "When you ressurect,I'll make sure you aren't a lap dog for anyone, that insults you."
    sci "but here, you will be your trueself, my little maso dog."
    mc "Y-yes Goddess."
    mc "Thank you so much for being this generous with me."
    sci "You willingly sold your soul and everyone you know just so you could cum being crushed by my feet."
    mc "..."
    mc_thought "I'm the worst but I can't take it anymore I'm going insane!!"
    sci "It's so pathetic I almost feel bad for then hahaha."
    sci "Now here is your reward." #she crushes his cock with her feet."
    with vpunch
    sci "ORA!!"
    with vpunch
    mc "AAAAArrgh!!!"
    with vpunch
    sci "CUM!"
    with vpunch
    mc "Goddess w-wait!!"
    mc_thought "I'm going to faint if she keeps this up..."
    mc_thought "Why is her feet turning me on so much."
    mc_thought "I wasn't even into this before."
    with vpunch
    with flash
    mc_thought " Oh god... she is being too hard."
    mc_thought " but I'm..."
    show licue sub3
    mc_shout "cumming..." with flash
    call change_location_to("Hospital Room")
    return
    #screen flashes white and with spurt sounds mc wakes up in the hospital bed scene.

label resist_then_relax:
    #resist then relax dialog. since this is the switch route, i forgot i would probaly need a more neutral
    #scene for this since the Dom and sub ones are pretty 'extreme' but use the sub route, see how that works otherwise i'll make a switch one.
    mc "W-what options."
    sci "Well dear."
    sci "I can send you back to earth alive and well."
    mc "Y-you can Goddess ?!"
    sci "Of course i can sweetie, but with one condition."
    mc "What condition ?!"
    sci "You will bear my mark and spread my influence on your world again."
    sci "Can you do that for me?"
    mc "I'll do it!"
    sci "Good boy."
    jump resist_2

label resist_everything:
    #resist everything.
    scene blacked
    # show licue throne:
    show licue throne:
            xpos -207 zoom 1.35 
    sci "Well then my little Hero."
    hide licue throne
    show licue throne
    mc_shout "cut the crap." with vpunch
    mc "what should I even call you ?"
    sci "Call me Licue."
    #mc stands up she looks surprised.
    mc "So Licue. What now ?"
    sci "Well you have two options really."
    mc "Well enlighten me then."
    hide licue throne
    show licue throne:
            xpos -207 zoom 1.35 
    with dissolve
    sci "Option one is I send you back the way you came, and you End up In hell or worse."
    mc "and what is option two."
    sci "Well I'm glad you ask."
    #she looks at him lewdly/horny
    sci "Option two is me sending you back to earth, as you were not supposed to die."
    hide licue throne
    show licue throne
    mc "Of course, and you send me back out of the kindness of your heart ?"
    mc "as if..."
    sci "Ahahaha."
    sci "You are quite amusing."
    sci "most mortals would be chomping at the bit for this kinda of second chance."
    sci "the fact that you were not supposed to die today means nothing to most Gods."
    sci "You would be tossed in the afterlife like garbage."
    mc "Make your fucking point."
    sci "Don't like to entertain a bored Goddess do you?"
    sci "so be it, I doesn't bother me."
    sci "I'll send you back,the only condition is you have to further my influence on the realm of the living."
    mc "How so ?"
    hide licue throne
    show licue throne:
            xpos -207 zoom 1.35 
    sci "I see."
    sci "You do want to go back after all."
    sci "haha"
    sci "Good Yes I like that, You have a fire burning inside of you kid You will be perfect for this."
    mc "So what now?"
    sci "Well now, I'll imbue you with some of my power, so you can easily influence others into worshiping me."
    sci "You will be my Avatar."
    mc "And how are you going to do that?"
    hide licue throne
    show licue throne:
            xpos -280 zoom 1.73
    with dissolve
    sci "Oh I think you will Enjoy this part."
    jump resist_2


    #CG she pushes him to the ground shake screen fade to black come back with her on top of him his clothes are gone and he is naked
    #one last resist prompt.

label resist_2:
    scene licue throne
    mc "I see...." 
    mc "But if are doing this."
    #wresteling sound screen shakes fades to black comes back to MC on top of her
    scene black with dissolve
    pause 0.5
    scene mc top with Dissolve(1.5)
    mc "We are going to do it my way Licue."
    sci "Who knew a virgin would be so full of energy..."
    mc "Shut up!!" with vpunch
    mc "I'm going to pound that smug Smile out of your face."
    sci "Oh yeah ?"
    sci "Go right ahead mortal show me what you are made of."
    show dom1 with dissolve
    menu:
        "put it in":
            pass
    show licue_penetration
    #have him insert in her pussy and the screen shakes, we are watching it on the third person as they fuck on the floor.
    sci_shout " Nngh..."
    mc "W-what's Wrong ?"
    mc "C-can't handle a mortal!?"
    sci "ooh It's been so long C'MON FUCK ME!!"
    # show licue_dom_deep_normal with dissolve
    mc_thought "Fuck she is so incredibly tight I can barely move inside of her."
    mc_thought "Her body is So hot too."
    mc_thought "Fuck It's like I'm fucking a oven."
    mc_thought "The way her insides move, her hot juices running down my balls."
    mc_thought "So this is what is like to have sex."
    sci "Huff.. Haha Are you getting Tired already mortal?!"
    mc "Grrr... Shut up you slutty goddess."
    sci "Make me."
    mc "As you wish."
    scene black  with dissolve
    sci_shout " What are you..."
    #MC kisses her while he fucks her missionary
    # once they separate from the kiss the a saliva trail unties then the succubus looks surprised
    scene licue kiss with dissolve
    sci_shout "mmmmmhnn!!"
    scene licue kiss2 with dissolve

    sci "You have some guts Mortal!"
    mc "Quit calling me that you bitch!"
    # have to differnet sprites for for insertion going in and out so you can animate then with dissolve transitions and maybe implement the slow fast mecanic
    # i'll have some lines here for you.
    #fast
    jump fucking_licue_dom
    return

    label fucking_licue_dom:
    menu:
        "Kiss her again \"as a test\"" if fucked_licue_already:
            $ fucked_licue_already = False
            scene kiss_licue with dissolve
            sci_shout "mmmmmhnn!!"
            scene kiss_licue2 with dissolve
            jump fucking_licue_dom
        "Fast":
            $ fucked_licue_already = True
            scene licue_doom_strokes_fast with dissolve
            sci "C'mon mortal! Give me all you got show me you really want to LIVE!!"
            mc_shout "So you want it HARDER FASTER?!"
            sci "Y-essss  nnnnnghhh."
            sci "FUCK!!"
            mc "Take it like the slut you are LICUE!"
            sci "YES! YES! Yeeeeess!!"
            sci "Keep going like that Mmmmmmm"
            mc_thought "Fuck! Her pussy is trying to rip my cock off, It's gripping me so hard."
            mc_thought "I'm at my limit but I want to keep going this feels too good to stop."
            mc_thought "I'm going to cum inside a Goddess?!"
            jump fucking_licue_dom
        "Slow":
            $ fucked_licue_already = True
            scene licue_dom_deep_normal with dissolve
            sci "Whats the matter ? Haha can't keep up the pace ?"
            sci " Afraid you will cum ?"
            mc "Let's see how long you keep talking shit Licue!"
            # intermitente cada vez que ele empurra fundo no utero dela usa hpunch pra monstrar que ele ta dando umas socada violenta.
            #also in this version have her make the ahegao face for a variation.
            sci " You talk big for a... Mmmmortaal..."#this be the line that u use to transition into the first hpunch socada bruta make her go ahegao
            sci "Oooh fuck fuck FUCK!!"
            mc "What's the matter? Am I going to hard for you ?!"
            sci "Mmmmh"
            mc_thought "Looks like she is out of it."
            mc_thought "Did I really Made a Goddess Lose her mind with my cock?!"
            jump fucking_licue_dom
        "Cum" if fucked_licue_already:
            jump dom_cum_inside_licue
    return
label dom_cum_inside_licue:
    scene licue_doom_strokes_fast
    mc_shout "Alright you Slut!"
    mc "Time to Mark that greedy Womb of yours."
    sci_shout "!!"
    sci_shout "What! WAIT!!" with hpunch
    mc_shout "Here I go!"
    #sound of fast pounding
    scene licue_creampie
    sci_shout "Nghhh I'm CUMMING." with hpunch
    sci_shout " AAAAAAAAAAAAAAAHHHHH"
    sci ". . ."
    mc "Fuck..."
    #CG of her on the floor pussy gaped and cum dripping out of it.
    scene gapped with Dissolve(1.5) 
    window hide
    pause 1.5
    window show
    mc "You look spent."
    sci "Y-you..."
    show licue tired with dissolve
    sci "..."
    sci "...?"
    mc "Come here I'm not done yet."
    show licue knees with dissolve
    mc "Get on your fucking knees for me."
    #mc grabs her by the hair and makes her kneel in front of his cock still hard.
    mc "Now clean my cock you worthless Goddess."
    sci_shout "H-how Dare you"
    menu:
        "Slap her":
            pass
        "Show her who is the boss":
            pass
    #Mc Slaps in the face
    show licue slap with hpunch
    with hpunch
    mc "Suck it!"
    show licue knees with dissolve
    sci "Y-yes!"
    mc "That's more like it."
    mc_shout "Useless cunt."
    window hide
    # scene licue blowjob:
    #     subpixel True 
    #     pos (-591, -850) yzoom 1.01 zoom 1.8 
    #     linear 1.86 pos (0, 0) yzoom 1.0 zoom 1.0 
    # with Pause(1.96)
    # show licue blowjob:
    #     pos (0, 0) yzoom 1.0 zoom 1.0 
    # window show
    show licue_blowjob with dissolve


    # scene licue blowjob with dissolve
    # she sucks his dick religiously
    sci "mmmmgn"
    mc "Don't choke, take it like a good girl."
    mc_thought "Oh this is heaven, I want to do this for eternity."
    mc "Ah who would have guessed that you were so good at sucking mortal cock."
    mc "Is this what you did in the past huh ?!"
    mc "Oh fuck!! that's the spot."
    with flash
    mc_shout " I'm going to cum again!!"
    mc "Aarrrrrghh  FUCK!!!"with hpunch 
    show mc cum with dissolve
    #mc shoot his load in her mouth cum leaks out of her nose and mouth the screen flashs white each rope of cum he shoots get sounds effects for it
    #cg of the mc on the ground sitting on his ass she gets up points at him and shots a magic beam on his chest.
    mc "aaah... *panting* fuck... that...was." 
    scene licue standing with dissolve
    pause 0.5
    window hide
    ""
    scene licue powerfull with dissolve
    pause 0.5
    window hide
    ""
    scene licue aim with dissolve
    pause 0.3
    window hide
    ""
    scene licue_beam with dissolve
    mc"AAAAAAAAAAAAAAAAAHG"
    #mc blacks out smoking rising from his body and a mark on his chest.
    scene licue aim with dissolve
    sci "Fucking bastard..."
    scene blacked with Dissolve(2.0)
    scene blacked
    #fades to black he wakes up
    scene licue throne with Dissolve (2.0)
    sci "Wakey wakey mortal."
    mc "ugh fuck..."
    mc "What was that ?!"
    scene licue throne:
            pos (-303, -80) zoom 1.53 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
    sci "Oh nothing sweetie just finishing the pact is all."
    sci "Since you were so kind to provide me with all of that energy..."
    sci "I was able to force you into it even without you agreeing to it."
    scene licue throne
    mc "You fucking what!!"
    #he feels a deep sharp pain in his chest make him look in pain.
    sci "Uh oh,is my little hero angry?!"
    sci "Aaawn. You make me sad."
    mc "T-the fuck you do to m-me."
    sci "Oh don't worry Goddess will send you back, but you have a mission to fulfill kid."
    mc "and what is that you bitch..."
    sci "You will spread my influence on earth and corrupt as many people as possible, the closer they are to you the better"
    sci "You will even be able to drawn from my powers to help you."
    mc "What does any of that means?"
    sci "Martha" with vpunch
    sci "Agatha" with vpunch
    sci "Ana" with vpunch
    sci "Amanda" with vpunch
    sci "Caroline" with vpunch
    mc_shout "WHAT!"
    mc_shout "HOW DO YOU KNOW THEIR NAMES !!!"
    sci "Ara? you think I don't know about everylast minute detail of your soul mc ?"
    mc "you..."
    sci "If you want then to be safe."
    sci "You will do to them what you did to me. That's how my power works."
    sci "The more corrupt and moraly degenerate they are the better."
    mc "Are you...GGGRR!!"
    mc "You can't expect me to do that are you fucking crazy!!"
    #make her dark live evelyn and switch the bg to the darkness one while she is mad make the screen tremble."
    scene licue throne:
        pos (-469, -67) zoom 1.46 crop (0.0, 0.0, 1.0, 1.0) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(-631.0) 
    with vpunch
    pause(0.1)
    hide licue throne    
    scene licue throne
    sci_shout "YOU WILL DO AS YOU ARE TOLD MORTAL!!"
    sci_shout "OR I'LL MAKE SURE THEIR SOULS BURN FOR ETERNITY!!"
    mc "..."
    sci "NOW WAKE UP!"
    mc" what?!"
    sci_shout "WAKE UP!"
    #mc vision fades to black
    call change_location_to("Hospital Room")
    return
    

label hospital_switch_route:
    mar "Heyy!!"
    mc "Hey..."
    mar "so how it went ?"
    #menu crack a joke or not.
    menu:
        "martha, He said I only have 8 weeks of life left":
            mar "WHAT!!!"
            mar "No-no This can't be true I just got you back and..."
            mc_thought "shit she took it to heart..."
            mc "Martha!! I-i was joking..."
            mar "Y-you Joking ?!!"
            mar "DO you have any Idea how much that messed up with me."
            mar "are you trying to give me a heart attack..."
            mc "I'm sorry..."
            mar "I-"
            mar "I'm sorry mc, It's been a rough day you have no idea how happy I'm that you survived."
            mc "Thanks, but ye."
            mc "I'll be here for 2 months or so."
            mar "!!"
            mar "that long ?!"
            mc "Why ?"
            mar "N-nothing I'm sure you will make a speedy recovery just like today!!"
            mc "Hopefully."
            mar "I'll be Going then, the girls are restless."
            mc "Tell then the news, oh and tell then to visit me and bring me my phone."
            mar "I'll tell then, about your phone..."
            mc "What ?"
            mar "it got crushed in the acident"
            mc "..."
            mar "I-i'll make sure to buy you a new one."
            mc "Don't worry about it."
            mc "Just don't forget to visit me alright."
            mar "Deal, let me go before the hospital staff kicks me out."
            mc "Bye martha." #(When he uses their names make sure to change to the code u use to be custom i'll explain if u need)
            mc_thought "Guess the only thing I can do now is Sleep..."
            jump licue_dream

        "I'll be here for 2 months or so.":
            mar "!!"
            marthat "that long ?!"
            mc "Why ?"
            mar "N-nothing I'm sure you will make a speedy recovery just like today!!"
            mc "Hopefully."
            mar "I'll be Going then, the girls are restless."
            mc "Tell then the news, oh and tell then to visit me and bring me my phone."
            mar "I'll tell then, about your phone..."
            mc "What ?"
            mar "it got crushed in the acident"
            mc "..."
            mar "I-i'll make sure to buy you a new one."
            mc "Don't worry about it."
            mc "Just don't forget to visit me alright."
            mar "Deal, let me go before the hospital staff kicks me out."
            mc "Bye martha." #(When he uses their names make sure to change to the code u use to be custom i'll explain if u need)
            mc_thought "Guess the only thing I can do now is Sleep..."
            jump licue_dream

label hospital_dominant_route:
        #dominant route
    #everyone gets in the room.

    mc "So Doc what are the news?"
    man "Yeah how long is he gonna be here ?!"
    aga "Is he going to live ?"
    aga "he is not a zombie is he ?!"
    man "Is he a vegetable?!"
    #doc looks embarrased
    mc "can you two not talk like I'm not in the room..."
    kim "quiet down girls lets hear the doctor."
    mar "how bad is it doctor, is my boy going to be allright ?!"
    medic "He is going to live ladys calm down."
    medic "We run a bunch of exams on him again and,he somehow recovered really well."
    man "Or maybe your first results were all wrong !!"
    #medic looks embarrased"
    medic "maybe...But [mc] you are going to be here for 8 weeks, until you are fully recovered."
    medic "Unless you miracly heal again, someone upstairs must really like you, I've never seen something like this before."
    "somehow I think I burned that bridge already doc..."
    medic "In any case, we'll be here for you, if you need anything just press the button next to your bed."
    medic "And ladys, visits have ended 3 hours ago, I recommend you don't stay here for much longer."
    man "of course ! we were just about to leave right Mom?"
    kim "wait Mandy. Doc, give us a few minutes with him ok?"
    medic "as you wish, you know the way out." #he leaves the room
    mc "looks like I'll be here for a while..."
    mar" Don't worry We'll visit you regularly so you don't feel alone right girls?"
    kim "Of course I'll bring you something to read."
    aga "..."
    man "I'm still mad at you for making me lose our opening cerimony..."
    man "B-but... I'm glad you are ok..."
    mc "Thank you Mandy agatha Amanda Martha."
    mc "I hope we'll see each other soon."
    mc "mc but now I'm feeling a little tired."
    kim "Get well soon kid."
    mar "Don't get into any trouble!"
    man "Idiot... I'll visit you tomorrow after college."
    aga "G-good luck mc."
    mc "..."

    #screen fades to black as they keep talking and before a bit of silence dream sequence
    kim "Looks like he is doosing off now."
    kim" can't blame him, what a rough day."
    mar "Don't even mention it, my heart is still pumping."
    man "mom you should do some exams too!!"
    mar "No way !  those are really expensive."
    kim "Hey show up to the Gym I'll help you..."
    jump licue_dream

label licue_dream:
    show licue realm morning


    #the same OST used to introduce licue, was thinking of something like an iconic track and sound effect so the player knows wheere he is


    #show the BG of licue dimension

    "this place..."

    #show Licue on her throne.

    sci "So mortal, how was your journey back to the world of the living ?"

    #sub
    if route == "sub":
        mc "I can't beleive I actually resurected this is insane!"
        sci "Oh you will do much more things that seemed insane to a mortal my little one."
        mc "Why did you call me back Goddess?!"
        mc "Do you need anything?!"

    #switch
    if route == "switch":
        mc "You... I really ressurected or was that a Illusion ?"
        sci "Ara Don't you trust me ?"
        mc "I...Yes I'm sorry."
        sci "Awn don't be so down my child."
        sci "There is a reason to why you are here."
        mc "What is it?!"

    #Dom
    if route == "dom":
        mc "You..."
        sci "Why the long face Hero ?"
        sci "Dissapointed HAHAHA!!"
        mc "So it was all bullshit then..."
        mc " Fine by me I'll fucking..."
        sci "Don't even finish that sentence Mortal."
        sci "And worry not, I did keep my promice, you are just in a deep slumber."
        mc "So why am I here ?"


    sci " You see I called Upon you from beyond the veil of dreams, so I could teach you something."
    sci "But this might not be a good idea to use on your state."

    #dom line
    if route == "dom":
        mc "Why the fuck didn't you fully heal me ?"
        sci "Do you think ressurecting a butchered and broken body is an easy task?"
        mc "..."

    sci " Now Remember this, and remember it well mortal."
    sci "You will feel my power flowing throwgh you as I absorve your influence on others."
    sci "When you want me to Nudge people in a certain way, Call Upon my name."
    sci "Coatlicue I call Upon thee give me thy strengh."#make her look scary.
    mc "..."
    sci "now go I need rest, as do you."
    sci " heed my words mortal you will need it."
    scene black with dissolve
    call update_image
    #here is a bit of a routine i'll add the time on a # so u can program it
    jump hospital_nurse


