label prologue:

    #Tramsition
    define flash = Fade(0.1, 0.0, 0.5, color="#fff")

    image hb4i = im.Scale("images/Prologue/hb4i.png", 1920, 1080)

    ##Default Variable
    
    # Label > Call> Menu > Jump


    # Prologue Start
    
    stop music fadeout 2.0

    scene blck
    with fade
    fb "Welcome{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}{/font}{/size}" with dissolve
    
    fbdisc "The Game is a work of fiction. Names, characters, businesses, places, events, locales, and incidents{vspace=15} are either the product of the author’s imagination or used in a fictitious manner. Any resemblance{vspace=15} to actual persons, living or dead, or actual events is purely coincidental." with dissolve
    
    fbdisc "While the story is fictional, it may derive some elements or details from real-world historical{vspace=15} events. The game contains mature themes and is intended for a mature audience. All{vspace=15} sexual situations portrayed in this game involve consenting adults who are of legal age." with dissolve
    
    fbdisc "{vspace=20} {vspace=20}The Studio is not responsible for any third party add-ons, mods, patches, cheats, etc." with dissolve
    fbdisc "{vspace=20} {vspace=20}A fair warning for people sensitive to sudden flash effects." with dissolve
    fbdisc "{vspace=20} {vspace=20}Keep the sound volume little below music volume." with dissolve
    fbdisc "{vspace=20} {vspace=20}You can use 'H' to hide the textbox." with dissolve
    fbdisc "{vspace=20} {vspace=20}This is our first production. It's always a work in progress." with dissolve
    fbdisc "{vspace=20} {vspace=20}We'll try our best to fix any issue that is reported." with dissolve
    fbdisc "{vspace=20} {vspace=20}Feel free to comment and report any issues about the game on our Discord." with dissolve
    fbdisc "{vspace=20} {vspace=20}Furthermore, the Prologue and Chapter 1 are intended to be introductory in nature." with dissolve
    
   
    scene blck
    with fade
    pause (0.6) 

# Player Name
    fbdisc "{vspace=20} {vspace=25}Enter your name.{i}The original is Max.{/i}" with dissolve
    python:
        
        mcp = renpy.input("{color=#FBFFFF}Enter your name (The original is Max){/color}")
        mcp = mcp.strip()
        if mcp == "":
            mcp = "Max"
            persistent.mc = mcp
        else:
            persistent.mc = mcp

    scene olj
    with fade

    pause (0.6) 

    scene blck
    with fade
    pause (0.6) 

    nvl clear
    fbs "Plaza Hotel{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}Los Angeles - Present Day{/font}{/size}" with dissolve


    scene mxmn1
    show mxmn1 at blurry
    with dissolve
    pause(0.5)
    play sound "audio/vfx_wrong_book.mp3"
    
    show enm
    $ shake()
    
    UV "Please! It's a misunderstanding!! We can talk about this!!"
    UV "I didn't mean to hurt you!"
    UV "Please! Don't hurt me!!"
    
    scene mxmn2
    with flash
    play sound "audio/sfx-avs-boom-Transmission.mp3"
    mcn "*Gasp*"

    pause (1.0)  

    play music "audio/ds_pa.mp3" fadein 2.0

    scene mxmn3
    with dissolve

    mcn "Fuck."
    mcn "Not again."
    pause (0.5)
    mcn "I'm getting sick of these nightmares."

    pause (0.5)
    
    scene mxmn4f
    with fade

    pause (0.6)  

    n "{i}*Ring Ring*{/i}"

    pause (0.6)  

    UV "nnhh.. Hellloo?"

    pause (0.6)  
    
    mc "Rise and shine, lazy lovebird."

    pause (0.6)  

    UV "Eughhh.. it's six in the morning [mc]."
    
    pause (0.6)  
    UV "Anika almost woke up because of you."

    pause (0.6)  

    mc "Heh... not gonna lie, Joe, might've been worth it just to hear her go off."

    pause (0.6)  

    joe "Of course, you'd think that. Wouldn't you?"

    pause (0.6)

    joe "So... what did you call for so early in the morning?"

    pause (0.6)

    mc "I'm coming back."
    
    
    pause (0.5)
    
    joe "Really?"
    joe "Ha-haaa... That's fucking great."

    pause (0.5)


    joe "When exactly though?"
    
    pause (0.6)
    mc "Today."

    pause (0.6)  

    mc "Don't tell anyone about it. Not yet, at least."
    mc "Not everyone knows I'm coming back."
 
    pause (0.5)
    
    joe "Sure."
    pause (0.5)
    joe "It'll just be you, me, and your brother then."  
    pause (0.2)
    joe "Just like old times."

    pause (0.6)  

    mc "Fuck me. I'm gonna wake up drunk in some woman's home again, huh?"

    pause (0.6)  

    joe "Hahahaha.... Come on, don't tell me you didn't have a good time that night."

    pause (0.6)  

    mc "Well, it was pretty good..."

    pause (0.6)  

    joe "There you go. You're welcome, by the way."

    pause (0.6)  

    mc "But really, I mean it. No booze or hookers this time."

    pause (0.6)  

    joe "Alright, alright, I know we're responisble adults now."

    pause (0.6)  

    joe "It'll just be the three of us."


    pause (0.6)  

    joe "Text me when you'll land and I'll come pick you up."
    
    pause (0.5)

    mc "Sure."
    
    pause (0.6)

    mc "And say hi to Anika for me."

    pause (0.6)  

    joe "Will do."


    #pause (0.5)
    play sound "audio/cinematic-swoosh-heartbeat.mp3"
    
    
    
    scene mxmn5ghf with flash
    
     

    UVr "{i}One last job [mc]."
    #play sound "audio/sfx-avs-boom-Transmission.mp3"
    pause (0.5) 

    scene mxmn5f
    with flash
    
    #play sound "audio/sfx-avs-whoosh-hit-Calypso.mp3"
    
    mc "*hh.. hh..*"
    pause (0.2)
    mcn "Fuck!"
    #pause (0.1)
    #mc "{i}Not again...{/i}"
    label plg_max_john_flasback_label:
    stop music fadeout 1.0


    play sound "audio/sfx-avs-boom-ShadowCloak.mp3" fadein 0.2    
    
    scene black with flash
    scene 6me with fade
    pause (0.5)
    scene black with dissolve
    pause (1.0)
    fbs "Some Armani Property{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}Somewhere in NY{/font}{/size}" with dissolve

    stop music fadeout 1.0
    play sound "audio/sfx_Timestamp.mp3"
    scene mxjf9 with fade
    play music "audio/ThatMindset.mp3"
    pause





    scene mxjf11 with dissolve
    myr "John... I’m doing what I can. My hands are tied."

    scene mxjf10 with dissolve

    jn "Tied? Or willingly playing the victim? Will’s been gone a year. Crime's back up. None of that helps you or us."

    jn "The city’s starting to bleed. And if voters see you as complacent… well, they might start listening to the other guy."

    scene mxjf11 with dissolve
    
    myr "You’re saying my re-election depends on you."

    scene mxjf10 with dissolve

    jn "I’m saying it depends on choosing the right allies. People who're willing to crusade against street crime but know when to cooperate with those keeping the city alive.."

    scene mxjf11 with dissolve
    
    myr "...And what do you need?"

    scene mxjf10 with dissolve

    jn "Co-operation, access, information."
    
    jn "A task force that actually wants to clean up the city and find Will while they’re at it."

    jn "Do that and I’ll make sure the unions and the Italian-American vote stay yours."































    pause (0.5)
    play music "audio/dh2_mmp.mp3" fadein 1.0


    scene mxjf1b with clr2
    pause (3.0)

    scene mxjf2f with dissolve

    mc "Hey Dad..."

    pause (0.6) 

    dad "Hey champ, glad you made it on time."

    pause (0.6) 

    dad "Take a seat."

    
    scene mxjf4 with dissolve

    pause (0.6) 

    dad "I've been thinking about your proposol from the other day."
    pause (0.4)
    dad "To double down south in Florida and other cities instead of Europe."

    pause (0.6) 

    mc "Okay..?"

    pause (0.6) 

    dad "I can't make any promises, so don't get your hopes up too high."
    pause (0.4)
    dad "But..."
    pause (0.4)
    dad "I do think you're on to something."
    dad "At least it's solid enough to sit down and have a talk."

    pause (0.6) 

    mc "Works for me."
    pause (0.5) 

    scene mxjf3i with dissolve
    scene mxjf3ii with dissolve

    dad "And no matter what we decide, I still want you to lead the whole thing."

    pause (0.5) 

    dad "The elections are coming soon, and no matter who wins, we need to make sure we're good."
    
    pause (0.5) 
    dad "But before we deal with that..."
    dad "I have one last job for you."

    
    scene ircl
    with flash
    pause (0.3)
    play sound "audio/sfx-avs-boom-ShadowCloak.mp3" fadein 0.1
    UV "One last job. now that's very amusing."
    

    pause (0.5)

    scene mxjf5 with dissolve

    mc "What is it?"


    scene mxjf3i with dissolve
    scene mxjf3ii with dissolve

    dad "*Sighs* It's a loose end."

    pause (0.5)

    dad "One of Ryan’s ex-girlfriends might’ve overheard him talking to the Salerno’s and possibly recorded the whole thing."

    pause (0.5)
    
    dad "Skipped town the same night."

    scene mxjf5 with dissolve

    mc "Shit."
    mcn "Leave it to Ryan to pick the premium crazies."

    pause (0.5)
    mc "Which ex are we talking about here?"
    mc "Cos he keeps swapping them out..."

    scene mxjf4 with dissolve

    dad "Someone named Amber."
    pause (0.2)

    mcn "Why am I surprised."
    mcn "How many times, I told Ryan this thing isn't gonna work out."

    pause (0.5) 

    dad "What do you think we should do?"

    pause (0.5) 

    mcn "I can think of a few convenient ways of my own to solve the problem."
    mcn "But only Dad can make the final call."

    pause (0.5) 
    
    menu:
        "Use the cops to track her phone":

            $ psyche -= 1

            mc "Have we talked with anyone on the force? Maybe pull some strings to get into her phone?"

            pause (0.6) 
    
            dad "We tried that."

            dad "No luck."


        "No clean way really.":

            $ psyche += 1

            mc "I can't really think of a non intruding way..."
            pause (0.5)
            
            dad "I've come to the same conclusion.."

            pause (0.5) 

            mcn "Dammit. She's not making this easy for herself."
    
    
    pause (0.5) 

    dad "She's gone completely off the grid."
    dad "Both her phone and laptop are turned off."
    dad "She hasn't used her socials or any cards since she vanished."
    

    

    pause (0.5)
    
    mc "The fact that she's gone out of her way to disappear only makes it look like she sure heard something."
    mc "Or... maybe someone's helping her stay off the radar."
    mc "Neither of them give her a great look."

    pause (0.5) 

    dad "Exactly."

    pause (0.5) 

    dad "Considering {color=#23C1FF}Will's{/color} disappearance, we just have to be extra careful with these kind of jobs."

    pause (0.5) 

    dad "We got a tip from the LAPD. We haven’t vetted it yet, but they say she’s in LA."

    pause (0.5)

    dad "Take {color=#23C1FF}Locke{/color} with you, set up shop there. I don't care how long it takes, get it done."

    pause (0.5)

    dad "Make sure she didn’t talk to anyone and take care of anything that could link us to her."

    pause (0.5)

    dad "Archon's name is on the line and I don't want some stupid broad bringing harm to the business image."

    pause (0.5)

    mc "I get it..."
    mc "But if you're putting Locke on the job, why do you even need me?"
    mc "He's more than capable of-"

    scene mxjf3i with dissolve
    scene mxjf3ii with dissolve

    pause (0.5)
    dad "I just..."
    pause (0.5)
    dad "I don’t want another situation like Will..."
    pause (1.0)
    dad "I let him go off alone for whatever personal reason he had, now he’s vanished off the face of the earth." 
    
    scene mxjf5
    with dissolve

    pause (0.5)  

    mcn "That makes the two of us. But is this another one of your tests, dad?"
    mcn "To see if I can still be on top of my game."

    scene mxjf3i with dissolve
    scene mxjf3ii with dissolve

    pause 0.5
    dad "I know you don’t like getting your hands dirty these days."
    dad "But I need you on this one." 

    pause (0.5) 

    scene mxjf5 with dissolve
    
    mc "{i}*Sighs*{/i} Alright, Dad."
    pause (0.5)
    
    
    scene mxjf3i with dissolve
    scene mxjf3ii with dissolve

    dad "Good, and I want you to know... you’ve done a damn good job holding things together after Will’s disappearance."
    dad "You were there for the business, and for the family when we needed you the most."
    dad "I really appreciate that."

    scene mxjf5 with dissolve
    
    mc "Anything for you and Uncle Will. Any developments on his case?" 

    pause (0.2)

    scene mxjf3i with dissolve
    scene mxjf3ii with dissolve

    dad "I wish I had anything new to say."

    pause (0.3)
    scene mxjf5 with dissolve

    mcn "*Sighs* Fuckin cops..."

    pause (0.2)
    
    mc "And put me anywhere that doesn't require me to go away for months."

    pause (0.5)
    
    mc "I'll be fine."

    pause (0.5)

    scene mxjf3i with dissolve
    scene mxjf3ii with dissolve

    dad "I'll talk with Ryan about it."

    pause (0.5)

    dad "He'll get you sorted when you come back."

    pause (0.5)

    dad "Alright, you better go see Locke and get ready for the trip."
    
    scene mxjf5 with dissolve
    mc "Okay."
    scene mxjf3i with dissolve
    scene mxjf3ii with dissolve
    dad "Goodluck, and [mc]."
    pause (0.3)
    dad "As much as I don't like to stay out of contact for long, both of you will be off the grid during the job there. Keep that in mind."

    


    stop music fadeout 3.0

    scene prs with flash
    play audio "audio/cinematic_airy_drone_decaying.mp3" fadein 0.1
    pause
    stop music fadeout 5.0
  

    show mxmn11 with fade

    pause (1.0)

    mcn "Six months flew by like nothing."

    pause (0.5)
    play music "audio/Standstill.mp3" fadein 1.0

    mcn "Cleaning up the Amber mess, handling Archon's work... just another Tuesday. I could do this in my sleep, like everything's on autopilot."
    pause (0.5)
    mcn "The thing that's breakin' my balls is Will. All this... all these resources, and poof. He's a ghost."
    pause (0.5)
    mcn "But who else? If anyone could just drop off the face of the earth, it's him."
    mcn "The Grim Reaper. Christ. What a moniker. And I'm supposed to be next in line." 
    pause (0.5)
    mcn "He was the family's main enforcer for a decade. The guy who handled things. Right up until Grandpa made Dad the {b}Boss{/b} and Will the {b}Underboss{/b}.."
    pause (0.5)
    mcn "Will knows every trick in the playbook. He taught me most of it. Hell, probably all of it."
    pause (0.5)
    mcn "But the thing is, Will has {color=#FF0EF3}Anne{/color}. A wife. Someone he wouldn’t just walk away from. Not without a damn good reason."
    pause (0.5)
    mcn "I wasted so much time here digging with Locke, going through everything, and couldn't find shit..."
    pause (0.5)
    mcn "But the whole thing feels wrong. Like a setup for a joke I'm not in on."

    
    pause (1.0)

    scene mxmn8 with clr2

    pause (0.6)

    #bathroom irene appears
    play sound "audio/sfx-avs-boom-ShadowCloak.mp3" fadein 0.1

    UV "What's the matter, honey?" 


    play music "audio/ds_pa.mp3" fadein 1.0

    pause (0.6)

    scene mxmn7 with dissolve

    mcn "Mom."

    pause (0.6)

    mcn "I know it's only my mind playing tricks on me."

    pause (0.6)

    scene mxmn9 with dissolve

    ir "Oh honey, who's to say I'm not real?"

    pause (0.6)

    mcn "I'm gonna open my eyes slowly."
    mcn "And you will be gone."

    pause (0.6)

    ir "It's ok, I'm not here to cause you any trouble..."
    
    pause (0.6)

    ir "God knows, you've been through enough already."

    pause (0.6)

    ir "Just go home honey. You're wasting time looking for Will here."
    
    pause (0.6)

    play sound "audio/vfx_exhale-whoosh.mp3" fadein 0.5

    ir "They need you back there."

    scene mxmn10 with dissolve

    pause (0.6)

    mcn "They need me, huh?"

    pause (1.0)

    scene mxmn12 with fade
    
    pause (0.5)

    mcn "Well, I better get going. Seen enough of this city's 'self-made' success stories, where capitalism meets insanity and the business plan involves a ring light and your dignity on sale..."

    pause (0.6)

    mcn "Let's leave a message first."

    pause (0.6)

    n "{i}Everything's taken care of...{/i}"

    stop music fadeout 2.0

    scene black with fade        

    pause (0.6)

    fbs "East Coast{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}Somewhere close to NY{/font}{/size}" with dissolve


    play music "audio/sfx_left_alone.mp3" fadein 2.5
    scene pl1
    with fade
    pause

    scene mxpl1
    with clr2
    pause (0.5)
    mcn "*Sigh*"

    scene mxpl2

    mcn "Every time I try to start a new chapter, there’s always some fuckin’ problem to drag me right back into my old habits."
    pause (0.6)
    mcn "But this time… with Amber, I hope I did the right thing."
    pause (0.6)
    mcn "Past me? He would’ve made very diffrent choices."
    pause (0.6)
    mcn "But I'm trying to find a balance now."

    stop music fadeout 1.0

    label plg_amber_LA_flasback_label:

    pause (0.6)
    play sound "audio/sfx-avs-whoosh-hit-Calypso.mp3"
    scene black with flash
    fbs "4 Months Ago{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}Some basement in LA{/font}{/size}" with dissolve
    pause (1.0)
    play music "audio/vfx_evil-storm-atmosphere.mp3" fadein 2.0

    

    scene mal1bw
    with flash
    pause (0.6)

    play sound "audio/vfx_heartbeatc1.mp3"
    

    mcn "Tracking Amber down wasn’t easy."  
    mcn "She covered her tracks well. But not well enough."  

    scene mal1 with dissolve  
    pause (1.0)  

    scene mal3 with dissolve  
    pause (1.0)  

    scene mal5 with dissolve  

    mcn "This has become more of a fuckin drill."  
    mcn "Locke doesn’t speak much, he doesn’t have to. He’s the kind who can intimidate a wall just by staring at it."  

    pause (0.4)  

    scene mal16 with dissolve  
    mcn "Now, what to do with her..."  
    mcn "If they had sent Rusty or Nate, she would already be six feet under."  
    pause (0.5)  
    mcn "But I want to do this differently."  
    pause (0.5)  

    scene mal7 with fade  
    amb "{size=-10}mm{size=+5}h.."

    scene mal8 with fade  
    amb "{size=-5}What's.. {size=+5}what's going on?"  
    scene mal9 with dissolve  
    amb "[mc]?"  
    amb "Oh God.. [mc]... What is this?"  
    amb "Why the hell am I tied up?"  

    scene mal12 with dissolve  
    scene mal11 with dissolve  
    lk "You got something that belongs to us, kid."  
    lk "Tell us where it is, and we all walk out of here."  

    scene mal13 with dissolve  
    scene mal15 with dissolve  
    amb "I don’t know... I don’t know what you’re talking about."  
    amb "Please let me go!"  
    amb "I... I won’t tell anyone. I swear."  

    mcn "She’s afraid. Real fear. But fear doesn’t mean truth."  

    scene mal2 with dissolve  
    pause 0.1  
    scene mal10 with dissolve  
    mc "Come on, Amber."  
    mc "Don’t make this harder than it needs to be."  
    mc "We know about the video you recorded before skipping town."  

    scene mal13 with dissolve  
    scene mal14 with dissolve  
    amb "I don’t... have any video."  

    scene mal2 with dissolve  
    mcn "She’s lying. No doubt."  
    scene mal13 with dissolve  
    mcn "All she needs is a little push."  

    scene mal10 with dissolve
    mc "Amber, you don't seem to understand the seriousness of the situation here."
    mc "I'm trying to make sure you walk out of this place alive after all this is over."
    mc "But I need you to be honest with me."
    
    scene mal14 with dissolve 
    amb "Please, I'm begging you…"
    amb "I don't have the video anymore."

    scene mal12 with dissolve
    scene mal11 with dissolve
    lk "You think we believe that crap?"
    lk "Start talking. NOW!"

    scene mal13 with dissolve 
    scene mal15 with dissolve 
    amb "[mc]... please... I'm telling the truth."
    amb "I deleted that damned video."
    pause (0.5)
    amb "I only took it to make sure your brother wouldn’t try something... whatever thing we had was just temporary."
    pause (0.5)
    amb "And I wanted out the minute I heard your brother talking to someone on his phone."
    pause (0.5)
    amb "I didn’t want to carry that around."
    pause (0.5)
    amb "Please... believe me."
    pause (0.5)
    amb "I promise I’m no longer a threat to you."

    pause

    menu:
        "Maybe she's telling the truth.":

            $ amber = False

            $ psyche += 1

            pause (0.5)

            scene mal10 with dissolve

            mc "Alright, just this once… I'm willing to hear you out."

            pause (0.5)

            mc "I’ll take you home and we're gonna make sure there's no funny surprises."

            pause (0.5)

            mc "If you’re really clean, we’ll forget this happened, and you can move on."

            pause (0.5)

            mc "But if you're lying, even just a little…"

            scene mal13 with dissolve 
            scene mal14 with dissolve

            amb "I disappear for good?"

            scene mal2 with dissolve
            scene mal10 with dissolve

            mc "Bingo..."

        "They never do.":

            $ amber = True

            pause (0.5)

            $ psyche -= 1

            scene mal10 with dissolve 

            mc "So this is how you wanna play it?"

            pause (0.5)

            mc "Fine."

            pause (0.5)

            mc "Let's take a walk to your house and see if you’re really telling the truth."

            pause (0.5)

            mc "And if there’s any funny business..."

            pause (0.5)

            play sound "audio/sfx-avs-boom-ShadowCloak.mp3"

            mc "They'll find no trace of your brother Travis, not even a single hair."
            scene mal13 with dissolve 
            scene mal14 with dissolve

            amb "Please no, I will do what you want [mc]. Please don't hurt my brother!"

            scene mal13 with dissolve 
            scene mal2 with dissolve

            scene mal10 with dissolve

            mc "Oh, don't beg now."
            mc "We're just getting started."

    
    scene prs with fade   
    stop music fadeout 4.0
    
    pause (0.6)
    play sound "audio/sfx_Danger_Hit.mp3"
    play music "audio/COAG - Orion.mp3" fadein 6.0

    label plg_max_plane_and_joe_label:

    
    scene mxpl2

    with vpunch
    pause (0.5)
    
    scene mxpl3
    with dissolve
    
    mcn "Fuck..."
    
    pause (0.5)

    cap "Hey [mc] wake up..."
    cap "We're gonna be landing soon."

    mcn "Home at last..."

    pause (0.5)

    scene mxtm2
    with clr2

    joe "There he is, man of the hour."

    scene mxtm1 with dissolve

    mcn "So great to see you brother, let's get out here."
    
    scene mjt1
    with dissolve

    mc "I look at that city, and it’s just one giant freak show. Every sidewalk is a damn photo shoot for some girl who thinks selling her privacy is 'empowerment.'"
    mc "They even asked me to join in."

    joe "Yeah, well, that's L.A. But the real kick in the teeth? They’re running a cleaner operation than half the guys here."

    mc "Too bad you're in a relationship."

    joe "Fuck you, Anika's good."

    mc "Hahaha."
    pause (0.2)
    mc "Well the bright side of spending 6 months in that hellscape is that our investment portfolio now covers all links in the backbone of the whole online industry. Everything that feeds that culture."

    mc "And the talent is also neccessary. That's why we opened the LA branch of Ethereal Studios."
    
    mc "It's a respectable agency that offers the girls a clean route to fame in that market, while benefitting us and also build a whole network there."

    joe "I heard. Smart. Why take the risk on the talent when you can own the infrastructure?"

    mc "It’s just business, Joe. It’s simply about controlling the supply chain."
    
    mc "Also I talked with our guys at JP, And now you and I have enough revenue streams to fund any spontanoues adventures, art projects or retire early."
    
    joe "All thanks to you and your family."

    mc "Couldn't have done without you brother. Thanks for sticking with me."

    joe "Always [mc]."
    scene mjt2
    with dissolve

    joe "Congrats on that Amber job, by the way."
    pause (0.2)
    joe "Heard you and Locke pulled it off without a hitch."
    pause (0.2)
    mc "Yeah, no hole in the woods this time."
    pause (0.2)
    joe "Always better that way."
    pause (0.2)
    mc "So.. do we still have eyes on her?"
    pause (0.2)
    joe "Yeah, but we should be calling it off soon."
    

    pause (0.5)

    if amber == True:

        joe "She's shaken for good..."
        pause (0.5)
        joe "I doubt she'll try to do something like that ever again."
        mc "Let's hope so."

    else:
        joe "She seems clean so far."
        joe "Looks like she wasn't really cutout for the big leagues."
        mc "Hope LA goes easy on her."


    scene mjt4
    with dissolve
    
    joe "By the way, I heard {color=#E4345A}Rose{/color} isn't quite happy about you suddenly going off the radar like that."

    pause (0.5)

    scene mjt3
    with dissolve

    mcn "Rose..."

    pause (0.5)
    
    scene mjt4
    with dissolve

    joe "Maybe you should try talking to her soon."

    play sound "audio/sfx_Dark_Texture.mp3" fadein 0.1
    joe "You know how she can be when it comes to you."



    
    scene black with flash
    
    fbs "{vspace=60}{size=+40}{font=fonts/RetroSignature.otf}12 Years Ago{/font}{/size}" with dissolve
    play music "audio/COAG - Who Will Save My Soul.mp3" fadein 1.0


    scene c1fb_mr1 with dissolve
    pause
    scene c1fb_mr2 with dissolve
    pause

    scene c1fb_mr3 with dissolve
    pause (0.2)

    scene c1fb_mr4 with dissolve
    
    rs "You know, I haven’t celebrated my birthday properly in quite a while."


    scene c1fb_mr5 with dissolve
    mc "Yeah. Ever since your dad—"

    scene c1fb_mr4 with dissolve
    rs "…and Aunt Irene."
    rs "Losing her took the joy out of a lot of things."

    scene c1fb_mr5 with dissolve
    mc "Yeah…"
    mc "I’ve gotten better at living with it."
    mc "Most days, anyway."

    scene c1fb_mr4 with dissolve
    rs "People always think they’re helping with all the cake, balloons, and surprises."

    scene c1fb_mr5 with dissolve
    mc "I didn’t bring cake."

    scene c1fb_mr6 with dissolve
    pause(0.3)
    scene c1fb_mr7 with dissolve
    rs "Just trespassing and a stolen yacht?"

    scene c1fb_mr8 with dissolve
    mc "Technically borrowed."

    scene c1fb_mr9 with dissolve
    rs "From who?"

    scene c1fb_mr10 with dissolve
    mc "…That’s classified."

    scene c1fb_mr9 with dissolve
    rs "It’s peaceful out here. Like everything just… slows down."

    scene c1fb_mr8 with dissolve
    mc "That was the idea."

    scene c1fb_mr9 with dissolve
    rs "You always know what’s going on in my head. That’s why I hate you sometimes."

    scene c1fb_mr10 with dissolve
    mc "That makes two of us."

    scene c1fb_mr9 with dissolve
    rs "Don’t joke."

    scene c1fb_mr8 with dissolve
    mc "Still not really a birthday, though."

    scene c1fb_mr7 with dissolve
    rs "No. It’s just what I needed."

    scene c1fb_mr9 with dissolve
    rs "If anyone else brought me out here, I would’ve shoved them overboard."

    scene c1fb_mr8 with dissolve
    mc "Good thing it’s me, then."

    scene c1fb_mr9 with dissolve
    rs "Yeah. Good thing…"

    scene c1fb_mr11 with dissolve
    pause (0.3)
    rs "You ever think how easy it’d be… for someone to disappear out here?"
    scene c1fb_mr7 with dissolve
    mc "…"
    
    rs "Relax."

    scene c1fb_mr12 with dissolve
    stop music fadeout 2.0
    rs "I would never do that to you-"

    play sound "audio/sfx_Timestamp.mp3"
    scene mjt2 with flash
    joe "[mc]..."
    
    scene mjt3
    with dissolve
    pause (0.5)
    menu:
        "Sure":

            pause (0.5)

            mcn "I have to smooth things with her."
            pause (0.2)
            mc "Sure, I'll pay her a visit..."


        "Maybe":

            pause (0.5)

            mc "We'll see."

    pause (0.5)
    
    

    scene mjt5
    with dissolve

    joe "Don't wait too long, man."
    joe "You’re gonna be busy as hell that first week, fixing up Hank’s weird little sex cult."
    mc "Haha, yeah, no kidding."
        
    
    
  
    joe "Oh, it almost slipped my mind... [mc], before you landed, {color=#23C1FF}Rusty{/color} gave me a call..."
    joe "The Rossis sent word for a sit-down later tonight."
    joe "And {color=#23C1FF}Frank's{/color} got me and Rusty on the ticket to be there."
    joe "So our plans to celebrate your return have to wait a little longer."

    pause (0.5)

    mc "{i}That's a lil odd, but Frank’s the {b}Consigliere{/b}. He knows what's up.{/i}"

    pause (0.5)

    joe "So, I'll just drop you off at Afterlife."

    pause (0.5)

    mc "Actually, why don't you just drop me at my place?"
    mc "I gotta freshen up and get changed first."
    mc "I'll head to Afterlife myself."

    pause (0.5)

    joe "You sure?"
    mc "Yeah."

    pause (0.5)
    
    joe "Well, okay then."
    joe "Sorry about the change of plans though.."

    stop music fadeout 2.5

    joe "Things really aren't going our way tonight."
    
    ############
    label plg_afterlife_ryan_label:

    scene black with fade
    fbs "Afterlife{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}Armanni Owned Club{/font}{/size}" with dissolve
    
    scene mrc1f with clr16
    pause (0.5)
    play music "audio/tk-ynts.mp3" fadein 0.5

    tv "Local investment group Archon is rumored to be eyeing two massive takeovers."
    pause (0.5)
    
    tv "However, Archon’s CEO, Ryan Armani, son of private investor {b}John Armani{/b}, chose not to comment on the matter."
    pause (0.5)

    scene mrc2 with dissolve
    
    pause (0.5)

    tv "Next up, a surge of a new designer drug called Angel X is said to be connected to the recent string of violent crimes occurring in the city."
    tv "Authorities are scrambling to solve the mystery behind this new wave of drug-induced mayhem."
    tv "The city had a relatively low homcide rate ever since The Grim Reaper's reign of terror stopped half a decade ago."
    pause (0.5)

    mcn "Little do these idiots know that The Grim Reaper is an idea not a single person." 
    mcn "And these Feds better get their shit together..."


    pause (0.5)

    ry "You're just gonna stand there watching the news all night?"

    #pause (0.5)

    

    scene mrc3 with dissolve
    
    ry "Come here..."

    pause (0.5)

    mc "Missed you brother."

    pause (0.5)

    ry "Me too, Junior..."

    pause (0.5)

    ry "Sit down, I'll turn this fucking news off."

    pause (0.5)

    scene mrc4 with dissolve
    
    ry "These media morons are starting to be a real headache."

    pause (0.5)

    scene mrc4i with dissolve

    mc "Free publicity eh?"

    scene mrc7i with dissolve
    scene mrc7 with dissolve
    
    pause (0.5)

    ry "The kind of publicity we don't need right now."

    pause (0.5)

    scene mrc4i with dissolve

    mc "Speaking of things we don't need right now."
    mc "We can't afford this much big name expansion with Archon. Investments are all fine by me, but active management and adding more employees."
    pause (0.5)

    mc "That's living dangerously. We have to keep the ship tight and lean."
    pause (0.5)
    
    scene mrc7i with dissolve
    scene mrc7 with dissolve
    

    ry "I know, I told Dad and Frank the same thing."
    pause (0.5)

    ry "We're all on the same page here. Hank and Delilah are already on it."

    ry "Once we have a sitrep, we will start mowing the company lawn."
    
    pause (0.5)

    scene mrc4 with dissolve

    ry "So, how was your trip?"

    pause (0.5)
  
    scene mrc6i with dissolve   
    scene mrc6 with dissolve

    mc "Just the usual.."
    mc "Deadlines, site tours, sit-downs..."

    pause (0.5)

    mc "And a high dose of jetlag..."

    scene mrc4 with dissolve

    ry "I hear you."
    ry "You should probably switch jobs..."
    ry "Something that's {i}juicier.{/i}"

    pause (0.5)

    scene mrc6i with dissolve   
    scene mrc5 with dissolve

    mc "No, thank you. I'd like to keep what's left of my sanity..."

    pause (0.5)

    
    scene mrc7i with dissolve
    scene mrc7 with dissolve


    ry "Still don't want the hot seat, huh?"
    
    pause (0.5)

    scene mrc5 with dissolve

    mc "Nah, too much spotlight..."

    
    scene mrc7i with dissolve
    scene mrc7 with dissolve

    
    ry "Mark my words, one day, that executive chair's gonna have your name on it..."
    
    ry "And when it does, let me tell ya, it's a heavy throne to sit in."

    pause (0.5)

    scene mrc4i with dissolve

    mc "We'll see when that time comes."

    pause (0.5)

    mc "But if it ever came to that... we both know, I will run things a lot better than you."
    
    pause (0.5)

    
    scene mrc7i with dissolve
    scene mrc7 with dissolve


    ry "Oh, look who's talkin' big now."

    pause (0.5)
        
    scene mrc7i with dissolve
    scene mrc7 with dissolve

    pause (0.5)

    ry "And hey.... thanks for takin' care of that whole Amber mess."

    pause (0.5)
    
    ry "I had no clue she was gonna go batshit crazy like that."

    pause (0.5)

    mc "Well, you gotta be more careful about these broads man."

    pause (0.5)

    mc "You're the CEO and the fuckin' {b}Acting Underboss{/b}."

    pause (0.5)
    
    scene mrc7i with dissolve
    scene mrc7 with dissolve

    ry "I know, I know."
    ry "My days of casual flings are ancient history now."

    pause (0.5)

    ry "I've been doin' some serious thinking, especially after this whole Amber shitshow."

    pause (0.5)

    mc "About what?"

    pause (0.5)

            
    scene mrc7i with dissolve
    scene mrc7 with dissolve


    ry "Maybe it's time to settle down, live that suburbanite life..."
            
    pause (0.5)
    scene mrc4 with dissolve

    ry "The whole nine yards."

    pause (0.5)

    scene mrc6i with dissolve   
    
    mc "{i}Hallelujah!{/i}"

    pause (0.5)
    scene mrc6ii with dissolve
    scene mrc6i with dissolve

    scene mrc6 with dissolve

    mc "So, someone finally changed your mind, huh?."
    mc "Who is she?"

    pause (0.5)

    scene mrc4 with dissolve

    ry "I started seeying Faye after you left."
    
    pause (0.5)

    ry "You remember her?"

    pause (0.5)

    mcn "The hot ginger? Who in their right mind wouldn't remember her?"

    pause (0.5)

    scene mrc4i with dissolve

    mc "Yeah, I remember."
    mc "She didn't like us all that much back in college, did she?"

    pause (0.5)

    
    scene mrc7i with dissolve
    scene mrc7 with dissolve


    ry "Hey, the way we were back then.. can you really blame her?"
    pause (0.5)
    mcn "Nah, I don't blame her. Poor girl saw so much fuckery."

    pause (0.5)

    
    menu:
        "Ask about Faye":
            
            $ psyche -= 1    
            scene mrc5 with dissolve
            mc "So, how long you been seein' her?"

            pause (0.5)

            
            scene mrc7i with dissolve
            scene mrc7 with dissolve


            ry "Five months, maybe more..."

            pause (0.5)

            ry "Time flies when you're with someone special."

            pause (0.5)

            scene mrc6i with dissolve
            scene mrc5 with dissolve

            mc "Seems like you were busy falling in love while I was cleanin' up your mess."

            pause (0.5)

            scene mrc4 with dissolve

            ry "Aw, come on, don't go holding that over me now..."

            pause (0.5)

            scene mrc4 with dissolve
            scene mrc6i with dissolve
            scene mrc5 with dissolve

            mc "I'm just messing with you..."

            pause (0.5)

        "Don't":
            $ psyche += 1 
            mcn "Faye's a good person, no need to pry. I've looked into her enough."

    scene mrc4 with dissolve

    ry "I'm just.... trying to do things right [mc]."
    ry "I've had my fun."
    ry "It's time for me to get serious about my life."

    pause (0.5)

    scene mrc4i with dissolve

    mc "I'm truly happy for you brother."

    scene mrc4 with dissolve

    n "*Ring Ring*"

    pause (0.5)

    scene mrc9 with dissolve

    ry "Hey baby..."

    ry "I was just chattin' with Junior about you."

    pause (0.5)

    ry "Yeah, he just got back from his business trip..."

    pause (0.5)

    ry "He's... "
    extend "doin' well."

    pause (0.5)

    ry "An hour or two. No promises."

    pause (0.5)

    ry "Yeah, love you..."

    pause (0.5)
    menu:
        "Poke fun":
            
            scene mrc6i with dissolve
            scene mrc5 with dissolve

            mc "Should I go ahead and hand over the penthouse for your new start?"

            pause (0.5)

            scene mrc4 with dissolve

            ry "You just can't quit bein' a wiseass, can you?"

            scene mrc5 with dissolve
            mc "Nah."

        "Nah":

            scene mrc6i with dissolve
            pause 
            mcn "Let's not piss him off, he's in a good mood."

    scene mrc7i with dissolve
    scene mrc7 with dissolve
    
    pause (0.5)

    ry "Alright, I gotta run. Got somethin' I need to handle before I head home."

    pause (0.5)

    ry "Oh, and a little heads-up, {color=#EF0888}Christy's{/color} still not thrilled about you missin' her birthday."

    pause (0.5)

    scene mrc6 with dissolve

    mc "I missed it because of the shitshow."
    pause (0.5)
    mcn "And finding Uncle Will."
    pause (0.5)
    mcn "And doing a cameo in some random bitch's first on screen fuck."


    scene mrc4 with dissolve

    ry "I know, and I already gave her a gift from you as well."

    pause (0.5)

    scene mrc6 with dissolve
    mc "Thank fuck."
    
    scene mrc7i with dissolve
    scene mrc7 with dissolve


    ry "Just have a chat with her, she'll come around."

    pause (0.5)

    ry "She can't stay mad at you forever."
    
    pause (0.5)

    ry "Alright, I'll see you later."

    pause (0.5)

    scene mrc5 with dissolve

    mc "Stay safe out there."

    pause (0.5)

    scene mrc4 with dissolve
    
    stop music fadeout 3.0

    ry "I will..."
    
    pause (0.5)

    label plg_max_graveyard_label:
    
    scene black with fade
    fbs "Armani Family Graveyard{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}Somewhere in NY{/font}{/size}" with dissolve

    play music "audio/dh2_mmp.mp3" fadein 1.0

    scene mgy1 with clr2

    mcn "Six months gone off the grid, and one of the few who’d call me out on it is six feet under."

    scene mgy2 with clr2

    pause (0.5)
    
    mcn "Hey Mom..."

    pause (0.6)

    mcn "Wish I could’ve come sooner. Life has this way of piling on, doesn’t it? The job... it never stops."

    pause (0.5)
    mcn "But I’m here now."

    pause (0.6)

    mcn "Talking to your grave like this..."
    
    mcn "like you’re actually listening."
    
    mcn "It’s crazy. But then again, so is everything else in my life."
    
    pause (0.6)

    mcn "And those visions I see of you. I don't know what to make of them, maybe it is you."

    pause (0.6)    

    mc "Or maybe it's just some fucked up part of my brain that takes your form."

    pause (0.6)    

    scene mgy3 with dissolve

    mcn "Truth be told, I think I'm starting to lose it with the whole Uncle Will thing."

    pause (0.6)

    mcn "*Sigh* I should accept he's gone and move the fuck on."
 
    pause (0.6)

    mcn "I hope it’s peaceful for you, wherever you are."
    
    mcn "I'm sorry I didn't see the signs."

    pause (0.6)

    mcn "Catch you later."

    pause (0.6)
    stop music fadeout 4.0

    
    label plg_fd_conspiracy_label:

    scene fmt2 with flash
    play sound "audio/sfx-avs-boom-Titan.mp3"

    play music "audio/sop- counting the cost.mp3" fadein 10.0
    

    uv1 "Hello..."

    pause (0.6)

    scene fmt1 with dissolve


    #play sound "audio/sfx-avs-boom-ShadowCloak.mp3" fadein 0.1
    uv2 "It's done."
    uv2 "The Rossis got the Armanis busy with a sitdown."
    uv2 "The others are either busy or underground."
    pause (0.6)

    uv2 "You already know where Ryan is heading..."

    pause (0.6)

    scene fmt3 with dissolve

    pause (0.6)
    
    uv1 "This is the first and last time I'm grabbing someone this high profile for you."
    
    scene fmt3 with dissolve

    uv1 "If things go south."

    pause (0.6)

    scene fmt1 with dissolve

    uv2 "They won't."

    pause (0.6)

    scene fmt1 with dissolve

    uv2 "Make sure he spills whatever he knows."
    uv2 "Names, locations, offshore accounts, anything that's worth knowing."
    
    uv2 "But if he wounds up dead or a vegetable, forget we ever had a deal."

    pause (0.6)

    uv2 "We can't go to war with the Armanis and Costellos at once."

    pause (0.6)

    uv1 "Well, start preparing for one then."
    pause (0.2)

    uv1 "There's a saying..."
    pause (0.5)

    uv1 "When you go down the path of revenge, you dig two graves."

    n "*Beep*"

    

    scene fmt2 with dissolve
    uv1 "One last job for this sly fuck shouldn't matter."

    uv1 "We do this and step away from this minefield."

    uv1 "Vlad, call it in."
    stop music fadeout 3.0

    label plg_john_norman_call_label:

    scene black with fade
    fbs "{vspace=60}{size=+40}{font=fonts/RetroSignature.otf}Somewhere in Miami{/font}{/size}" with dissolve


    scene jnj1 with clr3

    play music "audio/cold_suspense.mp3" fadein 2.0 

    play sound "audio/notif.mp3" fadein 2.0
    n "{i}Ring...{/i}"

    pause (0.5) 

    scene jnj2 with Dissolve(1.0)

    jn "Hello..."

    pause (0.5)

    scene nm1 with dissolve

    UV "Hello, John"

    pause (0.5)
    
    UV "Been a little while since we last spoke."    

    pause (0.5)
    
    scene jnj4 with Dissolve(1.0)

    jn "Norman..."

    pause (0.5)

    jn "It has indeed been a while..."

    pause (0.5)

    scene jnj3 with dissolve

    nm "Things aren't looking good for this thing of yours."

    pause (0.5)

    scene jnj4 with dissolve

    jn "Tell me something I don't know..."

    pause (0.5)

    scene nm1 with dissolve

    play sound "audio/sfx-avs-boom-ShadowCloak.mp3" fadein 0.2

    nm "Word is, someone’s planning something. Multiple parties."
    
    pause (0.5)

    nm "We’re working our sources, but it’s still murky."

    pause (0.5)

    scene jnj4 with dissolve

    jn "Multiple hands?"

    pause (0.5)

    scene jnj3 with dissolve
    
    nm "I wish I had more clear answers, John."

    pause (0.5)

    scene jnj4 with dissolve

    jn "Then get them fast Norman."

    pause (0.5)

    scene nm1 with dissolve

    nm "I’m not as fast as I used to be."

    pause (0.5)

    jn "You’re still faster than most."

    pause (0.5)

    nm "My job was to give you a heads-up."

    pause (0.5)

    jn "I appreciate that."

    pause (0.5)

    jn "And this won't be the first attempt."

    pause (0.5)

    nm "There've been another?"

    pause (0.5)

    jn "It’s possible. Someone tried to get Ryan’s ex to record him."

    pause (0.5)

    nm "Well, that's one explanation of why she skipped town... LA’s got its own set of problems."

    pause (0.5)

    
    nm "Watch your back, John. I’ve got a feeling something’s coming down the pipeline."
    

    scene jnj4 with dissolve

    jn "I'm having that same feeling now..."

    pause (0.5)

    jn "We will take care of it, we always do..."

    pause (0.5)

    scene jnj3 with dissolve

    nm "Will you?"

    pause (0.5)

    nm "You’ve been busy with that all corporate stuff."

    pause (0.5)

    nm "Complacency can cost a lot."

    pause (0.5)

    scene jnj4 with dissolve

    jn "I know, Norman. I’m fixing it."

    pause (0.5)

    jn "It’s not the same as the old days. Running a legit business is completely different than running the family."
    
    pause (0.6)

    jn "Times change."

    pause (0.5)

    scene nm1 with dissolve

    nm "And so have you..."

    pause (0.5)

    nm "From your father’s kid to Mr. Bigshot Investor."

    pause (0.5)

    jn "Ease up on the news, Norman. It's a one-way ticket to madness."

    pause (0.5)

    nm "{i}*Chuckles*{/i}"

    pause (0.5)

    nm "You've come a long way, Johnny."

    pause (0.5)

    jn "You too Norman..."
    
    pause (0.5)

    jn "Still the best detective in the city."

    pause (0.5)
    
    nm "Stop it, John. I’m not buying the flattery."

    pause (0.5)

    nm "We’re still on opposite sides."

    pause (0.5)        

    scene jnj4 with dissolve

    jn "Has that ever stopped our friendship?"

    pause (0.5)

    scene jnj3 with dissolve

    nm "No."

    pause (0.5)

    scene jnj4 with dissolve

    jn "So why the concern?"

    pause (0.5)

    scene nm1 with dissolve

    nm "You've climbed quite high on the ladder."

    pause (0.6)
    
    nm "I've got no appetite for the limelight."

    pause (0.5)

    jn "You've avoided it well."

    pause (0.5)

    jn "Can’t say the same for me."

    pause (0.5)

    nm "You've done alright."

    pause (0.5)

    scene jnj4 with dissolve

    jn "Thanks for the tip, Norman. Appreciate it."

    pause (0.5)

    scene jnj3 with dissolve

    nm "I still owe you and [mcp]. Big time..."

    pause (0.5)

    scene jnj4 with dissolve

    jn "Don't mention it."

    pause (0.5)

    jn "How's Riley?"

    pause (0.5)

    scene nm1 with dissolve

    nm "She's doing well. Landed a job at some fashion designer place."

    pause (0.5)

    jn "Good for her, she's a bright girl."
    
    pause (0.5)

    nm "She is..."

    pause (0.5)

    scene jnj4 with dissolve

    jn "If you need anything, you know where to find me."

    pause (0.5)

    scene jnj3 with dissolve

    nm "Still the generous one."

    pause (0.5)

    scene nm1 with dissolve

    jn "We take care of our own."

    pause (0.5)

    nm "Hard to believe you’re the big boss now."

    pause (0.5)

    scene jnj4 with dissolve

    jn "When they don't know you, they put labels on you Norman."

    pause (0.5)

    scene jnj3 with dissolve

    nm "Alright, I have to go."

    pause (0.5)

    nm "Something tells me we’ll meet again."

    pause (0.5)

    scene jnj4 with dissolve

    jn "I’ll make sure you’re taken care of."

    pause (0.5)

    scene jnj3 with dissolve

    nm "Good luck John."

    pause 

    scene jnj4i with dissolve
    pause

    scene nm2 with fade
    pause (0.5)
    nm "{i}*Sighs*{/i}"
    nm "Guess it's time to stock up on body bags and buy a few cops dinner."

    pause 

    scene jnj4i with fade
    pause
    scene jnj4ib with dissolve
    play sound "audio/sfx-avs-boom-ShadowCloak.mp3" fadein 0.2

    jn "God, I’m getting too old for this shit."
    stop music fadeout 2.0
    
    label plg_helena_label:
    
    scene h1 with clr2
    play music "audio/sfx_outro.mp3" fadein 1.0
    uv1 "Don't go here, don't go there."
    uv1 "You need to stay home tonight."

    scene h2 with Dissolve(1.0)
    uv1 "{i}Just what are you up to, Dmitry?{/i}"
    uv1 "{i}And why isn't it safe for me out there tonight?{/i}"

    scene h3 with fade
    uv1 "{i}Hmm... this month's ledger.{/i}"
    scene h4 with dissolve
    scene h6 with dissolve 
    play sound "audio/cinematic_airy_drone_decaying.mp3"
    uv1 "{i}{b}25 million.{/b}{/i}"
    uv1 "{i}That's a lot more money than last month.{/i}"
    pause (0.2)
    uv1 "{i}What new deal are you getting into now Dmitry?{/i}"
    pause (0.2)
    scene h5 with Dissolve(1.5)
    pause (0.2)
    uv1 "{i}*sigh*{/i}"
    uv1 "{i}I have enough on my plate with Iris and Nico, and now this...{/i}"
    pause (0.4)
    uv1 "{i}I need to clear my head.{/i}"

    scene h7 with clr2
    "..."

    scene h8 with clr18
    hel "{i}Ahh..{/i}"
    pause (1.0)
    
    scene h9 with dissolve
    "..."

    scene h8 with dissolve
    hel "{i}I have to get my act together.{/i}"
    hel "{i}I'm tired of dressing up, faking smiles, and playing the hostess for all your people Dmitry.{/i}"
    pause (1.0)

    scene h9 with dissolve
    hel "{i}And I feel like I'm failing Iris too.{/i}"
    hel "{i}God. Please watch over her...{/i}"
    pause (0.5)

    scene h8 with dissolve
    
    pause(0.5)
    play sound "audio/sfx-avs-boom-Transmission.mp3"
    hel "{i}I need to find an exit...{/i}"

    pause (0.5)

    label plg_hank_jane_label:


    play music "audio/ds_pa.mp3" fadein 4.0

    scene hkt8 with clr2
    pause 0.2
    scene hkt1 with clr2
    pause 0.2
    ja "Hank..."
 
    pause 0.4
    ja "Hank..."
    hk "Yes..?"

    scene hkt9 with dissolve
    pause(0.3)
    ja "Ya seem so distracted tonight?"

    scene hkt3 with dissolve
    pause 0.1
    scene hkt4 with dissolve
    pause 0.5
    scene hkt5 with dissolve
    hk "I'm sorry, doll."
    hk "Things have been a little tense lately."
    hk "And it's fucking with my sleep."

    scene hkt9 with dissolve

    ja "Care to share?"

    scene hkt5 with dissolve

    hk "The competition's getting more and more vicious."
    pause (0.5)
    play sound "audio/sfx-avs-boom-ShadowCloak.mp3"
    hk "Feels like everyone will be at each other's throat sooner or later."
    hk "And as the chief security guy for Archon, I gotta work twice as hard."
    
    scene hkt4 with dissolve

    ja "Why not just leave?"
    ja "Ya know? Start afresh."

    scene hkt5 with dissolve

    hk "It doesn't work like that."
    hk "At least, you don't get to walk away like that easily."

    hk "By the way, I got somethin' lined up for you."

    scene hkt4 with dissolve

    ja "A job?"

    scene hkt5 with dissolve

    hk "Yeah, it's gonna give you a nice little bonus."

    scene hkt4 with dissolve

    ja "What's the gig, Hank?"

    scene hkt5 with dissolve

    hk "Junior scoped some spots in Florida."

    hk "The offer's already made, but I want you to close the deal personally."
    
    hk "I want eveything bulletproof, no loopholes, sneaky clauses or leaks."


    scene hkt10 with dissolve

    ja "Gotcha."
    ja "I'll use all my charms to seal the deal."

    scene hkt5 with dissolve

    hk "And Jane, do me a favor, will ya?"
    
    hk "Stick around for a while down there."

    hk "Things are heating up here, and I don't want anything happening to you."

    scene hkt10 with dissolve

    ja "Always lookin' out for me, Hank..."

    scene hkt5 with dissolve

    hk "Alright, now scram."
    hk "I've got an important call to make."
    hk "Your flight's tomorrow afternoon. Make sure everything goes off without a hitch."

    scene hkt10 with dissolve

    ja "You got it, chief."

    pause (0.3)

 
    play sound "audio/sfx-avs-boom-ShadowCloak.mp3" fadein 0.1
    scene mhm1
    with clr16
    
    pause (0.5)

    label plg_max_monologue_label:

    play music "audio/mp_pain.mp3" fadein 4.0


    pause (0.5)

    scene mhm1f
    with dissolve
    pause (0.5)
    scene mhm2f
    with dissolve
    pause (0.5)
    scene mhm3
    with dissolve
    pause (0.5)
    scene mhm4
    with dissolve
    pause (1.0)
    mcn "The whiskey slides down easy, but it's a comfort, really. An old friend I can count on when nothing else sticks."
    pause (0.5)
    mcn "HAL keeps telling me about everything, missed calls, missed messages..."
    mcn "Missed moments I should’ve cared about more."


    
    

    pause (0.5)


    show rp5 at truecenter:
        xpos 1500 ypos 485
    with dissolve
    pause
    
    scene mhm4
    with dissolve
    pause (0.5)
    mcn "I have to see her soon. And take it from there, wherever it goes."

    pause

    

    show sp1 at truecenter:
        xpos 1500 ypos 485
    with fade
    with dissolve

    pause 

    mcn "Sarah..."

    mcn "You always see it. Doesn’t matter how I hide it."

    mcn "I could say it’s ‘cause of Dad. Being the supportive partner."

    mcn "But that’s not it."

    pause (0.5)

    mcn "You want me to call."

    mcn "Because you care. Because you never stopped."

    mcn "Even after everything."

    mcn "I'm trying to kill the noise but it's not goin away."

    mcn "And I’m running out of excuses."

    hide sp1

    show lp1 at truecenter:
        xpos 1500 ypos 485
    with fade
    with dissolve
    pause

    
    mcn "Ah. So she hasn’t killed me yet. That’s a relief."
    pause (0.5)
    mcn "I was expecting something more explicit. The kind of message that requires plausible deniability if my phone ever gets searched."
    pause (0.5)
    mcn "But no. Instead, I get a eulogy. Tasteful, tragic, just scandalous enough. Which means she’s amused for now."
    pause (0.5)
    mcn "The real danger starts when she gets bored and becomes a hungry monster."
    pause (0.5)

    menu:

        "A little fun would be nice.":

            $ psyche += 1

            play sound "audio/phone/send_msg.mp3"    
            show lp2 at truecenter:
                xpos 1500 ypos 485
            with dissolve

            pause (0.5)
            mcn "Could really use some fuckin fun after so much work."

            hide lp2

        "I’ll meat you soon.":

            play sound "audio/phone/send_msg.mp3"    
            show lp3 at truecenter:
                xpos 1500 ypos 485
            with dissolve

            $ psyche -= 1

            pause (0.5)
            mcn "A terrible pun. I know..."

            hide lp3                

    hide lp1    


    mcn "Now, let’s see how long that buys me...."

    
    
    pause (0.5)
    play sound "audio/notif.mp3" fadein 0.1

    
    hal "Sir."
    hal "Incoming call from Mr. Hank..."
    pause (0.5)
    mcn "Of course. The universe’s idea of a joke."
    mcn "Hank always calls at the worst time."
    mcn "Like he’s got a radar for when I’m staring into the bottom of a whiskey glass."
    mcn "Or thinking about doing something {i}fun{/i}..."
    pause (0.5)
    scene mhm5
    with dissolve

    mc "Put it through..."
    "*Beep*"


    pause (0.5)

    mc "Hey old man."

    pause (0.5)

    scene hkt6 with dissolve

    hk "How's my boy?"

    scene mhm5 with dissolve

    mc "Seen better days, but I'm fine."

    pause (1.0)

    scene hkt6 with dissolve

    hk "Nothing a bottle of good booze or a great blowjob can’t fix, right?"
    pause (0.5)

    scene mhm5 with dissolve

    mc "Have a glass with me right now."
    pause (0.5)
    
    scene hkt6 with dissolve

    hk "Good man..."
    pause (0.5)


    hk "And fat Sully told me you're coming over to our department."

    pause (0.5)

    scene mhm5
    with dissolve

    mc "Yeah, he said Hank has gone half retard and needs a bailout."

    pause (0.5)

    scene hkt7
    with dissolve

    hk "Hahaha. I'm sure he did."

    pause (0.5)
    
    scene hkt6
    with dissolve

    hk "Welcome to the madhouse, pal. Hope you like digging through other people's work and personal lives.."

    pause (0.5)

    scene mhm5
    with dissolve

    mc "Thank you Hank. It was my favorite past time you know.."

    pause (0.5)

    scene hkt7
    with dissolve

    hk "Haha, I remember that, you and Joe, all gung-ho about that."
    hk "Well, enjoy your time off Junior. You've earned it."
    hk "I'm hearing you got us some big hands off revenue streams for the next 5-10 years."
    pause (0.5) 

    scene mhm5
    with dissolve

    mc "Our teams already did all the hard work Hank, I just helped in the execution."

    pause (0.5)

    scene hkt6
    with dissolve

    hk "Still great job Junior. Also, about the places you wanted to buy down in Florida..."

    hk "I've sent Jane down there to close."

    pause (0.5)

    scene mhm5
    with dissolve

    mc "Thanks Hank, I appreciate it."
    mc "The city is looking shaky, it's better to have relocation plans."
    pause (0.5)

    scene hkt6
    with dissolve

    hk "It's no big deal. But let's hope things don't go that far."

    pause (0.5)

    scene mhm5
    with dissolve

    mc "Have a good night Hank."

    pause (0.5)

    scene mhm4
    with dissolve

    hk "You too Junior." 
    pause (0.5)

    n "*Beep*"
    pause (1.0)
    

    ##########################

    play sound "audio/sfx-avs-boom-ShadowCloak.mp3" fadein 0.1

    scene mxirhm1
    with dissolve
    #window hide
    ir "You really think {i}that{/i} bottle’s gonna drown all your pain?"
    
    scene mxirhm2
    with dissolve
    pause 0.1
    scene mxirhm3
    with dissolve
    
    
    
    mc "No... but it sure takes the edge off."
    
    pause (0.5)

    scene mxirhm2
    with dissolve

    ir "Come here, [mcp]. Rest your head for a while."
    pause (0.5)

    mc "....."
    pause (0.5)
    
    mcn "*Sigh*"
    mcn "Here goes nothing. Not like I’ll remember any of this by morning."
    pause (0.5)

    scene mxirhm7
    with Dissolve(1.0)

    pause 0.1

    scene mxirhm5
    with dissolve
    

    ir "You know I’ll always be here for you, right?"
    pause (0.5)

    scene mxirhm6
    with dissolve

    mc "Yeah. Dead people tend to stick around. Unfinished business and all that."
    
    scene mxirhm5
    with dissolve

    pause (0.5)

    ir "{i}*Scoffs*{/i} When did you get so cynical?"
    pause (0.5)

    scene mxirhm6
    with dissolve

    mc "Read some of Hunter S. Thompson's stuff on the flight back here."
    pause (0.5)

    scene mxirhm5
    with dissolve

    ir "If only you could channel all that brooding into something useful."
    ir "Like taking care of yourself for once."
    pause (0.2)
    
    ir "Or being around people who actually give a damn about you..."
    
    scene mxirhm4
    with dissolve
    pause (0.7)

    ir "{i}And he dozes off...{/i}"

    stop music fadeout 6.0

    
    
    #####################################
    
    
    play music "audio/vw.mp3" fadein 3.0

    scene rk1
    with dissolve

 
    pause 0.5
    ry "Let's get movin' Ryan..."

    scene rk1f
    with dissolve

    pause 0.3
    ry "Shouldn't have left my security detail back at the club..."
    ry "But they can't know about this."
    pause 0.3
    ry "Last job... I owed it to Taylor. Her mom needs that money."
    
    scene rk2 with Dissolve(1.0)
    pause 0.3
    ry "Faye wouldn't be happy if she found out... But she'd understand why I did it. It was the right thing to do..."

    pause (1.0)
    
    play sound "audio/cinematic-swoosh-heartbeat.mp3"
    scene rk3
    with flash
    
    pause (0.5)

    uv4 "DON'T MOVE!"
    play sound "audio/vfx_heartbeatc1.mp3" fadein 1.0
    pause (0.5)

    ry "What the fuck?"

    pause (0.5)

    uv4 "GET YOUR FUCKING HANDS UP!"
    pause (0.5)

    

    pause (0.5)

    ry "You got the wrong guy."
    ry "{i}My fuckin gun is in the car too...{/i}"

    scene rk4
    with flash
    
    pause (0.5)

    ry "Argh..."


    scene rk5f
    with fade
    
    ry "You fuckers! Whatever you're gonna do to me, I'm gonna pay you back a hundred times more!"

    pause (0.5)

    ry "You all just signed your fucking death warrants!"

    play sound "audio/sfx-avs-boom-ShadowCloak.mp3"
    scene rk5n1
    with flash
    window hide
    pause
    
    scene rk5n2
    with dissolve
    window hide
    pause

    scene rk6
    with clr2
    
    
    uv4 "He's a tough mortherfucker alright..."
    pause (0.5)
    uv4 "People just drop when they get hit with this."
    pause (0.5)
    
    scene rk7
    with dissolve
    scene rk8
    with dissolve
    uv2 "We'll see how tough he is, let's get him out of here..."
    pause (0.5)
    uv2 "We don't have all night..."
    scene rk7
    with dissolve
    uv4 "What about his car and stuff?"
    scene rk8
    with dissolve
    uv2 "Put all his stuff in the car..."    
    pause (0.5)
    uv2 "And use your gloves."
    scene rk7
    with dissolve
    uv4 "The Boss said don't rough him up too much, he's very high profile..."
    pause (0.5)
    scene rk8
    with dissolve
    uv2 "He wanted me to be in this... Then, I'll do it my way..."
    uv2 "If anybody has a problem, you can wait here and have a nice chat with the people that will come looking for sleeping beauty here."
    scene rk7
    
    window hide
    stop music fadeout 2.0
    pause
    show black with fade
    jump ep1

return
    
    