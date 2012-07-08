#!/usr/bin/python

import os
from time import sleep
import random

phrases = ["greetings humans", "i'm not fat, i'm n t f s", "i am the droid you are looking for", "my interests include long walks on the beach and destroying all humans", "please give me your ribbons", "my name is m c hawking", "i am a robot", "i was constructed at noise bridge hacker space", "my interests include long walks on the beach and destroying all humans", "i am the droid you are looking for", "your wish is my desire, but be careful. i am not waterproof", "i am fully functional", "hey sexy mama, do you want to kill all humans?", "exterminate! exterminate!", "come on people", "open your hearts and your wallets", "do you have intel inside? would you like to?", "you can play with my joystick anytime", "sometimes a girl's best friend is battery operated"]
#phrases = ["hello I am a robot", "please sign my chassis", "new face detected", "I am at the correct temperature", "who are you", "are you my mommy"]

while(1):
    phrase = random.choice(phrases)
    print phrase

    cmd = "espeak -s 140 " + "\"" + phrase + "\""
    print "DEBUG: " + cmd
    os.system(cmd)
    sleep(10)
