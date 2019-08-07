from discord.ext import commands
import discord
import asyncio
from champions import champions
from config import Config

bot		= commands.Bot(command_prefix="!s ")

@bot.event
async def on_ready():
	print("Silverwing is ready!")

@bot.command()
async def champion(ctx, arg):
	'''Get information on a specific champion'''
	info	= champions(arg.lower().title())
	embed	= discord.Embed(
		title = info["name"],
		description = "Information about " + info["name"],
		color = discord.Color.blue()
		)
	embed.set_footer(text="Powered by Silverwing. If you encounter any errors, contact Yukinox#6090")
	embed.set_thumbnail(url=info["img"] + ".png")
	embed.add_field(name="Tier", value=info["tier"])
	embed.add_field(name="Class", value=", ".join(info["class"]))
	embed.add_field(name="Ability", value=info["ability"])
	await ctx.send(embed=embed)

@bot.command()
async def item(ctx):
	'''Get information on a specific item'''
	await ctx.send("Item Command")

@bot.command()
async def team(ctx):
	'''Get a list of Teamfight Tactics team comps'''
	await ctx.send("Team Command")

config = Config()
bot.run(config.token)