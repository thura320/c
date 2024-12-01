import requests
import random
from telebot import types


def lookBin(cc):

    try:
        data = requests.get(
            "https://lookup.binlist.net/" + str(cc)[:6], proxies=genProxy()
        ).json()
    except:
        pass

    try:
        bank = data["bank"]["name"]
    except:
        bank = "𝒖𝒏𝒌𝒏𝒐𝒘𝒏"
    try:
        emjj = data["country"]["emoji"]
    except:
        emjj = "𝒖𝒏𝒌𝒏𝒐𝒘𝒏"
    try:
        cn = data["country"]["name"]
    except:
        cn = "𝒖𝒏𝒌𝒏𝒐𝒘𝒏"
    try:
        dicr = data["scheme"]
    except:
        dicr = "𝒖𝒏𝒌𝒏𝒐𝒘𝒏"
    try:
        typ = data["type"]
    except:
        typ = "𝒖𝒏𝒌𝒏𝒐𝒘𝒏"
    try:
        url = data["bank"]["url"]
    except:
        url = "𝒖𝒏𝒌𝒏𝒐𝒘𝒏"
    return bank, emjj, cn, dicr, typ, url


def genProxy():
    with open("./proxy.txt", "r") as pro:
        prxoy = pro.read().splitlines()
    res = random.choice(prxoy).split("|")

    proxy_auth = "{}:{}@{}".format(res[1], res[2], res[0])
    proxies = {"http": "http://{}".format(proxy_auth)}
    return proxies


def cvvMsg(
    msg,
    cc,
    ip="Live",
    bank="Unknown",
    emj="Unknown",
    cn="Unknown",
    dicr="Unknown",
    typ="Unknown",
    url="Unknown",
):
    bank, emjj, cn, dicr, typ, url=lookBin(cc)
    emj=random.choice("❁❃❊❀✿❂✧✦☆❋✣✤✪✱✩✰✯✼✺۞⊙※𓇻❋✾❈❉❊")
    
    return f"""
    {emj}𝗖𝗮𝗿𝗱 ➜ {cc} 
  
»»-------------¤-------------««

{emj} 𝗚𝗮𝘁𝗲𝘄𝗮𝘆  ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 𝘼𝙐𝙏𝙃
{emj} 𝗦𝘁𝗮𝘁𝘂𝘀    ➜ 𝘾𝙑𝙑 𝘾𝙃𝘼𝙍𝙂𝙀𝘿 ✅
{emj} 𝗠𝗲𝘀𝘀𝗮𝗴𝗲  ➜ {msg}

{emj} 𝑷𝑹𝑶𝑿𝒀𝑺  ➜ {ip}
»»-------------¤-------------««
              ╭──────────╮
{emj} 𝗕𝗶𝗻 𝗜𝗻𝗳𝗼 ➜   {cc[:6]}
              ╰──────────╯
{emj} 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ➜ {cn}-{emj}
{emj} 𝗕𝗮𝗻𝗸   ➜ {bank}
{emj} 𝗧𝘆𝗽𝗲   ➜  {typ}-{dicr}
{emj} 𝗗𝗲𝘃    ➜ @chk1212"""


def ccnMsg(
    msg,
    cc,
    ip="Live",
):
    bank, emjj, cn, dicr, typ, url=lookBin(cc)
    emj=random.choice("❁❃❊❀✿❂✧✦☆❋✣✤✪✱✩✰✯✼✺۞⊙※𓇻❋✾❈❉❊")
    return f"""
    {emj} 𝗖𝗮𝗿𝗱 ➜ {cc} 
  
»»-------------¤-------------««

{emj} 𝗚𝗮𝘁𝗲𝘄𝗮𝘆  ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 𝘼𝙐𝙏𝙃
{emj} 𝗦𝘁𝗮𝘁𝘂𝘀    ➜ 𝘾𝘾𝙉 𝙇𝙄𝙑𝙀 ✅
{emj} 𝗠𝗲𝘀𝘀𝗮𝗴𝗲  ➜ {msg}

{emj} 𝑷𝑹𝑶𝑿𝒀𝑺  ➜ {ip}
»»-------------¤-------------««
              ╭──────────╮
{emj} 𝗕𝗶𝗻 𝗜𝗻𝗳𝗼 ➜   {cc[:6]}
              ╰──────────╯
{emj} 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ➜ {cn}-{emjj}
{emj} 𝗕𝗮𝗻𝗸   ➜ {bank}
{emj} 𝗧𝘆𝗽𝗲   ➜  {typ}-{dicr}
{emj} 𝗗𝗲𝘃    ➜ @chk1212"""


#     return f"""◆ 𝑪𝑨𝑹𝑫  ➜ {cc}
# ◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ {msg} ✅
# ◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘾𝘾𝙉 𝙇𝙄𝙑𝙀
# ◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 𝘼𝙐𝙏𝙃
# ━━━━━━━━━━━━━━━━━
# ◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ}
# ━━━━━━━━━━━━━━━━━
# ◆ 𝑩𝒀: @chk1212
# ◆𝑷𝑹𝑶𝑿𝒀𝑺: {str(ip)}✅ """


def cardResponseFilter(last, am):
    if "risk" in last:
        last = "Declined"
        return 400, last
    elif "Duplicate" in last:
        last = "Approved"
        return 300, last
    if "Thank you" in last or 'success' in last:
        last = f"𝗖𝗵𝗮𝗿𝗴𝗲𝗱 ${str(am)}"
        return 200, last
    elif "security code is incorrect" in last or "security code is invalid" in last:
        last = "𝘀𝗲𝗰𝘂𝗿𝗶𝘁𝘆 𝗰𝗼𝗱𝗲 𝗶𝘀 𝗶𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁"
        return 300, last
    elif "insufficient funds" in last:
        
        last = "𝐈𝐧𝐬𝐮𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐭 𝐟𝐮𝐧𝐝𝐬"
        return 300, last
    elif "support this type of purchase." in last:
    
        last = "𝗗𝗼𝗲𝘀 𝗻𝗼𝘁 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝘁𝗵𝗶𝘀 𝗽𝘂𝗿𝗰𝗵𝗮𝘀𝗲"
        return 300, last
    elif "customer" in last:
        
        last = "3🇩🇸 Gate"
        return 300, last
    elif "declined" in last:
        last = "Your card was declined."
        return 400, last
    else:
        return 400, last


def editMssg(cc, live, charge, dd, total, last, ip):
    mes = types.InlineKeyboardMarkup(row_width=1)
    cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data="u8")

    status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {last} •", callback_data="u8")
    IP = types.InlineKeyboardButton(f"• 𝗣𝗿𝗼𝘅𝘆 ➜ {ip} •", callback_data="u8")
    cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ] •", callback_data="x")
    cm6 = types.InlineKeyboardButton(
        f"• 𝗖𝗵𝗮𝗿𝗴𝗲𝗱 ✅ ➜ [ {charge} ] •", callback_data="x"
    )
    cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data="x")
    cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data="x")
    stop = types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏🛑 ]", callback_data="stop")
    mes.add(status, cm1, IP, cm6, cm3, cm4, cm5, stop)
    return mes
