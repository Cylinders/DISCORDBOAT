import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_member_join(member):
    print(f'{member} has joined the Valorant Gamerz')


@client.event
async def on_member_remove(member):
    print(f'{member} decided to leave the Valorant Gamerz')


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! Your ping is {round(client.latency*100)}ms")


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    response = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "sarva says Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(response)}")


@client.command()
async def clear(ctx, *, amount=1):
    await ctx.channel.purge(limit=amount+1)

client.run('NzQ2NDA5MTg4OTUwOTMzNjc1.Xz_5ug.GxHjPxqVMTQD8tYhLHCEwmLjd2I')
