from players import *


the_fighter = Fighter("Beverly", "Moea", "Electric")
the_cleric = Cleric("Michelle", "Flats", "Calamari: The mermaid goddess")
item1 = Item("Door Key", 2)

def fighter_route():

         """
         This is the figter route where the player attacks everything

         Args:
            None

         Returns:
             None
         """



         print("Ah a fighter huh? well lets start!")
         print(f"Your name is {the_fighter.first_name} {the_fighter.last_name} You are a fighter! your element is {the_fighter.element}")
         first_choice = int(input("The dungeon guard wont let you in! what do you do? (1 for slash 2 for stab 3 for poke)"))
         if first_choice == 1:
             the_fighter.slash()
             print("But he was wearing chainmail!(Hint:good against slashes but not stabs) he slashes you even harder and you perish\nGAME OVER")
         elif first_choice == 2:
             the_fighter.stab()
             print("The stab is effective! he falls down perished and you may proceed!")
             item1.get_item()
         elif first_choice == 3:
             the_fighter.poke()
             print("you...poke him...he laughs at your attempt to kill him and hits you in the head with his sword. You perish\nGAME OVER")

def cleric_route():
        """
         This is the Cleric route where the player spares everything

         Args:
            None

         Returns:
             None
         """
        print("A cleric hmm? then let us begin~")
        print(f"Your name is {the_cleric.first_name} {the_cleric.last_name} You are a cleric! your god is {the_cleric.god}")
        first_choice = int(input("The dungeon guard wont let you in! though he seems a bit on edge. Maybe you could help him? what do you do? (1 for prayer 2 for heal 3 for buff) "))
        if first_choice == 1:
             the_cleric.prayer()
             print("His face looks a lot calmer now he sighs. 'Thank you...I guess I was so worried about my physical stength I forgot to take care of my mental strength as well, Go on proceed'")
             item1.get_item()
        elif first_choice == 2:
             the_cleric.heal()
             print("He looks at you strangely...'Do I look hurt to you moron? Get out!' he says then hits you in the head with his sword. you perish\nGAME OVER")
        elif first_choice == 3:
             the_cleric.buff()
             print("He scoffs looking offended 'What? you think I need help? think im not strong enough? Ill show you weak!' he says. He slashes you with his sword. You perish\nGAME OVER")

print("Hello there! welcome to Totally Acurate Dungeon Simulator!\nIn this game you pick one of our lively subjects and take them on a jorney through The Dungeon(tm)!")
the_choice = int(input("what do you fee like doing? hitting or healing? (1 for hitting 2 for healing) "))

if the_choice == 1:
    fighter_route()
elif the_choice == 2:
    cleric_route()

