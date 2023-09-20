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
    "✨ Untuk dapat di acc anda harus transfer terlebih dahulu pilih opsi dana/qris, kirim bukti pembayaran dengan klik tombol Order.",
    link_preview=False,
    buttons=(
      [
        Button.url('🌀 List Harga dan Deskripsi', 'https://t.me/Listpremium69')
      ], 
      [
        Button.url('💌 Vvip Indo', 'https://t.me/+JwJvH6WYxJUxYzM9'),
        Button.url('💌 Vvip Japan', 'https://t.me/+zYNYxA8ynMMyODA9'),
        Button.url('💌 Vvip Barat', 'https://t.me/+sp7IZ5sqyaQ5NzVh')
      ], 
      [
        Button.url('💌 Vvip Bdsm', 'https://t.me/+2tyGsbIO7-E2NGU1'),
        Button.url('💌 Vvip Gay', 'https://t.me/+gmjZ_HYqglwwMDZl'),
        Button.url('💌 Vvip Lesbi', 'https://t.me/+U_Rn_3JHTFI5Njll')
      ], 
      [
        
        Button.url('💌 Vvip Special', 'https://t.me/+4JQ3EUkO5KFjYjA1'),
        Button.url('💌 Vvip Hentai', 'https://t.me/+gq8z-m94T2E4OWE1'), 
        Button.url('💌 Random', 'https://t.me/+WBcdV9sTt1A3YjA1')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start'),
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ]
    )
  )
    

print(">> VVIP STARTED @nakama_asl<<")
client.run_until_disconnected()
