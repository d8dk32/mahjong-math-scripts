import math
import random

def pon_wait():
    #set up the wall, minus our starting hand, which we'll assume doesn't have the tiles we're looking for.
    #using 1s and 0s for "one of our waits" and "not one of our waits"
    wall = [0] * 121
    wall = wall + [1,1]
    random.shuffle(wall)

    #opp's hands. Our hand doesn't matter, it would be all 0's, and we'll just tsumogiri till we hit our wait
    hand1 = []
    hand2 = []
    hand3 = []
    #opps draw from wall to initialize their hands. This way they might start with one of our needed tiles
    for x in range(0,13):
        hand1.append(wall.pop())
        hand2.append(wall.pop())
        hand3.append(wall.pop())

    turns = 0 #I decided I want to track the number of turns it takes 
    discards = 0 #just going to sum all the opps discards. if its greater than 0, our tiles been discarded
    while len(wall) > 0 and discards < 1:
        try :
            turns += 1

            hand1.append(wall.pop())
            random.shuffle(hand1)
            discards += hand1.pop()

            hand2.append(wall.pop())
            random.shuffle(hand2)
            discards += hand2.pop()

            hand3.append(wall.pop())
            random.shuffle(hand3)
            discards += hand3.pop()

            #this represents our draw
            discards += wall.pop()

        except:
            #catch IndexError when we try to pop from an empty list, we went through the whole wall and never hit our wait
            pass

    #strictly speaking, discards > 1 could be true, but if that happens it still means we hit our wait so I think its fine
     #return whether or not we hit our wait, and how many turns it took
    return [int(discards > 0), turns]
        
        


def chi_wait():
    #using 1s and 0s for "one of our waits" and "not one of our waits"
    wall = [0] * 115
    wall = wall + [1,1,1,1,1,1,1,1]
    random.shuffle(wall)

    #opp's hands. Our hand doesn't matter, it would be all 0's, and we'll just tsumogiri till we hit our wait
    hand1 = []
    hand2 = []
    hand3 = []
    #opps draw from wall to initialize their hands. This way they might start with one of our needed tiles
    for x in range(0,13):
        hand1.append(wall.pop())
        hand2.append(wall.pop())
        hand3.append(wall.pop())

    turns = 0 #I decided I want to track the number of turns it takes 
    discards = 0 #just going to sum all the opps discards. if its greater than 0, our tiles been discarded
    while len(wall) > 0 and discards < 1:
        try:
            turns += 1

            hand1.append(wall.pop())
            random.shuffle(hand1)
            hand1.pop()

            hand2.append(wall.pop())
            random.shuffle(hand2)
            hand2.pop()

            #only track the discards of the player to our left
            hand3.append(wall.pop())
            random.shuffle(hand3)
            discards += hand3.pop()

            #this represents our draw
            discards += wall.pop()
        except:
            #catch IndexError when we try to pop from an empty list, we went through the whole wall and never hit our wait
            pass

    #strictly speaking, discards > 1 could be true, but if that happens it still means we hit our wait so I think its fine
    #return whether or not we hit our wait, and how many turns it took
    return [int(discards > 0) , turns]
        
pon_chance = 0
pon_turns = 0
chi_chance = 0
chi_turns = 0

x = 10000

for i in range(x):
   
    pon_result = pon_wait()
    pon_chance += pon_result[0]
    pon_turns += pon_result[1]
   
    chi_result = chi_wait()
    chi_chance += chi_result[0]
    chi_turns += chi_result[1]


pon_chance /= x
pon_turns /= x

chi_chance /= x
chi_turns /=x

print("PON WAIT")
print("Probability of completing: " + str(pon_chance))
print("avg. turns: " + str(pon_turns))

print("CHI WAIT")
print("Probability of completing: " + str(chi_chance))
print("avg. turns: " + str(chi_turns))