# How Are You Feeling?

## What is this?
A fun experiemnt of mine!

Over my past semester at school, I've beem amassing anonymous responses to the question "how are you feeling?" and now, the time has come to start analyzing them.

Technically, this is a project for my bookbinding class.

## Where did you get the responses?
So far, it's about an equal distribution between two methods. 

The first thing I did was bought a blank notebook at the campus bookstore, and printed out a little sign that said "How are you feeling?" I left the notebook in a prominent spot in our campus library, and left it alone for a couple of months. This gave me about 100 really awesome responses.

I decided it'd be interesting to try other methods as well, so I posted on Facebook with a link to an anonymous Google Form with one question, "how are you feeling?". About 80 people filled it out.

##How's the analysis going?
I'm still working on it. The word frequency analysis is probably the coolest part. I ran some sentiment analysis on it, but I'm looking to use more sophisticated technologies going forward. Namely, the library that I used tended to miss out on the more nuanced posts about depression and illness, and instead pick up on one-word "negative" posts like "Sick" or "Bad". 

Here's what I've found so far:
### Sentiment Analysis
#####Hunt Library
Number of responses analyzed: 96

Average response length: 56 characters

Average response polarity: 0.153537465824

Percent of responses that were negative: 0.136842105263

Percent of responses that were positive: 0.463157894737

Percent of responses that were neutral: 0.4

Most negative response: This assignment is bad. It sucks!

Most positive response: Awesome!


#####Facebook
Number of responses analyzed: 81

Average response length: 69 characters

Average response polarity: 0.00258494706026

Percent of responses that were negative: 0.296296296296

Percent of responses that were positive: 0.308641975309

Percent of responses that were neutral: 0.395061728395

Most negative response: Sick

Most positive response: To not do 213 and instead end up playing Skyrim till 6am: awesome. 

## Word Frequency
###### Hunt Library Most Frequent Words
feel, +1, have, need, do, she, will, about, was, you

###### Facebook Most Frequent Words
with, do, are, life, stressed, just, like, some, on, you

#### All Responses Most Frequent Words
that, have, do, are, life, just, like, be, about, you


##What's next?
Collect more responses in more ways. I'm thinking of doing in person interviews, or going out in other parts of Pittsburgh to collect data from more than just Carnegie Mellon students.

##Can I read the responses?
Yep! They're in two files, fb.txt contains the Facebook responses, and hunt.txt contains the Hunt Library responses.

#All in all, this is the most code I've ever written for a bookbinding project.
