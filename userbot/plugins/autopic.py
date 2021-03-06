import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
import asyncio
import shutil
from userbot.utils import admin_cmd

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

#@command(pattern="^.autopic", outgoing=True)
@borg.on(admin_cmd(pattern=r"autopic"))
async def autopic(event):
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("NGY")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 33)
        drawn_text.text((90, 200), current_time, font=fnt, fill=(138, 43, 226))
        img.save(photo)
        file = await bot.upload_file(photo)  # pylint:disable=E0602
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            counter -= 10
            await asyncio.sleep(10)
        except:
            return
