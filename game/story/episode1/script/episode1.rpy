label ep1:
    
    play sound "audio/Low-hit-thud.mp3" fadeout 4.0    
    
    scene e1 with flash
    pause
    play music "audio/Sleep_Dreamy.mp3" fadein 0.5
    
    pause

    scene black with dissolve
    fbs "Archon HQ{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}NY - Present{/font}{/size}" with dissolve


    #play music "audio/COAG - The Rake.mp3" fadein 0.5
    scene c1s2_ao1f with dissolve     
    pause

    
    play sound "audio/notif.mp3" fadein 0.5
    n " *ring ring* " 
    
    scene c1s2_ao2f with dissolve
    sec "Mr. [mc] is here to see you, sir."
    dad "Send him in."
    sec "Right away, sir."
    n " *Beep* "
    
    # Panel 2:
    scene c1s2_ao4f with fade
    mc "Hey Dad."
    scene c1s2_ao5f with fade
    dad "Welcome back, [mc]."
    dad "How was your flight?"
    mc "It was fine. Slept halfway."

    # Panel 3:
    dad "Good job in LA [mc]."
    dad "Thanks to you, the whole shitshow is behind us and we did some good business as well."
    mc "Thanks, Dad."
    mc "Locke and the rest of the teams did a lot of heavy lifting too."
    dad "Good, good. Always acknowledge the people you work with."
    dad "I keep telling everyone, you'd make a great boss one day."
    mc "..."
    dad "Sit down, we have a lot to catch up on."

    
    scene c1s2_ao6f with fade
    pause
    scene c1s2_ao9f with fade

    # Panel 4:
    dad "So, we’ve started moving some pieces for the upcoming elections… quietly, of course."
    dad "But as you know, we're not the only ones aiming for a win."
    dad "With you stepping in the C-suite back here, we can focus on more important things."

    # Panel 5-6:
    dad "You know, Junior..."
    dad "This wasn’t exactly my first choice for you, I know you like to be out there in the field, but seeing you take this on... it puts my mind at ease."
    dad "God knows, with the way things are going, I need someone in that chair who's ruthless and doesn't take bullshit."
    dad "Specially with that trimming the company lawn thing."
    scene c1s2_ao11f with dissolve
    mc "Oh, I'll see to that personally."
    scene c1s2_ao9f with dissolve
    dad "Good, we are due a cleanup."
    pause
    dad "Speaking of which, have you spoken to your brother yet?"
    dad "I’ve been trying to get a hold of him, but his phone’s been off this whole morning."
    scene c1s2_ao11f with dissolve
    mc "I was with him last night. I think he was going to stay at his girlfriend's place."
    scene c1s2_ao9f with dissolve
    dad "I see."
    "... "
    
    
    menu:
        "Press him about it.":
            
            $ pressed_john = True
            $ psyche -= 1

            mc "Come on, Dad. Finish the thought."
            scene c1s2_ao8f with dissolve
            dad "I just have a feeling your brother might actually settle down with this girlfriend of his."
            mc "{i}Wow. Sharp as ever.{/i}"
            scene c1s2_ao12f with dissolve
            mc "Well… Based on our conversation last night, I'd say you're onto something. Faye and Ryan have known each other since college."
            pause (0.5)
            mc "We've vetted her before."
            mcn "More like flipped through her life."
    
        "Let it go.":

            $ pressed_john = False
            $ psyche += 1
            mc "{i}No point pushing if he doesn’t want to say it.{/i}"
            scene c1s2_ao8f with dissolve
            dad "I just have a feeling your brother might actually settle down with this Faye girl. Seems like a good kid."
            mc "{i}Huh. spot on.{/i}"
            scene c1s2_ao11f with dissolve
            mc "Yeah… from what he told me, it sounds serious. They’ve known each other since college."


    scene c1s2_ao9f with dissolve
    dad "Heh.. Is that so?"

 
    
    scene c1s2_ao9f with dissolve
    dad "Good for him. I'd say it's about time really."
    
    dad "What about you?"
    dad "Is there any lucky lady in the picture?"

    
    scene c1s2_ao12f with dissolve
    mc "No-"
    mcn "Many, but lady luck and I aren't on good terms these days."

    scene c1s2_ao13f with dissolve
    play sound "audio/phone-ringtone.mp3" fadein 0.5
    n " *Ring Ring* "
    
    scene c1s2_ao9f with dissolve
    dad "Is that Ryan?"
    scene c1s2_ao14f with dissolve
    mc "No.. it's Riley."
    scene c1s2_ao9f with dissolve
    dad "Norman’s daughter?"
    scene c1s2_ao14f with dissolve
    mc "Yeah."

    # Reuse Panel 8 or 6 with John:
    scene c1s2_ao9f with dissolve
    dad "Well, it looks like I've held you up long enough."
    dad "I'm sure she would want to talk to you too."
    dad "Go and have fun today."
    dad "But be here early tomorrow."
    
    
    # Panel 10:
    scene c1s2_ao14f with dissolve
    mc "Sure."
    mc "I'll let you know if Ryan calls."
    scene c1s2_ao9f with dissolve
    dad "Good."

    scene c1s2_ao15f with fade

    # Panel 11:
    stop music fadeout 5.0
    mc "Hey Riley."
    mc "Yeah.. I just arrived last night."
    mc "mm-hmm.. Seven o'clock tonight, huh?"
    mc "Sure, I'll be there."
    pause




    scene black with dissolve
    play music "audio/bs-sunlitdepths.mp3" fadein 0.5
    fbs "Some Random Bar{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}Later in the evening{/font}{/size}" with dissolve
    
    scene ch1s3-1 with fade


    pause

    scene ch1s3-2 with dissolve
    uv4 "Hey there, handsome."
    uv4 "I saw you from across the room looking broody and cool, unlike those finance assholes."
    uv4 "Would you like to maybe help me take some pics and vids."
    uv4 "You know... I get content, you get a good time. Win win."

    scene ch1s3-3 with fade
    mc "Thanks for the offer, but I'm waiting for someone."
    uv4 "Come on, I bet whoever's coming over is nothing compared to me."
    mc "Also, you shouldn't sneak up on others like this."
    mc "I could've hit you."
    uv4 "Oooh, you're the kind who likes to play rough, huh? I like that."

    scene ch1s3-4 with fade
    pause
    mc "Again, no offence, you're probably hot and have a following. But I’m here to see a friend."
    uv4 "Tch. Stop playing hard to get. It’s such a turn off."

    scene ch1s3-5 with dissolve
    pause
    mc "Don't you understand the word not interested?"
    uv4 "This is your last chance. If you say no, you're gonna regret this."
  
    scene ch1s3-6 with dissolve
    uv2 "Oh, I'm sure he'll live."
    uv2 "So, why don't you just save yourself time and leave us alone."

    scene ch1s3-5 with dissolve
    mc "Hey, Riley."
    mc "What took you so long?"

    scene ch1s3-7 with dissolve
    rl "Hey, [mc]."
    rl "Got stuck in traffic."

    scene ch1s3-8 with dissolve
    rl "I swear, this traffic is just getting worse and worse by the day."
    mc "It's not that bad. You're probably missing the less busy routes.."
    uv4 "Are you seriously ignoring me right now?!"

    scene ch1s3-9 with dissolve
    rl "Jesus.. just how thick is your skull girl?"
    rl "No one wants you here. Take a hike."
    uv4 "*sniff* Whatever. He isn't that cute anyway."
    mcn "Finally, but this chick sure looked good..."

    show ch1s3-10 at fade_in_new
    pause 
    scene ch1s3-11a with dissolve
    pause
    scene ch1s3-11b with dissolve
    rl "God, what's with that cheeky smile on your face right now?"
    rl "Are you that happy someone hit on you?"

    menu:
        "No":

            $ riley += 1
            $ psyche += 1

            pause (0.5)
            scene ch1s3-11b with dissolve    
            mc "No, I'm just happy to see you."
            pause (0.2)
            rl "Right..."
            

        "Yeap":

            $ psyche -= 1
            pause (0.5)
            scene ch1s3-11b with dissolve
            pause (0.5)
            mc "Who isn't happy to be hit on."
            pause (0.2)
            rl "I knew it. Same old fuckboi energy from college."
            pause (0.2)
            mc "Hey, I'm past that phase now."            
            mcn "For the most part."

    
    scene ch1s3-12 with dissolve
    rl "It's so good to see you again."
    mc "It's good to be back."
    rl "I have so much to tell you."
    mc "So, let's sit down."

    scene ch1s3-nn with dissolve

    mcn "Goddamn, she isn't gonna make tonight easy with this dress."

    menu:
        "Take in the view":

            
            $ psyche -= 1

            pause (0.5)
            scene ch1s3-20 with dissolve    
            mcn "Wow, I don't remember her being in this great of a shape."
            pause (0.2)
            rl "Eye's up here handsome, I know I'm working hard in the gym."
            pause (0.2)
            scene ch1s3-13 with dissolve
            mc "Just admiring God's craft."        
            scene ch1s3-14 with dissolve
            rl "You haven't changed a bit."


        "Let's not ogle":

            $ riley += 1
            $ psyche += 1
            mcn "I know I'm due a release but this is not the time brain."            
            scene ch1s3-13 with dissolve
            scene ch1s3-14 with dissolve
    
    rl "By the way, you were way too soft on her."
    scene ch1s3-13 with dissolve
    mc "She was just an attention hungry girl."
    scene ch1s3-14 with dissolve
    rl "Exactly. Which means she needed it more."
    scene ch1s3-13 with dissolve
    mcn "Honestly, she wanted something else, but her timing was off..."

    scene ch1s3-14 with dissolve
    rl "Next time, someone might not be so nice."
    scene ch1s3-13 with dissolve
    mc "So, naturally, you had to break her ego?"
    scene ch1s3-14 with dissolve
    rl "Please. When I was her age, the idea of looking stupid scared me way more than the idea of getting hurt."
    scene ch1s3-15 with dissolve
    rl "God, did I really just say ‘when I was her age’?"
    mc "Heh. You sure did."
    rl "Please, just order the drinks, [mc]."
    rl "I’m gonna need enough to forget I officially sound like someone’s older sister."

    scene ch1s3-16 with fade
    rl "So... my manager said she'll do everything in her power to support me."
    rl "Now all I have to do is pull together some solid designs and impress."

    
    menu:
        "Can I see the designs?":
            $ designs_riley = True
            

            mc "Mind if I take a look at what you’ve got so far?"

            scene ch1s3-14 with dissolve
            rl "Mm, curious and bold. I like that."

            rl "They're still in their awkward teenage phase, give them a lil more time to glow up."

            scene ch1s3-13 with dissolve
            mc "I’ll pretend I know what that means."

            scene ch1s3-14 with dissolve
            rl "It means, give me a day or two. I’ll show you the good stuff, and you can tell me whether I’m a genius or high on caffiene."
            
            scene ch1s3-13 with dissolve
            mc "Sounds like a date."

            scene ch1s3-16c with dissolve
            rl "Mmhm... *professional consultation*, mister."

        "When’s the deadline?":
        

            mc "Interesting. And when’s the deadline?"

            scene ch1s3-14 with dissolve
            rl "Three days."
            scene ch1s3-13 with dissolve
            mc "..."

            scene ch1s3-16a with dissolve
            rl "Oh, don't give me that look."

            scene ch1s3-13 with dissolve
            mc "What look?"

            scene ch1s3-14 with dissolve
            rl "The 'why do you do this to yourself' look."

            scene ch1s3-13 with dissolve
            mc "Ah. That one."

            scene ch1s3-14 with dissolve
            rl "Yeah, I know it’s almost unreasonable. That’s the fun part."
            rl "But this is not just another project. It’s leverage. When I launch my own design line, every favor I’ve stacked will pay off."

            scene ch1s3-13 with dissolve
            mc "Still the same Riley, huh?"


            scene ch1s3-16b with dissolve
            rl "What, obsessive and slightly unhinged?"

            
            mc "I was going to say {i}dedicated{/i}, but sure, let’s go with that."

            scene ch1s3-16c with dissolve
            rl "You always know how to boost my ego..."

            scene ch1s3-13 with dissolve
            mc "You make it easy."
    

    #Panel 17:
    scene ch1s3-n17 with dissolve
    rl "But enough about me. What about you mystery man?"
    rl "You're back for good."
    rl "Since you were awol, I heard from Joe that you're going to work from the office here now."
    rl "A new role, [mc]."
    rl "Is that true?"


    #Panel 18:
    scene ch1s3-n18idle with dissolve    
    menu:

        "Not Really":

            $ psyche += 1

            mc "It's just a title, Riley. I do what's needed."

            scene ch1s3-n17 with dissolve

            rl "That’s what I like to hear."

            rl "You’re way too sharp to stay in the background."

            scene ch1s3-n18idle with dissolve

            mc "Background's the most strategic position anyway."

            
            scene ch1s3-n19a with dissolve
            rl "Please. You’re just scared of ending up on the gossipy tabloids."

            scene ch1s3-n18idle with dissolve
            mc "Can’t lie there."

            
            scene ch1s3-n19b with dissolve

            rl "Still... kind of hot, being C-suite this early."

           


        "Just cleanup":

            $ psyche -= 1

            mc "Oh, it’s just a cleanup job. Somebody started a sex cult and now HR’s on life support."

            
            scene ch1s3-n20a with dissolve

            rl "Pfft—*what?!*"

            mc "Kidding. Mostly, I'm just asked to root out all the bs and trim the place back into shape."

            rl "Oh, so you're gonna dig into people’s closets and look for skeletons now?"

            scene ch1s3-n20aidle with dissolve

            mc "Easy, detective. keep talking and I’m hiring you as my PA."

            

            scene ch1s3-n20b with dissolve

            rl "Please, you couldn't afford me."

            scene ch1s3-n20aidle with dissolve

            
            mc "I could pay in coffee and bonus for less clothing."

            

            scene ch1s3-n20c with dissolve

            rl "Tempting... very tempting."

            scene ch1s3-n20didle with dissolve


            mc "Especially if you're in charge of the wardrobe. Pretty sure productivity would skyrocket."

            

            scene ch1s3-n20a with dissolve
    

            rl "Careful... I {i}do{/i} have a series that HR would faint over."

            $ riley += 1

            
            
    scene ch1s3-n20didle with dissolve
    pause (0.6)


    scene ch1s3-n22 with dissolve
    rl "Let's do a toast"

    scene ch1s3-n21 with dissolve
    mc "Here's to us."
    rl "And to avoid corny tabloid and sex cults."

    scene ch1s3-n22 with dissolve
    rl "We should take a picture for my socials."

    scene ch1s3-n20didle with dissolve
    mc "Riley-"
    scene ch1s3-n22 with dissolve
    rl "Oh don't worry, I'll crop your face when posting it."

    scene black with fade    
    rl "Come a little closer."
    rl "Perfect."
    rl "Say cheese."
    play sound "audio/camera.mp3"
    scene ch1s3-18 with flash
    pause
    scene black with fade
    rl "Now, let's take one more for my private collection."

    play sound "audio/camera.mp3"
    scene ch1s3-17n with flash

    pause
    #Resume from here:✅  


    #Panel 23:
    scene ch1s3-n20didle with dissolve
    mc ""
    scene ch1s3-n22 with dissolve
    rl ""    

















    stop music fadeout 2.5

    pause


   






















    #scene 4


    
    #Panel 1:
    #(Max is in his room shirtless, lying on his bed, deep in thought)
    play music "audio/Standstill.mp3" fadein 1.5 
    scene black with dissolve
    mcn "If someone asked me when things between me and Sarah got strained, I probably wouldn't have an answer."
    mcn "But at some point in our lives, it did become strained."
    mcn "And it stayed that way ever since."
    mc "*sigh*"
    n "...."
    n "*Ring Ring*"


    #Panel 2:
    #(Max reaches his hand out to pick up the phone nearby)
    
    #Panel 3:
    #(Parking lot off camera)

    scene c1s4_rtm1 with fade

    tn "Think he’ll pick up this late?" 
    rt "Yeah. He’s usually up late."
    tn "Jesus. Rusty, this whole corporate grind’s turning half of us into jittery maniacs who can’t tell a quarterly report from a hit list."
    rt "What, you miss hijacking shipments and greasing unions?"
    tn "Try going home to a wife who treats the AmEx like it’s fucking monopoly money and expects me to smile about it."
    rt "Yeah, and that’s why we cooked up that prenup, loaded to your side. She thinks she’s got you by the balls? Joke’s on her."
    tn "Oh, I totally forgot, you’re a genius. Now I'm gonna make her think I’m halfway out the door and watch her slobber over me like a golden retriever on Viagra."
    rt "Exactly. She’ll do anything. Rimjobs, bdsm, even pretending she’s interested in your little dreams of retirement in Boca."


    #Panel 4:
    #(Max answers the phone)
    
    scene c1s4_rtm2 with dissolve
    pause (0.5)
    n "*Click*"

    scene c1s4_rtm3 with dissolve
    mc "Hello…"
    pause (0.5)
    scene c1s4_rtm4 with dissolve
    rt "Hey [mc]."
    pause (0.5)
    #Panel 5: (Rusty talking)
    
    rt "Just wanted to ask if you’ve heard from Ryan today?"

    #anel 4:
    scene blck with dissolve
    mc "No, I haven’t."
    rt "Okay.."
    mc "Is everything alright?"

    #Panel 5:

    scene c1s4_rtm4 with dissolve
    rt "Yeah, yeah. He probably had something personal to handle last night, so we couldn’t get through."
    rt "It’s probably just his phone acting up. Bad service, whatever."
    rt "Classic Ryan. He’ll check in."
    pause (0.5)
    #Panel 4:
    mc "Right. I'll let you know if he calls me."

    #Panel 5:
    scene c1s4_rtm4 with dissolve
    rt "Alright."
    rt "We’ll probably bump into you tomorrow at the office then."
    rt "Big day, right?"
    mc "Yeah."
    pause (0.5)
    
    #Panel 6:
    scene c1s4_rtm5 with dissolve
    rt "And, uh... [mc]."
    rt "When you come in, have your piece on you and run an SDR."
    rt "You know… like usual."
    pause (0.5)

    scene blck with dissolve
    #Panel 7:
    mc "I always do."
    rt "Good. Have a good night."
    n "*Beep*"

    #Panel:
    scene blck with dissolve
    mcn "..."
    mcn "He says everything’s fine, but his voice is off."
    mcn "And bringing up the SDR? I’m the one who implemented that protocol."
    mcn "Are the others slacking?"
















    play sound "audio/heartbeat-ambience.mp3" fadein 1.5
    scene c1s4_ry1 with clr9
    play music "audio/COAG - Orion.mp3" fadein 1.5
    
    pause
    scene c1s4_ry4 with fade

    ry "hh.. hh.. hh."
    
    scene c1s4_ry2 with dissolve
    uv4 "Come on, man…"
    uv4 "Why do you have ta make this so hard?"
    scene c1s4_ry3 with dissolve
    uv2 "Yeah, just tell us what we want and you get to walk home safe & sound."    
    uv2 "You really don't want us to get serious."
    
    #Panel 11:
    scene c1s4_ry5 with fade
    ry "Heh.. keep dreaming kids."
    ry "I'm not saying anything."
    stop music fadeout 2.5
    uv2 "Well… we tried."
    scene black with vpunch
    play sound "audio/woosh-punch.mp3"
    with flash
    pause
    

    fbs "Archon HQ{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}NY - Present{/font}{/size}" with dissolve
    scene black with dissolve
    scene c1s5_mx1 with fade
    play sound "audio/sfx-avs-screech-BrokenAlarm.mp3" fadein 0.1

    play music "audio/COAG - The Lost.mp3"
    mcn "Two many nervous glances. Are they on edge or am I over analyzing shit again."  
    mcn "Their eyes keep darting to me, like they’re trying to solve a fuckin cold case."
    mcn "Probably don’t like the idea of someone like me stepping in a role that can decide their future here."  
        

    scene c1s5_mx2 with fade
    mcn "Even as Dad introduces me as Chief of Intelligence & Internal Affairs, there's something off."  
    mcn "It’s only been a day since Ryan didn't show up, and they’re already spooked."     

    

    scene c1s9-fg1 with fade 
    play music "audio/COAG - M5.mp3" fadein 0.5
    
    "..."
    "........"
    play sound "audio/ringtone-1.mp3" fadein 0.5
    "*Ring Ring*"
    "...."
    "Let it ring."
    
    # Reuse Panel 2
    scene c1s9-fg2 with dissolve
    "*Phat!!*"
    

    # Panel 4
    scene c1s9-fg3 with dissolve
    uv2 "This better be fucking important!"

    scene c1s9-fg4 with fade
    uv2 "Yes?"
    uv1 "Good Morning, Sir."

    scene c1s9-fg6 with fade
    uv1 "This came in from one of our guys."
    uv1 "Word of Ryan's disappearance seems to be catching on."
    scene c1s9-fg5 with dissolve
    uv2 "Good, good."
    uv2 "I assume no one’s got the balls to say it out loud yet?"
    scene c1s9-fg6 with dissolve
    uv1 "Not yet, they're keepin' it quiet."
    scene c1s9-fg5 with dissolve
    uv2 "Give them another two days, and they'll all be less hush-hush about it."
    scene c1s9-fg6 with dissolve
    uv1 "With respect, boss… but wouldn't he open up by then?"

    # Panels 5 & 6
    scene c1s9-fg5 with dissolve
    uv2 "Don’t be stupid. The guy’s a tank."
    uv2 "Sure, he’ll break, but not today."
    uv2 "In the meantime, we keep up appearances and play dumb."
    uv2 "Did you get any hint on what they're planning to do next?"
    scene c1s9-fg6 with dissolve
    uv1 "No."
    uv1 "They’re playin' it real close to the chest."
    scene c1s9-fg5 with dissolve
    uv2 "Heh.. They can try."

    uv2 "Alright, just call me again once you've heard from her."
    scene c1s9-fg6 with dissolve
    uv1 "Yes, boss."
    "*click*"

    # Panel 7
    scene c1s9-fg7 with dissolve 
    "...."
    uv2 "{i}Fuckin come through this time Dmitry.{/i}"

    # Panel 8
    scene c1s9 - 1 with fade
    e1 "Dylan swears he heard those exact words."
    e2 "No way."
    e1 "Yes, said he even sounded a little scared."
    e2 "Alright, now you're just exaggerating."
    e2 "Seriously? Everyone knows he’s the toughest S.O.B. in this place."
    e2 "What would he be scared of?"
    
    # Panel 9
    scene c1s9 - 2 with dissolve

    e1 "Well, how else would you explain his absence?"

    scene c1s9 - 3 with dissolve

    e2 "Wow. The man skips one day.. and this is what you make of it?"
    e2 "That he's quit the business because someone’s got dirt on him?"
    e2 "I gotta give it to you. You've got a wild imagination."

    # Panel 10
    
    e2 "At least, Ayumi’s version had some semblance of reality to it."
    scene c1s9 - 2 with dissolve

    e1 "Oh really?"
    e1 "What exactly did she say that was so grounded in reality?"
    scene c1s9 - 3 with dissolve
    e2 "Well, you know how he often gets those mysterious calls during the meetings?"
    scene c1s9 - 2 with dissolve
    e1 "Yeah, what about them?"
    scene c1s9 - 3 with dissolve
    e2 "Ayumi mentioned she overheard him talking about birth control pills and all that."
    scene c1s9 - 2 with dissolve
    e1 "Oh stop. You're saying he's gone away for some woman? Hell no."
    scene c1s9 - 3 with dissolve
    e2 "Will you let me finish my story first?"
    scene c1s9 - 2 with dissolve
    
    e1 "Why? Clearly, it's just a bunch of pointless gossip Ayumi picked up from"
    play sound "audio/sfx_door_open.mp3"
    
    pause 0.5
    # Panel 11

    scene c1s9 - 4 with dissolve
    "..."
    "..."
    scene c1s9 - 5
    mc "Oh, sorry. Am I interrupting something?"
    mc "I wasn't getting any signal in my room."
    mc "I'll be out of your hair in a minute or two."
    e1 "Oh.. Erm.. not at all.."
    e2 "We were just.. ermm…"

    # Panel 12
    scene c1s9 - 6
    mc "Hmm…."
    "..."
    "..."
    "..."
    scene c1s9 - 7
    mc "Looks like it's no good here either."
    
    mc "Oh yeah, reviews are underway girls, I hope you're working hard and not slacking off, cos Delilah wont go easy on you..."
    
    mc "And I should call the IT nerds."
    mc "You carry on."
    e1 "Sure, Sir-"
    e2 "Thanks for the heads-up..."

    # Panel 14
    scene c1s9 - 8

    mcn "Interesting..."
    "..."
    "..."
    "..."
    scene c1s9 - 9
    e2 "You think he heard us?"
    e1 "God, I hope not."
    e1 "He didn't seem like he did."
    e1 "I'd say he looked rather cheerful."
    e2 "Yeah, that's not a face you make when your brother is gone missing."
    e1 "I mean, it's just been a day. And it's not like he hasn't taken leaves like this in the past."
    e2 "Maybe we did run away with the whole thing too far."
    e1 "I've had enough coffee for one day."

    # Panel 15
    scene c1s9 - 10
    e2 "Yeah, me too."
    e2 "I've got so much work to finish before the end of the day."
    e1 "Who exactly even started this whole thing about our CEO, anyway?"
    e2 "Beats me."
    e2 "God, Ayumi can be such a gossipy bitch sometimes."
    e2 "She'll do anything but her work."
    e1 "{size=-10}You sure he didn't hear us?"
    e2 "{size=-10}No, or we wouldn't be talking here."

    pause
 
    
    
    #Panel 5
    play music "audio/COAG - The Lost.mp3" fadein 0.5
    scene c1s5_hk3 with fade
    hk "I think you're right."  
    hk "Ryan’s been away on business countless times."  
    hk "No one at Archon finds it odd."  
    hk "Still... we can't afford to slack off."  

    #Panel 6:
    scene c1s5_mx4 with dissolve
    #(Reveal Full shot of the scene, the two are facing each other casually as they speak)
    hk "I sent two of our guys to check his city place, and the usual {i}recreational spots.{/i}"   
    hk "If he's somewhere there safe and sound... then maybe we’re just overthinking this."  
    hk "But..."  
    
    menu:
        "Something's off.":

            $ psyche += 1
            $ search_urg = True
            scene c1s5_mx5 with dissolve
            mc "Hank... we need to widen the search."  
            mc "Start looking around the last place he was seen..."  
            
            #Reuse Panel 5:
            scene c1s5_hk3 with dissolve
            hk "Maybe we should wait until our guy reports back."  
            hk "Ryan wouldn’t just disappear... not without a reason."  

            #Reuse Panel 7:
            scene c1s5_mx5 with dissolve        
            mc "I don't think we can afford to wait, Hank."


        "We're probably over thinking it.":
            $ psyche -= 1
            $ search_urg = False   
            scene c1s5_mx4 with dissolve 
            mcn "But we still need to be cautious..."
            scene c1s5_mx5 with dissolve 
            mc "I think we should still be cautious."
            mc "Can't afford another lapse on our part..."


    #Reuse Panel 5:
    scene c1s5_hk3 with dissolve    
    hk "*sigh*... You’re right."  
    hk "I’ll put the order out. But we keep this tight."  
    hk "Just our guys. No one outside the circle."  
    hk "And about his security detail... they said Ryan dismissed them himself at Afterlife."  
    hk "Didn’t want them following him."  

    scene c1s5_mx5 with dissolve
    play sound "audio/SP 17 Dark Scan.mp3"
    mc "Who saw him last?"  

    scene c1s5_hk3 with dissolve
    hk "His driver. Said Ryan went to meet someone alone. Didn't say where."
    hk "Said it was a very personal matter."
    mcn "Knowing him, {i}'very personal'{/i} could mean anything from an orgy to a quiet dinner."  
    hk "We’re calling him in now... see if he remembers anything else."  
    hk "But... if this goes sideways, we might have to involve the cops."  
    
    #Reuse Panel 7:
    scene c1s5_mx5 with dissolve
    play sound "audio/sfx-avs-DarkHit.mp3"
    mc "Let’s hope it doesn’t come to that."  
    mc "But keep our guys on the force alert... just in case."  

    #Panel 8:
    #(Hank looks at Max proudly, maybe even slightly pat on his shoulder/arm if it works.)
    scene c1s5_hk6 with dissolve
    hk "You’re handling this well, [mc]."  
    hk "Bad timing... but you’re making the right calls."  
    
    scene c1s5_mx5 with dissolve
    play sound "audio/SP 17 Dark Scan.mp3"
    mc "I hope you’re right, Hank."  
    
    scene c1s5_mx7 with dissolve
    hk "I’ll start making the calls now."  
    hk "Keep me posted if you hear anything."  
    mc "Okay."  
    stop music fadeout 2.5
    pause
    scene black with fade
    fbs "{vspace=60}{size=+40}{font=fonts/RetroSignature.otf}Sometime Later{/font}{/size}" with dissolve





    #SCENE 6
    # Panel 1-2: Max in his office room on the phone
    
    scene c1s6 - 1 with clr3
    play music "audio/sfx_dreamy_loop.mp3" fadein 2.0

    mcn "Call after call... they just keep coming."  
    mcn "Well-wishers congratulating me on the new job. My staff needing clearances for monitoring and opening reviews for the downsizing."  

    scene c1s6 - 2 with dissolve
    mcn "Now it's feeling more and more like a monday from all the memes Christy keeps sending me."  
    mcn "But it keeps me busy from being paranoid about Ryan."  
    scene c1s6 - 3 with fade
    
    mcn "Still, I can’t shake this feeling... What if he’s off with some flame for the ‘no strings attached’ special? Old habits sure die hard."  
    mcn "Damn it, Ryan... Where the hell are you?"  
    scene c1s6 - 4 with clr17
    mcn "......"
    

    # Panel 4: Max's mother's hallucination
    scene c1s6 - 5 with dissolve
    ir "Your brother will be alright, honey."
    ir "I'm sure they will call you anytime now and tell you he's okay."
    ir "So, why don't you stop worrying too much and take a little break?"

    # Options
    menu:
        "Not now.":
            $ psyche += 1
            scene c1s6 - 4 with dissolve
            mc "{i}No, I'm not doing this.{/i}"
            mc "{i}Not while I'm at work.{/i}"
            n "..."

            scene c1s6 - 5 with dissolve
            ir "Right, of course sweetheart."
            ir "I'll leave you to your work."

            # Reuse Panel 3
            scene c1s6 - 7 wo ir with dissolve

            mc "*Sigh*"
            n "...."
            play sound "audio/phone-ringtone.mp3"
            n "*Ring Ring*"

            # Panel 5: He attends the phone
            scene c1s6 - 9 wo ir with dissolve

            mc "Hello."

            scene c1s6 - 8 wo ir with dissolve
            hk "[mc]... you were right."  
            hk "Ryan wasn’t at any of the usual spots we suspected." 
            mcn "...I knew it."  
            hk "We’re expanding the search now from the Afterlife last night. I’ll keep you posted."  
            hk "Could be another escort bender, but we'll have to confirm."
            scene c1s6 - 9 wo ir with dissolve
            mc "Any luck tracking his phone?"  
            scene c1s6 - 8 wo ir with dissolve
            hk "We're on it already. I'll keep you posted if we get a lock."
            hk "It's a good thing you decided to start the search early."
     
            scene c1s6 - 9 wo ir with dissolve
            mc "Okay."
            n "*Beep*"

            # Panel 6: Close up of his fist clenching the phone
            scene c1s6 - 10 wo ir with fade
            pause
            stop music fadeout 5.0
            mc "Fuck."

        "You know that's a lie.":
            $ psyche -= 1
            scene c1s6 - 6 with dissolve
            mc "You know that's a lie."

            scene c1s6 - 7 w ir with dissolve
            ir "Maybe so sweetheart."
            ir "But it's okay to hope for good things."
            mc "..."
            play sound "audio/phone-ringtone.mp3"
            n "*Ring Ring*"

            # Panel 8: He attends the phone with his mom still hugging him
            scene c1s6 - 8 w ir with dissolve

            mc "Hello."

            scene c1s6 - 9 w ir with dissolve
            hk "I just got word from our guy, [mc]."
            hk "Ryan wasn’t at any of the spots we expected." 
            hk "We’re expanding the search now from the Afterlife last night. I’ll keep you posted."  
            hk "Could be another escort bender, but we'll have to confirm."

            # Panel 9: Same shot, but she now looks at Max worriedly
            scene c1s6 - 10 w ir with dissolve

            mc "I see. Any luck tracking his phone?"
            hk "We're on it already. I'll keep you posted if we get a lock."
            hk "It's a good thing you decided to start the search early."
            mc "Okay."
            n "*Beep*"

            # Panel 10: Close up of his fist clenching his fist
            scene c1s6 - 11 w ir with fade

            mc "Fuck."

            # Panel 11: His mother's hand gently holding his hand
            scene c1s6 - 12 w ir with dissolve
            stop music fadeout 5.0
            ir "I'm so sorry sweetheart."
            
    


    

    

    play sound "audio/Submarine Hit.mp3" fadein 0.3
    
    #Panel 1:
    #(Iris is on her phone looking at Modelling Websites to apply.)
    
    fbs "Volkov Residence{vspace=20}{size=+20}{font=fonts/RetroSignature.otf}NY{/font}{/size}" with fade
    show blck
    scene c1s7 - 1 with clr2
    play music "audio/refract.mp3"
    #Panel 2:
    uvg "{i}*humming*{/i} You're fireproof. Nothing breaks your heart..."

    scene c1s7 - 2 with dissolve
    uvg "{i}Maddy better be right about this... I can’t stay here forever.{/i}"
    uvg "{i}Work for you Dad? Yeah, right.{/i}"
    uvg "{i}Oh, this is that agency she wouldn’t shut up about.{/i}"
    scene c1s7 - 2a with dissolve
    uvg "{i}Ethereal Studios... yeah, she said they’re killing it, new branch in LA as well.{/i}"

    #Panel 3:
    scene c1s7 - 3 with dissolve     
    uvg "{i}Damn... they already got models doing big gigs.{/i}"
    scene c1s7 - 3b with dissolve  
    uvg "{i}Hmm. All-women leadership. Finally something not run by creepy fucks.{/i}"

    #Panel 4
    scene c1s7 - 4 with dissolve
    uvg "{i}Shit... do I even have a shot?{i}"
    uvg "{i}They’ll probably gloss over someone like me.{i}"

    #Panel 3
    scene c1s7 - 3 with dissolve
    pause 1.0
    uvg "{i}Screw it. Let’s just apply and see.{/i}"


    #Panel 5
    #(Nico watching from a  distance, Iris lost in her phone)

    scene c1s7 - 5
    play sound "audio/sfx_Danger_Hit.mp3" fadeout 0.2   
    uv4 "Fuck,  you should be in your room right now Iris."
    uv4 "Now I'm gonna have to make shit up."

    #Panel 6:
    #(Iris glances up, sees Nico enter and walk past. She watches him, head turning slightly.)
    show c1s7 - 6 with dissolve
    

    pause 1.0

    #Panel 7:
    scene c1s7 - 7 with dissolve
    
    irs "Oh, hey Nico. Back from the dead huh?"
    irs "Where were you last night?"

    #Panel 8:
    scene c1s7 - 8 with dissolve    
    nc "None of your business."


    #Panel 7:
    scene c1s7 - 7 with dissolve    
    irs "Seriously...?"
    irs "Don’t get all edgy and mysterious. Mom was looking for you."

    #Panel 9:
    scene c1s7 - 9 with dissolve    
    nc "I was out."

    #Panel 10:
    scene c1s7 - 10 with dissolve    
    irs "Yeah, no shit. I meant where."
    irs "Or is that classified as well?"


    #Panel 9:
    scene c1s7 - 9 with dissolve    
    nc "..."

    #Panel  10:
    scene c1s7 - 10 with dissolve    
    irs "Nico?"

    #Panel 11:
    scene c1s7 - 11 with dissolve    
    nc "Picked some bitch from the bar and got stoned."
    nc "She wanted a golden shower."
    
    #Panel 12:
    #(Close up of iris Making a face.. still looking in the direction nico went.)
    scene c1s7 - 12 with dissolve
    irs "Eurgh.. gross."
    nc "Want more details?"
    irs "No."
    nc "That's what I thought."
    
    nc "What’d Helena want?"
    scene c1s7 - 13 with dissolve
    irs "No clue..."
    irs "Just asked where you were. I said I don't know, probably high and chasing hoes somewhere."

    #Panel 14:

    scene c1s7 - 14 with dissolve    
    nc "Wait—she went in my room?!"

    #Panel 15:
    
    scene c1s7 - 15 with dissolve
    irs "She probably just went in to clean or grab some laundry, no big deal."

    #Panel 14:
    scene c1s7 - 14 with dissolve    
    nc "Fuck."
    play sound "audio/LDS_Clicker A.mp3"  
    stop music fadeout 0.5
    play music "audio/b-t.mp3" fadein 0.1

    
    #Panel 16:
    scene c1s7 - 16 with dissolve

    irs "Nico...?"
    irs "Is everything messed up again?"
    irs "Nico..."

    irs "....."

    scene c1s7 - 17 with dissolve
    pause (1.0)

    scene c1s7 - 18 with dissolve
    irs "{i}*music playing*{/i} I'm having trouble inside my skin..."







    #stop music fadeout 2.0
    #pause
    #play music "audio/b-t.mp3"
    show egs with flash
    pause
    show egs2
    with dissolve
    pause

return
