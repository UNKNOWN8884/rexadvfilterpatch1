class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/REX_BOTZ>𝚃𝚎𝚊𝚖 𝚁𝚎𝚡 𝚋𝚘𝚝𝚜</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/Tanujairam123/Rexadvautofilter  

<b>DEVS:</b>
- <a href=https://t.me/REX_BOTZ>𝚃𝚎𝚊𝚖 𝚁𝚎𝚡 𝚋𝚘𝚝𝚜</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. 𝚎𝚟𝚊 𝚖𝚊𝚛𝚒𝚊 𝚜𝚑𝚘𝚞𝚕𝚍 𝚑𝚊𝚟𝚎 𝚊𝚍𝚖𝚒𝚗 𝚙𝚛𝚒𝚟𝚒𝚕𝚕𝚊𝚐𝚎..
2. 𝚘𝚗𝚕𝚢 𝚊𝚍𝚖𝚒𝚗𝚜 𝚌𝚊𝚗 𝚊𝚍𝚍 𝚏𝚒𝚕𝚝𝚎𝚛𝚜 𝚒𝚗 𝚊 𝚌𝚑𝚊𝚝.
3. 𝚊𝚕𝚎𝚛𝚝 𝚋𝚞𝚝𝚝𝚘𝚗𝚜 𝚑𝚊𝚟𝚎 𝚊 𝚕𝚒𝚖𝚒𝚝 𝚘𝚏 64 𝚌𝚑𝚊𝚛𝚊𝚌𝚝𝚎𝚛𝚜.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. 𝙼𝚊𝚔𝚎 𝚖𝚎 𝚝𝚑𝚎 𝚊𝚍𝚖𝚒𝚗 𝚘𝚏 𝚢𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚒𝚏 𝚒𝚝'𝚜 𝚙𝚛𝚒𝚟𝚊𝚝𝚎.
2. 𝙼𝚊𝚔𝚎 𝚜𝚞𝚛𝚎 𝚝𝚑𝚊𝚝 𝚢𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚍𝚘𝚎𝚜 𝚗𝚘𝚝 𝚌𝚘𝚗𝚝𝚊𝚒𝚗𝚜 𝚌𝚊𝚖 𝚛𝚒𝚙, 𝚙𝚘𝚛𝚗 𝚊𝚗𝚍 𝚏𝚊𝚔𝚎 𝚏𝚒𝚕𝚎𝚜.
3. 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝚝𝚑𝚎 𝚕𝚊𝚜𝚝 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚘 𝚖𝚎 𝚠𝚒𝚝𝚑 𝚚𝚞𝚘𝚝𝚎𝚜.
   𝙸'𝚕𝚕 𝚊𝚍𝚍 𝚊𝚕𝚕 𝚝𝚑𝚎 𝚏𝚒𝚕𝚎𝚜 𝚒𝚗 𝚝𝚑𝚊𝚝 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚝𝚘 𝚖𝚢 𝚍𝚋.."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙰 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽.
2. 𝚂𝙴𝙽𝙳 <code>/connect</code> 𝙵𝙾𝚁 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙽𝙶 𝙼𝙴 𝚃𝙾 𝚄𝚁 𝙿𝙼

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
𝚃𝙷𝙴𝚂𝙴 𝙰𝚁𝙴 𝚃𝙷𝙴 𝙴𝚇𝚃𝚁𝙰 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝙾𝙵 𝙴𝙼𝙸𝙻𝙸𝙰 𝙲𝙻𝙰𝚁𝙺𝙴

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
