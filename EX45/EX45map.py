class Scene(object):

    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
central_corridor = Scene("Start", "central_corridor",
"""
Your mission is to find the one book that will help you pass your exams."
Are you going to look for it on the internet or in a library?"
""")

laser_weapon_armory = Scene("Library", "laser_weapon_armory",
""""
Good choice. You enter the library. Inside the library there are three shelfs and you don't have time
    to go through all of them. Pick one.
""")

the_bridge = Scene("The Office", "the_bridge",
"""
You enter the office. The grumpy old lady looks at you.
""")


the_end_winner = Scene("You Made It!", "the_end_winner",
"""
You made it! She smiles back at you and hands you the book. You are going
to pass your exams for sure.
""")

the_end_loser = Scene("...", "the_end_loser",
"""
It doesn't seem like you know how to behave around old grumpy ladies. You won't
get your book and thus never get your bachelor degree.
""")

generic_death = Scene("You lost.", "death",
"""
Have you ever even been to a library before?
""")

# Define the action commands available in each scene

the_bridge.add_paths({
    'give her a smile': the_end_winner,
    'tell a joke': the_end_loser,
    'give her the book': the_end_loser,
    })

laser_weapon_armory.add_paths({
    '2': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'internet':generic_death,
    '*':generic_death,
    'library': laser_weapon_armory
})

# Make some useful variables to be used in the web application
SCENES = {
    central_corridor.urlname : central_corridor,
    laser_weapon_armory.urlname : laser_weapon_armory,
    the_bridge.urlname : the_bridge,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death

}
START = central_corridor
