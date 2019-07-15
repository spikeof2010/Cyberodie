import random

def card_gen():
    card_type = open("./card_gen/card_type.txt").read().splitlines()
    colors = open("./card_gen/colors.txt").read().splitlines()
    #cost = open("./card_gen/cost.txt").read().splitlines()
    rarity = open("./card_gen/rarity.txt").read().splitlines()
    creature_type = open("./card_gen/creature_type.txt").read().splitlines()
    creature_class = open("./card_gen/creature_type.txt").read().splitlines()
    bonus_creature_type = ["Enchantment", "Artifact"]
    chosen_card_type = random.choice(card_type)
    if chosen_card_type == "Land":
        titlestyle = ["Design a {} {} {}"]
    elif chosen_card_type == "Creature":
        creature_complete_type = ["{}", "{} {}"]
        if random.randint(1,2) == 1:
            creature_type_output = random.choice(creature_complete_type).format(random.choice(creature_type),random.choice(creature_class))
        else:
            creature_type_output = random.choice(creature_complete_type).format(random.choice(creature_type),random.choice(creature_type))
        titlestyle = ["Design a {} {} {} -- {} with a CMC of {}"]
    else:
        titlestyle = ["Design a {} {} {} with a CMC of {}", "Design a {} {} {} with a CMC of {}"]
    #print(str(improved_qual))



    if chosen_card_type == "Creature":
        cardOutput = random.choice(titlestyle).format(random.choice(rarity),random.choice(colors),chosen_card_type,creature_type_output,random.randint(0,10))
    else:
        cardOutput = random.choice(titlestyle).format(random.choice(rarity),random.choice(colors),chosen_card_type,random.randint(0,10))

    return cardOutput

print(card_gen())
print(card_gen())
print(card_gen())
print(card_gen())
print(card_gen())