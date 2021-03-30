from PIL import Image , ImageDraw , ImageFont
import discord

client = discord.Client()

img = Image.open("customimage.png")

d = ImageDraw.Draw(img)

font = ImageFont.truetype(r'Location\PinyonScript-Regular.ttf', 150)
font_roll = ImageFont.truetype(r'Location\Charm-Regular.ttf', 55)
font_rec = ImageFont.truetype(r'Location\Charm-Regular.ttf', 40)

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  entry1 = ''
  entry2 = ''
  entry3 = ''
  if message.content.startswith('|Entry1'):
    entry1 = message.content
    entry1 = entry1[5:]
    d.text((550, 550), entry1, font=font, fill=(161, 126, 67))
  if message.content.startswith('|Entry2'):
    entry2 = message.content
    entry2 = entry2[5:]
    d.text((890, 740), entry2, font=font_roll, fill=(6, 6, 6))
  if message.content.startswith('|Entry3'):
    entry3 = message.content
    entry3 = entry3[7:]
    d.text((450, 820), entry3, font = font_rec, align="justify", fill=(6, 6, 6))
    img.save("cert.png")
    await message.channel.send(file=discord.File("cert.png"))

client.run('Token id')

#Kartik Shukla
#B190697CS
#For achieving a rank of 12 and creating a record for best rank in google hashcode