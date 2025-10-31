import discord
from discord.ext import commands
from get_class import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def kontrol(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            try:
                file_name = attachment.filename
                await attachment.save(f"./{file_name}")

                response = get_class(
                    model_path="C:/Users/alime/OneDrive/Desktop/Kodlar/AI Discord Bot/model_unquant.tflite",  #Burada kendi yolunuzu seçip değiştrmelisiniz.
                    labels_path="labels.txt",
                    image_path=f"./{attachment.filename}"
                )

                await ctx.send(response)

            except Exception as e:
                await ctx.send(f"🚫 Görsel işlenemedi: {str(e)}")
    else:
        await ctx.send("📎 Görsel yüklemediğiniz için işlem yapılamadı. Lütfen bir resim ekleyin.")



bot.run("MTM2NzkyMzI2OTI0MzYzMzg2NQ.GHx9-b.i8WarjPoeB3cu4ySR-jRP_CNvaCY3ufD0F4qQM")