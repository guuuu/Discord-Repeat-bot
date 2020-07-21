import discord
from discord.ext import commands
import time
import ctypes

try:
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    TOKEN = str("replace_with_your_discord_bot_token")
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
        await bot.change_presence(activity=discord.Game(name="!Rh / !Ri"))

    @bot.command(name='Rr')
    async def repeat(ctx, arg):
        if arg == "raise-exception":
            raise discord.DiscordException

        parts = str(arg).split(" ")
        content = ""
        for f in range(len(parts)):
            if f == 0:
                continue
            content += str(parts[f]) + " "

        if int(parts[0]) > 0: 
            for i in range(int(parts[0])):
                await ctx.send(f"{content}")
                time.sleep(0.7)

    @bot.command(name='Rh')
    async def help(ctx):
        await ctx.send('Para usar este bot escreve !rpt "x y"\nSendo que X é o número de vezes que queres que o bot repita\nE Y a frase que queres que o bot repita')

    @bot.command(name='Ri')
    async def info(ctx):
        await ctx.send("Este bot foi desenvolvido por @S1LV3R#3955 porque ele não tem vida :)")
    
    bot.run(TOKEN)
except:
    pass