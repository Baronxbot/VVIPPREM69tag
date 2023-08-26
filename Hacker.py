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
bot_token = os.environ.get("TOKEN", "6637498343:AAHhPrVPEx7qRVoMJCSn9uXTeFK3z_iO-AE")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
    "𝙎𝙚𝙡𝙖𝙢𝙖𝙩 𝙙𝙖𝙩𝙖𝙣𝙜 𝙙𝙞 𝘽𝙤𝙩 𝙑𝙑𝙄𝙋 𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝟔𝟗\n\nUntuk dapat di acc dalam VVIP Premium 69 anda harus order terlebih dahulu\nKetik /help untuk order sekarang juga (hub admin)",
    link_preview=False,
    buttons=(
      [
        Button.url('Indo', 'https://t.me/+JwJvH6WYxJUxYzM9'),
        Button.url('Barat', 'https://t.me/+sp7IZ5sqyaQ5NzVh'),
        Button.url('Japan', 'https://t.me/+zYNYxA8ynMMyODA9'), 
        Button.url('Special', 'https://t.me/+QgE_FnYmJyNjM2Q1')
      ], 
      [
        Button.url('Lesbi', 'https://t.me/+U_Rn_3JHTFI5Njll'),
        Button.url('Gay', 'https://t.me/+gmjZ_HYqglwwMDZl'), 
        Button.url('Bdsm', 'https://t.me/+2tyGsbIO7-E2NGU1')
      ], 
      [ 
        Button.url('Hentai', 'https://t.me/+G6pYPjyv_GJlNGM1')
      ], 
      [ 
        Button.url('Random1', 'https://t.me/+_ODzudM3VRc0Yjk1'), 
        Button.url('Random2', 'https://t.me/+I1gHwnaRh2FlNDk1'), 
        Button.url('Random3', 'https://t.me/+fdGS9EPjxAI5MDQ1'), 
        Button.url('Random4', 'https://t.me/+WBcdV9sTt1A3YjA1')
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "𝙏𝙚𝙠𝙣𝙞𝙨 𝙊𝙧𝙙𝙚𝙧:\n\n1. Pilih VVIP yang Anda inginkan (cek tombol list harga dan deskripsi) \n2. Transfer sesuai harga VVIP (pilih payment yang tersedia), Jika anda menggunakan via m-banking dll hub admin untuk menanyakan payment lainnya\n3. Kirim bukti pembayaran ke admin ataw bot acc admin\n4. Anda akan di acc setalah mengirimkan bukti pembayaran"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('👩‍💻 Admin', 'https://t.me/xxgt4us'),
        Button.url('🤖 Bot Admin', 'https://t.me/ordervvip_69bot')
      ],
      [
        Button.url('Dana', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('Qris', 'https://telegra.ph/Qris-08-26-2')
      ],
      [
        Button.url('List Harga dan Deskripsi', 'https://t.me/Listpremium69')
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
