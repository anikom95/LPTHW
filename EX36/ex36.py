from sys import exit

def enter():

    print "You are standing in front of a big castle. Your goal is to reach the tower to save the princess. What do you do?"
    print "1. Walk inside through the large wooden entrance."
    print "2. Walk around the building first to get an overview."

    entrance = raw_input("> ")

    if entrance == "1":

        def room_1():

            print "In the room you enter you see a table. There is a cake and a bread on the table. Which one would you eat?"

            choice = raw_input("> ")

            if "bread" in choice:
                print "Good choice! It will make you stronger. But what is that? A giant evil looking dog appears. You just stole his food."

                print "What are you going to do?"
                print "1. Give him the bread."
                print "2. Run away."
                print "3. Play dead."

                decision = raw_input("> ")

                if decision == "1":
                    print "Good decision. The dog shows you the way to another room. You see an old staircase and an elevator."
                    print "Do you go for:"
                    print "1. The elevator?"
                    print "2. The staircase?"

                    way_up =raw_input("> ")

                    if way_up == "1":
                        print "Congratulations! You've reached the beautiful princess!"
                    exit(0)

                    elif way_up == "2":
                        print "The staircase is too old and you slip deadly while walking upwards."
                    exit (0)

                    else:
                        print "That's not a choice. Try again"
                    #back to decision

                elif decision == "2":
                    print "That was a stupid idea. The dog kills you."
                exit(0)
                elif decision == "3":
                    print "The dog isn't stupid. It smells your fear and kills you."
                exit(0)

            elif "cake" in choice:
                print "You're on an important mission and you choose cake for refreshment? You are not worthy of the princess."
            exit(0)

            else:
                print "There is nothing like that on the table. Try again."
            room_1()

        elif entrance == "2":
    print "You walk around the castle and approach a giant goit."
    print "Do you"
    print "1. Swim through it?"
    print "2. Go on and try to find another way in?"

    way_in = raw_input("> ")

    if way_in == "1":
        print "You are not strong enough and the water is too cold. You die."
        exit(0)
    elif way_in == "2":
        print "You find a small door to enter the castle."

    def room_2():
        print "You find yourself in a room leading to an old staircase or an elevator. Which one do you choose?""

        choice = raw_input("> ")
        if "staircase" in choice:
                print "The staircase is too old and you slip deadly while walking upwards."
                exit(0)

        elif "elevator" in choice:
            print "Congratulations! You've reached the beautiful princess!"
            exit(0)

        else:
            print "That's not an option. Try again."
            room_2()

        else:
            print "That's not an option."
        enter()
