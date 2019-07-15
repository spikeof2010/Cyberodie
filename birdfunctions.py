import random

def loot_gen():
    adj = open("./loot_gen/adj.txt").read().splitlines()
    noun = open("./loot_gen/noun.txt").read().splitlines()
    qual = open("./loot_gen/qual.txt").read().splitlines()
    rarity = open("./loot_gen/rarity.txt").read().splitlines()
    titlestyle = ["{} {} of {}: LEVEL {}", "{} {} of the {}: LEVEL {}"]
    #print(str(improved_qual))
    
    if random.randint(1,100)<25:
        improved_qual = random.choice(adj) + " " + random.choice(qual)
        lootOutput = random.choice(titlestyle).format(random.choice(adj),random.choice(noun),improved_qual,random.randint(1,100))
        print(str(lootOutput))
    else:
        lootOutput = random.choice(titlestyle).format(random.choice(adj),random.choice(noun),random.choice(qual),random.randint(1,100))

    #25% to append rarity
    if random.randint(1,100)<25:
        lootOutput = random.choice(rarity) + " " + lootOutput
    return lootOutput

def attr_gen():
    attributes = open("./loot_gen/stats.txt").read().splitlines()
    attr_text = open("./loot_gen/attr.txt").read().splitlines()
    pos_or_neg = ["+", "-"]
    if random.randint(1,100)<25:
        attr_am = random.randint(1,5)*random.randint(2,5)
    else:
        attr_am = random.randint(1,5)
    if random.randint(1,5) == 1:
        attrOutput = random.choice(attr_text)
    else:
        attrOutput = "Provides {}{} to {}".format(random.choice(pos_or_neg),attr_am,random.choice(attributes))
    return attrOutput

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