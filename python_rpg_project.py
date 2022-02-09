import random

def display_character_menu():
    print("""                                      
                                      CHARACTER MENU 
============================================================================================
                 A                          B                           C
            name: KIWI                 name: MANGO                 name: GUAVA
            health: 300                health: 100                 health: 250
            strength: 50               strength: 100               strength: 50
            confidence: 0              confidence: 0               confidence: 0

""")

class Character:
    def __init__(self, name, letter, health, strength, confidence, attack_a, attack_b, attack_c, attack_a_phrase, attack_b_phrase, attack_c_phrase):
        self.name = name
        self.letter = letter
        self.health = health
        self.strength = strength
        self.confidence = confidence
        self.attack_a = attack_a
        self.attack_b = attack_b
        self.attack_c = attack_c
        self.attack_a_phrase = attack_a_phrase
        self.attack_b_phrase = attack_b_phrase
        self.attack_c_phrase = attack_c_phrase
    def display_current_stats(self):
        print(f"""
                   CURRENT STATS FOR {self.name}
====================================================================
HEALTH: {self.health}
STRENGTH: {self.strength}
CONFIDENCE: {self.confidence}
""")
    def display_attack_options(self):
        print(f"""
                  ATTACK OPTIONS FOR {self.name}
====================================================================
A. {self.attack_a}
B. {self.attack_b}
C. {self.attack_c}
""")

kiwi = Character("KIWI", "A", 300, 50, 0, "Tickle Vivian", "Throw your shoe at Vivian", "Sing the song that Vivian hates as loud as you can",
"\n** You tickled Vivian! She HATES being tickled! She lost 50 health points! **\n", 
"\n** You threw your shoe at Vivian! It hit her, but she threw it back at you!\nVivian lost 50 health points and you lost 20 health points! **\n", 
"\n** You sang the song that Vivian hates as loud as you can! She lost 50 health points! **\n")
mango = Character("MANGO", "B", 100, 100, 0, "Run your fingernails down a chalkboard", "Throw your shoe at Vivian", "Pinch Vivian as hard as you can", 
"\n** You ran your fingernails down a chalkboard! Vivian hates that sound!! She lost 100 points! **\n", 
"\n** You threw your shoe at Vivian! It hit her, but she threw it back at you!\nVivian lost 100 health points ans you lost 40 health points!**\n",
"\n** You pinched Vivian as hard as you can! She lost 100 health points! **\n")
guava = Character("GUAVA", "C", 250, 50, 0, "Flick Vivian as hard as you can", "Challenge Vivian to a mini dance battle", "Tickle Vivian",
"\n** You flicked Vivian as hard as you can! She lost lost 40 health points! **\n", 
"\n** You challenged Vivian to a mini dance battle! She's got some moves, but she isn't nearly as good as you!\nVivian lost 50 health points and you lost 20 health points!**\n",
"\n** You tickled Vivian! She HATES being tickled! She lost 40 health points! **\n")
vivian = Character("VIVIAN", "D", 300, 40, 60, "", "", "", "", "", "")

character_list = [kiwi,mango,guava]

line_one = input("Today is the day! You are headed to an interview for your dream job as an interior designer! (Press enter to continue)")
line_two = input("But wait .... You see Vivian (the girl who has been mean to you since 5th grade)! (Press enter to continue)")
line_three = input("She is definitely going to try to stop you from making it to the interview by attempting to defeat you in a battle! (Press enter to continue)")
line_four = input("If you can get past her, you can make it make it to the interview! (Press enter to continue)")
vivian_doesnt_know_name = input("...As you approach Vivian, she pretends she doesn't know your name to try to make you feel small. (Press enter to continue)") 
name_or_run_choice = input("""
Vivian: "HEY YOU! What's your name again?" 
Type your name to give her your name                 
OR                 
press 1 to point at a "squirrel" and run past her (Press enter to continue): """).upper()

while len(name_or_run_choice) > -1:
    if len(name_or_run_choice) > 0 and name_or_run_choice != "1":
        break
    elif name_or_run_choice == "1":
        line_five = input('It worked! Vivian got distracted looking for the "squirrel" that you pointed at and you ran past her! (Press enter to continue)')
        line_six = input("You made it to the interview, but you didn't get the job. (Press enter to continue)")
        line_seven =input("Maybe next time you see Vivian you should try to win the battle against her to gain some confidence before your interview! (Press enter to continue)")
        line_eight = input("...It's the next day and you are on your way to another interview you have set up for your dream job as an interior designer! (Press enter to continue)")
        line_nine = input("Oh no ..it's Vivian again! (Press enter to continue)")
        vivian_doesnt_know_name = input("...As you approach Vivian, she pretends she doesn't know your name to try to make you feel small. (Press enter to continue)") 
        name_or_run_choice = input("""
Vivian: "HEY YOU! What's your name again?" 
Type your name to give her your name                 
OR                 
press 1 to point at a "squirrel" and run past her (Press enter to continue): """).upper()
    else:
        while len(name_or_run_choice) == 0:
            name_or_run_choice = input('Please type your name OR press 1 to point at a "squirrel" and run past Vivian: ').upper()
            if len(name_or_run_choice) > 0 and name_or_run_choice != "1":
                break
            elif name_or_run_choice == "1":
                line_five = input('It worked! Vivian got distracted looking for the "squirrel" that you pointed at and you ran past her! (Press enter to continue)')
                line_six = input("You made it to the interview, but you didn't get the job. (Press enter to continue)")
                line_seven =input("Maybe next time you see Vivian you should try to win the battle against her to gain some confidence before your interview! (Press enter to continue)")
                line_eight = input("...It's the next day and you are on your way to another interview you have set up for your dream job as an interior designer! (Press enter to continue)")
                line_nine = input("Oh no ..it's Vivian again! (Press enter to continue)")
                vivian_doesnt_know_name = input("...As you approach Vivian, she pretends she doesn't know your name to try to make you feel small. (Press enter to continue)") 
                name_or_run_choice = input("""
Vivian: "HEY YOU! What's your name again?" 
Type your name to give her your name                 
OR                 
press 1 to point at a "squirrel" and run past her (Press enter to continue): """).upper()

if len(name_or_run_choice) > 0:
    print_name = input(f"""You: "Come on Vivian! You know that my name is {name_or_run_choice}! Now, let's get this battle over with. I have an interview to get to!" (Press enter to continue)""")
    must_decide_character = input("Now, you have to decide which character you would like to be during battle. (Press enter to see the menu of characters to choose from)")
    display_character_menu()
    character_letter = input("Type the letter of the character you would like to be during battle here (A, B, or C): ").upper()
 
while len(character_letter) > -1:
    matching_character_letter = [character_class for character_class in character_list if character_class.letter == character_letter]
    if character_letter == "A" or character_letter == "B" or character_letter == "C":
       break
    else:
        while character_letter != "A" or character_letter != "B" or character_letter != "C":
            display_character_menu()
            character_letter = input("PLEASE CHOOSE ONE OF THE CHARACTERS FROM THE MENU (A,B, or C): ").upper()
            break

display_character_letter = input(f"\nYou have chosen to be {matching_character_letter[0].name} during battle! (Press enter to see their stats)")
matching_character_letter[0].display_current_stats()
user_continue = input("(Press enter to continue)")

battle_begins = input(f"""
Random person on the street: "It's time for battle! {matching_character_letter[0].name} ATTACKS FIRST!" (Press enter to continue)
""")

vivians_attacks = ["\n>> Vivian unleashed her pet fire ant on you! OUCH! You lost 40 health points! <<\n", 
"\n>> Vivian hit you with her purse! WHY IS HER PURSE SO HARD?! You lost 40 health points! <<\n",
"\n>> Vivian does the one karate move that she knows on you! You lost 40 health points! <<\n"]

while vivian.health > 0 or matching_character_letter[0].health > 0:
    if vivian.health <= 0 or matching_character_letter[0].health <= 0:
        if vivian.health > matching_character_letter[0].health:
            print("Sadly, you lost the battle against Vivian and never made it to the job interview.")
            break
        elif matching_character_letter[0].health > vivian.health:
            matching_character_letter[0].confidence += 1000
            print(f"YAY! You won the battle against Vivian and your confidence is now at {matching_character_letter[0].confidence}!\nYou made it to the interview and got the job as an interior designer!!")
            break
    print("These are the attack options that you can use against Vivian:")
    matching_character_letter[0].display_attack_options()
    user_attack_choice = input("How would you like to attack Vivian? Choose A, B, or C: ").upper()
    if user_attack_choice == "A":
        vivian.health -= matching_character_letter[0].strength
        print(matching_character_letter[0].attack_a_phrase)
        attack_a_continue = input(f"""\nYOUR CURRENT HEALTH: {matching_character_letter[0].health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)\n""")
    elif user_attack_choice == "B":
        matching_character_letter[0].health -= (matching_character_letter[0].strength * 0.4)
        vivian.health -= matching_character_letter[0].strength
        print(matching_character_letter[0].attack_b_phrase)
        attack_b_continue = input(f"""\nYOUR CURRENT HEALTH: {matching_character_letter[0].health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)\n""")
    elif user_attack_choice == "C":
        vivian.health -= matching_character_letter[0].strength
        print(matching_character_letter[0].attack_c_phrase)
        attack_c_continue = input(f"""\nYOUR CURRENT HEALTH: {matching_character_letter[0].health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)\n""")
    else: 
        while user_attack_choice != "A" or user_attack_choice != "B" or user_attack_choice != "C":
            matching_character_letter[0].display_attack_options()
            user_attack_choice = input("!!! PLEASE CHOOSE AN ATTACK OPTION FROM THE MENU !!! (A,B,or C): ").upper()
            if user_attack_choice == "A":
                vivian.health -= matching_character_letter[0].strength
                print(matching_character_letter[0].attack_a_phrase)
                attack_a_continue = input(f"""\nYOUR CURRENT HEALTH: {matching_character_letter[0].health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)\n""")
                break
            elif user_attack_choice == "B":
                matching_character_letter[0].health -= (matching_character_letter[0].strength * 0.4)
                vivian.health -= matching_character_letter[0].strength
                print(matching_character_letter[0].attack_b_phrase)
                attack_b_continue = input(f"""\nYOUR CURRENT HEALTH: {matching_character_letter[0].health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)\n""")
                break
            elif user_attack_choice == "C":
                vivian.health -= matching_character_letter[0].strength
                print(matching_character_letter[0].attack_c_phrase)
                attack_c_continue = input(f"""\nYOUR CURRENT HEALTH: {matching_character_letter[0].health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue)\n""")
                break
    if vivian.health <= 0 or matching_character_letter[0].health <= 0:
        if vivian.health > matching_character_letter[0].health:
            print("Sadly, you lost the battle against Vivian and never made it to the job interview.")
            break
        elif matching_character_letter[0].health > vivian.health:
            matching_character_letter[0].confidence += 1000
            print(f"YAY! You won the battle against Vivian and your confidence is now at {matching_character_letter[0].confidence}!\nYou made it to the interview and got the job as an interior designer!!")
            break
    matching_character_letter[0].health -= vivian.strength
    vivians_random_attack = random.choice(vivians_attacks)
    print(vivians_random_attack)
    vivians_attack_continue = input(f"""YOUR CURRENT HEALTH: {matching_character_letter[0].health}
VIVIAN'S CURRENT HEALTH: {vivian.health}
(Press enter to continue) """)