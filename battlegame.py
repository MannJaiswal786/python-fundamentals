wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True: 
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")
    character = input("Choose your Character: ")
    if character == wizard:
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("You have choosen the character: Wizard")
        print("Health: ",my_hp)
        print("Damage: ",my_damage)
        break
    if character == elf:
        my_hp = elf_hp
        my_damage = elf_damage
        print("You have choosen the character: Elf")
        print("Health: ",my_hp)
        print("Damage: ",my_damage)
        break
    if character == human:
        my_hp = human_hp
        my_damage = human_damage
        print("You have choosen the character: Human")
        print("Health: " , my_hp)
        print("Damage: " , my_damage)
        break
    else:
        print("Unknown Character")

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's HP is now: " , dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at", character)
    print("The", character, "HP is now", my_hp)

    if my_hp <= 0:
        print("The ", character, "has lost the battle")
        break



