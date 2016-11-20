from sys import exit
from random import randint

class Scene (object):

    def enter(self):
        exit(1)

class Engine(object):

        def __init__(self, scene_map):
            self.scene_map = scene_map

        def play(self):
            current_scene = self.scene_map.opening_scene()
            last_scene = self.scene_map.next_scene('finished')

            while current_scene != last_scene:
                next_scene_name = current_scene.enter()
                current_scene = self.scene_map.next_scene(next_scene_name)

            #be sure to print out the last scene
            current_scene.enter()

#end of the game
class Death(Scene):
    def enter(self):
        print "You will never get your bachelor degree."
        exit()

#start of the game
class Start(Scene):
    def enter(self):
        print "Your mission is to find the one book that will help you pass your exams."
        print "Are you going to look for it on the internet or in a library?"

        choice = raw_input("> ")

        if choice == "internet":
            print "That's not where you look for proper literature."
            return 'death'

        elif choice == "library":
            print "Good choice. You enter the library."
            return 'library'

        else:
            print "This is not a choice"
            return 'start'

#uses random number generator
class Library(Scene):
    def enter(self):
        print "Inside the library there are three shelfs and you don't have time"
        print "to go through all of them. Pick one."

        good_option = randint(1,3)
        guess = raw_input("> ")

        if guess == good_option:
            print "Good choice. You chose shelf %s and you've found your book, you go to the office to rent it." % guess
            return 'office'

        else:
            print "That was the wrong shelf. You have on more try."

            guess = raw_input("> ")

            if guess == good_option:
                print "Good choice. You've found your book, you go to the office to rent it."
                return 'office'

            else:
                print "That was the wrong shelf. Your time is up."
                return 'death'



class Office(Scene):
    def enter(self):
        print "You enter the office. The grumpy lady looks at you. You"
        print "a: give her a smile"
        print "b: Tell a joke"
        print "c: Just give her the book in order to rent it"

        option = raw_input("> ")

        if option == "a":
            print "She smiles back at you and you get the book. You will pass your exams."
            return 'finished'

        elif option == "b":
            print "She doesn't get your joke. You are completely fucked because she won't give you the book."
            return 'death'

        elif option == "c":
            print "She says: 'Why are you so unpolite? If you say 'please'"
            print "the next time you want to rent a book, maybe you'll even get one.'"
            return 'death'

        else:
            print "The lady doesn't understand you. Try again."
            return 'office'

# you won the game scene
class Finished(Scene):

    def enter(self):
        print "You won! You will pass your exams."
        return 'finished'

# map of all scenes
class Map(object):

    scenes = {
        'start': Start(),
        'library': Library(),
        'office': Office(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('start')
a_game = Engine(a_map)
a_game.play()
