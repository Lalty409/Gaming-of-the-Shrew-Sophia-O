# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Toby", color = "#ff8000")
define l = Character("Lucien", color = "#9e69f3")
define b  = Character("Brianna", color = "#00ff00")
define p = Character("Petur", color = "#0000ff")
define k = Character("Katherine", color = "#ff0000")
define g = Character("Grumie", color = "#663300")
define ba = Character("Sp. General Baptista", color = "#b3b3b3")
define te = Character("Tenny", color = "#ff33ff")
define n = Character(None, what_italic=True, what_color = "#f5c907")

define flashbulb = Fade(0.2, 0.0, 0.8, color="#fff")
define fadehold = Fade(0.5, 1.0, 0.5)

transform flip:
    xzoom -1.0

transform very_left: 
    xalign 0.0
    yalign 1.0

transform very_right: 
    xalign 1.0
    yalign 1.0 

transform pretty_left: 
    xalign 0.10
    yalign 1.0

transform pretty_right: 
    xalign 0.90
    yalign 1.0 

transform right:
    xalign 0.80
    yalign 1.0

transform left: 
    xalign 0.20
    yalign 1.0

transform bapnerf: 
    xalign 0.6
    yalign 1.0
    zoom 1.2

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg street
    with fade

    n "- Enter Lucien, standing next to his vendor cart with his buddy and assistant, Toby - "

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show luc sigh at right
    with moveinright
    # These display lines of dialogue.

    l " I feel ridiculous Toby. This costume is too tight, my hat is itchy, and I look… I look like a—"

    show toby happy at flip, left
    with moveinleft
    t "A great salesman, Luci! Dare I say the greatest salesman to ever walk these streets!" 
    t "Padua won’t know what hit them, and we’ll be out of here with a mountain of gold in no time at all!"

    show luc point 

    l "Thank you Toby, your opinion is always a pleasure!"
    
    show luc alas

    l "But alas, I believe we’ll need more than my handsome looks if we’re really going to sell this whole stock!"

    show toby point

    t "Sure is rough of your father to send you to the most war-torn country in the East." 
    t "I know he wants you to prove yourself as worthy to inherit the whole trading company, but still, Padua!?"

    show luc point
    
    l "Don’t go jinxing us now, Tobs, we’ve yet to meet any… violent criminals the rumors have foretold." 
    l "With any luck they’ll just stay out of our way until we’re back in Pisa safe and—"

    n "- Two scary-looking women are loudly fighting while walking down the market street -"

    show toby cry  

    t "Ah, speaking of!"
    t "Hide!"

    hide toby cry 
    with moveoutleft
    hide luc point
    with moveoutleft

    n "- Lucien and Toby hide behind their vending cart - " 

    show kat scold at left
    with moveinright 

    k "Look, all I’m saying is if you want to ditch your country so bad like the rest of these AWOLs, go ahead and do it already!"

    show bri angry at right, flip  
    with moveinright
 
    b "What I’m saying is that I’d like to keep my people and my social life intact, thank you!"
    b "I don’t even like ordering these idiots around anyway!"
 
    show kat potsword at flip 
    k "You have a duty to uphold Brianna! If you don’t like it you should have been born into a different family!"
    k "I’m already sticking my neck out running your stupid errands with you! So just be quiet so we can get back to camp before someone important sees us."

    b "But Katherine please! This senseless war has been going on for far too long and I just wish you’d see that-"
    
    k "See what? How much of a- "

    n " - Enter the incredibly tall Supreme General Baptista, He looks annoyed..."

    hide bri angry
    hide kat potsword

    show bap at bapnerf

    ba "{size=*2.5} Girls! {/size}"

    hide bap 

    show bri uncomfy at center
    show kat shock at pretty_left, flip

    b "Uh oh..."

    scene bg street 
    show bap at bapnerf
   
    ba "What are you two doing this far from your stations!? Without guards?!" 
    ba "You don’t know who could be out here! What’s the meaning of this!?"

    hide bap 

    show bri uncomfy at right
    show kat potsword at pretty_left, flip

    k "Brianna wanted to buy wine!"

    show bri angry at right, flip 
    b "Snitch!"

    scene bg street 
    show bap at bapnerf

    ba "But Briannnaaaaaaaaaa, don’t you have wine at the camp?" 
    ba "I could have sworn I double triple checked that it was fully stocked!"

    hide bap 

    show bri shrug at right
    show kat angsword at pretty_left, flip

    b "I can’t drink that wine, Dad. All the guys keep drinking out of it straight from the bottle. It's disgusting."
    show bri angry at right
    b "I’m tired of drinking spit-washed white wine - I don't even really like white wine!"

    scene bg street

    show bap at bapnerf
    ba "But I buy it straight from Antonio, only the best prosecco to make my best little general happy!"

    hide bap 

    show bri uncomfy at right
    show kat angsword at pretty_left, flip

    b "You know what would really make me happy, Dad?"
 
    scene bg street

    show bap at bapnerf

    ba "Yes, Briaaannaaaaaaaaaaaaaaaaaaa?"
 
    hide bap

    show bri angry at right
    show kat shock at pretty_left, flip



    b "If you invested a little bit of that wine money into a peace treaty with Verona!"

    scene bg street

    show bap at bapnerf

    ba "Ahahaha! You’re hilarious Brianna! Only the best jokes from the best daughter of the best supreme general."

    hide bap

    show bri shrug at right
    show kat angsword at pretty_left, flip

    b "But, I’m serious!"

    scene bg street

    show bap at bapnerf
    ba " Oh.. really?"
    ba "For the last time Brianna, this country is simply too deep into this war to back out now. What are we? Quitters?"

    hide bap 

    show bri sad at right
    show kat angsword at pretty_left, flip

    b "I’ve been leading this army since I was 13, Dad. I’m not sure how much longer I can do this for."
    b "If you won’t stop the war can you at least pick out a different general?"

    scene bg street

    show bap at bapnerf

    ba "Absolutely not! This family runs on war, and seeing as I have two perfectly heritable daughters you two must do the same."

    hide bap

    show bri sad at right
    show kat angsword at pretty_left, flip

    b "But Da-"

    scene bg street

    show bap at bapnerf

    ba "No buts! These are your men and you will serve them until you become the best general just like your glorious father!"

    hide bap 

    show bri sad at right
    show kat shock at pretty_left, flip

    b "..."
    k "..."

    scene bg street

    show bap at bapnerf

    ba "Ahem... Now that is final."

    hide bap

    show bri sad at right
    show kat potsword at pretty_left, flip

    k "Just suck it up, you wimp."
    k "The better you are at your job the faster we’re out of this war, so quit complaining and get your head in the game."

    show bri angry at right, flip 

    b "You don’t understand Katherine!"
    b "I’m on my 3rd assassination attempt this week, I hate these stupid ugly war clothes, I hate all these man children I have to babysit all day! I hate everything!"
    b "Why couldn’t I have just gotten a normal job!? I want to get married! And work on a farm or something! Anything but this!"

    k "That sounds miserable."

    b "You sound miserable!"
  
    scene bg street

    show bap at bapnerf

    ba "Enough!"
    ba "You know what, fine. Brianna, you can quit your job..."
    ba "..."
    ba "When Katherine does!"

    hide bap
  
    show bri sad at right
    show kat hapsword at pretty_left, flip

    k "Hah!"

    b "Sul serio?!"
    show bri angry 
    b "Come on Dad, you know she’s never going to do that!"

    scene bg street

    show bap at bapnerf

    ba "Exactly my point dearest Briaannaaaaaaaaaaa! This war will die when the family business dies."
    ba "Which it will not."
    ba "Because we are the best."

    hide bap
  
    show bri angry at right, flip 
    show kat hapsword at pretty_left, flip

    b "UghhhHHH! Whatever! I’m going home! Thanks for throwing me under the bus Katherine!"

    hide bri angry 
    with moveoutright

    n " - Exit Brianna - "
  
    scene bg street

    show bap at bapnerf

    ba "Wow, isn’t she the best?"
    ba "You should really get going too, Katherine, you know how your men get when you’re not around."

    hide bap
  
    show kat hapsword at left, flip

    k "You don’t have to worry about that."

    show kat potsword at left, flip
    k "I told them that if the camp wasn’t spotless by the time I came back, I’d take a pinky from each of them…"

    show kat hapsword at left, flip
    k "All of those who still have one to give, at least."

    hide kat hapsword with moveoutleft
  
    n " - Exit Baptista and Katherine , Enter Lucien and Toby - "

    show luc swoon at left, flip 
    with moveinright 

    l "My goodness Toby! Did you see that woman!? She’s simply enchanting!"

    show toby point at right 
    with moveinleft

    t "Really? I don’t know, she seemed a tad… unkind."
    t " I know you have a strange taste in women, Luci, but she’s not exactly something I’d sacrifice a pinky for!"

    show luc sigh 

    l "Not that woman! The other woman!"
    show luc swoon
    l "Ohhh…. The way her hair blew in the breeze.. I simply couldn’t look away!"
    show luc alas 
    l "The poor women, forced into war by a cruel nation, a cruel father, the tragedy!"
    show luc swoon
    l "A perfect girl, the best girl! She even hates white wine just like me!"

    t "But sir, were you not drinking a bottle of Fiano on the voyage here?"

    show luc sigh
    l "Please Toby, don’t be daft, that wine was clearly yellow." 
    show luc point
    l "More importantly: Toby, do you like your job?"

    show toby happy 
    t "Why of course sir, vending is a stockhands lifestyle."   

    l "Do you like it enough to skip a once-in-a-lifetime adventure whilst we pursue the thrill of forbidden war-torn love?"

    show toby point 
    t "..."
    t "Yes...I do?"

    show luc sigh
    l "Ah..."
    l "You know, that wasn't the answer I was expecting."

    show toby angry 
    t "Well pardon me Luci but I hardly think some street damsel is worth a month's pay."
    t "Besides, your father put much faith in you to meet this quota by the year's end.  It would be in poor taste to permit you such dillydallying."

    show luc alas
    l "Hmmm… quite the puzzling puzzle dear Tobias… If only there were a way to.."
    
    show luc point
    l "Aha!" with flashbulb 
    l "I've got it!"

    show toby happy 
    t "What is it sir?"

    l "What if there were a way to keep the shop open and allow me time to woo that beautiful maiden?"
    l "To grow closer to Brianna I must go under the radar, people in this town must know of my face by now."

    t "Quite hard to miss indeed, sir. Stunning, sir."

    l "I will undertake a disguise, and you will disguise yourself as I in my absence!"

    t "Aha! Brilliant!"

    l "But of course, what better a veil of deceit than to disguise myself as…!"
    
    t "Her latin tutor!"

    l "A Paduinian soldier!"

    show luc sigh
    
    l "What...? No Toby, that would be ridiculous."

    show toby cry

    t "My apologies, sir, I thought for certain we were on the same page"

    l "I mean I don’t even understand what could’ve spawned that idea in the first place."

    t "Deepest apologies once again, sir."

    show luc alas at very_left 
    with move

    l "Hmm… now the only remaining question is where I could find a proper disguise."
    
    show luc sigh 

    l "Maybe I could stea- No no that’ll never work."
    l "Hmmmmmm..."

    "???" "AHEM!"

    l "Bless you, Toby" 
    show toby point at center
    with move
    
    t "I beg your pardon?"

    "???" "AHEM! You two!"

    l "For goodness sakes, Toby, clear your throat! I’m thinking!"

    show toby angry 
    t "My throat is nothing less than spotless, I assure you!"

    show ten angry at very_right, flip 
    with moveinright

    te "You! Old man Cap! I’m talkin’ to you!"

    show luc point 
    show toby angry at flip
    l "Ah! You frightened me sir!"
    l "Welcome to Piece of Pisa, only the finest Pisanese artisanal goods brought straight to your door in Padua!"

    te "I don’t give a hoot about your foreign knicknacks!"
    te "A deaf man coulda heard you eyeballin’ my girlfriend from across the street! What’s the meanin' of this!?"

    show luc sigh 
    l "Oh… you don’t speak of that damsel Brianna.. Do you?"

    te "Who else!? You dolt!"

    show luc alas
    l "Ah catastrophe! Toby! My bride is already wed!"  
    l "O’ cruel world what hath thou against me!?"

    show toby angry at center, flip
    t "Wait one moment Luci, I know I saw no ring on that finger! This man is a liar!"

    show ten sad 
    te "Well… yes and no."
    te "Technically me and Brianna aren’t exactly conventionally “romantically involved”"

    show luc sigh 
    l "Conventionally?"

    show toby point at center, flip
    t "Involved?"

    l "Are you two together or not?"

    show ten angry
    te "Well! No! But we should be! We’re gonna be!"

    show toby happy at center, flip
    t "It sounds like this fellow’s game is but naught, sir Luci." 

    show luc point
    
    l "Delightful! Then it seems our course remains unassailed!"

    te "Um.. No! It remains very assailed!"
    te " Look kid, I’ve been after this gal for 5 odd months and it ain’t given me nothin’ to show, so you might as well just quit while you’re ahead."
    te "After all I do for her! I make all of her equipment for squat and this is the thanks I get? Hopeless romance?"

    l "Well my friend, seeing as how we’re equally disadvantaged, I’ll let you in on a little plan my stockhand and I have devised while you coughed at us from a distance."

    scene bg street with fade
    show luc point at very_left, flip
    show toby point at center, flip 
    show ten happy at very_right, flip

    l "That’s about it! I’m in need of a suit of armor, you’re in need of a chance to get close to Brianna. It’s foolproof!"

    te "Now that here is nothing short of brilliant! You’ve got yourself a deal old man! I’ll get everything we need right now!"

    hide ten happy with moveoutright

    show toby point at right 
    t "Pardon me sir, but is adding more competition to the…competition really the right move here?"

    l "It’s either a little friendly rivalry or no chance at all, dear Toby."
    l "This man may be able to mold tools, but mold hearts he certainly can not!"

    scene bg ship with fade
    show pet happy at left
    with moveinright

    show gru look at very_right
    with moveinright
    
    p "Wow, the sun is shining, birds are singing, what a wonderful day to be at peace, eh grumie?"

    g "hee-haw!"

    p "I’m so glad those nice parliament folks picked me to go make peace between Verona and Padua!"
    p "I mean, our countries have been at war for decades now! Dear mumsy back home will be so proud… Won’t she Grumie!"

    g "{i} Donkey noises {/i}"

    show pet think 
    p "And just look at that castle! If only those officials back home could see me now…"

    show pet shock
    p "Shoot Grumie, it’s the enemy battalion! Act natural!"

    hide gru look with moveoutleft
    show pet shock at very_left
    with move 

    show aluc shock at center
    show ate shock at very_right, flip

    p "Oh, Hello fellas! Off to serve your country I see! Well, nothing to see here, I’m just another resident of Padua, like you!"

    te "Good day sir, nothing to see here, we’re just two soldiers doing soldiery things!"

    show aluc sigh at center, flip
     
    
    l "{i}Tenny, we’re supposed to ask what his business is! He’s going to see right through our act! {/i}"

    hide aluc sigh
    show aluc shock at center
    show ate shock at flip, very_right
    te "Ah- right, right! {i} Ahem {/i}"

    show ate angry at very_right 
    te "What is your business here at the castle wall sir?"

    show pet shock 

    p "{i} (uh oh, he’s going to see right through my act!) {/i}"
    p "Well, uh, I’ve got this donkey here and- uh… citizen-y… things?"
    
    n "Tenny and Lucien stare at Petur with confusion"

    show pet sigh 
    p "Um- the truth is-! I’m an ambassador from Verona, and I’m here to arrange peace between our warring countries once and for all!"

    show aluc sigh 
    l "P-peace-!? Verona and Padua?? Please!"

    show ate happy at very_right 
    te "Hahahaha! Haha"

    l "Now, seriously. We aren’t supposed to let you in unless you tell us why you’re here."

    show pet angry 
    p "But I am serious! I was sent by Verona’s very parliament to do just that! I’m not going anywhere until a treaty is drafted to end the war!"

    show aluc shock at center, flip 
    l "Tenny, are you hearing this?"

    show ate shock at very_right 
    te "This guy wackadoodle! What are we going to tell our (beloved) “boss”?!"

    show aluc shock
    l "Hang on Tenny, I’ve got a plan!"

    show ate happy 
    te "Trying to woo the loveliest Briannaaaaaaaaaaaaaaaaaaaa.., of course?"
   
    show aluc sigh 
    l "And why can’t we do that?"

    show ate angry 
    te "because that oaf general said we can’t do that until both her and her sister lay down their swords for love!"

    show aluc shock 
    l "And Look! See! Perceive, Tenny! Right there before us, a man who may just be crazy enough to go near Katherine the Killer!"

    show ate happy 
    te "Ah! You’re right!"

    hide aluc shock
    show aluc sigh at center 
    l "listen, uh…"

    show pet happy 
    p "Petur."

    show aluc shock 
    l "Petur! Turns out, we’re as excited for all this ‘peace’ stuff as you, so we’re gonna help you out."

    p "Oh, thank you!!"
  
    show aluc cry 
    l "See, the guy you want is Supreme General, he’s the one calling the shots of this war, so cruel!"

    p "Magnificient! So you’ll take me to him?"

    show aluc sigh 
    l "No, no, no, not so fast my friend. The only way you’re ever gonna get to his heart is to first get through that of his daughters."
    l "See, General Baptista proclaimed that if any man, Paduain or Veronian, can get his dearest daughters to lay down their swords and stop fighting, he’ll put a stop to the war!"
  
    show ate shock 
    te "(But Lucien, I thought he was joking when he said that?)"

    l "shhhh!"

    l "But fear not! To help you out as two authentic civil servants do, Tenny and I over here are going to try our hand at his youngest daughter: Brianna."

    show ate happy
    te "To convince her to stop fighting, of course!"

    show aluc shock
    l "Yes! And you sir, we leave the most important part to you."

    p "What’s that?"

    l "The eldest: Katherine the Killer. That lady’s a real heartless monster, or so I’ve heard."

    te "Frightening!"

    l "They say she doesn’t have a soul! Impossible to sway! And worst of all,"

    te "She's got a taste for blood! Terrible, really." 

    l "Quite."
    l "Well, we leave everything in your capable hands Pete. Good luck!"

    hide aluc shock with moveoutright
    hide ate happy with moveoutright

    n "- Lucien and Tenny open the gate for Petur to enter -"

    show pet shock
    p "Oh- uh- thank you! . Man…. Katherine the Killer… what a scary name. Long one, too."

    show pet happy 
    p "Maybe I’ll just call her Katie instead. I’m sure she wouldn’t mind, right Grumie?"

    show gru sus at very_right
    with moveinright

    g "{i} Huff! {/i}"

    scene bg camp with fade 

    show pet happy at very_left
    with moveinleft
    n "- Petur enters, Lucien and Tenny behind him, the gates close with a loud bang, all eyes bat towards him -"
    n "- Most importantly, the singular eye of a blonde important-looking woman meets his gaze -"

    show kat angsword at very_right 
    with moveinright

    k "Who are you supposed to be?"

    show pet shock
    p "Oh… hi! My name is uhm.. Petur and I’m here on some um.."
    p "important… business."

    k "What kind of important business?"

    p "Like a uh… diplomatic kind of business… from Veron-"

    show kat potsword
    k "Verona?!?! Spy! Guards, Take him out!"

    show aluc shock at center, flip 
    with moveinleft

    l "Whoa! Whoa Whoa! Hold on, general! Just a moment, please!"

    show kat potsword
    k "Get out of my way Rookie! If you’re not going to kill this guy I’ll cut him up myself."

    l "Will all due respect Miss Minola, this is an ambassador you’re speaking to! He’s quite unarmed!"

    k "Did you check his horse?"

    show aluc sigh 
    l "Well no, but-"

    show aluc shock 
    show kat scold
    k "He could have weapons on its saddle, you idiot!"
    
    show kat potsword
    k "Giovanni! Check the horse!"

    show pet angry 
    p "Don’t you dare touch Grumie! And he’s a donkey!"

    k "So you ARE hiding something with that horse!"

    p "I might be, if I had one!"

    hide pet angry 
    with moveoutleft
    hide aluc shock 
    show aluc sigh at pretty_left
    with move
    l "Petur! Stop being an idiot, man! This lady is about to gut you!"

    hide aluc sigh
    show aluc shock at pretty_left, flip

    show kat scold at center 
    with move 

    show bri chill at very_right, flip

    b "What’s with all this noise!?"

    show kat potsword at center, flip

    k "Oh, nothing, there’s a Veronian spy IN THE CAMP Brianna! One that your freshest recruits just let right in!"

    l "Lady Brianna, your sister is sorely mistaken! This man is an ambassador from Verona, swordless, mind you."

    b "That sounds wonderful!"

    k "Brianna are you serious? You just met this guy, you don’t know what he’s really here for!"

    k "He could be assassin #4! Is that what you want?!"

    show bri shrug 
    b "Katherine look at him, this kid wouldn’t hurt a fly. I’m not actually sure he could if he wanted to."

    k "I don’t care! The only Veronian I want in this camp is a dead one."

    show bri angry 
    b "If you kill an ambassador, we’ll lose hope of ever putting an end to this stupid war!! All this hopeless bloodshed—they haven’t sent an ambassador in ages!"
    b "Plus father would be pissed."

    k "Dad can shove it! So what if we lose a couple ambassadors?! We’re not exactly overflowing with peace anyway!"

    b "I’m not going to let you kill a civilian, Katherine."

    show kat scold
    k "Ughhhhhhh fine! I don’t have time for this!"

    hide kat potsword
    show kat potsword at center
    k "You! New guy! Throw him in the jail cell and we’ll decide what to do with him later. "

    l "Right away, Madame."

    hide aluc shock 
    with moveoutleft

    scene bg jail with fade 

    show pet sigh at right, flip
    with moveinleft

    show aluc sigh at left, flip 
    with moveinleft

    p "Wait! You’re actually putting me in prison?"

    l "Look at the bright side! It’s less of a prison and more of a… temporary holding cell."

    show pet angry 
    p "Yeah, temporary until that woman kills me! This wasn’t part of the deal!"

    show aluc cry 
    l "I’m sure that the lovely Briannaaaaaaaa, so gorgeous and without a single violent bone in her body, would never let that fate befall you."
    l "I see nothing to worry about my friend!"

    play sound "bell.mp3"

    n "- DONG -"

    show aluc shock 

    l "Ah! Time for lunch already? Well I simply must get going sir Petur! Farewell!"

    hide aluc shock 
    with moveoutleft
    
    play sound "door.mp3"
    p "Wha- are you serious!?"

  

    show pet sigh
    p "Man, we’re really in for it now Grumie."

    show pet shock
    p "Grumie?"

    show pet sigh 
    p "Ugh..."

    scene bg camp with fade 
    show aluc sigh at center
    with moveinright
    with moveinleft 
    show ate happy at very_left 

    n "- Enter Lucien and Tenny, eating lunch in the courtyard -"

    show aluc shock
    l "My word! This bread is like iron!"
    l "Is Paduinian food always this impenetrable, Tenny?"

    te "Yep! Pretty much! This stuff is the only thing they can afford when they ain’t spending all their money on trebuchets or whatever."

    play sound "crunch.mp3"
    queue sound "spit.mp3"
    pause(1.5)
    l "Ptoo!"
    l "There’s a rock in my food!"

    te "Ya get used to it. You know some of the pinkish ones taste good if ya chew on them for a while."

    l "This is preposterous! And inedible! Tell me Tenny, is it not in a General’s best interest to ensure the nutrition of their soldiers?"

    show ate shock
    te "Mama always used to tell me that minerals were nutritious."

    l "Hanged, be! I’d like to speak with this woman, she must be as good a cook as you are a blacksmith!"

    show ate happy 
    te "Why, thank you!"

    show aluc sigh 
    l "Ugh..."

    show bri chill at very_right, flip 
    with moveinright

    b "Hey newbies, everything looking okay over here?"

    show ate happy at very_left 
    show aluc shock at center, flip

    l "My word Miss Brianna! I dare to detest madame! Are you aware that your nutriment contains pebbles and stones?"

    show bri shrug 
    b "Sigh.. that’ll happen."
    b "Most of the other men around her like to close their eyes and swallow as fast as possible."
    b "I hear it helps."

    show aluc sigh 
    l "Well I hardly wish to dine on ore whilst shrouded in the dark! But I will do what I must for my country, I suppose."
    show aluc cry 
    l " That’s what a mighty soldier would do, of course!"

    show ate angry 
    te "H- Hey! Well I would also eat some rock bread too! Isn’t that manly, Brianna!?"

    show bri uncomfy 
    b "Wha… I guess?"

    show ate happy 
    te "Hehe… Alright…"

    show bri chill 
    b "Oh! I just remembered what I came here for!"

    show aluc shock 
    l "What might that be, Lady Brianna?"

    b "I have a special mission that must be attended to at once! I fear that I must request the assistance of one of you."

    l "I’ll do it!"
    pause(0.5)
    show ate angry 
    te "I’ll do i- hey!"

    n "- Lucien discreetly dumps his food under the table -"

    hide aluc shock
    show aluc shock at center
    l "Well seeing as how my plate, pristine as the night sky, is bare, and yours remains full of your rations, you are unfit for a special mission!"
    show aluc cry 
    l "I would hate to disturb your lunch my friend!"

    te "Wha- I know you didn’t eat that fast! Yer a cheat!"

    show aluc shock
    l "I was simply rather starved, but now, my belly is full and I am ready to serve my glorious nation with the might of ten!"

    b "Well, he does have a point. I would hate to disturb your meal, Mr. Hortens."

    show ate shock 
    te "No! Please! Disturb my meal! Consider it disrupted! | I’ll do anything this mission takes! Really! Anything!"
    te "I’ll scrub the floor! i’ll scrub the walls! I’ll scrub the bathroom floor and walls! With my bare hands if I must!"
    te "..."

    show aluc shock 
    l "..."

    show bri uncomfy 
    b "..."

    l "Yeesh…"
    
    b "You know what, why don’t you just sit this one out, Mr. Hortens."
    b "I’ll explain on the way, Lucien. Let's not waste time."

    hide aluc shock 
    with moveoutright
    hide bri uncomfy 
    with moveoutright 

    te "Grumble… what could I have possibly done to deserve this?"

    scene bg wine 

    show bri chill at left
    with moveinleft 
    show aluc sigh at right 
    with moveinleft

    b "Welcome to the wine cabinet. This is where I present to you your first mission, rookie! Are you ready?" 

    show aluc shock 
    l "Why of course madame!"

    b "Wonderful! I need you… To lift this box!"

    l "Wait..? That’s really it?"
    
    b "Yep! It's too heavy for me to pick up, and it looks small enough for you to handle!"

    show aluc sigh 
    l "Oh… Okay."

    n "- Lucien lifts the box and places it on the counter -"

    show aluc shock
    l "Wait a moment, Miss Brianna! Could this be!?"
    l "Sangiovese!?"

    b "It is! One of my favorite reds in Padua!"

    l "Why, the blood of Jupiter is my favorite as well! This is wonderful!"
    l "Pardon me Brianna, but may I perhaps indulge in a sip of this delightful liquor?"

    show bri shrug
    b "Of course you may! It’s been much too long since I shared a drink with a person other than my harpy of a sister."

    l "Incredible! I mean- not that your sister is a harpy of course, she’s um… more like a… goose?"
    show aluc sigh
    
    l "Anyway! I will grab glasses right away!"

    b "Wait… you’re going to get… glasses?"

    show aluc shock 
    l "Well unless you’d like to drink it out of your palms, then of course!"

    show bri chill
    b "Unheard of…No man that has ever walked in this cellar has left without chugging straight from the bottle!"
    b "In all my days as general, I have never seen a general as sophisticated as you, Mr. Lucien."

    show aluc shock
    l "Oh.. er- well- uh. Thank you, lady Brianna!" 
    l "I must be going to get those glasses now!"

    hide aluc shock 
    with moveoutright

    pause(0.5)
    play sound "rummage.mp3"
    pause(4.6)
    show aluc shock at right
    with moveinright

    l "Behold! Glasses!"

    b "Beautiful! Pour me a little, would you?"

    l "I’m much too pleased that this is none of that yellow stuff. I simply can not bear it."
    l "You have fine taste, Lady Brianna."

    show bri shrug 
    b "Wait, excuse me? Yellow?"

    show aluc sigh 
    l "Yes, yellow wine of course, the curse’d stuff!"

    show bri chill 
    b " Aha! Mr. Lucien you loon! That wine isn’t yellow, it’s white."

    show aluc shock 
    l "You jest! It is clear as day that this wine bears color."
    l "Rather I mean, not clear at all, because this wine is not white."

    b "The grape it comes from is green, dear Lucien, but the folks who make it prefer to label it as white."

    show aluc cry
    l "For what purpose?"

    b "Haha! I’ve not a clue."

    l "Quite ludicrous if you ask me. these winemakers, colorblind I tell you!"

    b "{i} Pfft! {/i} Indeed!"

    b "..."

    show aluc sigh
    l "..."

    show bri shrug 
    b "Say Mr. Lucien, can you keep a secret?"

    show aluc shock 
    l "Why of course, I’d like to think that I’m quite covert myself."

    show bri sad
    b "I’m not supposed to have this wine in this camp, my father would never let me hear the end of it if he knew I had red wine in the cellar."

    l "What does it matter to him whether this wine is red or yell- I mean- white?"

    b "It’s not the color, it’s that it only costs less than a couple sequin."
    b "He says that he buys the best for me, but I think his idea of the best is just what costs the most."
    b "He’s got his head so wrapped up in all this mindless warfare that he won’t even listen to me. It’s so frustrating! Y-you know?"

    l "Well, if you ever need to smuggle in more crates of liquor, I know a humble civil servant!"

    show bri chill
    b "Haha! Wonderful, one less battle for me to worry about!"

    show aluc sigh 
    l "While we are disclosing our secrets, may I share one with you as well?"

    b "Of course, that seems only fair."
    
    l "I’m not a real soldier!"

    show bri shrug
    b "Wha- What!? Then what are you!?"

    show aluc cry
    l "A travelling merchant… from Pisa. But, but, but, I intend to do no harm!"
    l "If it were up to me, I’d have put a stop to this war, just like you."

    show bri chill 
    b "Well, you look in-uniform enough to me, you guard a post decently, and you can drink wine like a human being."
    b "A fine soldier if you’d ask me!"

    show bri sad
    b "However I must warn you, do you understand what Katherine will do to you if she finds out?"

    show aluc shock 
    l "Oh, lady Brianna, I assure you that is completely under my control!"

    show bri shrug 
    b "..."
    b "How, exactly?"

    scene bg jail with fade 

    show pet sigh at right, flip
    p "9,986 Galileos up on the wall, 9,987 Galileos up on the wall…"

    play sound "door.mp3"
    
    show kat angsword at left, flip 
    with moveinleft

    k "Hey! Horse Boy!"

    show pet shock 
    p "Ahh!"
    show pet angry 
    p "Hey, that's donkey-boy to you lady!"

    show kat potsword
    k "Whatever, here’s your rations for today."

    p "Wow, surprised to see that you're the one feeding me… or feeding me at all"

    show kat scold 
    k "Well, if I left it up to one of these no-brained jocks they’d probably find some way to screw it up, and Brianna would probably give you double the amount and then some since she’s little Ms. Charity."
    k "As much as I would appreciate it if you dropped dead, Brianna would likely try to assassinate me if I left you to starve, so eat."

    show pet sigh 
    p "Service here is impeccable, I’m glad to hear. Say, could I maybe get a napkin, Katie?"

    show kat potsword
    k "No, use your clothes. And don’t call me that!"

    p "A fork then?"

    k "No!"

    p "Spoon?"

    k "No! You can’t eat bread with a spoon anyway you three-inch fool!"

    show pet angry 
    p "I hope you know that I’ll be leaving no tip after this, Katie."

    show kat scold 
    k "Grah!! Are you always this persistent!?"

    k "You don’t make peace by being a smart-ass you know! I figured an ambassador would know that!"

    p "And what do you know about peace then?"

    k "I know that it’s stupid! And I also know that the naive nice guy act isn’t exactly moving me!"

    p "Honestly I don’t know what I was expecting when I asked. Of course a lady dubbed “The Killer” wouldn’t know how to be happy!"

    k "Hey, I know how to be happy perfectly well thank you!"
    hide kat scold
    show kat scold at left
    k "Hey, Now I’ll just be on my w- "

    p "Oh yeah, what makes you happy then?"

    show kat potsword at left, flip
    k "Um… well… I like war! And fighting! Fighting is fun! Watching the life of the enemy drain from their eyes as they-"

    show pet sigh 
    p "Come on now, there has to be something you actually like doing. War doesn’t count."

    k "Nope! War’s my thing, war prisoner, and I intend to keep it my thing, thank you!"

    show pet think
    p "You’ve never been to like… a play or something?"

    show kat scold
    k "Those are for babies, art is lame."

    show pet angry 
    p "They’re not for babies! I love plays!"

    k "My point stands."

    show pet sigh 
    p "Aw, well I bet if you’d been to one, you wouldn’t be saying that."

    show kat angsword 
    k "Doubt it."

    show pet happy 
    p "Aha! I have an idea!"
    p "Katie, I have a proposition for you."

    k "Oh, yay."

    p "Clearly, you’ve never been to a city before. I mean a {i} real {/i} city , that wasn’t on fire"
    p "So how about… we go out and have some fun!"
    p "You and me, out on the town! It’d be awesome!"
    p "{i} (This is totally my chance! Who knew being arrested would work out so well!) {/i}"

    show kat potsword
    k "Why the hell would I ever do something like that, especially with you, Veronian!?"

    show pet angry
    p "Hey, hey! Don’t jump to conclusions about me just yet! I’d like to make a deal with you."
    p "If I can’t show you that there’s more to life than senseless warfare by the end of the day, then I hereby lay my life down consensually on behalf of my country."
    p "Your sister certainly can’t be angry if it is my own decision. Therefore, you get to be rid of me! Free of charge!"
    p "{i} (Uh oh, I might’ve just blown it.) {/i}"

    show kat angsword 
    k "Hmmm… | I hope you understand that you just dug your own grave. I accept."

    show pet happy
    p "Wonderful! I promise I won’t let you down, Katie!"

    play sound "unlock.mp3"
    n "- Katherine lets Petur free -"

    k "I could kill you right now, don’t call me that."
    show pet shock 
    p "I’m sorry!"

    scene bg street with fade 

    show pet happy at center 
    with moveinleft
    show kat scold at very_left 
    with moveinleft
    show toby happy at very_right

    p "Look Katie! A travelling merchant! From Pisa! I love these guys!"

    show kat scold at very_left, flip
    k "Ugh, Pisa? That’s the one place Dad never allowed me to attack."

    t "You there! The cute couple! Step right up to Piece of Pisa for an authentic taste of-"

    show kat potsword 
    k "Not a couple! And your shop’s name is corny!"

    p "But Katherine, that’s what makes it so compelling!"
    p "Just look at the salesman’s hat! Doesn’t it make you want a piece… of Pisa?"

    show toby cry
    t "Ah! | My apologies sir and madame, I assure you I meant no offense!"
    hide toby cry 
    with moveoutright

    show pet happy at right, flip 
    with move 

    k "What is Pisa even good for anyway? These all look like tourist trap souvenirs."

    show pet shock 
    p "Well, it appears I’ve been trapped, and you’ll have to save me!"

    n "- Petur is fixated on the small trinkets -"

    show kat scold 
    k "Of course you would fall for this."

    show pet happy
    p "It’s all in good fun, nothing more fun than spending money!"

    k "Eugh..."

    p "Katie! Look! A little replica of the leaning tower of Pisa! I used to love this place when I was a wee lad."

    k "A {i} leaning {/i} tower? Excuse me?"

    show pet sigh
    p "Yeah, I guess the ground was too soft when they built it and it threw the foundation all off."

    show kat hapsword
    k "Hah! Classic Pisanese architecture at work, I fear."

    show pet happy 
    p "No, it's really cool actually! It’s honestly better in person."

    k "If I were to see it in person, I would knock it over and finish what those lousy builders started."

    p "Haha!"

    show kat potsword
    k "What!? Why are you laughing!?"

    p "The joke you made, it was funny."

    show kat scold
    k "That wasn’t a joke! I’d really do it!"

    p "Yes, I’m sure you would."

    k "I’m serious! I don’t joke!"

    show pet sigh 
    p "Well if you’re so serious, then I’d appreciate it if you didn’t knock it down! I quite like it."

    k "I almost want to do it more now."

    show kat potsword 
    k "Where’s the appeal in this dumb tower anyway?"

    show pet happy 
    p "I don’t know… perhaps that it’s funny?"

    k " It’s inefficient, that’s what it is. Nobody can live in it and it gives me second hand embarrassment when I look at it."
    k "It’s a waste of mortar, if you ask me."

    p "Not everything needs to serve a purpose. Maybe its purpose is to be entertaining?"

    k "I don’t understand you! So what, you just want every tower in the world to lean because it’s “funny”?"

    show pet shock 
    p "Well of course not, then it wouldn’t be special anymore"

    show pet happy 
    p "Plus, I’d be out of a place to live!"

    show kat scold 
    k "Yeah, I’ll believe it when I see it!"

    show pet happy 
    p "Maybe you’ll end up seeing it sooner than you think."

    hide pet happy
    show pet happy at right
    p "Excuse me, sir! How much for the tower replica?"

    scene bg street with fadehold 

    show kat scold at left, flip
    show pet happy at right

    k "I can’t believe you actually bought that thing. Personally, I wouldn’t take that even if you paid me to."

    show pet think at right, flip 
    p "And how much is that?"

    show kat shock 
    k "Wh- What? What do you mean?"

    show pet happy 
    p "How much would I have to pay you to take this?"

    k "Um… I don’t know. I didn’t really get to think that far ahead."

    p "How about I just give it to you as a gift, for free?"

    k "Oh… alright. It’d make a good paperweight, I guess…"

    p "You’re very welcome!"

    show kat scold
    k "I’ll keep it after I chop your head off as a memoir. It’s poorly constructed and dumb. Like you."

    show pet sigh
    p "Hey! Well… at least you like it." 
    show pet happy
    p "Progress!"

    k "So what now? Pointless shopping won't convince me to let you keep your head, you know."
 
    p "That's a surprise!"

    scene bg play with fade

    show kat angsword at left, flip
    with moveinleft
    show pet happy at right, flip 
    with moveinleft
    k "Oh no, please tell me this isn’t what I think it is."

    p "It's exactly what you think it is!"

    show kat scold 
    k "A play..."
    p "A play!"

    show kat potsword 
    k "Horse-guy, I really must detest your most pitiful of attempts. These are soooooo boring!"

    p "Come on, give it a shot! I’ve been going to plays for as long as I can remember and I love them every time!"
    p "You know, the first time I went to one of these I still had diapers on!"

    show kat hapsword
    k "Haha! So you admit they’re for babies!"

    show pet angry 
    p "What!? No!"

    k "“My name is Petur and I watch dumb comedies for dumb idiots and I pee in my pants”"
    k "That’s you, that’s what you sound like, because you’re a baby."

    p "I am not!"

    k "You definitely are!"

    p "Whatever! Be quiet, it’s starting!"

    scene bg play with fadehold

    show kat angsword at left, flip
    
    show pet happy at right, flip 
  
    k "What is this even about? Why does that guy have a donkey for a face?"

    show pet sigh 
    p "Honestly, I could never figure this one out. It’s a little too convoluted, even for me."

    show kat scold
    k "Oh, so you thought this would be a good first timer for me?"

    p "It was the only one playing tonight!"

    "???" "SHHHHHHHHHHHH!"

    show pet shock
    p "Sorry!"

    scene bg street with fade

    show kat angsword at left, flip
    with moveinright
    show pet sigh at right, flip 
    with moveinright

    p "Man, I still have no idea what actually happens in that play"

    show kat shock
    k "What didn’t you understand? Seems pretty clear to me."

    show pet angry
    p "How!? The whole fairy thing didn’t throw you off at all?"

    k "Mmmm… no not really."

    show pet happy 
    p "Aha! You liked it! You liked the play!"

    show kat potsword 
    k "N- No! I’m just able to retain information because I’m not an idiot! Like you!"

    p "Katie, I love plays and even that one puts me to sleep sometimes. You had to have liked it!"

    k "Whatever! Look at the sky, it's gonna get dark soon! We should start heading back now."

    show pet shock 
    p "Uh oh, it’s the end of the day already!?"

    show kat angsword
    k "Yeah, that usually happens when it gets dark."

    p "No, I mean, our deal!"
    p "Ah! I’m running out of time! I had three more places lined up and we haven’t even eaten yet!"
    p "Unless… did I do a good job?"

    show kat angsword
    k "Hmmm… You did an {i}okay{/i} job, I don’t know if I’d call it {i}good{/i}, though. "

    show pet happy
    p "Wait, really? I’ll take okay job over bad job!"
    p "Does that mean I get to live?"

    show kat scold 
    k "Urgghhhhh! I don’t know! I should kill you!"
    k "..."
    
    show kat potsword
    k "Why don’t I want to kill you!?"

    p "Maybe because I’m a great host!"

    k "Why are you so aggravating!?"

    show pet shock
    p "Oh, I’m sorry!"
  
    k "No, it's fine."
    k "I’m just… confused."

    show kat shock 
    k "I’ve never met a Veronian that I haven’t wanted to murder before."

    show pet think 
    p "So… you aren’t going to kill me?"

    show kat scold 
    k "..."
    k "I don’t think so, but what would my Dad think?"
    k "He’d give Brianna even more attention if I’m not the warlord that he wants me to be!"
    k "I try so hard to be a perfect General! Brianna doesn’t even show up to battles sometimes and somehow I get the short end of the stick!"

    p "Do you even like fighting wars?"

    show kat angsword
    k "Well, I probably should, it’s the only thing I’m good at."
  
    show pet happy 
    p "You’re pretty good at watching plays and looking at funny towers, that’s talent to me!"
    p "If it were me, I’d go full time!"

    show kat shock 
    k "I guess you’re right"

    p "Hooray! I’m right!"

    show kat angsword 
    k "But how the hell am I going to convince my Dad to end a war he loves more than me, probably?"

    p "I can help with that! That’s practically my entire job!"
    p "Let me introduce you to the odd soldier I met the other day…"

    scene bg ship with fadehold 

    show bri chill at very_left 
    show kat angsword at center 
    show pet happy at very_right, flip

    b "Hi Dad! What’re you doing?"
    
    scene bg ship
    show bap at bapnerf

    ba "Why hello Briannnnaaaaaa! I was just watering these beautiful lily’s! One of the best flowers I’ve ever had the pleasure of nurturing!"

    hide bap

    show bri chill at very_left 
    show kat angsword at center 
    show pet think at very_right, flip

    p "Wow, I wasn’t really expecting him to be a flower guy."
    
    scene bg ship
    show bap at bapnerf

    ba "Oh! I could hardly see you! Who might you be, young man?"

    hide bap

    show bri chill at very_left 
    show kat angsword at center 
    show pet shock at very_right, flip

    p "Oh- I’m Petur, I-"
  
    b "He’s an ambassador! From Verona!"
    
    scene bg ship
    show bap at bapnerf

    ba "Non ci credo, another one of you. I thought your nation would have well run out by now. Well son, how may I help you?"

    hide bap

    show bri chill at very_left 
    show kat angsword at center 
    show pet happy at very_right, flip

    p "I’d like to politely request an end to the war! Sir!"

    scene bg ship
    show bap at bapnerf
    ba "Haha! Ho! Nonsense, my boy! War does not simply end because the losers say so!"
    hide bap
  
    show bri chill at very_left 
    show kat angsword at center 
    show pet think at very_right, flip

    p "Well, I don’t know much about being a general, but it must be hard to fight a war without any soldiers."

    scene bg ship
    show bap at bapnerf
    ba "Surely you jest, son! Padua has a surplus of only the finest soldiers! Almost too many!"
    ba "Besides, no war is unwinnable with my wonderful little generals around! Isn’t that right girls?"
    hide bap

    b "No, it isn’t right."
    scene bg ship
    show bap at bapnerf
    ba "Precisely, well sai-"
    ba "Excuse me?"
    hide bap

    show bri uncomfy at very_left 
    show kat angsword at center 
    show pet think at very_right, flip

    b "I quit, Dad."
  
    scene bg ship
    show bap at bapnerf
    ba "You can’t possibly mean… your job!?"
    hide bap
    
    show bri uncomfy at very_left 
    show kat angsword at center 
    show pet think at very_right, flip

    b "Yes, I mean my job!"
  
    scene bg ship
    show bap at bapnerf
    ba "Have you forgotten what I told you? You may not under any circumstance abandon your position until your sister does! So there!"
    hide bap

    show bri uncomfy at very_left 
    show kat scold at center 
    show pet happy at very_right, flip 

    k "..."
    p "Katherine quits too!"
    show kat scold at center, flip
    k "Hey! I wasn’t ready yet!"  
    k "But yes, he’s right, I quit."
   
    scene bg ship
    show bap at bapnerf
    ba "I don’t believe it! I was just joking, of course! "
    hide bap

    show bri chill at very_left 
    show kat angsword at center 
    show pet happy at very_right, flip 
   
    k "Joking or not, I’ve already made my decision. I don’t need your approval anymore."
    p "Yeah, she doesn’t!"
    k "{i}(Petur! Stop stealing my moment!){/i}"
   
    scene bg ship
    show bap at bapnerf
    ba "I would have never expected this out of you of all people, Katherine! Have you forced this fate upon your sister as well?"
    hide bap

    show bri chill at very_left 
    show kat potsword at center 
    show pet happy at very_right, flip   
   
    k "What? No! She wants this more than me!"

    scene bg ship
    show bap at bapnerf
    ba "Is this true, Brianna?"
    hide bap    
   
    show bri chill at very_left 
    show kat potsword at center 
    show pet happy at very_right, flip 
    
    b "Of course! "
   
    scene bg ship
    show bap at bapnerf
    ba "..."
    ba "Well it appears I have no choice."
    ba "I will speak with parliament about forming a treaty committee."
    hide bap  

    show bri chill at very_left 
    show kat hapsword at center 
    show pet happy at very_right, flip 

    b "Yes! Thank you, Thank you, Dad! I’ll tell Luci right away!"
    hide bri chill 
    with moveoutleft 

    scene bg ship
    show bap at bapnerf
    ba "What am I going to do without a battle to fight? Is there anything in this world that could provide such a thrill?"
    hide bap  

    show kat hapsword at left
    show pet happy at right, flip 

    p "You like lilies, right? Why not open a flower shop?"

    scene bg ship
    show bap at bapnerf
    ba "Hmmm… Ah! Aha! You’re a genius, young man! An ambassador from the heavens!"
    ba "I simply must speak with Veronica right away! I know for certain she will provide me with the be-"
    hide bap  

    n "- Baptista walks away rambling to himself, but he seems happy -" 
    hide kat hapsword 
    show kat hapsword at left, flip
    show pet think at right, flip 
  
    p "..."
    p "So what now?"

    show kat shock 
    k "I… don’t know exactly. I was kind of hoping you had that figured out with your weird plan making skills."

    show pet happy 
    p "You could… work at your dad’s flower shop when it opens. I can see that!"

    show kat angsword
    k "Ew, I can’t, no."

    p "Aha! A better idea!"
    p "We could travel the world together! A Katie-Petur adventure, you and I, for a hundred years!"

    show kat shock 
    k " I doubt there’s anywhere we can go with a battalion that wouldn’t instantly kill me, though."

    show pet think 
    p "Hmmm..."
    show pet happy
    p "Aha! Pisa! You’ve never been there, correct?"
    p "They wouldn’t know your face!"

    show kat hapsword
    k "The kingdom with that doltishly constructed tower?"
    
    p "Precisely! Not doltish, but, Precisely!"

    k "..."
    k "Sounds… entertaining. You know, I forgot to mention the last reason tower reminds me of you."
    k "Despite it's poor foundations, even poorer architecture, and surely being the laughingstock of the century… It's still standing tall."
    show kat bow 
    k "It's still standing tall. And doing a marvelous job at that."

    p "Admit it!"

    show kat hapsword 
    k "Excuse me?"
   
    show pet happy  
    p "You like me."

    show kat angsword
    k "No! I like you as much as I like plays!" 

    show pet happy 
    p "My point still stands."

    scene bg black with fade

    n "The END"












    # This ends the game.


    return
