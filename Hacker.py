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
    "✨ 𝗦𝗲𝗹𝗮𝗺𝗮𝘁 𝗗𝗮𝗻𝘁𝗮𝗻𝗴 𝗗𝗶 𝗩𝗩𝗜𝗣 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝟲𝟵 \n\n➡️ Silahkan Pilih VVIP yang Anda Inginkan (Cek list harga dan deskripsi) \n➡️ Untuk dapat di acc dalam VVIP anda harus tf terlebih dahulu sesuai dengan harga VVIP ke payment kami (pilih opsi dana dan qris, hubungi admin jika anda tf menggunakan opsi lain) \n➡️ Kirim bukti pembayaran pada bot asisten admin dengan Klik Order Sekarang.",
    link_preview=False,
    buttons=(
      [
        Button.url('List Harga dan Deskripsi', 'https://t.me/Listpremium69')
      ], 
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
        Button.url('Hentai', 'https://t.me/+vT6fFhFvsNZhN2Vl')
      ], 
      [ 
        Button.url('Random1', 'https://t.me/+_ODzudM3VRc0Yjk1'), 
        Button.url('Random2', 'https://t.me/+I1gHwnaRh2FlNDk1'), 
        Button.url('Random3', 'https://t.me/+fdGS9EPjxAI5MDQ1'), 
        Button.url('Random4', 'https://t.me/+WBcdV9sTt1A3YjA1')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ],
      [
        Button.url('🛒 Order Sekarang', 'Https://t.me/ordervvip_69bot?start')
      ]
    )
  )


print(">> VVIP STARTED @nakama_asl<<")
client.run_until_disconnected()
