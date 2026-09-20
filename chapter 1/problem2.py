# install an external module and use it to perform an operation of your interest 
import math
print(math.sqrt(25)) # output = 5.0

from random import randint
print(randint(1,20))

import pyttsx3
engine = pyttsx3.init()


engine.say("""Hey, woman
Let me be your woman
Woman, woman, woman (ayy)
I can be your woman
Woman, woman, woman
Let me be your woman
Woman, woman, woman (ayy)
I can be your woman
Woman, woman, woman

""")
engine.runAndWait()

    

