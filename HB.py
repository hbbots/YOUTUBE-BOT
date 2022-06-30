
import os 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import Client, filters,emoji
from pyrogram.types import Message

HB = Client(
    "Echo-bot", 
    api_id = 2152187,
    api_hash = "1a0208e94456f4799a5f5269f1198d62",
    bot_token = "1946471767:AAEZYPiyUQKnyXWXwpNA1acdacxPEx2pGqU"
)

START_TEXT = """**
HI {}, 
youtubebot

MADE BY @TELSABOTS**"""

HELP_TEXT = """**
SENT ANY TEXT MESSAGE.......

THEN REPLY WITH ANY /COMMAND

eg :- /python

PRESS /LIST COMMAND TO KNOW ABOUT
CUREENTLY SUPPORTED EXTENSIONS

MADE BY @TELSABOTS**
"""

ABOUT_TEXT = """
 🤖<b>BOT :MEDIA INFO 🤖</b>

📢<b>CHANNEL :</b>@TELSA BOTS

🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT

"""


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='python'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )


result_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )




result_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

result_text = """**JOIN @TELSABOTS"""

@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )




from pytube import YouTube

ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

import asyncio 
@HB.on_message(filters.regex(ytregex))
async def ytdl(_, message):
   l = message.text.split()
   global var
   global ythd
   global ythigh
   global ytlow
   global ytverylow
   global ytmedium
   global ytworst
   global yt
   global ytaudio
   global song
   var=message.text
   url= message.text
   yt = YouTube(url)
   chat_id =message.chat.id
   thumb = yt.thumbnail_url

   ythigh = yt.streams.get_highest_resolution()
   ythd = yt.streams.get_by_resolution(resolution = '720p')
   ytmedium = yt.streams.get_by_resolution(resolution = '480p')
   ytlow = yt.streams.get_by_resolution(resolution ='360p')
   ytverylow = yt.streams.get_by_resolution(resolution = '240p')
   ytworst = yt.streams.get_by_resolution(resolution = '144p')
   
   result_buttons2 = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('🎬 1080P', callback_data='high'),
        InlineKeyboardButton('🎬 720p', callback_data='720p')
    ],[
        InlineKeyboardButton('🎬 480p', callback_data='480p'),
        InlineKeyboardButton('🎬 360p ', callback_data='360p')
    ],[
        InlineKeyboardButton('🎬 240p', callback_data='240p'),
        InlineKeyboardButton('🎬 144p', callback_data='144p')
    ]]
   )
   await message.reply_photo(
            photo=thumb,
            caption="🎬 TITLE : "+ yt.title +  "\n\n📤 UPLOADED : " + yt.author  + "\n\n📢 CHANNEL LINK " + f'https://www.youtube.com/channel/{yt.channel_id}',
            reply_markup=result_buttons2,
            quote=True,
    
    )

@HB.on_callback_query()
async def cb_data(bot, update):
    if update.data == '720p':
     try:
      await HB.send_video(
        chat_id = update.message.chat.id, 
        video = ythd.download())
     except:
        await HB.send_message(
            chat_id = update.message.chat.id,
            text="**😔 720P QUALITY IS NOT AVIALBLE\n CHOOSE ANY OTHER QUALITIES**")   
    elif update.data == '480p':
      try:
       await HB.send_video(
       chat_id = update.message.chat.id, 
       video = ytmedium.download())
      except:
        await HB.send_message(
            chat_id = update.message.chat.id,
            text="**😔 480P QUALITY IS NOT AVIALBLE \n CHOOSE ANY OTHER QUALITIES**")  
    
    elif update.data == 'high':
     try:
        await  HB.send_video(
            chat_id = update.message.chat.id, 
            video = ythigh.download())
     except:
        await HB.send_message(
            chat_id = update.message.chat.id,
            text="**😔 1080P QUALITY IS NOT AVIALBLE\n CHOOSE ANY OTHER QUALITIES**")    
    
    elif update.data == '360p':
     try:
      await  HB.send_video(
        chat_id = update.message.chat.id, 
        video = ytlow.download())
     except:
        await HB.send_message(
            chat_id = update.message.chat.id,
            text="**😔 360P QUALITY IS NOT AVIALBLE \n CHOOSE ANY OTHER QUALITIES**")  
    
    elif update.data == '240p':
     try:
      await  HB.send_video(
        chat_id = update.message.chat.id, 
        video = ytverylow.download())
     except:
         await HB.send_message(
        chat_id = update.message.chat.id,
         text="**😔 240P QUALITY IS NOT AVIALBLE\n CHOOSE ANY OTHER QUALITIES**")    

    elif update.data == '144p':
     try:
        await  HB.send_video(
        chat_id = update.message.chat.id,
        video= yt.worst.download())
     except:
        await HB.send_message(
            chat_id = update.message.chat.id,
            text="😔 144P QUALITY IS NOT AVIALBLE\n CHOOSE ANY OTHER QUALITIES**")
    
    elif update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    
    else:
        await update.message.delete()

print("HB")

HB.run()
