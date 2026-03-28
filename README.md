# VITyarthi-CSA2001-Project
Toxicity Detector (Because the internet can be a garbage fire)

Let's be real for a second. If you run a Discord server, a subreddit, a gaming clan, or literally *any* place where humans can type things on the internet... you're going to deal with trolls. 

I got so tired of manually deleting toxic comments and dealing with people being awful to each other that I decided to build a robot to do it for me. 

This is a machine learning tool built in Python that basically acts as your digital bouncer. It reads messages in real-time and figures out if someone is just having a heated gamer moment, or if they're actually being toxic, dropping slurs, or making threats. 

---

 What does this thing actually do?

* **It doesn't just say "Bad Word" (Multi-Label):** Using a basic swear filter is annoying because context matters. This AI actually breaks down *how* awful a message is into 6 categories:
    * **Toxic** (Just generally being a jerk)
    * **Severe Toxic** (Being a HUGE jerk)
    * **Obscene** (Dropping F-bombs and vulgar stuff)
    * **Threat** ("I'm going to hack your router")
    * **Insult** ("You have the IQ of a wet paper towel")
    * **Identity Hate** (Racism, sexism, homophobia, etc.)
* **It actually understands context:** It knows the difference between *"Shut up, that meme is hilarious"* (friendly) and *"Shut up, nobody likes you"* (toxic). Take that, standard Regex filters!
* **It runs fast:** Like, really fast. You can hook this up to a live chat and it'll score messages before anyone even has time to read them.
* **Easy to plug in:** I didn't want to make this complicated. You can import it into your existing bot or backend in like three lines of code.

---

 Stuff you need before we start

You don't need a supercomputer, but you do need a few things installed on your machine:

* **Python 3.8+** 
* **TensorFlow / Keras** 
* **Pandas & NumPy** 

---

Bash
cd toxicity-detector
Install the boring dependencies:

Bash
pip install -r requirements.txt

 How to actually use it
I tried to make the code as dummy-proof as possible. Once you have it installed, here's how you use the detector in your own Python scripts:

Python
from toxicity_detector import BouncerBot

# 1. Wake up the bot and load the brain (the .h5 model file)
bouncer = BouncerBot(model_path="models/my_cool_model.h5")

# 2. Let's test some messages
nice_message = "Dude your Minecraft house looks awesome."
mean_message = "You are literal trash at this game, uninstall."

# 3. See what the AI thinks!
print("Checking the nice message...")
print(bouncer.score(nice_message))
# Output: {'toxic': 0.01, 'insult': 0.00...} -> We are chilling! 

print("Checking the mean message...")
print(bouncer.score(mean_message))
# Output: {'toxic': 0.95, 'insult': 0.89...} -> Get the ban hammer! 

Tweaking the rules
In the config.json file, you can set the "strictness" levels.
If your community is meant for adults, maybe you don't care about the obscene category and set the threshold to 0.99. But if it's a family-friendly server, you can set it to 0.50 so it catches everything. You make the rules!

The Nerd Stuff (How it works under the hood)
If you're wondering how the AI actually works, here's the quick version:
I trained this model on the Kaggle Jigsaw Toxic Comment dataset, which is basically over 150,000 real Wikipedia comments ranging from super helpful to incredibly toxic.

The architecture uses something called a Bidirectional LSTM. 
In plain English? It reads a sentence forwards and backwards at the same time. This helps it understand the grammar and the vibe of the sentence, rather than just looking for naughty words.

FAQ (Questions nobody actually asked yet)
Q: Why not just use an auto-mod word blacklist?
A: Because people are creative. If you ban the word "idiot", they'll just type "1diot" or "id!ot". AI doesn't care about spelling tricks; it looks at the whole sentence's meaning.

Q: Will this accidentally ban my friends for making sarcastic jokes?
A: Maybe? Sarcasm is notoriously hard for AI to understand. I recommend using this tool to flag messages for a human moderator to review, rather than auto-banning people instantly (unless the "Threat" or "Identity Hate" score is like 99%).

Help me fix my spaghetti code
This is an open-source project because I think the internet should be less toxic, and also because I'm definitely not the best coder in the world.

The Legal Stuff
This project is under the MIT License. Basically, do whatever you want with it. Put it in your Discord bot, use it for a school project, build a startup around it. Just don't sue me if it accidentally bans your mom from your server.

Hit me up
If you use this and like it, or if you completely break it and need help, lemme know........
