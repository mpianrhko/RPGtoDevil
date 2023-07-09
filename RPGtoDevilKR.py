import random
import sys
import time

gold = 500
inventory = []
player_health = 100
player_damage = 10
strong_monster_defeated = False
fishing_rod = False

def print_inventory():
    print("\n인벤토리:")
    if not inventory:
        print("당신의 가방은 현재 비어있습니다.")
    else:
        for item in inventory:
            print("- " + item)
    print("골드: " + str(gold))

def market_option():
    global gold, player_damage, player_health, fishing_rod
    print("\n상점에 오신 것을 환영합니다!")
    print("0. 나가기")
    print("1. 아이템 구매")
    print("2. 아이템 판매")
    choice = input("옵션 중 선택해주세요: ")

    if choice == "1":
        buy_item()
    elif choice == "2":
        sell_item()
    elif choice == "0":
        return
    else:
        print("가능하신 선택이 아닙니다!")

def buy_item():
    global gold, player_damage, player_health, fishing_rod
    print("\n이곳에서는 아이템을 구매하실 수 있습니다!")
    print("0. 나가기")
    print("1. 검 (50 골드)")
    print("2. 방패 (30 골드)")
    print("3. 낚시대 (50 골드)")
    choice = input("옵션 중 선택해주세요: ")
    
    if choice == "1":
        if gold >= 50:
            gold -= 50
            inventory.append("검")
            player_damage += 10
            print("당신은 검을 성공적으로 구매하셨습니다!")
            print("공격력이 10 상승합니다!")
        else:
            print("골드가 부족합니다!")
    elif choice == "2":
        if gold >= 30:
            gold -= 30
            inventory.append("방패")
            num_shields = inventory.count("방패")
            player_health += 20 * num_shields
            print("당신은 방패를 성공적으로 구매하셨습니다!")
            print("체력이", 20 * num_shields, "상승합니다!")
        else:
            print("골드가 부족합니다!")
    elif choice == "3":
        if gold >= 50:
            gold -= 50
            inventory.append("낚시대")
            fishing_rod = True
            print("당신은 낚시대를 성공적으로 구매하셨습니다!")
        else:
            print("골드가 부족합니다!")
    elif choice == "0":
        return
    else:
        print("가능하신 선택이 아닙니다!")

def sell_item():
    global gold, fishing_rod, player_damage, player_health
    print("\n판매하실 아이템을 선택해주세요:")
    print_inventory()
    choice = input("몇번째의 아이템을 판매하실 건가요? (0은 취소입니다): ")
    
    if choice.isdigit():
        index = int(choice) - 1
        if index >= 0 and index < len(inventory):
            item = inventory.pop(index)
            if item == "검":
                player_damage -= 10
                gold += 25
                print("당신은", item, "을 25 골드에 팔았습니다!")
            elif item == "방패":
                player_health -= 20
                num_shields = inventory.count("방패")
                player_health -= 20 * num_shields
                gold += 15
                print("당신은", item, "를 15 골드에 팔았습니다!")
            elif item == "낚시대":
                fishing_rod = False
                gold += 25
                print("당신은", item, "를 25 골드에 팔았습니다!")
        elif index == -1:
            return
        else:
            print("가능하신 선택이 아닙니다!")
    else:
        print("가능하신 선택이 아닙니다!")

def fish():
    global gold
    print("\n낚시를 시작하셨습니다...")
    time.sleep(3)  # Simulate waiting for a few seconds
    print("3")
    time.sleep(3)  # Simulate waiting for a few seconds
    print("2")
    time.sleep(3)  # Simulate waiting for a few seconds
    print("1")
    time.sleep(3)  # Simulate waiting for a few seconds
    print("잡았다!")
    fish_result = random.choice([0, 5, 10, 15])
    
    if fish_result == 0:
        print("앗... 물고기가 미끼만 물고 가버렸다.")
    else:
        gold += fish_result
        print("당신은", fish_result, "골드 가치의 물고기를 잡으셨습니다!")
    
    return

def fight_monster():
    global player_health, gold, strong_monster_defeated, player_damage
    print("\n싸우실 몬스터를 골라주세요:")
    print("0. 나가기")
    print("1. 일반 몬스터")
    print("2. 엘리트 몬스터")
    if strong_monster_defeated:
        print("3. 마왕")
    choice = input("옵션 중 선택해주세요: ")

    if choice == "1":
        monster_health = random.randint(50, 100)
        monster_damage = random.randint(5, 15)
        print("\n일반 몬스터가 나타났습니다!")
    elif choice == "2":
        monster_health = random.randint(100, 200)
        monster_damage = random.randint(10, 30)
        print("\n엘리트 몬스터가 당신을 공격합니다!")
    elif choice == "3" and strong_monster_defeated:
        monster_health = random.randint(200, 400)
        monster_damage = random.randint(20, 60)
        print("\n마왕이 강림했습니다! 조심하세요...!")
    elif choice == "0":
        return
    else:
        print("가능하신 선택이 아닙니다!")
        return

    while True:
        print("\n당신은 전투 상황에 들어왔습니다:")
        print("q. 공격")
        print("w. 도망")
        choiceA = input("옵션 중 선택해주세요: ")

        if choiceA == "q":
            base_damage = random.randint(10, 20)
            num_swords = inventory.count("검")
            player_damage_g = base_damage + 10 * num_swords
            monster_health -= player_damage_g
            player_health -= monster_damage
            print("몬스터에게", player_damage_g, "데미지!")
            print("당신에게", monster_damage, "데미지!")
            print("현재 당신의 체력은:", player_health)
            print("현재 몬스터의 체력은:", monster_health)

            if monster_health <= 0:
                print("\n몬스터를 성공적으로 무찌르셨습니다!")
                if player_health <= 0:
                    print("\n그러나 안타깝게도 몬스터또한 동귀어진을 감행했습니다...")
                    print("누구도 끝까지 싸운 당신의 희생을 잊지 않을 겁니다. 플레이해주셔서 감사합니다.")
                    sys.exit()
                elif choice == "2":
                    earned_gold = random.randint(40, 100)
                    gold += earned_gold
                    print("당신은", earned_gold, "골드를 획득하셨습니다!")
                    if not strong_monster_defeated:
                        strong_monster_defeated = True
                        print("마왕에게로 가는 길이 열렸습니다!!")
                elif choice == "1":
                    earned_gold = random.randint(20, 50)
                    gold += earned_gold
                    print("당신은", earned_gold, "골드를 획득하셨습니다!")
                elif choice == "3":
                    print("축하합니다! 악한 마왕을 무찌르고 당신은 세상을 구하셨습니다!")
                    print("감사합니다, 용사님! 플레이해주셔서 감사합니다.")
                    sys.exit()
                break
            elif player_health <= 0:
                print("\n당신은 몬스터에게 죽었습니다...")
                print("당신은 멋진 영웅이었습니다. 플레이해주셔서 감사합니다.")
                sys.exit()
        elif choiceA == "w":
            if random.random() < 0.2:
                print("\n몬스터가 당신의 발목을 붙잡았습니다!")
                monster_damage = random.randint(10, 20)
                player_health -= monster_damage
                print("이런! 몬스터는 도망가던 당신에게", monster_damage, "데미지!")
                print("현재 당신의 체력은:", player_health)
                print("현제 몬스터의 체력은:", monster_health)
                if player_health <= 0:
                    print("\n당신은 몬스터에게 찢겨져버렸습니다...")
                    print("당신은 쓸쓸하게 죽어갔습니다... 플레이해주셔서 감사합니다")
                    sys.exit()
            else:
                print("\n당신은 성공적으로 도망쳤습니다!")
                break
        else:
            print("가능하신 선택이 아닙니다!")

def temple_option():
    global player_health, gold
    print("\n템플에 들어오셨습니다.")
    print("사제가 20골드에 완전한 회복을 권합니다.")
    choice = input("쉬고 가시겠습니까? (예/아니요): ")

    if choice.lower() == "예":
        if gold >= 20:
            gold -= 20
            if "방패" in inventory:
                num_shields = inventory.count("방패")
                max_health = 100 + 20 * num_shields
                if player_health == max_health:
                    print("\n당신의 체력은 이미 가득 차 있습니다.")
                    print("용사님, 여기는 사우나가 아닙니다...")
                else:
                    player_health = max_health
                    print("\n당신의 체력이", max_health, "(으)로 온전히 회복되었습니다.")
            else:
                if player_health == 100:
                    print("\n당신의 체력은 이미 가득 차 있습니다.")
                    print("용사님, 꾀병부리지 마시고 그냥 돌아가셔도 됩니다.")
                else:
                    player_health = 100
                    print("\n당신의 체력이 100으로 온전히 회복되었습니다.")
        else:
            print("\n죄송합니다, 용사님... 우리도 자선사업은 아니라서...")
    elif choice.lower() == "아니요":
        return
    else:
        print("\n가능하신 선택이 아닙니다!")

def state_check():
    global player_health, player_damage
    print("\n상태 확인:")
    print("체력:", player_health)
    print("공격력:", player_damage, "-", player_damage + 10)

def play_game():
    global fishing_rod
    print("\n플레이어님, 게임에 접속하신 걸 환영합니다!")
    print("이곳은 미노 대륙... 당신의 모험이 시작되는 곳입니다.")
    print("마왕을 무찌르기 위해 일어나세요, 용사여!")
    
    while True:
        print("\n무엇을 하시겠습니까?")
        print("1. 상점")
        print("2. 인벤토리")
        print("3. 상태 확인")
        print("4. 전투")
        print("5. 템플")
        if fishing_rod:
            print("6. 낚시")
        print("e. 게임 종료")
        choice = input("옵션 중 선택해주세요: ")
        
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
            confirm_quit = input("\n정말로 게임을 종료하시겠습니까? (예/아니요): ")
            if confirm_quit.lower() == "예":
                print("\n플레이 해주셔서 감사합니다! 즐거운 모험이었습니다.")
                sys.exit()
            elif confirm_quit.lower() == "아니요":
                continue
            else:
                print("가능하신 선택이 아닙니다!")
        else:
            print("가능하신 선택이 아닙니다!")

play_game()