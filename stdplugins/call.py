"""
Available Commands
.call"""

from telethon import events

import asyncio








@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

  if event.fwd_from:

      return
      
animation_interval = 3

animation_ttl = range(0, 20)

input_str = event.pattern_match.group(1)

if input_str == "call":

   await event.edit(input_str)

   animation_chars = [
   
     "`connecting to telegram headquarters...`",
     "`call connected.`",
     "`Telegram: Hlw this is telegram hq. who is this??`",
     "`Me: चाचा बोल रहा हूं भोसडीके मेरे भाई गंजेड़ी को कॉल लगा`",
     "`user authorised...`",
     "`calling गंजेड़ी` `at 7890542378`",
     "`private call connected`",
     "`me: हेल्लो गंजेड़ी भाई कहा हैं`",
     "`गंजेड़ी: कोन भोसडिका बोल रहा हैै`",
     "`me: अबे चाचा बोल रहे हैं हम`",
     "`गंजेड़ी: राम राम चाचा`",
     "`me: राम राम पुत्र`",
     "`गंजेड़ी: कैसे याद किया आज`",
     "`me: आज बहुत बडी चोट हो गई हमारे साथ`",
     "`गंजेड़ी: क्या हुआ चाचा सब ठीक तो ह ना`",
     "`me: तुम्हारी चाची खड़े लंड पे लात मार गई`",
     "`गंजेड़ी: तो हम क्या करे`",
     "`me: चाचा विधायक है हमारे`",
     "`गंजेड़ी: bye`",
     "`private call disconnect.`"
  ]
  
  for i in animation_ttl:
  
      await asyncio.sleep(animation_interval)
      
      await event.edit(animation_chars[i % 20])
