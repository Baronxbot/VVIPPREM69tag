import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", "22825629"))
api_hash = os.environ.get("API_HASH", "e8db542482a1638b4e5b03ed1ddae521")
bot_token = os.environ.get("TOKEN", "6445056221:AAGPEJs9VS378GDfHdfqkWwVg6hN3UhGizQ")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
    "𝙎𝙚𝙡𝙖𝙢𝙖𝙩 𝙙𝙖𝙩𝙖𝙣𝙜 𝙙𝙞 𝘽𝙤𝙩 𝙑𝙑𝙄𝙋 𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝘾𝘼𝙎𝙀𝙔\n\nUntuk dapat di acc dalam VVIP Premium Casey anda harus order terlebih dahulu\nKetik /help untuk order sekarang juga (hub admin)",
    link_preview=False,
    buttons=(
      [
        Button.url('Indo', 'https://t.me/+ogAPs2a5V6Q5MDg1'),
        Button.url('Barat', 'https://t.me/+ZPGGejCtidI2YmZl'),
        Button.url('Japan', 'https://t.me/+AfnaaWvPy_M3OGZl'), 
        Button.url('Special', 'https://t.me/+2P_gt1UC8NUyNTdl')
      ], 
      [
        Button.url('Lesbi', 'https://t.me/+Dnj_Rl12uz4yNDQ9'),
        Button.url('Gay', 'https://t.me/+1jMoO7jdWfcyNDM9'), 
        Button.url('Bdsm', 'https://t.me/+SydNzuyT4nc1Mjc1')
      ], 
      [ 
        Button.url('Hentai', 'https://t.me/+G6pYPjyv_GJlNGM1'), 
      ], 
      [ 
        Button.url('Random1', 'https://t.me/+vafRZM3V_HI1N2Q1'), 
        Button.url('Random2', 'https://t.me/+vUJLYw2PQF0xNTA1')
        Button.url('Random3', 'https://t.me/+vafRZM3V_HI1N2Q1'), 
        Button.url('Random4', 'https://t.me/+vUJLYw2PQF0xNTA1')
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "𝙏𝙚𝙠𝙣𝙞𝙨 𝙊𝙧𝙙𝙚𝙧:\n\n1. Pilih VVIP yang Anda inginkan (cek tombol list harga dan deskripsi) \n2. Transfer sesuai harga VVIP (pilih payment yang tersedia), Jika anda menggunakan via m-banking hub admin\n3. Kirim bukti pembayaran ke admin ataw bot acc admin\n4. Anda akan di acc setalah mengirimkan bukti pembayaran"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('👩‍💻 Admin', 'https://t.me/CASEYYTRUSTED'),
        Button.url('Bot Admin', 'https://t.me/ordervvip_69bot')
      ],
      [
        Button.url('Dana', 'https://t.me/PemuasHasrat_Horny/46')
        Button.url('Ovo', 'https://t.me/pay_area69')
        Button.url('Gopay', 'https://t.me/pay_area69')
        Button.url('Qris', 'https://t.me/pay_area69')
      ],
      [
        Button.url('List Harga dan Deskripsi', 'https://t.me/PemuasHasrat_Horny/46')
      ]
    )
  )
    
@client.on(events.NewMessage(pattern="^/settings$"))
async def help(event):
  helptext = "Hungungi Bot Teknisi Jika ada Kendala Pada Setiap Bot Kami"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('🤖 Teknisi', 'https://t.me/teknisi69_bot')
      ]
    )
  )



print(">> VVIP STARTED @nakama_asl<<")
client.run_until_disconnected()
