"""Делает скриншот сайта
Команда: .scr <ссылка>"""

import io
import requests
from telethon import events
from uniborg.util import admin_cmd


@borg.on(admin_cmd("scr (.*)"))
async def _(event):
    if event.fwd_from:
        return
    if Config.SCREEN_SHOT_API_AIVENGO is None:
        await event.edit("В конфигурации вбей API https://screenshotlayer.com/product \nЯ не могу так работать!")
        return
    await event.edit("В процессе")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(sample_url.format(
        Config.SCREEN_SHOT_API_AIVENGO,
        input_str,
        "1",
        "2560x1440",
        "PNG",
        "1"
    ))
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers['content-type']
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screenshot.png"
            try:
                await borg.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=input_str,
                    force_document=True,
                    reply_to=event.message.reply_to_msg_id
                )
                await event.delete()
            except Exception as e:
                await event.edit(str(e))
    else:
        await event.edit(response_api.text)
