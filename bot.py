import discord
from datetime import datetime
import pytz
import random

client = discord.Client()

cnt_msg = ["super", "super mega", "super ultra", "ultimate super", "super ultimate", "ultra super", "super mega ultra ultimate"]
suf_msg = ["gei", "đại ca", "múp", "khoai to", "trẩu tre", "phê đá", "3d", "chết tịt", "suck", "ngáy to", ""]
pre_msg = ["ê", "fuck", "cc", "chó", "king", ""]

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.channel.DMChannel):
        return
    if message.author == client.user or message.guild.id != 952847230648348722:
        return

    tz_VN = pytz.timezone('Asia/Ho_Chi_Minh') 
    datetime_VN = datetime.now(tz_VN)
    time = datetime_VN.strftime("%H:%M:%S %d/%m/%Y")

    channell = client.get_channel(994925167887253544)
    await channell.send( 
                         random.choice(pre_msg) + " <@852863854031142913> " + random.choice(cnt_msg) + " " + random.choice(suf_msg)
                         + "\n{"
                         + "\n      author: " + message.author.display_name + " (" + message.author.name + "#" + message.author.discriminator + ")"
                         + "\n      channel: " + "<#" + str(message.channel.id) + ">"
                         + "\n      time: " + time
                         + "\n      link: https://discord.com/channels/952847230648348722/" + str(message.channel.id) + "/" + str(message.id) 
                         + "\n}"
                       )
client.run('you are gei!')
