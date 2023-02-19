
import discord
from discord.ext import commands
from config import *
from keep_alive import keep_alive

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="+",
                   description="Test ryze bot !",
                   intents=intents)

@bot.event
async def on_ready():
  print("Ryze has Rise")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content.startswith('+re'):
    userText = message.content[4:len(message.content)]
    userChannel = message.author.voice.channel
    invitation = await userChannel.create_invite(max_age=300, max_uses=5)
    members = userChannel.members
    embed = discord.Embed(colour=0x3498DB, type='rich')

    embed.set_author(name=message.author, icon_url=message.author.avatar)

    embed.add_field(name=userChannel,
                    value="[Bấm để tham gia](" + invitation.url + ") (" +
                    str(len(members)) + "/" +
                    ("Unlimited" if userChannel.user_limit == 0 else str(
                      userChannel.user_limit)) + ")",
                    inline=False)
    embed.set_footer(
      text="Cách sử dụng: +re <Điều Kiện>",
      icon_url=
      "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/LoL_icon.svg/1200px-LoL_icon.svg.png"
    )
    await message.channel.send(content=f'{message.author.mention} {userText}',
                               embed=embed)
    await message.delete()
    
keep_alive()    
bot.run(Your token, reconnect=True)