import discord
import codecs
from FLIB import *
import random as rd
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, bot_has_permissions
with codecs.open('pands.txt', 'r', 'utf8') as F:
    for conchos in F:
        b = conchos.strip(',').split(',')
StBd = []
rdd = ["*NO*", "NO!!", "DONT ASKING ABOUT THAT", ">:L", "SUSSY BAKA", "nah", "_summoning banfm1_","ඞඞ AMOGUS ඞඞ", "NO YOU SUඞඞSSIE BAKA", "ඞ", "suggest another one",  "```N-n... N-no... You s-sussy bbaka...```"]
cl = commands.Bot(command_prefix="!")
cl2 = discord.Client()
@commands.has_permissions(manage_messages=True)
@cl.command(name="Kill", pass_context=True)
async def Kill(ctx):
	await ctx.message.delete()
	await ctx.send('*OOF*')
	quit()
@cl.command(name="learn", pass_context=True)
async def learn(ctx, ww):
	w =ww.lower()
	StBd.append(w)
	c= ""
	with codecs.open('pands.txt', 'r', 'utf8') as F:
	    for conchos in F:
	        b = conchos.strip(',').split(',')
	        b.append(w)
	        m = JNL2Str(",", b)
	        c = m
	        # print(m)
	        await ctx.send("*learned:* " + w )
	with codecs.open("pands.txt","w",'utf8') as F: 
		F.write(c)
@cl.event
async def on_ready():
    print('i have login as {0.user}'.format(cl))
    print("console.log")
@cl.event
async def on_message(message):
	global b, StBd,a,rdd
	k = 1
	k2 = 1
	inp = message.content 
	d = list(inp.strip().lower().split(' '))
	print(d)
	if message.author == cl.user:
	    return
	for i in range(0,len(d)):
		if k == 1:
			# print(d[i])
			for j in range(0,len(b)):
				# print(b[j])
				if d[i].replace(" ","") == b[j]:
					print(d[i].replace(" ",""))
					k = 0
					# await message.delete()
					await message.channel.send(file=discord.File('pand.jpg'))
					await message.channel.send(rd.choice(rdd))
				if k == 0: break

		if k2 == 1:
			for jk in range(0,len(StBd)):
				if d[i].replace(" ","") == StBd[jk]:
					print(StBd)
					k2 = 0
					# await message.delete()
					await message.channel.send(file=discord.File('pand.jpg'))
					await message.channel.send(rd.choice(rdd))
					if k2 == 0: break

	await cl.process_commands(message)
	

tok = <ur token goes here>
cl.run(tok)
