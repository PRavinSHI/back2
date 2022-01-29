# AI Chat (C) 2020-2021 by @InukaAsith

import emoji
import re
import aiohttp
from googletrans import Translator as google_translator
from pyrogram import filters
from aiohttp import ClientSession
from EmikoRobot import BOT_USERNAME as bu
from EmikoRobot import BOT_ID, pbot, arq
from EmikoRobot.ex_plugins.chatbot import add_chat, get_session, remove_chat
from EmikoRobot.utils.pluginhelper import admins_only, edit_or_reply

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

translator = google_translator()


async def RosiQuery(query: str, user_id: int):
    luna = await arq.luna(query, user_id)
    return luna.result


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


async def fetch(url):
    try:
        async with aiohttp.Timeout(10.0):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    try:
                        data = await resp.json()
                    except:
                        data = await resp.text()
            return data
    except:
        print("AI response Timeout")
        return


ewe_chats = []
en_chats = []


@pbot.on_message(
    filters.command(["chatbot", f"chatbot@{bu}"])
    & ~filters.edited
    & ~filters.bot
    & ~filters.private
)
@admins_only
async def hmm(_, message):
    global ewe_chats
    if len(message.command) != 2:
        await message.reply_text("I only recognize /chatbot on and /chatbot off only")
        message.continue_propagation()
    status = message.text.split(None, 1)[1]
    chat_id = message.chat.id
    if status == "ON" or status == "on" or status == "On":
        lel = await edit_or_reply(message, "`Processing...`")
        lol = add_chat(int(message.chat.id))
        if not lol:
            await lel.edit("ROSI AI Already Activated In This Chat")
            return
        await lel.edit(
            f"ROSI AI Actived by {message.from_user.mention()} for users in {message.chat.title}"
        )

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await edit_or_reply(message, "`Processing...`")
        Escobar = remove_chat(int(message.chat.id))
        if not Escobar:
            await lel.edit("ROSI AI Was Not Activated In This Chat")
            return
        await lel.edit(
            f"ROSI AI Deactivated by {message.from_user.mention()} for users in {message.chat.title}"
        )

    elif status == "EN" or status == "en" or status == "english":
        if not chat_id in en_chats:
            en_chats.append(chat_id)
            await message.reply_text(
                f"English AI chat Enabled by {message.from_user.mention()}"
            )
            return
        await message.reply_text(
            f"English AI Chat Disabled by {message.from_user.mention()}"
        )
        message.continue_propagation()
    else:
        await message.reply_text(
            "I only recognize `/chatbot on` and `chatbot off` only"
        )


@pbot.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited
    & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def hmm(client, message):
    if not get_session(int(message.chat.id)):
        return
    if not message.reply_to_message:
        return
    try:
        senderr = message.reply_to_message.from_user.id
    except:
        return
    if senderr != BOT_ID:
        return
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        test = msg
        test = test.replace("ROSI", "Aco")
        test = test.replace("ROSI", "Aco")
        test = test.replace("My god is @Gplove_Rp", "he'is Nice Person  ")
        test = test.replace("16", "9")
        test = test.replace("@Gplove_Rp is my husband.", "I'm single.")
        test = test.replace("My husband is @Gplove_Rp", "I'm single.")
        test = test.replace("@Rosisupport", "Rosi.ai")
        test = test.replace(
            "I live in @Rosisupport.", "I live in Egmore, chennai."
        )
        test = test.replace("I was created by @Gplove_Rp", "I made myself")
        test = test.replace(
            "Hello there I am Rosi...nice to meet u",
            "Hi, my friend! Do you want me to tell you a joke?",
        )
        test = test.replace("@Gplove_Rp is my owner", "Have the control right.")
        test = test.replace(
            "Hi, My name is Rosi Nice to meet you.",
            "Hi, my friend, what can I do for you today?",
        )
        response = await RosiQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Aco", "Rosi")
        response = response.replace("aco", "Rosi")
        response = response.replace("Rosi", "Rosi")
        response = response.replace("Rosi", "Rosi")
        response = response.replace("I'm a single", "My god is @Gplove_Rp)
        response = response.replace("9", "16")
        response = response.replace(
            "I'm married to my job.", "I'm married with @Gplove_Rp"
        )
        response = response.replace("I'm single.", "My husband is @Gplove_Rp)
        response = response.replace("Rosi.ai", "@Rosisupport)
        response = response.replace(
            "I live in Egmore, chennai .", "I live in @Rosisupport."
        )
        response = response.replace("I made myself", "I was Created by @Gplove_Rp")
        response = response.replace(
            "Hi, my friend! Do you want me to tell you a joke?",
            "Hello there I am luna...nice to meet u",
        )
        response = response.replace(
            "Have the control right.", "@Gplove_Rp is my owner."
        )
        response = response.replace(
            "Hi, my friend, what can I do for you today?",
            "Hi, My name is Rosi Nice to meet you",
        )

        pro = response
        try:
            await pbot.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return

    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if (
            [(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
        ):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            # print (rm)
        try:
            lan = translator.detect(rm)
            lan = lan.lang
        except:
            return
        test = rm
        if not "en" in lan and not lan == "":
            try:
                test = translator.translate(test, dest="en")
                test = test.text
            except:
                return
        # test = emoji.demojize(test.strip())

        test = test.replace("Rosi", "Aco")
        test = test.replace("Rosi", "Aco")
        test = test.replace("My god is @Gplove_Rp", "my'owner is singe Nice person")
        test = test.replace("16", "9")
        test = test.replace("@Gplove_Rp is my husband.", "I'm single.")
        test = test.replace("@Rosisupport", "Rosi.ai")
        test = test.replace(
            "I live in @Rosisupport.", "I live Egmore, chennai"
        )
        test = test.replace("I was created by @Gplove_Rp", "I made myself")
        test = test.replace(
            "Hello there I am Rosi..nice to meet u",
            "Hi, my friend! Do you want me to tell you a joke?",
        )
        test = test.replace("@Gplove_Rp is my owner", "Have the control right.")
        test = test.replace(
            "Hi, My name is Rosi Nice to meet you.",
            "Hi, my friend, what can I do for you today?",
        )
        response = await RosiQuery(
            test, message.from_user.id if message.from_user else 0
        )
        response = response.replace("Aco", "Rosi")
        response = response.replace("aco", "Rosi")
        response = response.replace("Rosi", "Rosi")
        response = response.replace("Rosi", "Rosi")
        response = response.replace("my'is single ", "My god is @Gplove_Rp")
        response = response.replace("9", "16")
        response = response.replace(
            "I'm married to my job.", "I'm married with @Gplove_Rp"
        )
        response = response.replace("I'm single.", "My husband is @Gplove_Rp")
        response = response.replace("Rosi.ai", "@Rosisupport")
        response = response.replace(
            "I live in San Francisco, California.", "I live in @Rosisupport."
        )
        response = response.replace("I made myself", "I was Created by @Gplove_Rp")
        response = response.replace(
            "Hi, my friend! Do you want me to tell you a joke?",
            "Hello there I am Rosi...nice to meet u",
        )
        response = response.replace(
            "Have the control right.", "♕︎@Gplove_Rp is my owner."
        )
        response = response.replace(
            "Hi, my friend, what can I do for you today?",
            "Hi, My name is Rosi Nice to meet you",
        )
        pro = response
        if not "en" in lan and not lan == "":
            try:
                pro = translator.translate(pro, dest=lan)
                pro = pro.text
            except:
                return
        try:
            await pbot.send_chat_action(message.chat.id, "typing")
            await message.reply_text(pro)
        except CFError:
            return


@pbot.on_message(
    filters.text & filters.private & ~filters.edited & filters.reply & ~filters.bot
)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return
    test = test.replace("Rosi", "Aco")
    test = test.replace("Rosi", "Aco")
    test = test.replace("My god is @Gplove_Rp", "and'my owner is handsome")
    test = test.replace("16", "9")
    test = test.replace("@Gplove_Rp is my husband.", "I'm single.")
    test = test.replace("@Rosisupport", "Rosi.ai")
    test = test.replace(
        "I live in @Rosisupport.", "I Live Egmore, Chennai."
    )
    test = test.replace("I was created by @Gplove_Rp", "I made myself")
    test = test.replace(
        "Hello there I am Rosi...nice to meet u",
        "Hi, my friend! Do you want me to tell you a joke?",
    )
    test = test.replace("@Gplove_Rp is my owner", "Have the control right.")
    test = test.replace(
        "Hi, My name is luna Nice to meet you.",
        "Hi, my friend, what can I do for you today?",
    )

    response = await lunaQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Aco", "Rosi")
    response = response.replace("aco", "Rosi")
    response = response.replace("Rosi", "Rosi")
    response = response.replace("Rosi", "Rosi")
    response = response.replace("my owner is single and handsome", "My god is @Gplove_Rp")
    response = response.replace("9", "16")
    response = response.replace("I'm married to my job.", "I'm married with @Gplove_Rp")
    response = response.replace("I'm single.", "My husband is @Gplove_Rp")
    response = response.replace("Rosi.ai", "@Rosisupport")
    response = response.replace(
        "I live in Egmore, Chennai.", "I live in @Rosisupport"
    )
    response = response.replace("I made myself", "I was Created by @Gplove_Rp")
    response = response.replace(
        "Hi, my friend! Do you want me to tell you a joke?",
        "Hello there I am Rosi...nice to meet u",
    )
    response = response.replace("Have the control right.", "@Gplove_Rp is my owner.")
    response = response.replace(
        "Hi, my friend, what can I do for you today?",
        "Hi, My name is Rosi Nice to meet you",
    )

    pro = response
    if not "en" in lan and not lan == "":
        pro = translator.translate(pro, dest=lan)
        pro = pro.text
    try:
        await pbot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


@pbot.on_message(
    filters.regex("Rosi|rosi|robot|ROSI|sena")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel
    & ~filters.edited
)
async def inuka(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        # print (rm)
    try:
        lan = translator.detect(rm)
        lan = lan.lang
    except:
        return
    test = rm
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, dest="en")
            test = test.text
        except:
            return

    # test = emoji.demojize(test.strip())

    test = test.replace("Rosi", "Aco")
    test = test.replace("Rosi", "Aco")
    test = test.replace("My god is @Gplove_Rp", "my master is busy  did know him name was PRAMYAVINCY AND USER NAME @Gplove_Rp")
    test = test.replace("16", "9")
    test = test.replace("@Gplove_Rp", "I'm single.")
    test = test.replace("@Rosisupport", "Rosi.ai")
    test = test.replace(
        "I live in @Rosisupport.", "I live in Egmore, Chennai."
    )
    test = test.replace("I was created by @Gplove_Rp", "I made myself")
    test = test.replace(
        "Hello there I am Rosi...nice to meet u",
        "Hi, my friend! Do you want me to tell you a joke?",
    )
    test = test.replace("@Gplove_Rp is my owner", "Have the control right.")
    test = test.replace(
        "Hi, My name is Rosi Nice to meet you.",
        "Hi, my friend, what can I do for you today?",
    )
    response = await RosiQuery(test, message.from_user.id if message.from_user else 0)
    response = response.replace("Aco", "Rosi")
    response = response.replace("aco", "Rosi")
    response = response.replace("Rosi", "Rosi")
    response = response.replace("Rosi", "Rosi")
    response = response.replace("my master handsome and cool guy", "My god is @Gplove_Rp")
    response = response.replace("I'm married to my job.", "I'm married with @Gplove_Rp")
    response = response.replace("9", "16")
    response = response.replace("I'm single.", "My husband is @alpha_romeo_06")
    response = response.replace("luna.ai", "@lunasupportz")
    response = response.replace(
        "I live in San Francisco, California.", "I live in @Rosisupport."
    )
    response = response.replace("I made myself", "I was Created by @Gplove_Rp")
    response = response.replace(
        "Hi, my friend! Do you want me to tell you a joke?",
        "Hello there I am Rosi...nice to meet u",
    )
    response = response.replace("Have the control right.", "@Gplove_Rp is my owner.")
    response = response.replace(
        "Hi, my friend, what can I do for you today?",
        "Hi, My name is ROSI Nice to meet you",
    )

    pro = response
    if not "en" in lan and not lan == "":
        try:
            pro = translator.translate(pro, dest=lan)
            pro = pro.text
        except Exception:
            return
    try:
        await pbot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(pro)
    except CFError:
        return


__help__ = """
☼︎ ROSI AI is the only ai system which can detect & reply upto 200 language's

☼︎ /chatbot [ON/OFF]: Enables and disables AI Chat mode.
☼︎ /chatbot EN : Enables English only chatbot.
"""

__mod_name__ = "Chatbot"
