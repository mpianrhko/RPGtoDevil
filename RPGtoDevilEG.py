import random
import sys
import time

gold = 50
inventory = []
player_health = 100
player_damage = 10
strong_monster_defeated = False
fishing_rod = False

def print_inventory():
    print("\nInventory:")
    if not inventory:
        print("Empty")
    else:
        for item in inventory:
            print("- " + item)
    print("Gold: " + str(gold))

def market_option():
    global gold, player_damage, player_health, fishing_rod
    print("\nWelcome to the market!")
    print("0. Exit")
    print("1. Buy items")
    print("2. Sell items")
    choice = input("Enter your choice: ")

    if choice == "1":
        buy_item()
    elif choice == "2":
        sell_item()
    elif choice == "0":
        return
    else:
        print("Invalid choice!")

def buy_item():
    global gold, player_damage, player_health, fishing_rod
    print("\nWelcome to the item shop!")
    print("0. Exit")
    print("1. Sword (50 gold)")
    print("2. Shield (30 gold)")
    print("3. Fishing Rod (50 gold)")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        if gold >= 50:
            gold -= 50
            inventory.append("Sword")
            player_damage += 10
            print("You bought a sword!")
            print("Your damage increased by 10!")
        else:
            print("Not enough gold!")
    elif choice == "2":
        if gold >= 30:
            gold -= 30
            inventory.append("Shield")
            num_shields = inventory.count("Shield")
            player_health += 20 * num_shields
            print("You bought a shield!")
            print("Your health increased by", 20 * num_shields, "!")
        else:
            print("Not enough gold!")
    elif choice == "3":
        if gold >= 50:
            gold -= 50
            inventory.append("Fishing Rod")
            fishing_rod = True
            print("You bought a fishing rod!")
        else:
            print("Not enough gold!")
    elif choice == "0":
        return
    else:
        print("Invalid choice!")

def sell_item():
    global gold, fishing_rod, player_damage, player_health
    print("\nSelect an item to sell:")
    print_inventory()
    choice = input("Enter the number of the item to sell (or 0 to cancel): ")
    
    if choice.isdigit():
        index = int(choice) - 1
        if index >= 0 and index < len(inventory):
            item = inventory.pop(index)
            if item == "Sword":
                player_damage -= 10
                gold += 25
                print("You sold the", item, "for 25 gold!")
            elif item == "Shield":
                player_health -= 20
                num_shields = inventory.count("Shield")
                player_health -= 20 * num_shields
                gold += 15
                print("You sold the", item, "for 15 gold!")
            elif item == "Fishing Rod":
                fishing_rod = False
                gold += 25
                print("You sold the", item, "for 25 gold!")
        elif index == -1:
            return
        else:
            print("Invalid item number!")
    else:
        print("Invalid choice!")

def fish():
    global gold
    print("\nYou start fishing...")
    time.sleep(3)  # Simulate waiting for a few seconds
    print("3")
    time.sleep(3)  # Simulate waiting for a few seconds
    print("2")
    time.sleep(3)  # Simulate waiting for a few seconds
    print("1")
    time.sleep(3)  # Simulate waiting for a few seconds
    print("Got it!")
    fish_result = random.choice([0, 5, 10, 15])
    
    if fish_result == 0:
        print("You caught nothing...")
    else:
        gold += fish_result
        print("You caught", fish_result, "golds worth fish!")
    
    return

def fight_monster():
    global player_health, gold, strong_monster_defeated, player_damage
    print("\nChoose the type of monster to fight:")
    print("0. Exit")
    print("1. Normal Monster")
    print("2. Strong Monster")
    if strong_monster_defeated:
        print("3. Devil")
    choice = input("Enter your choice: ")

    if choice == "1":
        monster_health = random.randint(50, 100)
        monster_damage = random.randint(5, 15)
        print("\nA normal monster appears!")
    elif choice == "2":
        monster_health = random.randint(100, 200)
        monster_damage = random.randint(10, 30)
        print("\nA strong monster appears!")
    elif choice == "3":
        monster_health = random.randint(200, 400)
        monster_damage = random.randint(20, 60)
        print("\nThe Devil appears!")
    elif choice == "0":
        return
    else:
        print("Invalid choice!")
        return

    while True:
        print("\nOptions:")
        print("q. Attack")
        print("w. Run")
        choiceA = input("Enter your choice: ")

        if choiceA == "q":
            base_damage = random.randint(10, 20)
            num_swords = inventory.count("Sword")
            player_damage_g = base_damage + 10 * num_swords
            monster_health -= player_damage_g
            player_health -= monster_damage
            print("You attack the monster for", player_damage_g, "damage.")
            print("The monster attacks you for", monster_damage, "damage.")
            print("Your health:", player_health)
            print("Monster health:", monster_health)

            if monster_health <= 0:
                print("\nYou defeated the monster!")
                if player_health <= 0:
                    print("\nBut you were also defeated...")
                    print("You Lost. Thanks for playing!")
                    sys.exit()
                elif choice == "2":
                    earned_gold = random.randint(40, 100)
                    gold += earned_gold
                    print("You earned", earned_gold, "gold!")
                    if not strong_monster_defeated:
                        strong_monster_defeated = True
                        print("Now you are ready to fight the DEVIL!!")
                elif choice == "1":
                    earned_gold = random.randint(20, 50)
                    gold += earned_gold
                    print("You earned", earned_gold, "gold!")
                elif choice == "3":
                    print("Congratulations! You saved the world. Thanks for playing!")
                    sys.exit()
                break
            elif player_health <= 0:
                print("\nYou were defeated...")
                print("You Lost. Thanks for playing!")
                sys.exit()
        elif choiceA == "w":
            if random.random() < 0.2:
                print("\nYou failed to run away!")
                monster_damage = random.randint(10, 20)
                player_health -= monster_damage
                print("The monster attacks you for", monster_damage, "damage.")
                print("Your health:", player_health)
                print("Monster health:", monster_health)
                if player_health <= 0:
                    print("\nYou were defeated...")
                    print("You Lost. Thanks for playing!")
                    sys.exit()
            else:
                print("\nYou successfully ran away!")
                break
        else:
            print("Invalid choice!")

def temple_option():
    global player_health, gold
    print("\nYou enter the temple.")
    print("The priest offers to fully restore your health for 20 gold.")
    choice = input("Do you want to proceed? (yes/no): ")

    if choice.lower() == "yes":
        if gold >= 20:
            gold -= 20
            if "Shield" in inventory:
                num_shields = inventory.count("Shield")
                max_health = 100 + 20 * num_shields
                if player_health == max_health:
                    print("\nYour health is already full.")
                else:
                    player_health = max_health
                    print("\nYou have been fully restored to", max_health, "health.")
            else:
                if player_health == 100:
                    print("\nYour health is already full.")
                else:
                    player_health = 100
                    print("\nYou have been fully restored to 100 health.")
        else:
            print("\nNot enough gold!")
    elif choice.lower() == "no":
        return
    else:
        print("\nInvalid choice!")

def state_check():
    global player_health, player_damage
    print("\nState Check:")
    print("Your health:", player_health)
    print("Your damage range:", player_damage, "-", player_damage + 10)

def play_game():
    global fishing_rod
    print("\nWelcome to the RPG game!")
    print("You wake up in a small village...")
    
    while True:
        print("\nOptions:")
        print("1. Market")
        print("2. Check inventory")
        print("3. State Check")
        print("4. Fight monster")
        print("5. Temple")
        if fishing_rod:
            print("6. Fishing")
        print("e. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            market_option()
        elif choice == "2":
            print_inventory()
        elif choice == "3":
            state_check()
        elif choice == "4":
            fight_monster()
        elif choice == "5":
            temple_option()
        elif choice == "6" and fishing_rod:
            fish()
        elif choice == "e":
            confirm_quit = input("\nDo you really want to quit the game? (Yes/No): ")
            if confirm_quit.lower() == "yes":
                print("\nThanks for playing!")
                sys.exit()
            elif confirm_quit.lower() == "no":
                continue
            else:
                print("Invalid choice!")
        else:
            print("Invalid choice!")

play_game()
