from YashuAlpha.Database.sudo import add_sudo, del_sudo, is_sudo, get_sudos
from pyrogram import Client, filters
from pyrogram.types import Message
from config import STUFF, DEV
from .verify import verify

hl = STUFF.COMMAND_HANDLER

async def eor(m, t):
    await m.reply(t)

async def get_id(_, m):
    if str(m.chat.id)[0] != "-":
        return int(m.chat.id)
    if not m.reply_to_message:
        text = m.text.split()
        un_or_id = text[1]
        if un_or_id[0] == "@":
            id = (await _.get_users(un_or_id)).id
        else:
            id = int(un_or_id)
    else:
        id = m.reply_to_message.from_user.id
    return id 

@Client.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(DEV.OWNER_ID))
async def add_or_del_sudo(_, m):
    try:
        id = await get_id(_, m)
    except:
        return await eor(m, f"<i>{hl}addsudo or {hl}rmsudo [Reply | Username | Id]</id>")
    sudo = await is_sudo(id)
    if m.text.split()[0][1].lower() == "r":
        if not sudo:
            return await eor(m, f"<i>This user isn't sudo..!</i>")
        await del_sudo(id)
        return await eor(m, f"<i>Sudo removed for the user {id} .</i>")
    if sudo:
        return await eor(m, f"<i>{id} is already a sudo user..!</i>")
    await add_sudo(id)
    return await eor(m, f"<i>{id} is added to sudo...!</i>")

@Client.on_message(filters.command("sudos", hl))
async def sudo_users(_, m):
    if not await verify(m.from_user.id):
        return
    SUDOS = await get_sudos()
    if not SUDOS:
        return await eor(m, f"<i>No sudo users..!</i>")
    msg = ""
    for SUDO in SUDOS:
        SUDO = int(SUDO)
        msg += f"\n<code>{SUDO}</code>"
    return await eor(m, f"<i>Sudo :-</i>\n{msg}\n\n<i>Count :- {len(SUDOS)}</i>")
