class Chatter(object):
    def start(self, start_emotion):
        self.emotion = start_emotion
        print "Hello there, how are you doing?"
        userinput = raw_input("> ")
        while userinput != "quit":
            if "angry" in userinput:
                self.emotion = Angry()
            elif "silly" in userinput:
                self.emotion = Coy()
            elif "hello" in userinput:
                self.emotion = Welcoming()
            response = self.emotion.respond(userinput)
            print response
            userinput = raw_input("> ")

class Emotion(object):
    pass

class Angry(Emotion):
        def respond(self, userinput):
            if "good" in userinput:
                return "I don't care if you're good or not."
            elif "bad" in userinput:
                return "Great, go away."
            else:
                return "What do you want?"

class Welcoming(Emotion):
    def respond(self, userinput):
        if "good" in userinput:
            return "I'm so glad that you're good."
        elif "bad" in userinput:
            return "That's such a shame..."
        else:
            return "Tell me how you're doing."

class Coy(Emotion):
        def respond(self, userinput):
            if "good" in userinput:
                return "Oh, that's interesting."
            elif "bad" in userinput:
                return "Ah, why don't you tell me more?"
            else:
                return "Tell me how you're doing."

#Start the program
from random import choice
emotions = [Welcoming(), Angry(), Coy()]
startemo = choice(emotions)
app = Chatter()
app.start(startemo)
