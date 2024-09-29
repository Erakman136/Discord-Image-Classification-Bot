import discord
from discord.ext import commands
from bot_token import token
from yeni import detect_bird
from hello import detect_pepe

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def mantar(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await ctx.send('Resminiz algılandı!')
            file_name = attachment.filename
            await ctx.send('Dosya Kaydediliyor!')
            file_path = f"images/{file_name}"
            await attachment.save(file_path)
            await ctx.send('Dosya Kaydedildi!')
            name, score = detect_bird(file_path, "converted_keras\keras_model.h5", "converted_keras\labels.txt")
            await ctx.send(f"bu bir {name.strip()} bundan % {int(score*100)} eminim!")
    else:

      await ctx.send(f'Lütfen bir fotoğraf ekleyin!')
@bot.command()
async def meyve(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await ctx.send('Resminiz algılandı!')
            file_name = attachment.filename
            await ctx.send('Dosya Kaydediliyor!')
            file_path = f"images/{file_name}"
            await attachment.save(file_path)
            await ctx.send('Dosya Kaydedildi!')
            name, score = detect_pepe(file_path, "converted_kerascik\keras_model.h5", "converted_kerascik\labels.txt")
            await ctx.send(f"bu bir {name.strip()} meyve bundan % {int(score*100)} eminim!")
    else:

      await ctx.send(f'Lütfen bir fotoğraf ekleyin!')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run(token)