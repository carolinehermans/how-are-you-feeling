from textblob import TextBlob
hunt = """It's too difficult to find a good job! But I will try my best. 

I'll try my best. This week feels like half of the semester. It was tired, but I have reason to expect a better result.

Mom called a week ago. She has cancer. She doesn't want me home for the surgery. Numb, sad, scared, But, also okay for now.
    prayers for your mother.
    I've been there. prayers for you. <3
    +1 +1 +1 +1 +1 +1 +1 +1 +1

I'm feeling good! Why is that the default answer?

My problem is: I have *excess ego*. I want to find that my true self is selfless.

Hot. :(
    what?

Overwhelmed.!!!

Awesome!

Tired, but life still needs to continue.

WAY TO NEW LIFE! 

I feel very excited for the future and very nervous at the same time! Things are happening for me right now which is exciting, but I'm scared and just waiting for myself to mess up and everything to be ruined.

I feel good even though I am going through fire and pain! From previous challenges and failures. But guess what! Am living my imagination.

NO.

I am about to have a one person learning party up in this piece. I'm feeling good.

Over the Christmas break, I proposed to someone I love dearly. She said she needs time to think about it. I've waited for a year to do this. Excited. Hopeful. Without regrets. 
Please pray this works out for me!!!

Good!

Not sure if everything will go to plan, but hopeful nonetheless. Glad to be back. :)
ALSO, YOU'RE REALLY COOL.
Thanks for caring about us, you lovely stranger.

I am very tired now.

Okay, I'm doing better than I was yesterday, which is good. I want to do better tomorrow too. Stay safe everyone!

ENDURANCE + RESILIENCE is what I learned till now!!

How can I be lost when I got nowhere to go Unforgiven III Metallica. Pretty much sums up my life. What about you?!

7/10

Great!

Good, how are you?

[Charlie Brown yelling "AUGH" here]

IN LOVE!

This assignment is bad. It sucks!

Never better.

Since the semester has started, there has been so much to do. Assignments, hackathons, internships. It's very stressful. Yesterday, I analyzed 911 data of NYC. It was pretty cool. I also read about Cinncinnati's blight problems. It was pretty cool. Also, I think I need a boyfriend! Really bored and stressed. Need to take that out sometime. xoxo gossip girl <3

Nah.

I need a job soon!!! :)

Really tired. + boys are kind of xx to deal with

too much.

100

poopy pants!

Some typa way

About as ready as a Spongebob on crack.

Quiero que me acepten en el PhD and don't want to go back home.

Voglio un messagio del mio vicimo di case per dore un seuso a tutto cio. Sto levaudio Troppo!!! {{{there is no way i transcribed this correctly}}}

I've been better. I got rejected from two fellowship ensembles I applied for this week, and have an audition coming up Thursday evening. I'm realizing how much I still need someone to guide/mentor me because I feel like my favorite professor who was this to me and I have kind of drifted apart, and I'm not really sure why, but I still need her :(
Thanks for giving me someone to vent to. I feel alone a lot of the time.

Peachy!

Determined.

I have to poop!
Update: I pooped. Mission Accomplished.

Whoo Hoo! Yeah, baby! Way to go!

The surgery was quick and easy. Mostly: relieved. Next week: lymphectomy biopsy results come back. So... a tempered relief for the time being. Guess it was more of a biopsy along with the lymphectomy, then. My mistake.

It looks like my life is falling apart. I feel overwhelmed and stressed out.

Okay, I'm just visiting from Williams College in MA. I'm trying to get my life together w/ internships. Hopefully not too many sick people touched this pencil. Oh wait I'm sick...

I feel so sad about myself, because I just do not want to do things but play video games. I have my dream  making an anime  and I am takign related course, but I don't want to put efforts. I know it is impossible to achieve anything without doing something. My thoughts and my actions are never agreed :(

Nearly ready for the next step.

Vim is the best editor.

same.

I am happy. I completed a lot of work I should do :)

Oggi somo distrutta! 2016.01.30 I feel destroyed.

Like it's time to start a new page!

Great! Cause the *Lord* is my strength #CRU

poop.

Indecisive.

Optimistic!

Overwhelmed, but positive! Happy day :) I will work really hard but I am ready!

YOLO Life!!!

Hunt is always LIT!!

Estoy abburido de la vida!

Real good. :)

{{cannot read this. AJ says it's in chinese, will get someone else to translate for me}}

Stressed out.

I get distracted whoops.

Currently in the middle of an all  nighter.

Pray for my grandma. She went into hospice.

That feeling when you just finish an assignment and you feel so relaxed in comparison to how you felt 30 mins ago it's wonderful

I ask you what the homework is. You give me a racoon. One of these days, I get reborn as an ocelot. You disapprove.
Your disapproval sends ripples across the void that separates life and death.
Somewhere in Phoenix, a dog gets fed steak for the rest of its natural life.

This place has ruined my life. I cannot think. I cannot write. I am inarticulate, and I hate you all.

Tired.

By using my hands.

Better.

frayed and still fragile, but also like I might finally be okay again.

great!

today, i am just fine :)

God is dead.

Good.

Alone.

Okay.

"Be strong and courageous. Do not be afraid or terrified because of them, for the LORD your God goes with you; he will never leave you nor forsake you." Deuteronomy 31:6 WIV

Sore due to exercise. HOPE for increasing strength.

THUG LIFE!


"""

fb = """
Lost in the world

Overwhelmed with work but enjoying life to the fullest :)

I have some huge head pains because I was just on a date, and we were in the guy's room, and it was getting a little heated, and he pick me up, and I go down to do a backbend so he can do some fun things, and he drops me-- my head slams HARD into his bedpost, and I lay there crippled for like a minute. It was bad, and now I'm in bed with ice cream thinking about life. 

I can't believe I did this

I just want to squat 500lbs

Content. And that's really scary. I don't feel like I deserve to be happy. All my art and drive comes from a place of sadness, and I'm afraid without that I can't do anything of worth.
"I'm currently debating seeing a mental health professional. I feel anxiety and melancholy and have for years, but not to the point where I fail to function. 


I see most if not all anecdotes of depression depict it as a kind of catastrophic, desperate ennui, and my encounter with (tentatively diagnosed) bipolar in a loved one certainly provided a stark realization of the depths one's mind can sink. 
And in comparison to all of that, I can't help but think maybe my personality just isn't wired for any kind of overt happiness, that there isn't any kind of aberration of brain chemistry at work. Maybe the best I can really achieve is a kind of resigned contentment, given that my baseline mood is somber. Am I okay with that?"

Really stressed out, feel like life is moving way too fast. I hate how the pressures of the future are keeping me from enjoying the now. The worst part is, I know what I'm doing wrong - stressing too much, but it's difficult to snap out of it.

feeeelsbad

Inspired

Like sunshine on a rainy day bursting through the dingy gray clouds to bring life and warmth to the fogotten green plants reminding them that they are loved. You are my sunshine.

I'm feeling relatively on top of the things that I have to and want to do right now.

Kind of okay. Just came out of a CAPS session. What happens if you've racked up a ton of successes in life but when you actually feel numb about everything that's going on? Big tech companies offer you internships and whatnot but you don't get excited anymore really. You keep setting lofty goals for yourself and you reach them which is great but the happy feeling is fleeting and last for something like an hour or a week at most. What happens when this bubble of everything is too good to be true breaks?

Hype

Feelin some melons 

Vague

"Like a plastic bag, drifting through the wind, wanting to start again.
So paper thin, like a house of cards, one blow from caving in.
Already buried six feet under- screams but no one seems to hear a thing."

"Gray days like this confirm my belief that I'd kill myself in a heartbeat if I didn't think it would hurt anyone other than me. 
I hate how cold winter is...
I'm thankful it's almost the weekend. "

Tired. So so tired.

"I wrote a pretty depressing response to this a few minutes ago, and I'd like to add that while I fantasize about killing myself sometimes, I'm not suicidal. I could never make my mother cry.
I'm going to go hide in the warmth and pretend outside doesn't exist for a bit, maybe watch some netflix and de-stress before doing my work for tomorrow. I'll leave you with a bit of an upbeat note - http://theawkwardyeti.com/comic/personal-today/ .
Also I loved reading the edit history of your Facebook status ;) Thank you for doing this."

Exhausted all the time

Eh, could be better. I just feel like my happiness is just going to go down over the next couple weeks

"Exhausted.....

"
Tired, inadequate, hopeless, and bored
Stressed
"Anxious. Worried. Stressed. 

Loved. Warm. 

Freezing cold. 

Able and unable.

Like the physical embodiment of juxtaposition. "

Eh. Pretty good.

In love!!!

I'm leaving next week and I haven't told any of my friends, I'm probably never seeing them again.
So I'm feeling pretty sad

exhausted but excited about life
a bit glum tbh
but hopeful that it'll pass in a couple days"

Sick

depressed as fuck

My life is great right now - but right now, I feel restless and stressed out.

Quite, quite exhausted at life in general ~
anxious but excited aka THINGS ARE HAPPENING I THINK I LIKE THAT AHHHHHH
https://www.youtube.com/watch?v=luM6oeCM7Yw

weird. things are just weird. idk. 

I'm kind of sad about wanting someone. I'm not too comfortable with wanting someone this much."

Okay, but my boyfriend didn't text me back or reply to my snapchat asking what I should name my new cactus. Sadness. 

"honestly? pretty sad. all of the time. and the one person I want to talk to I can't talk to anymore for fear of pushing him away even more. but I'm working on it. always.
how are you Caroline? u da bomb"

I'm not okay. I promise.

Not bad ^.^ I feel a little sick, but it's giving me an excuse to spoil myself

A
E
S
T
H
E
T
I
C

"I've been really sad lately. Part of that is because the anniversary of my mom's death is just around the corner, some of it is because a close friend just told me his mom has a brain tumor, and some of it is just stress and relationship troubles. Mostly it's because I feel like things shouldn't be the way they are, and it saddens me to think of how the world would be if she hadn't died.
Mostly though I'm optimistic. I'm surrounded by amazing people who do amazing things, and maybe, if I try hard enough, I can make them so happy that I don't have to be.
The world is a wonderful place. I think the future is looking up."

A bit down and stressed out. But still excited and determined to push through.

I've been better, but life goes on

stressed b/c i have to do hw on my bday

"At the bus stop; pacing 
It helps the cold.
Talking out loud; pacing
People think I'm crazy
Its ok; more space for pacing "

wink wonk

To not do 213 and instead end up playing Skyrim till 6am: awesome. 



"""

huntSplit = hunt.splitlines()
for huntResponse in huntSplit:
    if huntResponse == "":
        huntSplit.remove(huntResponse)

responseCount=0
responseLengthSum = 0

mostPositive = ""
mostNegative = ""
highestPolarity = 0
lowestPolarity = 0
currPolarity = 0
huntSentiments = []
for response in huntSplit:
    responseLengthSum+=len(response)
    responseCount+=1
    totalPolarity = 0
    numSentences = 0
    blobresponse = TextBlob(response)
    for sentence in blobresponse.sentences:
        totalPolarity += sentence.sentiment.polarity
        numSentences += 1
    if (numSentences!=0): 
        currPolarity = totalPolarity/numSentences
        huntSentiments.append(totalPolarity/numSentences)
        if (currPolarity > highestPolarity): 
            mostPositive = response
            highestPolarity = currPolarity
        if (currPolarity < lowestPolarity): 
            mostNegative = response
            lowestPolarity = currPolarity



total = 0
negSum = 0
posSum = 0
neutralSum = 0
for sentiment in huntSentiments:
    if (sentiment<0): negSum += 1
    if (sentiment>0): posSum += 1
    if (sentiment==0): neutralSum +=1
    total+=sentiment
avg = total/len(huntSentiments)
negPercent = float(negSum)/len(huntSentiments)
posPercent = float(posSum)/len(huntSentiments)
neutralPercent = float(neutralSum)/len(huntSentiments)



print"*******Hunt Library*******"
print "Number of responses analyzed: " + str(responseCount)
print "Average response length: " + str((responseLengthSum)/len(huntSplit)) + " characters"
print "Average response polarity: " + str(avg)
print "Percent of responses that were negative: " + str(negPercent)
print "Percent of responses that were positive: " + str(posPercent)
print "Percent of responses that were neutral: " + str(neutralPercent)
print "Most negative response: " + mostNegative
print "Most positive response: " + mostPositive


fbSplit = fb.splitlines()
for fbResponse in fbSplit:
    if fbResponse == "":
        fbSplit.remove(huntResponse)

responseLengthSum=0
responseCount=0
mostPositive = ""
highestPolarity = 0.0
mostNegative = ""
lowestPolarity = 0.0
currPolarity = 0.0


fbSentiments = []
for response in fbSplit:
    responseLengthSum+=len(response)
    totalPolarity = 0
    numSentences = 0
    responseBlob = TextBlob(response)
    for sentence in responseBlob.sentences:
        totalPolarity += sentence.sentiment.polarity
        numSentences += 1
    if (numSentences!=0): 
        currPolarity = totalPolarity/numSentences
        fbSentiments.append(totalPolarity/numSentences)
        if (currPolarity > highestPolarity): 
            mostPositive = response
            highestPolarity = currPolarity
        if (currPolarity < lowestPolarity): 
            mostNegative = response
            lowestPolarity = currPolarity
    if (numSentences!=0): responseCount+=1



total = 0
negSum = 0
posSum = 0
neutralSum = 0
for sentiment in fbSentiments:
    if (sentiment<0): negSum += 1
    if (sentiment>0): posSum += 1
    if (sentiment==0): neutralSum +=1
    total+=sentiment
avg = total/len(fbSentiments)
negPercent = float(negSum)/len(fbSentiments)
posPercent = float(posSum)/len(fbSentiments)
neutralPercent = float(neutralSum)/len(fbSentiments)

print "\n"
print"*******Facebook*******"
print "Number of responses analyzed: " + str(responseCount)
print "Average response length: " + str((responseLengthSum)/len(fbSplit)) + " characters"
print "Average response polarity: " + str(avg)
print "Percent of responses that were negative: " + str(negPercent)
print "Percent of responses that were positive: " + str(posPercent)
print "Percent of responses that were neutral: " + str(neutralPercent)
print "Most negative response: " + mostNegative
print "Most positive response: " + mostPositive

