import datetime
import random
import re
import json

import discord
from discord.ext import commands

import birdfunctions


config = json.load(open("config.json"))

bot = commands.Bot(command_prefix=config['prefix'])

@bot.event
async def on_ready():
    print('Starting bot')
    print(bot.user.name + " Online")
    print(bot.user.id)
    print('------------------')
    await bot.change_presence(activity=discord.Game('tests'))

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    await bot.process_commands(message)  

    if message.author.id == config['ownerId']:
        if message.content.lower().startswith("/echo"):
            await message.delete()
    

    channel = message.channel

    if message.content.lower().startswith("chirp"):
        await channel.send("coocoo")
    if message.content.lower().startswith("hoot"):
        await channel.send( "who?")
    if message.content.lower().startswith("caw"):
        await channel.send( "caw")
    if message.content.lower().startswith("cheep"):
        await channel.send( "tweet tweet")
    if message.content.lower().startswith("cluck"):
        await channel.send( "cock-a-doodle-doo")
    if message.content.lower().startswith("good bot"):
        await channel.send( "<3")
    if message.content.lower().startswith("oh yeah yeah"):
        await channel.send( "oh yeah yeah yeah yeah")
    if message.content.lower().startswith("show me the pidove") or message.content.lower().startswith("show me pidove") or message.content.lower().startswith("show me the bird"):
        await channel.send( "<:pidove:277147728071360513>")
    if message.content.lower().startswith("show me the grookey") or message.content.lower().startswith("show me grookey") or message.content.lower().startswith("who is the best gen 8 starter?"):
        await channel.send( "<:grook:550434809038766090>")           
    
        

#CORE
@bot.command()
async def ping(ctx):  
    await ctx.message.channel.send("Pong")

@bot.command()
async def trueecho(ctx, *args):  
    await ctx.message.delete()
    await ctx.message.channel.send(' '.join(args))

@bot.command()
async def echo(ctx, *args):  
    await ctx.message.channel.send(' '.join(args))

@bot.command()
async def version(ctx): 
    await ctx.message.channel.send("Chirptown")

@bot.command()
async def patreon(ctx): 
    await ctx.message.channel.send("Donate to my patreon!\n <http://tinyurl.com/berdpatreon>")

#pyramid command
@bot.command()
async def pyramid(ctx, *args): 
    args = " ".join(args)
    pyr_chars = list(args)
    pyr_c = 0
    pyr = [""]
    while pyr_c<len(pyr_chars):
        pyr.append("".join(pyr_chars))
        pyr_chars.remove(pyr_chars[0])
    pyr = "```{}```".format("\n".join(pyr))
    await ctx.message.channel.send(pyr)

#help commands
@bot.command()
async def commands(ctx): 
    await ctx.message.channel.send("""```
    o===Commands===o
    \/\/\/\/\/\/\/\/
    ''''''''''''''''
    commands - Displays this message
    battle @user - Battles a user
    birdfact - Displays a bird fact
    loot - generates some loot
    face - generates a random ascii face
    ................
    /\/\/\/\/\/\/\/\\
    o==============o```""")
    
@bot.command(pass_context=True)
async def playing(ctx, *args): 
    args = ' '.join(args)
    if(ctx.author.id != config['ownerId']):
        return
    try:
         await bot.change_presence(activity=discord.Game(args))
         await ctx.message.channel.send("Now playing " + args)
         print("Status changed to {}".format(args))
    except:
         author = "__**" + str(ctx.message.author) + "**__: "
         await ctx.message.channel.send("Sorry {}, couldn't change my status to '{}'".format(author, args))

@bot.command(pass_context=True)
async def birdfact(ctx, *args): 
    bird_file="./bird/bird_facts.txt"
    lines = open(bird_file, encoding="utf8").read().splitlines()
    fact = random.choice(lines)
    await ctx.message.channel.send(fact)

@bot.command(pass_context=True)
async def cardprompt(ctx, *args): 
    cardprompt = birdfunctions.card_gen()
    await ctx.message.channel.send(cardprompt)

@bot.command()
async def battle(ctx,*arx):
    userlist = []
    message = ctx.message
    ment = message.mentions
    if ment == []:
        await message.channel.send("You need to ping someone to battle them.")
        return
    userlist.append(ment[0].id)
    userlist.append(message.author.id)
    epitaph = open("./situ/epitaph.txt").read().splitlines()
    selected_user = random.choice(userlist)
    userlist.remove(selected_user)
    selected_user = bot.get_user(selected_user)
    remaining_user = userlist[0]
    remaining_user = bot.get_user(remaining_user)
    situation = open("./situ/fight.txt").read().splitlines()
    option = random.choice(situation)
    option = option.split("&")
    option = "**" + str(selected_user) + "**" + option[1] + "**" + str(remaining_user) + "**" + option[2]
    userlist.clear()
    await message.channel.send( option + "\n" + random.choice(epitaph) )

@bot.command(pass_context=True)
async def ball(ctx, *args): 
    bird_file="./8b/8b.txt"
    lines = open(bird_file, encoding="utf8").read().splitlines()
    fact = "**{}**".format(random.choice(lines))
    await ctx.message.channel.send(fact)

@bot.command(pass_context=True)
async def face(ctx, *args):
    face = []
    hair = open("./face_gen/hair.txt").read().splitlines()
    eyes = open("./face_gen/eyes.txt").read().splitlines()
    nose = open("./face_gen/nose.txt").read().splitlines()
    mouth = open("./face_gen/mouth.txt").read().splitlines()
    chin = open("./face_gen/chin.txt").read().splitlines()
    beard = open("./face_gen/beard.txt").read().splitlines()
    dialog = open("./face_gen/dialog.txt").read().splitlines()
    name1 = open("./face_gen/name1.txt").read().splitlines()
    name2 = open("./face_gen/name2.txt").read().splitlines()
    face.append("\n" + random.choice(hair))
    if random.randint(1,100) < 15:
        face.append("|     |")
        if random.randint(1,100) < 15:
            face.append("|     |")
    face.append(random.choice(eyes) + "    (" + random.choice(dialog) + ")")
    face.append(random.choice(nose) + "   /")
    face.append(random.choice(mouth) + " .'")
    if random.randint(1,100) < 15:
        face.append("|     |")
    face.append(random.choice(chin))
    if random.randint(1,100) < 25:
        face.append(random.choice(beard))
    face.append("\n{Now presenting " + random.choice(name1) + random.choice(name2) + "!}")
    face = "```{}```".format("\n".join(face))
    await ctx.message.channel.send(face)

@bot.command(pass_context=True)
async def jahcoin(ctx, *args): 
    jah = "You currently have {} jahdollars, which is roughly equal to {} USD. <:XXX:539162270568284160>".format(float(random.randint(2,999)), float(random.randint(2,999)/random.uniform(0.5,10)))
    await ctx.message.channel.send(jah)

@bot.command(pass_context=True)
async def jahrate(ctx, *args): 
    jah = "1 Jahdollar is equal to {} USD. <:XXX:539162270568284160>".format(1/(random.uniform(0.1,10)))
    await ctx.message.channel.send(jah)

@bot.command(pass_context=True)
async def loot(ctx, *args): 
    #initial values for loot and attributes
    output = birdfunctions.loot_gen()
    attr_output = birdfunctions.attr_gen()
    fug_loot = []
    #determines the number of loot to generate
    loot_num = random.randint(1,4)
    #start of print code
    fug_loot.append("\n\n\nYou got some sick loot! What's inside?")
    size= len(output) + 7
    sword_border ="o" + "===}}|{}>>-\n".format("=" *size)
    fug_loot.append(sword_border)
    #loop for starting the loot generation
    for i in range(loot_num):
        fug_loot.append("   *" + output + "*")
        output = birdfunctions.loot_gen()
        attr_num = random.randint(1,3)
        #loop for starting the attribute generation
        for i in range(attr_num):
            fug_loot.append(" >-" + attr_output)
            attr_output = birdfunctions.attr_gen()
        attr_output = birdfunctions.attr_gen()
    fug_loot.append("\n" + sword_border)
    fug_loot = "\n".join(fug_loot)
    fug_loot = "```\n{}```".format(fug_loot)
    await ctx.message.channel.send(fug_loot)


#CORE

#write here

bot.run(config['token'])
