define slow_interval = 2
define normal_interval = 1
define custom_interval = 0.4
define custom_dissolve_time = 0.2
image sub_licue_suck:
    animation
    "bg/licue sub2.jpg"
    subpixel True 
    zoom 1.0 
    linear normal_interval zoom 1.06 
    linear normal_interval zoom 1.0
    repeat

define flash = Fade(.15, 0, .75, color = "#b8b8b8ff")
define flashbulb = Fade(0.2, 0.0, 0.8, color = '#fff')

image licue_dom_shallow:
    animation
    "bg/dom2.jpg" with Dissolve(custom_dissolve_time)
    # "bg/dom2.jpg" with vpunch
    pause custom_interval
    "bg/dom3.jpg" with Dissolve(custom_dissolve_time)
    pause custom_interval
    repeat

image licue_doom_strokes_normal:
    animation
    "bg/dom2.jpg" with Dissolve(custom_dissolve_time)
    # pause custom_interval -0.15
    # "bg/dom3.jpg" with Dissolve(custom_dissolve_time)
    pause custom_interval 
    "bg/dom4.jpg" with Dissolve(custom_dissolve_time-0.1)
    "bg/dom4.jpg" with vpunch
    pause custom_interval 
    # "bg/dom3.jpg" with Dissolve(custom_dissolve_time)
    # pause custom_interval 
    repeat

image licue_doom_strokes_fast:
    animation
    "bg/dom2.jpg" with Dissolve(custom_dissolve_time)
    pause custom_interval -0.15

    "bg/dom4.jpg" with Dissolve(custom_dissolve_time-0.1)
    "bg/dom4.jpg" with vpunch
    pause custom_interval 
    repeat

image licue_creampie:
    animation
    "bg/dom2.jpg" with Dissolve(custom_dissolve_time -0.15)
    pause custom_interval + 0.5
    "bg/dom3.jpg" with Dissolve(custom_dissolve_time)
    pause custom_interval + 0.1

    "bg/dom4.jpg" with Dissolve(custom_dissolve_time-0.1)
    "bg/dom4.jpg" with vpunch
    pause 1.5
    "bg/dom4.jpg" with vpunch
    pause 1.5
    "bg/dom4.jpg" with vpunch
    pause 1.5
    "bg/dom4.jpg" with vpunch
    pause 2
    "bg/dom5.jpg" with Dissolve(2.0)
    pause 0.1


    
image licue_dom_deep_normal:
    animation
    "bg/dom2.jpg" with Dissolve(custom_dissolve_time)
    pause custom_interval
    "bg/dom3.jpg" with Dissolve(custom_dissolve_time)
    pause custom_interval
    "bg/dom4.jpg" with Dissolve(custom_dissolve_time-0.1)
    "bg/dom4.jpg" with vpunch
    pause custom_interval - 0.1
    "bg/dom3.jpg" with Dissolve(custom_dissolve_time)
    pause custom_interval 
    repeat

image kiss_licue:
    animation
    "licue kiss" with Dissolve(custom_dissolve_time)

    pause custom_interval
    "licue kiss" with Dissolve(custom_dissolve_time-0.1)
    "licue kiss" with vpunch
    pause custom_interval - 0.1
    "licue kiss" with Dissolve(custom_dissolve_time)
    pause custom_interval 
    repeat 

image kiss_licue2:
    animation
    "licue kiss2" with Dissolve(custom_dissolve_time)

    pause custom_interval
    "licue kiss2" with Dissolve(custom_dissolve_time-0.1)
    "licue kiss2" with vpunch
    pause custom_interval - 0.1
    "licue kiss2" with Dissolve(custom_dissolve_time)
    pause custom_interval 
    repeat 

image licue_penetration:
    animation
    "dom1" with Dissolve(0.3)
    pause 0.1
    "dom2" with Dissolve(0.2)
    pause 0.1
    "dom3" with Dissolve(0.2)
    pause 0.05
    "dom4" with Dissolve(0.2)
    "dom 4 no blur" with vpunch

image licue_blowjob:
    animation
    "licue blowjob" 
    zoom 1.04 
    # ypos 0 
    linear 1.0 yalign 0.5
    # pause 1
    linear 1.0 yalign 0.0
    # linear 0.51 ypos 0 
    repeat

image licue_beam:
    animation 
    "licue beam" with vpunch
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    "licue beam" with vpunch
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.2)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    "licue beam" with vpunch
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.4)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    "licue beam" with vpunch
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.7)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    "licue beam" with vpunch
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.4)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    "licue beam" with vpunch
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.3)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    "licue beam" with vpunch
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.2)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    "licue beam" with vpunch
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.1)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    "licue beam" with vpunch
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    pause 0.3
    repeat
