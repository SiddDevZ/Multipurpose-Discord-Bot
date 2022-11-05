token = "your bot token here"


"""


Sparty Discord Bot

Made with ❤️ by Sidd#2248


"""

import os

try:
    import discord
    from discord.commands import SlashCommandGroup
    from discord import Intents
    from discord.ext import commands, tasks
    from discord.commands import Option
    from discord.ui import Select, View, Button
except:
    os.system("pip3 install py-cord")
    import discord
    from discord.commands import SlashCommandGroup
    from discord import Intents
    from discord.ext import commands, tasks
    from discord.commands import Option
    from discord.ui import Select, View, Button
try:
    import wavelink
except:
    os.system("pip3 install wavelink")
    import wavelink
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests
import json
import random
import time
try:
    import aiohttp
except:
    os.system('pip install aiohttp')
    import aiohttp
try:
    import datetime
    from datetime import timedelta
except:
    os.system("pip3 install datetime")
    from datetime import timedelta
try:
    from colorama import Fore
except:
    os.system("pip3 install colorama")
    from colorama import Fore
try:
    import io
except:
    os.system("pip3 install io")
    import io
try:
    import cpuinfo
except:
    os.system("pip3 install py-cpuinfo==5.0.0")
    import cpuinfo
try:
    import humanfriendly
except:
    os.system("pip3 install humanfriendly")
    import humanfriendly
try:
    import psutil
except:
    os.system("pip install psutil")
    import psutil
try:
    import asyncio
except:
    os.system("pip install asyncio")
    import asyncio
try:
    import aiosqlite
except:
    os.system("pip install aiosqlite")
    import aiosqlite

print(Fore.GREEN + 'Module import success!')
truth_a = ["When was the last time you told a lie?",
"What is your biggest fear?",
"What is your guilty pleasure?",
"Who do you have a crush on?",
"If you had to date someone in this room who would it be?",
"Have you ever been cheated on someone?",
"Have you ever been cheated on?",
"What is the meanest thing that you have done?",
"What was your first kiss like?",
"Who is the last person that you stalked on social media?",
"What is the craziest event that you have ever been to?",
"When was the last time you peed yourself?",
"What is the worst dream that you have had?",
"Why did your last relationship end?",
"What is the most embarrassing thing that has happened to you this year?",
"What habit can't you seem to quit?",
"Who is your celebrity crush?",
"What is your least favorite thing about your best friend?",
"What don't you like about your boyfriend or girlfriend?",
"Have you ever hooked up with the same sex?",
"What is a secret that you have never told anyone before?",
"How many people have you kissed?",
"How many people have you been with?",
"Has anyone ever accidentally seen you naked? Who?",
"Have you ever gone out without wearing a bra and underwear?",
"Who is your crush in this server?",
"Who was your first love?"
"Would you stop talking to all of your friends for a million dollars?",
"Have you ever committed a crime? If so what was it?",
"Have you ever been to jail?",
"Who was your first crush?",
"Would you ever cheat on your significant other if they said it was okay?",
"Would you ever be polygamous?",
"Have you ever had a crush on your teacher/professor?",
"Have you ever had a crush on your best friend's mom or someone generally much older that you?",
"If you were the opposite gender for the day? What do you think you would wear? What would you do?",
"What is the most embarrassing music that you like to listen to?",
"If you and one person in this room could be the last people on Earth left alive who would that person be?",
"Would you ever donate an organ to someone in this room?",
"Who in this room do you think would be the worst date?",
"If you were a superhero what would your power be?",
"Have you ever performed a striptease for anyone before?",
"Have you ever eaten food from the floor?",
"Have you ever cheated on an exam?",
"Have you ever been suspended from school?",
"What is the most trouble that you ever got into in school?",
"What is the most trouble that you ever got into at home / with your parents?",
"When was a time that someone really betrayed your trust?",
"Talk about a time that you failed in life.",
"Tell us about a time that you were really drunk.",
"Have you ever spread a rumor?",
"Have you ever been intimate in a public place?",
"What is something you used to do that makes you cringe now?",
"Do you sing in the shower?",
"When is the last time you threw up?",
"When is the last time you cried?",
"Have you ever laughed so hard that you cried?",
"Have you ever cried from watching a TV show or a movie?",
"What is the most embarrassing thing that you have ever done in front of a crush?",
"What do you look for in a potential love interest?",
"Would you rather be rich or famous? You cannot be both.",
"What would you do with a million dollars?",
"Could you survive without any phone or internet for a month?",
"What is the most that you have ever had to drink?",
"What is the longest amount of time that you have ever been awake?",
"If you could do it what would you change your name to?",
"Name a famous person that you would like to be friends with.",
"Who are 5 famous people that you would like to have dinner with? They can either be dead or alive.",
"What is your biggest pet peeve?",
"When was the worst time that you threw up?",
"If you could only save one person in this room from a fire who would it be?",
"Who is the most attractive person in the room?",
"Who is the most annoying person in the room?",
"Which person in the room do you think gossips the most?",
"What is your biggest insecurity?",
"What is the most expensive thing you bought that wasn't a house or a car?",
"What is a common misconception about you?",
"What is something that you would do that people would assume you would never do?",
"Where is the weirdest place that you have gone to the bathroom?",
"What is the most embarrassing thing that your parents have caught you doing?",
"When was the most embarrassing time that you passed gas?",
"What was the most disgusting thing to ever come out of your body?",
"What is the most disgusting thing that you have ever had in your mouth?",
"How old do you think you will live to be?",
"What do you want to do when you are retired?",
"If you could live anywhere in the world where would it be?"]
# dares

dare_a = ["Do a free-style rap for the next minute.",
"Let another person post a status on your behalf.",
"Hand over your phone to another player who can send a single text saying anything they want to anyone they want.",
"Let the other players go through your phone for one minute.",
"Smell another player's armpit.",
"Smell another player's bare foot.",
"Eat a bite of a banana peel.",
"Do an impression of another player until someone can figure out who it is.",
"Say pickles at the end of every sentence you say until it's your turn again.",
"Imitate a YouTube star until another player guesses who you're portraying.",
"Act like a chicken until your next turn.",
"Talk in a British accent until your next turn.",
"Call a friend, pretend it's their birthday, and sing them Happy Birthday to You.",
"Name a famous person that looks like each player in the room.",
"Show us your best dance moves.",
"Eat a packet of hot sauce straight.",
"Let another person draw a tattoo on your back with a permanent marker.",
"Put on a blindfold and touch the other players' faces until you can figure out who's who.",
"Serenade the person to your right for a full minute.",
"Do 20 squats.",
"Let the other players redo your hairstyle.",
"Gulp down a raw egg.",
"Dump out your purse, backpack, or pockets and do a show and tell of what's inside.",
"Let the player to your right redo your makeup.",
"Do a prank call on one of your family members.",
"Let another player create a hat out of toilet paper  and youve got to wear it for the rest of the game.",
"Do a plank for a full minute.",
"Let someone give you a wedgie."]

prefix = "/"
icon = "https://cdn.discordapp.com/attachments/906982723128791150/997792716081598494/images_43-01.jpeg"
name = 'Sparty'
api_error = 'Api error!'
no_emoji = '<a:no_sidd:979072393685401611>'
yes_emoji = '<a:yes_sidd:979072441362038814>'
#foot = f'Command executed by {ctx.author.name} | https://sparty.dev'

intents = Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)
bot = discord.Bot()

"""@client.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title=f'**Relax babe**, try again in {error.retry_after:.2f}s. <a:no_sidd:979072393685401611>', colour=discord.Colour.red())
        await ctx.respond(embed=embed)
    else:
        raise error"""
@client.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        hmm = [f'You dont have all the required permissions! {no_emoji}', 'Your missing some permissions to use that command!', f'Sorry {ctx.author.name}, but you are missing some permissions which was required for this command. {no_emoji}']
        hmm1 = random.choice(hmm)
        mis_embed = discord.Embed(title=hmm1, colour=discord.Colour.red())
        await ctx.respond(embed=mis_embed, ephemeral=True)
    elif isinstance(error, commands.CommandOnCooldown):
        errors = [f'**Relax babe**, try again in {error.retry_after:.2f}s. {no_emoji}', f'You need to wait {error.retry_after:.2f} seconds before running the command again!', f'Hey, you need to wait {error.retry_after:.2f} more seconds to use that command! {no_emoji}']
        error = random.choice(errors)
        embed = discord.Embed(title=error, colour=discord.Colour.red())
        await ctx.respond(embed=embed, ephemeral=True)
    elif isinstance(error, discord.ext.commands.errors.BadArgument):
        em = discord.Embed(title=f'{no_emoji} I cannot find anything with that please try again with something else.', colour=discord.Colour.red())
        await ctx.respond(embed=em)
    elif isinstance(error, discord.errors.ApplicationCommandInvokeError):
        em = discord.Embed(title=f'{no_emoji} you cant do that.', colour=discord.Colour.red())
        await ctx.respond(embed=em)
    elif isinstance(error, requests.exceptions.ConnectionError):
        #errors = [f'**Relax babe**, try again in {error.retry_after:.2f}s. {no_emoji}', f'You need to wait {error.retry_after:.2f} seconds before running the command again!', f'Hey, you need to wait {error.retry_after:.2f} more seconds to use that command! {no_emoji}']
        #error = random.choice(errors)
        embed = discord.Embed(title='error', colour=discord.Colour.red())
        await ctx.respond(embed=embed, ephemeral=True)
        #requests.exceptions.ConnectionError
    else:
        raise error


"""@tasks.loop(seconds=10) 
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help | https://sparty.dev"))
    time.sleep(7.5)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.users)} members in {len(client.guilds)} servers"))"""

@client.event
async def on_ready():
    #change_status.start()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help | https://sparty.dev"))
    print(f'Bot is Online, logged in as {client.user}' + Fore.RED + '.')
    client.db = await aiosqlite.connect('warns.db')
    await asyncio.sleep(3)
    async with client.db.cursor() as cursor:
        await cursor.execute("CREATE TABLE IF NOT EXISTS warns(user INTEGER, reason TEXT, time INTEGER, guild INTEGER)")
    await client.db.commit()
    client.loop.create_task(node_connect())



@client.slash_command(name='ban', description='bans an user')
@commands.has_permissions(ban_members = True)
@commands.cooldown(1,2,commands.BucketType.user)
async def ban(ctx, member:Option(discord.Member,
    'enter the user who u want to ban!',
    required=True
), reason:Option(str,
    'reason for banning the selected user',
    required=False,
    default=None)):
    await member.ban(reason = reason)
    embed = discord.Embed(title=f'{member} has been banned from this guild with the reason: {reason}! <a:yes_sidd:979072441362038814>', colour=discord.Colour.blue())
    embed.set_footer(text=f'command executed by {ctx.author.name}')
    embed.set_author(name=name, icon_url=icon)
    await ctx.respond(embed=embed)

@client.slash_command(name='slowmode', description='sets slowmode.')
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, time:Option(int, 'time (in seconds)', required=True)):
    try:
        await ctx.channel.edit(reason='Bot Slowmode Command', slowmode_delay=int(time))
        embed = discord.Embed(title=f'Slowmode set to {time}s <a:yes_sidd:979072441362038814>', colour=discord.Colour.blue())
        await ctx.respond(embed=embed)
    except discord.Errors.Forbidden:
        await ctx.respond('I do not have the permission to do this, please try again')

@client.slash_command(name='kick', description='kicks the selected user!')
@commands.has_permissions(kick_members=True)
async def kick(ctx, user:Option(discord.Member, 'who do u want to kick?', required=True), reason:Option(str, 'reason for banning the selected user!', required=False)):
    await user.kick(reason=reason)
    embed = discord.Embed(title=f'{user.name} has been kicked from this guild with the reason: {reason}! <a:yes_sidd:979072441362038814>', colour=discord.Colour.blue())
    embed.set_footer(text=f'command executed by {ctx.author.name}')
    embed.set_author(name=name, icon_url=icon)
    await ctx.respond(embed=embed)

@client.slash_command(
    name='meme',
    description='shows an random meme'
)
@commands.cooldown(1,7,commands.BucketType.user)
async def meme(ctx):
    try:
        response = requests.get('https://meme-api.herokuapp.com/gimme')
        print(response)
        jsondata = response.json()
        title = jsondata['title']
        ups = jsondata['ups']

        embed = discord.Embed(title = f"{title}")
        embed.set_image(url = jsondata['preview'][2])
        embed.set_footer(text=f'👍: {ups} | https://sparty.dev')
        await ctx.respond(embed=embed)
    except Exception:
        await ctx.respond(api_error)
@client.slash_command(
    name='quote',
    description='gives an inspirational quote.'
)
@commands.cooldown(1,4,commands.BucketType.user)
async def quote(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    jsonsdata = response.json()
    quote = jsonsdata[0]['q'] + " -" + jsonsdata[0]['a']
    embed = discord.Embed(
        description = f'{quote}',
        colour = discord.Colour.blue()
    )
    embed.set_author(name=name,icon_url=icon)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    embed.set_thumbnail(url=ctx.author.avatar)
    await ctx.respond(embed=embed)

@client.slash_command(
    name='covid_all',
    description='Get global covid-19 statistics!'
)
@commands.cooldown(1,8,commands.BucketType.user)
async def covid(ctx):
    req = requests.get('https://disease.sh/v3/covid-19/all')
    json = req.json()
    cases = json['cases']
    deaths = json['deaths']
    recovered = json['recovered']
    active = json['active']
    critical = json['critical']
    today_cases = json['todayCases']
    today_deaths = json['todayDeaths']
    deaths_million = json['deathsPerOneMillion']
    embed = discord.Embed(
        title='COVID-19 Statistics for Global',
        description=f'**Cases**\n{cases}\n**Deaths**\n{deaths}\n**Recovered**\n{recovered}\n**Active**\n{active}\n**Critical**\n{critical}\n**Cases Today**\n{today_cases}\n**Deaths Today**\n{today_deaths}\n**Deaths Per Million**\n{deaths_million}\n\n**Help Stop Coronavirus**\n[Advice for public](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public)')
    embed.set_thumbnail(url='https://imgs.search.brave.com/3STJGMclQatXk8QLq1V-A5pOaP6Rf2oUaXCjqCItM-I/rs:fit:552:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5G/NXFuNDFSV2RjUTY0/U2tKNjg4VlJ3SGFH/WCZwaWQ9QXBp')
    embed.set_footer(text='stay safe!')

    await ctx.respond(embed=embed)
@client.slash_command(
    name='mcserver',
    description='shows stats'
)
@commands.cooldown(1,4,commands.BucketType.user)
async def mcserver(ctx, serverip:Option(str,
    'gets stats for a minecraft server!',
    required=True)):
    req = requests.get(f'https://api.mcsrvstat.us/2/{serverip}')
    jsondata = req.json()
    try:
        issrvronline = jsondata['online']
        online = jsondata['players']['online']
        max = jsondata['players']['max']
        version = jsondata['version']
        #icon = jsondata['icon']
        embed = discord.Embed(
            title = f'**Minecraft Server info for, {serverip}**',
            description = f'online: {issrvronline}\nversion: {version}\n**Players**\nonline: {online}\nmax: {max}',
            colour = discord.Colour.blue()
        )
        embed.set_author(name=name,icon_url=icon)
        embed.set_footer(text=f'command executed by {ctx.author.name} | https://sparty.dev')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/977226293798121522/978948285349912675/Capture.PNG')
        await ctx.respond(embed=embed)
    except:
        em = discord.Embed(title=f'Your minecraft server **{serverip}** seems to be offline maybe try rechecking your spelling or wait for it to start {no_emoji}',colour=discord.Colour.blue())
        em.set_footer(text=f'command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=em)
@client.slash_command(
    name='purge',
    description='purge many messages in just one click'
)
@commands.cooldown(1,3,commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit:Option(int,
    'purge many messages in just one click',
    required=True
)):
    #limit: int
#    await ctx.message.delete()
    await ctx.channel.purge(limit=limit)
    embed = discord.Embed(
        title = 'purge',
        description = f'<a:yes_sidd:979072441362038814> purged/deleted {limit} messages successfully.',
        colour = discord.Colour.blue()
    )
    embed.set_author(name=name,icon_url=icon)
    embed.set_thumbnail(url=ctx.author.avatar)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

client.remove_command("help")

@client.slash_command(
    name='hypixel',
    description='gets stats for hypixel!'
)
@commands.cooldown(1,4,commands.BucketType.user)
async def hypixel(ctx, name:Option(str,
    'gets stats for hypixel lobby!',
    required=True
)):
    try:
        req = requests.get('https://api.slothpixel.me/api/players/' + name)
        try:
            json = req.json()
            user = json['username']
            online = json['online']
            rank = json['rank']
            level = json['level']
            games = json['total_games_played']
            kills = json['total_kills']
            wins = json['total_wins']

            embed = discord.Embed(
            title = f"{user}'s hypixel stats",
            description = f"**Total stats**\nTotal wins: {wins}\nTotal kills: {kills}\nTotal games: {games}\n\n**Online**\n{online}\n**Rank**\n{rank}\n**Level**\n{level}",
            colour = discord.Colour.blue()
            )
            embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
            embed.set_author(name=name,icon_url=icon)
            embed.set_thumbnail(url='https://imgs.search.brave.com/pcLD_-eN09Q75-APFZFu_m8BBE1T8NmNpjxxIYh29Ag/rs:fit:900:900:1/g:ce/aHR0cHM6Ly92aWdu/ZXR0ZS53aWtpYS5u/b2Nvb2tpZS5uZXQv/eW91dHViZS9pbWFn/ZXMvOS85MC9IeXBp/eGVsLmpwZy9yZXZp/c2lvbi9sYXRlc3Q_/Y2I9MjAxODA3MDgw/MTQ1MTY')
            await ctx.respond(embed=embed)
        except:
            await ctx.respond(f'the username {name} does not exist')
    except:
        await ctx.respond('api is down probably')

@client.slash_command(
    name='fact',
    description='gets an random fact!'
)
@commands.cooldown(1,4,commands.BucketType.user)
async def fact(ctx):
    limit = str('1')
    req = requests.get('https://api.api-ninjas.com/v1/facts?limit={}'.format(limit), headers={'X-Api-Key': 'r9Mr3NWAa0MoTcUsh76ajw==E5Pki5FACJq8hOLC'})
    json = req.json()
    fact = json[0]['fact']
    embed = discord.Embed(
        title = 'Fact',
        description = f'{fact}.',
        colour = discord.Colour.blue()
    )
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    embed.set_author(name=name,icon_url=icon)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/977226293798121522/978919451456065566/Capture.PNG')
    await ctx.respond(embed=embed)
@client.slash_command(
    name='bedwars',
    description='shows hypixel bedwars stats!'
)
@commands.cooldown(1,4,commands.BucketType.user)
async def bedwars(ctx, name:Option(str,
    'shows hypixel bedwars stats!',
    required=True
)):
    req = requests.get('https://api.slothpixel.me/api/players/' + name)
    json = req.json()
    coins = json['stats']['BedWars']['coins']
    bedlevel = json['stats']['BedWars']['level']
    wins = json['stats']['BedWars']['wins']
    losses = json['stats']['BedWars']['losses']
    games = json['stats']['BedWars']['games_played']
    kills = json['stats']['BedWars']['kills']
    deaths = json['stats']['BedWars']['deaths']
    beds = json['stats']['BedWars']['beds_broken']
    final_kill = json['stats']['BedWars']['final_kills']
    embed = discord.Embed(
    title = f"{name}'s bedwars stats",
    description = f'**Wins**\n{wins}\n**Losses**\n{losses}\n**Played Games**\n{games}\n**Kills**\n{kills}\n**Deaths**\n{deaths}\n**Beds Broken**\n{beds}\n**Bedwars Level**\n{bedlevel}\n**Final kills**\n{final_kill}\n**Coins**\n{coins}',
        colour = discord.Colour.blue()
    )
    embed.set_author(name=name,icon_url=icon)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    embed.set_thumbnail(url='https://imgs.search.brave.com/pcLD_-eN09Q75-APFZFu_m8BBE1T8NmNpjxxIYh29Ag/rs:fit:900:900:1/g:ce/aHR0cHM6Ly92aWdu/ZXR0ZS53aWtpYS5u/b2Nvb2tpZS5uZXQv/eW91dHViZS9pbWFn/ZXMvOS85MC9IeXBp/eGVsLmpwZy9yZXZp/c2lvbi9sYXRlc3Q_/Y2I9MjAxODA3MDgw/MTQ1MTY')
    await ctx.respond(embed=embed)

"""@client.slash_command(
    name='kitten',
    description='shows an random kitty!',
    guild_ids=[977226293345153075]
)
@commands.cooldown(1,5,commands.BucketType.user)
async def kitten(ctx):
    req = requests.get('https://api.thecatapi.com/v1/images/search')
    json = req.json()
    embed = discord.Embed(
        title = 'Random Kitty',
        colour = discord.Colour.blue()
    )
    embed.set_author(name=name,icon_url=icon)
    embed.set_image(url = json[0]['url'])
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)"""

"""@client.slash_command(
    name='doggo',
    description='shows an random doggo!',
    guild_ids=[977226293345153075]
)
@commands.cooldown(1,5,commands.BucketType.user)
async def doggo(ctx):
    req = requests.get('https://dog.ceo/api/breeds/image/random')
    json = req.json()
    embed = discord.Embed(
        title = 'Random Doggo',
        colour = discord.Colour.blue()
    )
    embed.set_author(name=name,icon_url=icon)
    embed.set_image(url = json['message'])
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

@client.slash_command(
    name='fox',
    description='shows an random fox!',
    guild_ids=[977226293345153075]
)
@commands.cooldown(1,5,commands.BucketType.user)
async def fox(ctx):
    req = requests.get('https://randomfox.ca/floof/?ref=apilist.fun')
    json = req.json()
    embed = discord.Embed(
        title = 'Random Fox',
        colour = discord.Colour.blue()
    )
    embed.set_author(name=name,icon_url=icon)
    embed.set_image(url = json['image'])
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)"""
@client.slash_command(
    name='yomomma',
    description='gives an random yomomma joke!'
)
@commands.cooldown(1,6,commands.BucketType.user)
async def yomomma(ctx, mention:Option(discord.Member,
    'gives an random yomomma joke!',
    required = True
)):
        req = requests.get('https://api.yomomma.info/')
        json = req.json()
        ymjoke = json['joke']
        embed = discord.Embed(
            description = f'{mention}, {ymjoke}',
            colour = discord.Colour.blue()
        )
        embed.set_author(name=name, icon_url=icon)
        embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=embed)
determine_flip = [1, 0]
@client.slash_command(
    name='coinflip',
    description="gives Tails or Heads it's random!"
)
@commands.cooldown(1,2,commands.BucketType.user)
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(
        title="Coinflip",
        description=f"{ctx.author.mention} Flipped coin, we got **Heads**!",
        colour = discord.Colour.blue()
        )
        embed.set_author(name=name, icon_url=icon)
        embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=embed)

    else:
        embed = discord.Embed(
        title="Coinflip",
            description=f"{ctx.author.mention} Flipped coin, we got **Tails**!",
            colour = discord.Colour.blue()
            )
        embed.set_author(name=name, icon_url=icon)
        embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=embed)
@client.slash_command(
    name='ping',
    description="used to check if the bot is alive"
)
@commands.cooldown(1,4,commands.BucketType.user)
async def ping(ctx):
    late = client.latency
    true_late = late * 1000
    embed = discord.Embed(
        description = f'It took me {round(true_late)} miliseconds to reply.',
        colour = discord.Colour.blue()
    )
    embed.set_author(name=name, icon_url=icon)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)
#    await ctx.send(f'it took me {round(true_late)} miliseconds to reply')
@client.slash_command(
    name='dadjoke',
    description='gives an random dadjoke!'
)
@commands.cooldown(1,5,commands.BucketType.user)
async def dadjoke(ctx):
    req = requests.get('https://icanhazdadjoke.com/slack')
    json = req.json()
    joke = json['attachments'][0]['fallback']
    embed = discord.Embed(
        title = 'random dadjoke',
        description = f'{joke}',
        colour = discord.Colour.blue()
    )
    embed.set_author(name=name, icon_url=icon)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')

    await ctx.respond(embed=embed)
@client.slash_command(
    name='fortune',
    description='shows your Fortune!'
)
@commands.cooldown(1,5,commands.BucketType.user)
async def fortune(ctx):
    req = requests.get('http://yerkee.com/api/fortune/all')
    json = req.json()
    fortune = json['fortune']
    embed = discord.Embed(
        title = 'Your fortune says....',
        description = f':fortune_cookie: {fortune}',
        colour = discord.Colour.blue()
    )
    embed.set_author(name=name, icon_url=icon)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)
@client.slash_command(
    name='truth',
    description='gives you an random truth to answer!'
)
@commands.cooldown(1,3,commands.BucketType.user)
async def truth(ctx):
    embed = discord.Embed(
        title = f'{random.choice(truth_a)}',
        colour = discord.Colour.blue()
    )
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    embed.set_author(name='Random Truth.', icon_url=icon)

    await ctx.respond(embed=embed)
@client.slash_command(
    name='dare',
    description='gives you an random dare to do!'
)
@commands.cooldown(3,10,commands.BucketType.user)
async def dare(ctx):
    embed = discord.Embed(
        title = f'{random.choice(dare_a)}',
        colour = discord.Colour.blue()
    )
    embed.set_footer(text='Tell us if u did it or no :)')
    embed.set_author(name='Random Dare.', icon_url=icon)

    await ctx.respond(embed=embed)
@client.slash_command(
    name='kiss',
    description='Kisses an selected user!'
)
@commands.cooldown(2,7,commands.BucketType.user)
async def kiss(ctx, user:Option(discord.Member,
    'User, who u want to kiss.',
    required=True)):

    kiss_gifs = ['http://i.imgur.com/W7arBvy.gif','http://i.imgur.com/p6hNamc.gif', 'http://i.imgur.com/kJEr7Vu.gif', 'http://i.imgur.com/PPw83Ug.gif', 'http://i.imgur.com/IsIR4V0.gif', 'http://i.imgur.com/LBWIJpu.gif']
    embed = discord.Embed(
        title=f'{ctx.author.name} kisses {user}',
        colour = discord.Colour.blue()
    )
    embed.set_image(url=random.choice(kiss_gifs))
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')

    await ctx.respond(embed=embed)
@client.slash_command(
    name='slap',
    description='Slaps an selected user.'
)
@commands.cooldown(2,8,commands.BucketType.user)
async def slap(ctx, user:Option(discord.Member,
    'User, who u want to slap',
    required=True)):
    slap_gifs = ['https://cdn.weeb.sh/images/SkSCyl5yz.gif','https://cdn.weeb.sh/images/ry_RQkYDb.gif','https://cdn.weeb.sh/images/r1siXJKw-.gif','https://cdn.weeb.sh/images/HyV5mJtDb.gif','https://cdn.weeb.sh/images/rJ52XyYD-.gif', 'https://cdn.weeb.sh/images/SJx7M0Ft-.gif','https://cdn.weeb.sh/images/Byjqm1tDW.gif','https://cdn.weeb.sh/images/rJvR71KPb.gif']
    embed = discord.Embed(
        title=f'{ctx.author.name} slaps {user}',
        colour = discord.Colour.blue()
    )
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    embed.set_image(url=random.choice(slap_gifs))

    await ctx.respond(embed=embed)

@client.slash_command(name='wink', description='wink wink 0-0')
@commands.cooldown(2,10,commands.BucketType.user)
async def wink(ctx):
    await ctx.defer()
    req = requests.get('https://some-random-api.ml/animu/wink')
    jason = req.json()
    link = jason['link']
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_image(url=link)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

@client.slash_command(name='pat', description='Give someone a pat!')
@commands.cooldown(2,10,commands.BucketType.user)
async def pat(ctx, member:Option(discord.Member, 'who youwu wanna pat!', required=True)):
    await ctx.defer()
    if member == client.user:
        await ctx.respond(f'*Smiles to {ctx.author.name}* :heart:')
    else:
        req = requests.get('https://some-random-api.ml/animu/pat')
        jason = req.json()
        link = jason['link']
        embed = discord.Embed(title=f'*{member.name}, you got a pat from {ctx.author.name}*',colour=discord.Colour.blue())
        embed.set_image(url=link)
        embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=embed)

@client.slash_command(name='dictionary', description='Searches for the given word!')
@commands.cooldown(2,10,commands.BucketType.user)
async def dictionary(ctx, word:Option(str, 'What word do u wanna search for?', required=True)):
    req = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    jason = req.json()
    try:
        deff = jason[0]['meanings'][0]['definitions'][0]['definition']
        await ctx.respond(f':books: Definitions for **{word}**\n```{deff}```')
    except:
        await ctx.respond(f'No word was found {no_emoji}')

rand = discord.SlashCommandGroup('random', 'Get random data!')

@rand.command(
    name='number',
    description='Gets random numbers!'
)
@commands.cooldown(1,8,commands.BucketType.user)
async def number(ctx, max:Option(int, 'Range to get numbers (ex- 0-max)', required=True)):
    numb = random.randrange(0,max)
    await ctx.respond(f"you're random number is: **{numb}**")

@rand.command(
    name='color',
    description='gives an random color!'
)
@commands.cooldown(1,3,commands.BucketType.user)
async def color(ctx):
    random_colours = ['Red', 'Pink', 'Purple', 'Blue', 'Cyan', 'Lime', 'Green', 'Yellow', 'Orange']
    await ctx.respond(f"you're random color is: **{random.choice(random_colours)}**")

client.add_application_command(rand)

@client.slash_command(name='stab', description='stabs an user!')
@commands.cooldown(1,5,commands.BucketType.user)
async def stab(ctx, user:Option(discord.Member,
    'user who u want to stab!',
    required=True)):
    stab_msg = [f'_stabs {user}_.', f'You stab {user}', f"stab? isn't that like illegal..?", "i woudn't recommand doing that tbh",f'You stab {user}', f'{user} has been stabbed']
    await ctx.respond(f'{random.choice(stab_msg)}')
@client.slash_command(name='8ball', description='Gives an asnwer to your yes/no question!')
@commands.cooldown(1,4,commands.BucketType.user)
async def ball(ctx, question:Option(str,
    'The question u want to get answer to!',
    required=True)):
    no_8ball = ['no lmfao', 'no bruh', 'ehh no', 'thats an bad idea no.', 'no.', 'ummm no', 'lmfaoooo what did u say, no', 'heck no', ' i can tell you certainly, no', 'no shot up']
    yes_8ball = ['sure, why not', "yea that's an good idea", 'ummmm sure', 'why not?', 'beep boop beeep boop, yes', "do it rn", 'thats an very very good idea', 'u should, yes', 'maybe u should', 'i dont know how i feel about this but u should do it, yes']
    mix_8ball = [f'{random.choice(no_8ball)}', f'{random.choice(yes_8ball)}']
    await ctx.respond(f'{random.choice(mix_8ball)}')

@client.slash_command(name='hack', description="hacks an user! TOTALLY REAL I SWEAR")
@commands.cooldown(1,4,commands.BucketType.user)
async def hack(ctx, user:Option(discord.Member,
    "user, who u want to hack",
    required=True)):
    await ctx.respond(f'hacking started on {user.name} now!')
    await asyncio.sleep(1.5)
    await ctx.edit(content='finding discord login info... (2fa bypassed)')
    await asyncio.sleep(1.5)
    await ctx.edit(content=f'found the discord info!\nEmail = {user.name}iscoolxd@yahoo.com\nPassword = {user.name}HasBigPP6969!')
    await asyncio.sleep(3)
    await ctx.edit(content='fetching the last dm ( if any at all )')
    await asyncio.sleep(1.5)
    await ctx.edit(content='Last dm found: Imagine having an small pp as mine')
    await asyncio.sleep(2)
    await ctx.edit(content='74.43% hacking medical records')
    await asyncio.sleep(1)
    await ctx.edit(content='Finding ip address!')
    await asyncio.sleep(1)
    await ctx.edit(content='ip address found\n**127.0.0.1:6969**')
    await asyncio.sleep(1)
    await ctx.edit(content='selling data in the dark web')
    await asyncio.sleep(1.5)
    await ctx.edit(content=f'Finished hacking {user.name}')
    
    await ctx.send('The _totally_ real hack is complete.')

async def addwarn(ctx: commands.Context, user, reason):
    async with client.db.cursor() as cursor:
        await cursor.execute("INSERT INTO warns (user, reason, time, guild) VALUES (?, ?, ?, ?)", (user.id, reason, int(datetime.datetime.now().timestamp()), ctx.guild.id))
    await client.db.commit()

@client.slash_command(
    name='warn',
    description='warns an user!'
)
@commands.has_permissions(manage_messages = True)
@commands.cooldown(2,10,commands.BucketType.user)
async def warn(ctx, member:Option(discord.Member,
    'user who u want to warn',
    required=True
), reason: str="No reason provided."):
    await addwarn(ctx, member, reason)
    #await ctx.respond(f"{yes_emoji}{member.name}")
    em = discord.Embed(title=f"{yes_emoji} **{member.name}** has been warned, ```Member ID: {member.id}```", colour=discord.Colour.green())
    await ctx.respond(embed=em)

@client.slash_command(name='clearwarns', description='Clears all warnings of the given member.')
@commands.has_permissions(manage_guild = True)
@commands.cooldown(2,10,commands.BucketType.user)
async def clearnwarn(ctx, member: discord.Member):
    async with client.db.cursor() as cursor:
        await cursor.execute('SELECT reason FROM warns WHERE user = ? AND guild = ?', (member.id, ctx.guild.id))
        data = await cursor.fetchone()
        if data:
            await cursor.execute('DELETE FROM warns WHERE user = ? AND guild = ?', (member.id, ctx.guild.id))
            #await ctx.respond(f'deleted {member.name}\'s warnings')
            em = discord.Embed(title=f"I have cleared {member.name}'s warnings.", colour=discord.Colour.red())
            await ctx.respond(embed=em)
        else:
            em = discord.Embed(title=f'{no_emoji} no warnings were found for this user.', colour=discord.Colour.red())
            await ctx.respond(embed=em)

@client.slash_command(name='warnings', description="View a member's warnings")
@commands.has_permissions(manage_messages = True)
@commands.cooldown(2,10,commands.BucketType.user)
async def warnings(ctx, member: discord.Member):
    async with client.db.cursor() as cursor:
        await cursor.execute('SELECT reason, time FROM warns WHERE user = ? AND guild = ?', (member.id, ctx.guild.id))
        data = await cursor.fetchall()
        if data:
            em = discord.Embed(title=f"{member.name}'s warnings", colour=discord.Colour.blue())
            warnum = 0
            for table in data:
                warnum += 1
                em.add_field(name=f"Warning {warnum}", value=f"Reason: {table[0]} | Date of warn: <t:{int(table[1])}:F>")
            await ctx.respond(embed=em)
        else:
            em = discord.Embed(title=f'{no_emoji} no warnings were found for this user.', colour=discord.Colour.red())
            await ctx.respond(embed=em)

@client.slash_command(
    name='weather',
    description='Get weather information!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def weather(ctx, city:Option(str,
    'City/State of which you wanna get weather of!')):
    try:
        req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7c81eeac6daecc743739e360e0633629')
        json1 = req.json()
        lon = json1['coord']['lon']
        lat = json1['coord']['lat']
        req2 = requests.get(f'https://www.timeapi.io/api/Time/current/coordinate?latitude={lat}&longitude={lon}')
        json2 = req2.json()
        time = json2['time']
        sec = json2['seconds']
        date = json2['date']
        country = json1['sys']['country']
        country1 = country.lower()
        wthr = json1['weather'][0]['main']
        timezone = json2['timeZone']
        temp = json1['main']['temp']
        temp = round(temp / 9.5)
        humi = json1['main']['humidity']
        wind = json1['wind']['speed']
        name = json1['name']
        embed = discord.Embed(
            description=f':flag_{country1}: {city}, {country}\n:calendar_spiral: {date}\n:clock10: {time}:{sec} ({timezone})\n\n:fog: {wthr}\n:thermometer: {temp}C\n:foggy: {humi}% humidity\n:leaves: {wind} m/s wind',
            #description=f':flag_{country1}: {name}, {country}\n:calendar_spiral: {date}\n:clock10: {time}:{sec} ({timezone})\n\n:fog: {wthr}\n:thermometer:',
            colour = discord.Colour.blue()
            )
        embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=embed)
    except Exception:
        await ctx.respond('Could you please check your spelling and try again! <a:no_sidd:979072393685401611>')

@client.slash_command(name='lock', description='locks the channel where command is used or the specified channel.')
@commands.has_permissions(manage_guild = True)
@commands.cooldown(2,10,commands.BucketType.user)
async def lock(ctx, channel:Option(discord.TextChannel, 'The channel which you wanna lock', required=False, default=None)):
    if channel is None:
        channel = ctx.channel
    await channel.set_permissions(ctx.guild.default_role, reason=f"{ctx.author.name} locked {channel.name}", send_messages=False)
    em = discord.Embed(description=f'{yes_emoji} I have locked down **{channel.name}**', colour=discord.Colour.green())
    await ctx.respond(embed=em)

@client.slash_command(name='lockall', description='locks down all channels of the server.')
@commands.has_permissions(manage_guild = True)
@commands.cooldown(2,10,commands.BucketType.user)
async def lockall(ctx):
    for channel in ctx.guild.channels:
        await channel.set_permissions(ctx.guild.default_role, reason=f"{ctx.author.name} locked {channel.name}", send_messages=False)
    em = discord.Embed(description=f'{yes_emoji} I have locked down all the channels of **{ctx.guild.name}**', colour=discord.Colour.green())
    em.set_footer(text='Note: this is only a panic only command u might have to unlock all channels manually later.')
    await ctx.respond(embed=em)

@client.slash_command(name='unlock', description='unlocks the channel where command is used or the specified channel.')
@commands.has_permissions(manage_guild = True)
@commands.cooldown(2,10,commands.BucketType.user)
async def unlock(ctx, channel:Option(discord.TextChannel, 'The channel which you wanna unlock', required=False, default=None)):
    if channel is None:
        channel = ctx.channel
    await channel.set_permissions(ctx.guild.default_role, reason=f"{ctx.author.name} unlocked {channel.name}", send_messages=True)
    em = discord.Embed(description=f'{yes_emoji} I have unlocked **{channel.name}**', colour=discord.Colour.green())
    await ctx.respond(embed=em)

"""@client.slash_command(name='unlockall', description='unlock all channels of the server.', guild_ids=[977226293345153075])
@commands.has_permissions(manage_guild = True)
@commands.cooldown(2,10,commands.BucketType.user)
async def unlockall(ctx):
    for channel in ctx.guild.channels:
        await channel.set_permissions(ctx.guild.default_role, reason=f"{ctx.author.name} unlocked {channel.name}", send_messages=None)
    em = discord.Embed(description=f'{yes_emoji} I have unlocked down all the channels of **{ctx.guild.name}**', colour=discord.Colour.green())
    await ctx.respond(embed=em)"""

@client.slash_command(
    name='coffee',
    description='Get an coffee pic!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def coffee(ctx):
    req = requests.get('https://coffee.alexflipnote.dev/random.json')
    jsoon = req.json()
    coffee = jsoon['file']
    em = discord.Embed(
        title=':coffee:',
        colour=discord.Colour.blue()
    )
    em.set_image(url=coffee)
    em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=em)
@client.slash_command(
    name='duck',
    description='Get duck pics!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def duck(ctx):
    req = requests.get('https://random-d.uk/api/v1/random')
    jsoon = req.json()
    duck = jsoon['url']
    em = discord.Embed(
        title=':duck:',
        colour=discord.Colour.blue()
    )
    em.set_image(url=duck)
    em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=em)
@client.slash_command(
    name='poll',
    description='Start a poll!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def poll(
    ctx: discord.ApplicationContext,
    question: Option(str, "What's you question?", required=True),
    choices:Option(str, 'How many choices do u want? (8 max)', required=True),
    choice1: Option(str, "choice1", required=True),
    choice2: Option(str, "choice2", required=True),
    choice3: Option(str, "choice3", required=False),
    choice4: Option(str, "choice4", required=False),
    choice5: Option(str, "choice5", required=False),
    choice6: Option(str, "choice6", required=False),
    choice7: Option(str, "choice7", required=False),
    choice8: Option(str, "choice8", required=False)):
        foot = f'Command executed by {ctx.author.name} | https://sparty.dev'
        if choices == '2':
            em = discord.Embed(title=f'{question}', description=f':one: {choice1}\n\n:two: {choice2}', colour=discord.Colour.blue())
            em.set_footer(text=foot)
            interaction = await ctx.respond(embed=em)
            message = await interaction.original_message()
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
        elif choices == '3':
            em = discord.Embed(title=f'{question}', description=f':one: {choice1}\n\n:two: {choice2}\n\n:three: {choice3}', colour=discord.Colour.blue())
            em.set_footer(text=foot)
            interaction = await ctx.respond(embed=em)
            message = await interaction.original_message()
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
        elif choices == '4':
            em = discord.Embed(title=f'{question}', description=f':one: {choice1}\n\n:two: {choice2}\n\n:three: {choice3}\n\n:four: {choice4}', colour=discord.Colour.blue())
            em.set_footer(text=foot)
            interaction = await ctx.respond(embed=em)
            message = await interaction.original_message()
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction('4️⃣')
        elif choices == '5':
            em = discord.Embed(title=f'{question}', description=f':one: {choice1}\n\n:two: {choice2}\n\n:three: {choice3}\n\n:four: {choice4}\n\n:five: {choice5}', colour=discord.Colour.blue())
            em.set_footer(text=foot)
            interaction = await ctx.respond(embed=em)
            message = await interaction.original_message()
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction('4️⃣')
            await message.add_reaction('5️⃣')
        elif choices == '6':
            em = discord.Embed(title=f'{question}', description=f':one: {choice1}\n\n:two: {choice2}\n\n:three: {choice3}\n\n:four: {choice4}\n\n:five: {choice5}\n\n:six: {choice6}', colour=discord.Colour.blue())
            em.set_footer(text=foot)
            interaction = await ctx.respond(embed=em)
            message = await interaction.original_message()
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction('4️⃣')
            await message.add_reaction('5️⃣')
            await message.add_reaction('6️⃣')
        elif choices == '7':
            em = discord.Embed(title=f'{question}', description=f':one: {choice1}\n\n:two: {choice2}\n\n:three: {choice3}\n\n:four: {choice4}\n\n:five: {choice5}\n\n:six: {choice6}\n\n:seven: {choice7}', colour=discord.Colour.blue())
            em.set_footer(text=foot)
            interaction = await ctx.respond(embed=em)
            message = await interaction.original_message()
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction('4️⃣')
            await message.add_reaction('5️⃣')
            await message.add_reaction('6️⃣')
            await message.add_reaction('7️⃣')
        elif choices == '8':
            em = discord.Embed(title=f'{question}', description=f':one: {choice1}\n\n:two: {choice2}\n\n:three: {choice3}\n\n:four: {choice4}\n\n:five: {choice5}\n\n:six: {choice6}\n\n:seven: {choice7}\n\n:eight: {choice8}', colour=discord.Colour.blue())
            em.set_footer(text=foot)
            interaction = await ctx.respond(embed=em)
            message = await interaction.original_message()
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction('4️⃣')
            await message.add_reaction('5️⃣')
            await message.add_reaction('6️⃣')
            await message.add_reaction('7️⃣')
            await message.add_reaction('8️⃣')
        else:
            await ctx.respond(f'please select atleast 2 choices and not more than 8 !! {no_emoji}')

async def node_connect():
    await client.wait_until_ready()
    await wavelink.NodePool.create_node(bot=client, host='node1.kartadharta.xyz', port='443', password='kdlavalink', https=True)

@client.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f'Node {node.identifier} is ready')
    
@client.slash_command(name='play', description='Play your chill beats.')
@commands.cooldown(2,10,commands.BucketType.user)
async def play(ctx, song:Option(wavelink.YouTubeTrack, 'Which song do u want to search?', required=True)):
    if not ctx.voice_client:
        vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
    else:
        vc: wavelink.Player = ctx.voice_client
    await vc.play(song)
    print("Someone's playing a song!")
    em = discord.Embed()
    em.add_field(name='<a:playing_sidd:996729733054218311> Now playing:', value=f'```{song.title}```')
    em.add_field(name='<:users_sidd:996736988201893889> Requested By', value=f'```{ctx.author.name}```')
    em.add_field(name='<:stage_sidd:996729590976360498> Song By', value=f'```{vc.track.author}```')
    em.add_field(name='<a:duration_sidd:996729273790500984> Song Duration', value=f'```{str(datetime.timedelta(seconds=vc.track.length))}```')
    em.set_footer(text='Thanks for using Sparty Music.')
    await ctx.respond(embed=em)
    """if vc.queue.is_empty and vc.is_playing:
        await vc.play(song)
        await ctx.respond(f'Playing {song.title}')
    else:
        await vc.queue.put_wait(song)
        await ctx.respond(f'added {song.title} to the queue!')
    vc.ctx = ctx
    setattr(vc, "loop", False)"""
    
    

@client.slash_command(name='pause', description='Pause the music playing.')
@commands.cooldown(2,10,commands.BucketType.user)
async def pause(ctx):
    if not ctx.voice_client:
        em = discord.Embed(title=f'{no_emoji} Not Playing any music.', colour=discord.Colour.red())
        await ctx.respond(embed=em)
    else:
        vc: wavelink.Player = ctx.voice_client
        
    await vc.pause()
    em = discord.Embed(title=f'{yes_emoji} I have paused you\'re music, do ```/resume``` to play it again.', colour=discord.Colour.green())
    await ctx.respond(embed=em)

@client.slash_command(name='resume', description='Resume the music.')
@commands.cooldown(2,10,commands.BucketType.user)
async def resume(ctx):
    if not ctx.voice_client:
        em = discord.Embed(title=f'{no_emoji} Not Playing any music.', colour=discord.Colour.red())
        return await ctx.respond(embed=em)
    else:
        vc: wavelink.Player = ctx.voice_client
        
    await vc.resume()
    em = discord.Embed(title=f'{yes_emoji} I have resumed your music continue vibing!', colour=discord.Colour.green())
    await ctx.respond(embed=em)
    
@client.slash_command(name='stop', description='Stop the music.')
@commands.cooldown(2,10,commands.BucketType.user)
async def stop(ctx):
    if not ctx.voice_client:
        em = discord.Embed(title=f'{no_emoji} Not Playing any music.', colour=discord.Colour.red())
        await ctx.respond(embed=em)
    else:
        vc: wavelink.Player = ctx.voice_client
        
    await vc.stop()
    em = discord.Embed(title=f':stop_button: I have destroyed the player.')
    await ctx.respond(embed=em)
    
@client.slash_command(name='nowplaying', description='Check the music playing.')
@commands.cooldown(2,10,commands.BucketType.user)
async def nowplaying(ctx):
    if not ctx.voice_client:
        em = discord.Embed(title=f'{no_emoji} Not Playing any music.', colour=discord.Colour.red())
        await ctx.respond(embed=em)
    else:
        vc: wavelink.Player = ctx.voice_client
    if not vc.is_playing():
        return await ctx.respond('Nothing is playing.')
    em = discord.Embed()
    em.add_field(name=f'<a:playing_sidd:996729733054218311> Song URL:', value=f'[Click Me]({str(vc.track.uri)})')
    em.add_field(name=f'<a:duration_sidd:996729273790500984> Duration:', value=f'```{str(datetime.timedelta(seconds=vc.track.length))}```')
    em.add_field(name=f'<:stage_sidd:996729590976360498> Filter:', value='```Unknown```')
    em.add_field(name=f'Artist:', value=f'```{vc.track.author}```')
    em.set_footer(text='Thanks for choosing Sparty.')

    #em.add_field(name='duration', value=f'{str(datetime.timedelta(seconds=vc.track.length))}')
    #em.add_field(name='Extra info', value=f'Song URL: [Click Me]({str(vc.track.uri)})')
    em.set_author(name=f'Sparty Music')
    return await ctx.respond(embed=em)
    
@client.slash_command(name='disconnect', description='Disconnect the bot from the voice channel.')
@commands.cooldown(2,10,commands.BucketType.user)
async def disconnect(ctx):
    try:
        vc: wavelink.Player = ctx.voice_client
            
        await vc.disconnect()
        em = discord.Embed(title=f'{yes_emoji} Disconnecting the bot now.', colour=discord.Colour.green())
        await ctx.respond(embed=em)
    except:
        em = discord.Embed(title=f'{no_emoji} Bot is not in vc.', colour=discord.Colour.red())
        await ctx.respond(embed=em)

@client.slash_command(name='mute', description='Mutes the member.')
@commands.cooldown(2,10,commands.BucketType.user)
@commands.has_permissions(moderate_members = True)
async def mute(ctx, member: discord.Member, reason:Option(str, "Reason for muting the member", required=False, default="No reason provided."), seconds:Option(int, required=False), minutes:Option(int, required=False), hours:Option(int, required=False), days:Option(int, required=False)):
    #time = humanfriendly.parse_time(time)
    try:
        if seconds == None:
            seconds = 0
        if minutes == None:
            minutes = 0
        if hours == None:
            hours = 0
        if days == None:
            days = 0
        dur = timedelta(seconds=seconds, minutes=minutes, hours=hours, days=days)
        if reason == None:
            await member.timeout_for(dur)
            em = discord.Embed(title=f'{yes_emoji} {member.name} has been muted.', colour=discord.Colour.green())
            await ctx.respond(embed=em)
        else:
            await member.timeout_for(dur, reason=reason)
            em = discord.Embed(title=f'{yes_emoji} {member.name} has been muted.', colour=discord.Colour.green())
            await ctx.respond(embed=em)
    except:
        await ctx.respond(f'{no_emoji} You must specify time to mute a member.')
    #await member.timeout(until = discord.utils.utcnow() + datetime.timedelta(seconds=time), reason=reason)
@client.slash_command(name='unmute', description='Unmutes the member.')
@commands.cooldown(2,10,commands.BucketType.user)
@commands.has_permissions(moderate_members = True)
async def unmute(ctx, member: discord.Member):
    await member.remove_timeout()
    em = discord.Embed(title=f'{yes_emoji} {member.name} has been unmuted.', colour=discord.Colour.green())
    
    await ctx.respond(embed=em)
"""@client.event
async def on_wavelink_track_end(player: wavelink.Player, track: wavelink.YouTubeTrack, reason):
    ctx = player.ctx
    vc: player = ctx.voice_client
    
    if vc.loop:
        return await vc.play(track)
    try:
        next_song = vc.queue.get()
        await vc.play(next_song)

    except wavelink.errors.QueueEmpty:
        pass
    await vc.play(next_song)
    await ctx.respond(f'Now playing {next_song.title}')
    
@client.slash_command(name='loop', description='loop the current song/queue.')
@commands.cooldown(2,10,commands.BucketType.user)
async def loop(ctx):
    if not ctx.voice_client:
        return await ctx.respond('Not playing any music')
    elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.respond(f'{no_emoji} You need to actually join a vc smh.')
    else:
        vc: wavelink.Player = ctx.voice_client
        
    try:
        vc.loop = True
    except Exception:
        setattr(vc, "loop", False)
    if vc.loop:
        return await ctx.respond('loop is now enabled')
    else:
        await ctx.respond('loop is now disanled.')

@client.slash_command(name='queue', description='Check the current song queue.')
@commands.cooldown(2,10,commands.BucketType.user)
async def queue(ctx):
    if not ctx.voice_client:
        return await ctx.respond('Not playing any music')
    elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.respond(f'{no_emoji} You need to actually join a vc smh.')
    else:
        vc: wavelink.Player = ctx.voice_client
    if vc.queue.is_empty:
        return await ctx.respond('Queue is empty')
    em = discord.Embed(title='Queue', colour=discord.Colour.blue())
    queue = vc.queue/copy()
    song = 0
    for song in queue:
        song += 1
        em.add_field(name=f'Song num {song}', value=f'{song.title}')
    await ctx.respond(embed=em)

@client.slash_command(name='volume', description='Change the song volume.')
@commands.cooldown(2,10,commands.BucketType.user)
async def volume(ctx, volume: int):
    if not ctx.voice_client:
        return await ctx.respond('Not playing any music')
    elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.respond(f'{no_emoji} You need to actually join a vc smh.')
    else:
        vc: wavelink.Player = ctx.voice_client
    if volume > 100:
        await ctx.respond('Volume to too high')
    elif volume < 0:
        await ctx.respond("Volume too low")
    await ctx.respond(f'setting the volume to {volume}%')
    return await vc.set_volume(volume)"""

"""@client.slash_command(name='queue', description='Check the songs that will play next.')
@commands.cooldown(2,10,commands.BucketType.user)
async def queue(ctx):
    """

@client.slash_command(
    name='sparty',
    description='Shows infos about Sparty!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def sparty(ctx):
    def size(bytes, suffix='8'):
        factor = 1028
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < factor:
                return f'{bytes:.2f}{unit}{suffix}'
            bytes /= factor
    vir = psutil.virtual_memory()
    swap = psutil.swap_memory()
    ram_swap = size(swap.total)
    used_swap = size(swap.used)
    disk = psutil.disk_usage('/')
    disk_total = round(disk.total /1024**3)
    disk_used = round(disk.used /1024**3)
    ram_total = size(vir.total)
    #free = size(vir.available)
    used = size(vir.used)
    psutil
    cpu_per = psutil.cpu_percent()
    cpu = cpuinfo.get_cpu_info()['brand']
    #perc = size(vir.percent)
    em = discord.Embed(
        title=f'Info about Sparty!',
        #description=f'**Language**\nPython 3.10.5\n**Main library**\nPycord\n**Servers**\n{len(client.guilds)}\n**Users**\n{len(client.users)}\n**Developer**\nSidd#3538',
        colour=discord.Colour.blue()
    )
    em.add_field(name='Language', value='```Python 3.10.5```', inline=True)
    em.add_field(name='Main library', value='```Pycord```', inline=True)
    em.add_field(name='Extra Library', value='```Discord.py```', inline=True)
    em.add_field(name='Servers', value=f'```{len(client.guilds)}```', inline=True)
    em.add_field(name='Users', value=f'```{len(client.users)}```', inline=True)
    em.add_field(name='Specs and usage', value=f'```Ram usage: {used} / 24GB\nDisk usage: {disk_used}GB / {disk_total}GB\nCpu usage: {cpu_per}%\ncpu: {cpu}```', inline=False)
    em.add_field(name='Developer', value='```Sidd#3538```', inline=False)
    em.set_author(name=name, icon_url=icon)
    em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    em.set_thumbnail(url=icon)
    button1 = Button(label='Invite Bot', url='https://discord.com/oauth2/authorize?client_id=979611617467727912&scope=bot&permissions=2617632990&scope=bot%20applications.commands', emoji='<a:diamond_sparty:980474185476350013>')
    button2 = Button(label='Support server', url='https://discord.gg/5r8rEstMgT', emoji='<a:discord_sparty:979072519992643655>')
    button3 = Button(label='Vote', url='https://top.gg/bot/979611617467727912/vote', emoji='<:arrow_sidd:983755280418476052>')
    button4 = Button(label='Website', url='https://sparty.dev/', emoji='<:globe_sparty:980477059145035838>')
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    await ctx.respond(embed=em, view=view)
"""import wikipedia
@client.slash_command(
    name='wiki',
    description='Searches on wikipedia for info!',
    guild_ids=[977226293345153075]
)
@commands.cooldown(1,7,commands.BucketType.user)
async def wiki(ctx, name:Option(str,
    'What do u want to search for?')):
    try:
        summ = wikipedia.summary(name)
    except wikipedia.exceptions.DisambiguationError as e:
        opti = e.options
        summ = wikipedia.summary(opti[1])
    print(summ)
    embed = discord.Embed(
        description=f'{summ}',
        colour=discord.Colour.blue()
    )
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)
    except Exception:
        await ctx.respond(f'Wikipedia api might be down atm! {no_emoji}')"""
@client.slash_command(
    name='password',
    description='Generates an random!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def password(ctx, length:Option(int,
    'How long do u want your password to be?')):
    if length > 40:
        em = discord.Embed(description=f'Are you trying to break me? the password length cannot be more than 40! {no_emoji}', colour=discord.Colour.blue())
        await ctx.respond(embed=em)
    else:
        alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        symbol = '\!$%&/(=?^[]}{+*@#<>;.:_'
        alll = alpha + symbol
        password = "".join(random.sample(alll, length))
        await ctx.author.send(f'Your new randomly generated password is: ||{password}||')
        embed = discord.Embed(description=f'{ctx.author.name}, i have sent you your password please check your dms! {yes_emoji}', colour=discord.Colour.blue())
        await ctx.respond(embed=embed)
@client.slash_command(
    name='urban',
    description='Get urbandictionary search results for name meanings and more!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def urban(ctx, name:Option(str,
    'name/word you wanna search')):
    try:
        req = requests.get(f'https://api.urbandictionary.com/v0/define?term={name}')
        try:
            jason = req.json()
            defi = jason['list'][0]['definition']
            link = jason['list'][0]['permalink']
            example = jason['list'][0]['example']
            word = jason['list'][0]['word']
            em = discord.Embed(title=f'{word} {link}', description=f'{defi}', colour=discord.Colour.blue())
            em.set_footer(text=example)
            await ctx.respond(embed=em)
        except:
            await ctx.respond(f'i have searched that word and i cant find it sry {no_emoji}')
    except:
        await ctx.respond(f'urbandictionary api is down atm ;-; {no_emoji}')
@client.slash_command(
    name='f',
    description='Pays respect to the given user!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def f(ctx, user:Option(discord.Member,
    'Who do u want to pay respect!')):
    heart = ['❤️', '🧡', '💛', '💚', '💙', '💜', '🤎', '🖤', '🤍']
    randhrt = random.choice(heart)
    await ctx.respond(f'**{ctx.author.name}** has paid their respect for **{user.mention}** {randhrt}')
@client.slash_command(
    name='fruit',
    description='Give someone a fruit snack :) !'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def fruit(ctx, user:Option(discord.Member, 'Who do u wanna give the fruit to?', required=True), reason:Option(str, 'reason for giving fruits', required=False, default=None)):
    fruits = [':apple:', ':pear:', ':tangerine:', ':lemon:', ':banana:', ':watermelon:', ':grapes:', ':blueberries:', ':strawberry:', ':peach:', ':kiwi:']
    fruit = random.choice(fruits)
    if reason != None:
        await ctx.respond(f'{user.mention}, you got a {fruit} from {ctx.author.name}\n\nReason: {reason}\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ {fruit}')
    else:
        await ctx.respond(f'{user.mention}, you got a {fruit} from {ctx.author.name}\n\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ {fruit}')
@client.slash_command(
    name='drake',
    description='drake meme maker!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def drake(ctx, wrong:Option(str, 'Top text?', required=True), right:Option(str, 'Bottom text?', required=True)):
    try:
        params = {
            "template_id": 181913649,
            "username": "siddiscoolxd",
            "password": "Siddarth123@",
            "font": "arial",
            "boxes[0][text]": f"{wrong}",
            "boxes[0][color]": "#000000",
            "boxes[1][text]": f"{right}",
            "boxes[1][color]": "#000000",
        }
        req = requests.get('https://api.imgflip.com/caption_image', params=params)
        jsoan = req.json()
        url = jsoan['data']['url']
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=em)
    except:
        await ctx.respond(f'Meme api might be down atm ;-; {no_emoji}')
@client.slash_command(
    name='changemymind',
    description='Change my mind meme maker!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def changemymind(ctx, text:Option(str, 'Text?', required=True)):
    try:
        params = {
            "template_id": 129242436,
            "username": "siddiscoolxd",
            "password": "Siddarth123@",
            "font": "arial",
            "boxes[0][text]": f"{text}",
            "boxes[0][color]": "#000000",
            "boxes[1][text]": "",
            "boxes[1][color]": "#000000",
        }
        req = requests.get('https://api.imgflip.com/caption_image', params=params)
        jsoan = req.json()
        url = jsoan['data']['url']
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=em)
    except:
        await ctx.respond(f'Meme api might be down atm ;-; {no_emoji}')
@client.slash_command(
    name='twobuttons',
    description='two buttons meme maker!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def twobuttons(ctx, button1:Option(str, 'Left text?', required=True), button2:Option(str, 'Right text?', required=True)):
    try:
        params = {
            "template_id": 87743020,
            "username": "siddiscoolxd",
            "password": "Siddarth123@",
            "font": "arial",
            "boxes[0][text]": f"{button1}",
            "boxes[0][color]": "#000000",
            "boxes[1][text]": f"{button2}",
            "boxes[1][color]": "#000000",
        }
        req = requests.get('https://api.imgflip.com/caption_image', params=params)
        jsoan = req.json()
        url = jsoan['data']['url']
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=em)
    except:
        await ctx.respond(f'Meme api might be down atm ;-; {no_emoji}')

@client.slash_command(
    name='waiting',
    description='Waiting skeleton meme maker!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def waiting(ctx, text:Option(str, 'Text?', required=True)):
    try:
        params = {
            "template_id": 4087833,
            "username": "siddiscoolxd",
            "password": "Siddarth123@",
            "font": "arial",
            "boxes[0][text]": f"",
            "boxes[0][color]": "#FFFFFF",
            "boxes[1][text]": f"{text}",
            "boxes[1][color]": "#FFFFFF",
        }
        req = requests.get('https://api.imgflip.com/caption_image', params=params)
        jsoan = req.json()
        url = jsoan['data']['url']
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=em)
    except:
        await ctx.respond(f'Meme api might be down atm ;-; {no_emoji}')
@client.slash_command(
    name='hidethepain',
    description='Hide the pain meme maker!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def hidethepain(ctx, text:Option(str, 'Text?', required=True)):
    try:
        params = {
            "template_id": 27813981,
            "username": "siddiscoolxd",
            "password": "Siddarth123@",
            "font": "arial",
            "boxes[0][text]": f"{text}",
            "boxes[0][color]": "#FFFFFF",
            "boxes[1][text]": f"",
            "boxes[1][color]": "#FFFFFF",
        }
        req = requests.get('https://api.imgflip.com/caption_image', params=params)
        jsoan = req.json()
        url = jsoan['data']['url']
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=em)
    except:
        await ctx.respond(f'Meme api might be down atm ;-; {no_emoji}')

@client.slash_command(
    name='cardboard',
    description='Guy holding cardboard sign meme maker!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def cardboard(ctx, text:Option(str, 'Text?', required=True)):
    try:
        params = {
            "template_id": 216951317,
            "username": "siddiscoolxd",
            "password": "Siddarth123@",
            "font": "arial",
            "boxes[0][text]": f"{text}",
            "boxes[0][color]": "#FFFFFF",
            "boxes[1][text]": f"",
            "boxes[1][color]": "#FFFFFF",
        }
        req = requests.get('https://api.imgflip.com/caption_image', params=params)
        jsoan = req.json()
        url = jsoan['data']['url']
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=em)
    except:
        await ctx.respond(f'Meme api might be down atm ;-; {no_emoji}')

@client.slash_command(
    name='successkid',
    description='Success kid meme maker!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def successkid(ctx, text:Option(str, 'Text?', required=True)):
    try:
        params = {
            "template_id": 61544,
            "username": "siddiscoolxd",
            "password": "Siddarth123@",
            "font": "arial",
            "boxes[0][text]": f"",
            "boxes[0][color]": "#FFFFFF",
            "boxes[1][text]": f"{text}",
            "boxes[1][color]": "#FFFFFF",
        }
        req = requests.get('https://api.imgflip.com/caption_image', params=params)
        jsoan = req.json()
        url = jsoan['data']['url']
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=em)
    except:
        await ctx.respond(f'Meme api might be down atm ;-; {no_emoji}')

@client.slash_command(
    name='cutecat',
    description='Cute cat meme maker!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def cutecat(ctx, text:Option(str, 'Text?', required=True)):
    try:
        params = {
            "template_id": 8279814,
            "username": "siddiscoolxd",
            "password": "Siddarth123@",
            "font": "arial",
            "boxes[0][text]": f"",
            "boxes[0][color]": "#FFFFFF",
            "boxes[1][text]": f"{text}",
            "boxes[1][color]": "#000000",
        }
        req = requests.get('https://api.imgflip.com/caption_image', params=params)
        jsoan = req.json()
        url = jsoan['data']['url']
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
        await ctx.respond(embed=em)
    except:
        await ctx.respond(f'Meme api might be down atm ;-; {no_emoji}')
@client.slash_command(
    name='whoasked',
    description='random who asked meme'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def whoasked(ctx):
    memes = ['https://c.tenor.com/tgXQ-yWDKggAAAAM/crazy-no-one-cares.gif','https://c.tenor.com/Pk681SQt0doAAAAM/who-tf-asked-nasas-radar-dish.gif', 'https://c.tenor.com/d9P9RUDnHjMAAAAM/me-looking-for-who-asked-me-looking-for-who-asked-meme.gif', 'https://c.tenor.com/O_A6p_n5PEAAAAAM/kanye-kanye-west.gif', 'https://c.tenor.com/3a2vosRA9UEAAAAM/did-you.gif', 'https://c.tenor.com/2Gsf2UQ7Qw4AAAAM/who-asked.gif', 'https://c.tenor.com/hUUIxQe_Ut4AAAAM/nobody-cares-who-asked.gif', 'https://c.tenor.com/yheo1GGu3FwAAAAM/rick-roll-rick-ashley.gif']
    who = random.choice(memes)
    em = discord.Embed(colour=discord.Colour.blue())
    em.set_image(url=who)
    em.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=em)
@client.slash_command(
    name='cookie',
    description='Give someone a cookie :) !'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def cookie(ctx, user:Option(discord.Member, 'Who do u wanna give the cookie to?', required=True)):
    await ctx.respond(f'{user.mention}, you got a :cookie: from **{ctx.author.name}**\n\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ :cookie:')

@client.slash_command(
    name='love',
    description='calculate love between two users!'
)
@commands.cooldown(2,10,commands.BucketType.user)
async def love(ctx, user1:Option(discord.Member, 'user one.'), user2:Option(discord.Member, 'user two.')):
    lov = random.randint(0,100)
    if user1 == client.user:
        await ctx.respond("B-but I don't have feelings :(")
    elif user2 == client.user:
        await ctx.respond("B-but I don't have feelings :(")
    elif lov < 50:
        em = discord.Embed(title=':broken_heart: **Love Calculator** :broken_heart:', description=f'Love between {user1.name} and {user2.name} is at {lov}%', colour=discord.Colour.red())
        await ctx.respond(embed=em)
    else:
        em = discord.Embed(title=':heart: **Love Calculator** :heart:', description=f'Love between {user1.name} and {user2.name} is at **{lov}%**', colour=discord.Colour.red())
        await ctx.respond(embed=em)

@client.slash_command(name='user', description='Gets user info!')
@commands.cooldown(2,10,commands.BucketType.user)
async def user(ctx, user:Option(discord.Member, 'Who do u wanna get info for?', required=True)):
    user = user or ctx.author
    show_roles = ", ".join(
        [f"<@&{x.id}>" for x in sorted(user.roles, key=lambda x: x.position, reverse=True) if x.id != ctx.guild.default_role.id]
    ) if len(user.roles) > 1 else "None"
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.add_field(name="Full name", value=user, inline=True)
    embed.add_field(name="Nickname", value=user.nick if hasattr(user, "nick") else "None", inline=True)
    embed.add_field(name="Account created", value=user.created_at)
    embed.add_field(name="Joined this server", value=user.joined_at)
    embed.add_field(name="Roles", value=show_roles, inline=False)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(content=f"ℹ About **{user.id}**", embed=embed)

@client.slash_command(name='server', description='Shows server info!')
@commands.cooldown(2,10,commands.BucketType.user)
async def server(ctx):
    find_bots = sum(1 for member in ctx.guild.members if member.bot)
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
    embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
    embed.add_field(name="Bots", value=find_bots, inline=True)
    embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
    embed.add_field(name="Created", value=ctx.guild.created_at),
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(content=f"ℹ information about **{ctx.guild.name}**", embed=embed)

@client.slash_command(name='mods', description='Shows how many mods are in the guild!')
@commands.cooldown(2,10,commands.BucketType.user)
async def mods(ctx):
    message = ""
    all_status = {
        "online": {"users": [], "emoji": "🟢"},
        "idle": {"users": [], "emoji": "🟡"},
        "dnd": {"users": [], "emoji": "🔴"},
        "offline": {"users": [], "emoji": ""}
    }
    for user in ctx.guild.members:
        user_perm = ctx.channel.permissions_for(user)
        if user_perm.kick_members or user_perm.ban_members:
            if not user.bot:
                all_status[str(user.status)]["users"].append(f"**{user}**")
    for g in all_status:
        if all_status[g]["users"]:
            message += f"{all_status[g]['emoji']} {', '.join(all_status[g]['users'])}\n"
    await ctx.respond(f"Mods in **{ctx.guild.name}**\n\n{message}")

@client.slash_command(name='triggered', description='Triggered image meme maker!')
@commands.cooldown(2,10,commands.BucketType.user)
async def triggered(ctx, member:Option(discord.Member, 'User who u want to trigger!', required=True)):
    await ctx.defer()
    try:
        if not member:
            member = ctx.author
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar.with_format('png').url}") as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read())
                await ctx.respond(file=discord.File(imageData, 'triggered.gif'))
    except:
        await ctx.respond(f'The user must have an profile picture {no_emoji}')

@client.slash_command(name='gay', description='Make someone gay, yes !')
@commands.cooldown(2,10,commands.BucketType.user)
async def gay(ctx, member:Option(discord.Member, 'User who u want to gayify!', required=True)):
    await ctx.defer()
    try:
        if not member:
            member = ctx.author
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f"https://some-random-api.ml/canvas/gay?avatar={member.avatar.with_format('png').url}") as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read())
                await ctx.respond(file=discord.File(imageData, 'gay.gif'))
    except:
        await ctx.respond(f'The user must have an profile picture {no_emoji}')

@client.slash_command(name='wasted', description='Wasted image meme maker!')
@commands.cooldown(2,10,commands.BucketType.user)
async def wasted(ctx, member:Option(discord.Member, 'Select an discord member!', required=True)):
    await ctx.defer()
    try:
        if not member:
            member = ctx.author
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar.with_format('png').url}") as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read())
                await ctx.respond(file=discord.File(imageData, 'wasted.gif'))
    except:
        await ctx.respond(f'The user must have an profile picture {no_emoji}')

@client.slash_command(name='passed', description='Mission passed respect+ image meme maker!')
@commands.cooldown(2,10,commands.BucketType.user)
async def passed(ctx, member:Option(discord.Member, 'Select an discord member!', required=True)):
    await ctx.defer()
    try:
        if not member:
            member = ctx.author
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f"https://some-random-api.ml/canvas/passed?avatar={member.avatar.with_format('png').url}") as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read())
                await ctx.respond(file=discord.File(imageData, 'missionpassed.gif'))
    except:
        await ctx.respond(f'The user must have an profile picture {no_emoji}')

@client.slash_command(name='jail', description='Jail image meme maker!')
@commands.cooldown(2,10,commands.BucketType.user)
async def jail(ctx, member:Option(discord.Member, 'Select an discord member!', required=True)):
    await ctx.defer()
    try:
        if not member:
            member = ctx.author
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f"https://some-random-api.ml/canvas/jail?avatar={member.avatar.with_format('png').url}") as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read())
                await ctx.respond(file=discord.File(imageData, 'jail.gif'))
    except:
        await ctx.respond(f'The user must have an profile picture {no_emoji}')

@client.slash_command(name='invert', description='Make an image more spooky with invert  !')
@commands.cooldown(2,10,commands.BucketType.user)
async def invert(ctx, member:Option(discord.Member, 'Select an discord member!', required=True)):
    await ctx.defer()
    try:
        if not member:
            member = ctx.author
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f"https://some-random-api.ml/canvas/invert?avatar={member.avatar.with_format('png').url}") as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read())
                await ctx.respond(file=discord.File(imageData, 'invert.gif'))
    except:
        await ctx.respond(f'The user must have an profile picture {no_emoji}')

@client.slash_command(name='bright', description='Brighten the image!')
@commands.cooldown(2,10,commands.BucketType.user)
async def bright(ctx, member:Option(discord.Member, 'Select an discord member!', required=True)):
    await ctx.defer()
    try:
        if not member:
            member = ctx.author
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f"https://some-random-api.ml/canvas/brightness?avatar={member.avatar.with_format('png').url}") as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read())
                await ctx.respond(file=discord.File(imageData, 'bright.gif'))
    except:
        await ctx.respond(f'The user must have an profile picture {no_emoji}')

@client.slash_command(name='pixelate', description='Make someone like an minecraft painting !')
@commands.cooldown(2,10,commands.BucketType.user)
async def pixelate(ctx, member:Option(discord.Member, 'Select an discord member!', required=True)):
    await ctx.defer()
    try:
        if not member:
            member = ctx.author
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f"https://some-random-api.ml/canvas/pixelate?avatar={member.avatar.with_format('png').url}") as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read())
                await ctx.respond(file=discord.File(imageData, 'pixelate.gif'))
    except:
        await ctx.respond(f'The user must have an profile picture {no_emoji}')

@client.slash_command(name='youtube-comment', description='Make some comment on youtube.. totally real xd !')
@commands.cooldown(2,10,commands.BucketType.user)
async def youtube(ctx, member:Option(discord.Member, 'Select an discord member!', required=True), comment:Option(str, 'What do u want to comment?!', required=True)):
    await ctx.defer()
    try:
        if not member:
            member = ctx.author
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={member.avatar.with_format('png').url}&username={member.name}&comment={comment}") as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read())
                await ctx.respond(file=discord.File(imageData, 'youtube-comment.gif'))
    except:
        await ctx.respond(f'The user must have an profile picture {no_emoji}')

@client.slash_command(name='tweet', description='Make some tweet on twitter.. totally real xd !')
@commands.cooldown(2,10,commands.BucketType.user)
async def tweet(ctx, member:Option(discord.Member, 'Select an discord member!', required=True), comment:Option(str, 'What do u want to comment?!', required=True)):
    await ctx.defer()
    reply = random.randint(200, 1600)
    try:
        if not member:
            member = ctx.author
        async with aiohttp.ClientSession() as trigSession:
            async with trigSession.get(f"https://some-random-api.ml/canvas/tweet?avatar={member.avatar.with_format('png').url}&username={member.name}&displayname={member.name}&comment={comment}&replies={reply}") as trigImg: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await trigImg.read())
                await ctx.respond(file=discord.File(imageData, 'tweet.gif'))
    except:
        await ctx.respond(f'The user must have an profile picture {no_emoji}')

@client.slash_command(name='panda', description='Get panda pics and panda facts !')
@commands.cooldown(2,10,commands.BucketType.user)
async def panda(ctx):
    await ctx.defer()
    req = requests.get('https://some-random-api.ml/animal/panda')
    jason = req.json()
    image = jason['image']
    fact = jason['fact']
    embed = discord.Embed(title=fact, colour=discord.Colour.blue())
    embed.set_image(url=image)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

@client.slash_command(name='dog', description='Get dog pics and dog facts !')
@commands.cooldown(2,10,commands.BucketType.user)
async def dog(ctx):
    await ctx.defer()
    req = requests.get('https://some-random-api.ml/animal/dog')
    jason = req.json()
    image = jason['image']
    fact = jason['fact']
    embed = discord.Embed(title=fact, colour=discord.Colour.blue())
    embed.set_image(url=image)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

@client.slash_command(name='cat', description='Get cat pics and cat facts !')
@commands.cooldown(2,10,commands.BucketType.user)
async def cat(ctx):
    await ctx.defer()
    req = requests.get('https://some-random-api.ml/animal/cat')
    jason = req.json()
    image = jason['image']
    fact = jason['fact']
    embed = discord.Embed(title=fact, colour=discord.Colour.blue())
    embed.set_image(url=image)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

@client.slash_command(name='fox', description='Get fox pics and fox facts !')
@commands.cooldown(2,10,commands.BucketType.user)
async def fox(ctx):
    await ctx.defer()
    req = requests.get('https://some-random-api.ml/animal/fox')
    jason = req.json()
    image = jason['image']
    fact = jason['fact']
    embed = discord.Embed(title=fact, colour=discord.Colour.blue())
    embed.set_image(url=image)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

@client.slash_command(name='red-panda', description='Get red panda pics and facts !')
@commands.cooldown(2,10,commands.BucketType.user)
async def red_panda(ctx):
    await ctx.defer()
    req = requests.get('https://some-random-api.ml/animal/red_panda')
    jason = req.json()
    image = jason['image']
    fact = jason['fact']
    embed = discord.Embed(title=fact, colour=discord.Colour.blue())
    embed.set_image(url=image)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

@client.slash_command(name='koala', description='Get koala pics and facts !')
@commands.cooldown(2,10,commands.BucketType.user)
async def koala(ctx):
    await ctx.defer()
    req = requests.get('https://some-random-api.ml/animal/koala')
    jason = req.json()
    image = jason['image']
    fact = jason['fact']
    embed = discord.Embed(title=fact, colour=discord.Colour.blue())
    embed.set_image(url=image)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

@client.slash_command(name='birb', description='Get birb pics and birb facts !')
@commands.cooldown(2,10,commands.BucketType.user)
async def birb(ctx):
    await ctx.defer()
    req = requests.get('https://some-random-api.ml/animal/birb')
    jason = req.json()
    image = jason['image']
    fact = jason['fact']
    embed = discord.Embed(title=fact, colour=discord.Colour.blue())
    embed.set_image(url=image)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

@client.slash_command(name='raccoon', description='Get raccoon pics and raccoon facts !')
@commands.cooldown(2,10,commands.BucketType.user)
async def raccoon(ctx):
    await ctx.defer()
    req = requests.get('https://some-random-api.ml/animal/raccoon')
    jason = req.json()
    image = jason['image']
    fact = jason['fact']
    embed = discord.Embed(title=fact, colour=discord.Colour.blue())
    embed.set_image(url=image)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

@client.slash_command(name='kangaroo', description='Get kangaroo pics and kangaroo facts !')
@commands.cooldown(2,10,commands.BucketType.user)
async def kangaroo(ctx):
    await ctx.defer()
    req = requests.get('https://some-random-api.ml/animal/kangaroo')
    jason = req.json()
    image = jason['image']
    fact = jason['fact']
    embed = discord.Embed(title=fact, colour=discord.Colour.blue())
    embed.set_image(url=image)
    embed.set_footer(text=f'Command executed by {ctx.author.name} | https://sparty.dev')
    await ctx.respond(embed=embed)

# https://some-random-api.ml/lyrics?title=
@client.slash_command(name='lyrics', description='Get your favourite song lyrics!')
@commands.cooldown(2,10,commands.BucketType.user)
async def lyrics(ctx, songname:Option(str, 'Which song do u wanna get lyrics for?', required=True)):
    await ctx.defer(ephemeral=True)
    try:
        req = requests.get(f'https://some-random-api.ml/lyrics?title={songname}')
        jason = req.json()
        try:
            #[website](https://sparty.dev)
            title = jason['title']
            author = jason['author']
            lyrics = jason['lyrics']
            thumbnail = jason['thumbnail']['genius']
            #link = jason['links']['genius']
            em = discord.Embed(title=f'<a:music:990264330786312253>   {title}', description=f'```{lyrics}```', colour=discord.Colour.blue())
            em.set_author(name=f'Song by {author}')
            em.set_thumbnail(url=thumbnail)
            await ctx.respond(embed=em)
        except:
            await ctx.respond(f"Sorry I couldn't find that song's lyrics {no_emoji}")
    except:
        await ctx.respond(f'Maybe api service is down please try again later! {no_emoji}')

#base = discord.SlashCommandGroup('base64', 'Base64 encoder/decoder!')
@client.slash_command(name='base64-encode', description='Base64 Encoder!')
@commands.cooldown(2,10,commands.BucketType.user)
async def encode(ctx, text:Option(str, 'Text which you want to encode!', required=True)):
    try:
        req = requests.get(f'https://some-random-api.ml/base64?encode={text}')
        jason = req.json()
        output = jason['base64']
        await ctx.respond(f'Your output is: **{output}**')
    except:
        await ctx.respond('api is down ;-;')
@client.slash_command(name='base64-decode', description='Base64 Decoder!')
@commands.cooldown(2,10,commands.BucketType.user)
async def decode(ctx, text:Option(str, 'Text which you want to decode!', required=True)):
    try:
        req = requests.get(f'https://some-random-api.ml/base64?decode={text}')
        jason = req.json()
        output = jason['text']
        await ctx.respond(f'Your output is: **{output}**')
    except:
        await ctx.respond('api is down ;-;')

@client.slash_command(name='hex', description='Get hex from rgb!')
@commands.cooldown(2,10,commands.BucketType.user)
async def hex(ctx, rgb:Option(str, 'Type the rgb here example= "255,255,255"!', required=True)):
    try:
        req = requests.get(f'https://some-random-api.ml/canvas/hex?rgb={rgb}')
        jason = req.json()
        output = jason['hex']
        await ctx.respond(f'Hex for {rgb} is: **{output}**')
    except:
        await ctx.respond(f'Invalid rgb {no_emoji} your rgb was "**{rgb}**".')

@client.slash_command(name='rgb', description='Get rgb from hex!')
@commands.cooldown(2,10,commands.BucketType.user)
async def rgb(ctx, hex:Option(str, 'Type the hex here example= "ffffff"!', required=True)):
    try:
        req = requests.get(f'https://some-random-api.ml/canvas/rgb?hex={hex}')
        jason = req.json()
        r = jason['r']
        g = jason['g']
        b = jason['b']
        await ctx.respond(f'Rgb for {hex} is: **{r},{g},{b}**')
    except:
        await ctx.respond(f'Invalid hex {no_emoji} your hex was "**{hex}**".')

@client.slash_command(name='bored', description="Get some fun activity to do if your bored!")
@commands.cooldown(2,10,commands.BucketType.user)
async def bored(ctx):
    try:
        req = requests.get('http://www.boredapi.com/api/activity')
        jason = req.json()
        activity = jason['activity']
        await ctx.respond(activity)
    except:
        await ctx.respond('maybe api is down try again later i guess.')
@client.slash_command(name='animal', description="Random animals!")
@commands.cooldown(2,10,commands.BucketType.user)
async def animal(ctx):
    try:
        req = requests.get('https://zoo-animal-api.herokuapp.com/animals/rand')
        jason = req.json()
        name = jason['name']
        url = jason['image_link']
        em = discord.Embed(title=f'{name}', colour=discord.Colour.blue())
        em.set_image(url=url)
        await ctx.respond(embed=em)
    except:
        await ctx.respond(f'Maybe api is down {no_emoji}')

@client.slash_command(
    name='help',
    description='If u ever get confused use this command!'
)
@commands.cooldown(1,10,commands.BucketType.user)
async def help(ctx):
    button1 = Button(label='Invite Bot', url='https://discord.com/oauth2/authorize?client_id=979611617467727912&scope=bot&permissions=2617632990&scope=bot%20applications.commands', emoji='<a:diamond_sparty:980474185476350013>')
    button2 = Button(label='Support server', url='https://discord.gg/5r8rEstMgT', emoji='<a:discord_sparty:979072519992643655>')
    button3 = Button(label='Vote', url='https://top.gg/bot/979611617467727912/vote', emoji='<:arrow_sidd:983755280418476052>')
    button4 = Button(label='Website', url='https://sparty.dev/', emoji='<:globe_sparty:980477059145035838>')
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)

    select = Select(
        placeholder='Select help category!',
        options=[
        discord.SelectOption(label='Utility', emoji='<a:diamond_sidd:979072492893245450>'),
        discord.SelectOption(label='Moderation', emoji='<:staff_sidd:983994541147324437>'),
        discord.SelectOption(label='Fun', emoji='<:greydice:991688599403765851>'),
        discord.SelectOption(label='Meme', emoji='<a:laugh_sidd:983995336353779742>'),
        discord.SelectOption(label='Images', emoji='<a:978943406288027689:parrot_dancing_sidd>'),
        discord.SelectOption(label='Music', emoji='<a:playing_sidd:996729733054218311>')])

    view.add_item(select)
    async def callback(interaction: discord.Interaction):
        await interaction.response.defer()
        utility_embed = discord.Embed(
            description=f'**Sparty help menu**\n\nThis is the help menu select an category from below!\n\nWe have an commands section in our [website](https://sparty.dev) which guides you through all commands!\n\n**Utility commands <a:diamond_sidd:979072492893245450>**\n{prefix}sparty   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}ping   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}quote   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}mcserver   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}hypixel   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}bedwars   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}random number   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}random color   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}fortune   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}8ball   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}covid_all   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}weather   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}password   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}user   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}server   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}mods   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}dictionary   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}base64-encode   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}base64-decode   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}hex   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}rgb   [[Docs]](https://sparty.dev/pages/commands.html)',
            colour=discord.Colour.blue()
        )
        moderation_embed = discord.Embed(
            description=f'**Sparty help menu**\n\nThis is the help menu select an category from below!\n\nWe have an commands section in our [website](https://sparty.dev) which guides you through all commands!\n\n**Moderation commands <:staff_sidd:983994541147324437>**\n{prefix}purge   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}kick   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}ban   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}slowmode   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}warn   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}clearwarns   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}warnings   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}poll   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}lock   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}unlock   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}lockall   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}mute   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}unmute   [[Docs]](https://sparty.dev/pages/commands.html)',
            colour=discord.Colour.blue()
        )
        meme_embed = discord.Embed(
            description=f'**Sparty help menu**\n\nThis is the help menu select an category from below!\n\nWe have an commands section in our [website](https://sparty.dev) which guides you through all commands!\n\n**Meme commands <a:laugh_sidd:983995336353779742>**\n{prefix}drake   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}changemymind   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}twobuttons   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}waiting   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}hidethepain   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}cardboard   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}successkid   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}cutecat   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}whoasked   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}triggered   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}gay   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}wasted   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}passed   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}jail   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}invert   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}bright   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}pixelate   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}youtube-comment   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}tweet   [[Docs]](https://sparty.dev/pages/commands.html)\n',
            colour=discord.Colour.blue()
        )
        fun_embed = discord.Embed(
            description=f'**Sparty help menu**\n\nThis is the help menu select an category from below!\n\nWe have an commands section in our [website](https://sparty.dev) which guides you through all commands!\n\n**Fun commands <:greydice:991688599403765851>**\n{prefix}meme   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}fact   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}yomomma   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}coinflip   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}dadjoke   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}truth   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}dare   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}kiss   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}slap   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}stab   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}love   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}pat   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}wink   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}cookie   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}fruit   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}f   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}bored   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}urban   [[Docs]](https://sparty.dev/pages/commands.html)',
            colour=discord.Colour.blue()
        )
        image_embed = discord.Embed(
            description=f'**Sparty help menu**\n\nThis is the help menu select an category from below!\n\nWe have an commands section in our [website](https://sparty.dev) which guides you through all commands!\n\n**Images commands <a:parrot:978943406288027689>**\n{prefix}panda   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}dog   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}cat   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}fox   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}red-panda   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}koala   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}birb   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}raccoon   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}kangaroo\n{prefix}duck   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}coffee   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}animal   [[Docs]](https://sparty.dev/pages/commands.html)',
            colour=discord.Colour.blue()
        )
        music_embed = discord.Embed(
            description=f'**Sparty help menu**\n\nThis is the help menu select an category from below!\n\nWe have an commands section in our [website](https://sparty.dev) which guides you through all commands!\n\n**Music commands <a:playing_sidd:996729733054218311>**\n{prefix}play   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}pause   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}resume   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}nowplaying   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}stop   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}disconnect   [[Docs]](https://sparty.dev/pages/commands.html)\n{prefix}lyrics   [[Docs]](https://sparty.dev/pages/commands.html)',
            colour=discord.Colour.blue()
        )
        if select.values[0] == 'Utility':
            await interaction.message.edit(embed=utility_embed)
        if select.values[0] == 'Meme':
            await interaction.message.edit(embed=meme_embed)
        if select.values[0] == 'Moderation':
            await interaction.message.edit(embed=moderation_embed)
        if select.values[0] == 'Fun':
            await interaction.message.edit(embed=fun_embed)
        if select.values[0] == 'Images':
            await interaction.message.edit(embed=image_embed)
        if select.values[0] == 'Music':
            await interaction.message.edit(embed=music_embed)
    select.callback = callback
    normal_embed = discord.Embed(
        description='**Sparty help menu**\n\nThis is the help menu select an category from below!\n\nWe have an commands section in our [website](https://sparty.dev) which guides you through all commands!',
        colour=discord.Colour.blue()
    )
    await ctx.respond(embed=normal_embed, view=view)


client.run(token)