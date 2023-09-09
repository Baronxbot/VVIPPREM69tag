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
    "Silahkan tekan salah satu command di bawah untuk melihat vvip premium yang tersedia\n\n𝗩𝗩𝗜𝗣 𝗜𝗡𝗗𝗢\n/vvip_indo — 📩 Untuk Melihat Channel dan  Order channel VVIP indo\n𝗩𝗩𝗜𝗣 𝗕𝗔𝗥𝗔𝗧\n/vvip_barat — 📩 Untuk Melihat Channel dan  Order channel VVIP barat\n𝗩𝗩𝗜𝗣 𝗝𝗔𝗣𝗔𝗡\n/vvip_japan — 📩 Untuk Melihat Channel dan  Order channel VVIP Japan\n\n𝗩𝗩𝗜𝗣 𝗚𝗔𝗬\n/vvip_gay — 📩 Untuk Melihat Channel dan  Order channel VVIP Gay\n𝗩𝗩𝗜𝗣 𝗟𝗘𝗦𝗕𝗬\n/vvip_lesby — 📩 Untuk Melihat Channel dan  Order channel VVIP LESBY\n𝗩𝗩𝗜𝗣 𝗕𝗗𝗦𝗠\n/vvip_bdsm — 📩 Untuk Melihat Channel dan  Order channel VVIP Bdsm\n\n𝗩𝗩𝗜𝗣 𝗥𝗔𝗡𝗗𝗢𝗠\n/vvip_random — 📩 Untuk Melihat Channel dan  Order channel VVIP Random\n𝗩𝗩𝗜𝗣 𝗛𝗘𝗡𝗧𝗔𝗜\n/vvip_hentai — 📩 Untuk Melihat Channel dan  Order channel VVIP Hentai\n\n𝗠𝗘𝗧𝗢𝗗𝗘 𝗣𝗘𝗠𝗕𝗔𝗬𝗔𝗥𝗔𝗡\n/order —  🛒 Untuk melanjutkan pembayaran\n\n𝗡𝗼𝘁𝗲 ❗️\nLakukan Pembayaran agar anda di acc dalam VVIP PREMIUM 69.",
    link_preview=False,
    buttons=(
      [
        Button.url('👀 Testy', 'https://t.me/+wrS0J0dsDh82NmI1')
      ]
    )
  )
    
@client.on(events.NewMessage(pattern="^/vvip_indo$"))
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
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ]
    )
  )
    
@client.on(events.NewMessage(pattern="^/vvip_japan$"))
async def start(event):
  await event.reply(
    "✨ Untuk dapat di acc anda harus transfer terlebih dahulu pilih opsi dana/qris, kirim bukti pembayaran dengan klik tombol Order.",
    link_preview=False,
    buttons=(
      [
        Button.url('🌀 List Harga dan Deskripsi', 'https://t.me/Listpremium69')
      ], 
      [
        Button.url('💌 Vvip Japan', 'https://t.me/+zYNYxA8ynMMyODA9'),
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ]
    )
  )   

@client.on(events.NewMessage(pattern="^/vvip_barat$"))
async def start(event):
  await event.reply(
    "✨ Untuk dapat di acc anda harus transfer terlebih dahulu pilih opsi dana/qris, kirim bukti pembayaran dengan klik tombol Order.",
    link_preview=False,
    buttons=(
      [
        Button.url('🌀 List Harga dan Deskripsi', 'https://t.me/Listpremium69')
      ], 
      [
        Button.url('💌 Vvip Barat', 'https://t.me/+sp7IZ5sqyaQ5NzVh'),
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ]
    )
  )  
    
@client.on(events.NewMessage(pattern="^/vvip_special$"))
async def start(event):
  await event.reply(
    "✨ Untuk dapat di acc anda harus transfer terlebih dahulu pilih opsi dana/qris, kirim bukti pembayaran dengan klik tombol Order.",
    link_preview=False,
    buttons=(
      [
        Button.url('🌀 List Harga dan Deskripsi', 'https://t.me/Listpremium69')
      ], 
      [
        Button.url('💌 Vvip Special', 'https://t.me/+QgE_FnYmJyNjM2Q1'),
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ]
    )
  )   

@client.on(events.NewMessage(pattern="^/vvip_gay$"))
async def start(event):
  await event.reply(
    "✨ Untuk dapat di acc anda harus transfer terlebih dahulu pilih opsi dana/qris, kirim bukti pembayaran dengan klik tombol Order.",
    link_preview=False,
    buttons=(
      [
        Button.url('🌀 List Harga dan Deskripsi', 'https://t.me/Listpremium69')
      ], 
      [
        Button.url('💌 Vvip Gay', 'https://t.me/+gmjZ_HYqglwwMDZl'), 
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ]
    )
  )   

@client.on(events.NewMessage(pattern="^/vvip_lesby$"))
async def start(event):
  await event.reply(
    "✨ Untuk dapat di acc anda harus transfer terlebih dahulu pilih opsi dana/qris, kirim bukti pembayaran dengan klik tombol Order.",
    link_preview=False,
    buttons=(
      [
        Button.url('🌀 List Harga dan Deskripsi', 'https://t.me/Listpremium69')
      ], 
      [
        Button.url('💌 Vvip Lesbi', 'https://t.me/+U_Rn_3JHTFI5Njll'),
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ]
    )
  )   

@client.on(events.NewMessage(pattern="^/vvip_bdsm$"))
async def start(event):
  await event.reply(
    "✨ Untuk dapat di acc anda harus transfer terlebih dahulu pilih opsi dana/qris, kirim bukti pembayaran dengan klik tombol Order.",
    link_preview=False,
    buttons=(
      [
        Button.url('🌀 List Harga dan Deskripsi', 'https://t.me/Listpremium69')
      ], 
      [
        Button.url('💌 Vvip Bdsm', 'https://t.me/+2tyGsbIO7-E2NGU1'), 
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ]
    )
  )   

@client.on(events.NewMessage(pattern="^/vvip_random$"))
async def start(event):
  await event.reply(
    "✨ Untuk dapat di acc anda harus transfer terlebih dahulu pilih opsi dana/qris, kirim bukti pembayaran dengan klik tombol Order.",
    link_preview=False,
    buttons=(
      [
        Button.url('🌀 List Harga dan Deskripsi', 'https://t.me/Listpremium69')
      ], 
      [
        Button.url('💌 Random1', 'https://t.me/+_ODzudM3VRc0Yjk1'), 
        Button.url('💌 Random2', 'https://t.me/+I1gHwnaRh2FlNDk1')
      ], 
      [ 
        Button.url('💌 Random3', 'https://t.me/+fdGS9EPjxAI5MDQ1'), 
        Button.url('💌 Random4', 'https://t.me/+WBcdV9sTt1A3YjA1')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ], 
      [
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start')
      ]
    )
  )   

@client.on(events.NewMessage(pattern="^/vvip_hentai$"))
async def start(event):
  await event.reply(
    "✨ Untuk dapat di acc anda harus transfer terlebih dahulu pilih opsi dana/qris, kirim bukti pembayaran dengan klik tombol Order.",
    link_preview=False,
    buttons=(
      [
        Button.url('🌀 List Harga dan Deskripsi', 'https://t.me/Listpremium69')
      ], 
      [
        Button.url('💌 Vvip Hentai', 'https://t.me/+gq8z-m94T2E4OWE1'), 
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ]
    )
  )   

@client.on(events.NewMessage(pattern="^/order$"))
async def start(event):
  await event.reply(
    "✨ Untuk dapat di acc anda harus transfer terlebih dahulu pilih opsi dana/qris, kirim bukti pembayaran dengan klik tombol Order.",
    link_preview=False,
    buttons=(
      [
        Button.url('🛒 Order', 'Https://t.me/ordervvip_69bot?start')
      ], 
      [
        Button.url('❤️ Dana ', 'https://link.dana.id/qr/owbvx6i'), 
        Button.url('❤️ Qris', 'https://telegra.ph/Qris-08-26-2')
      ]
    )
  )   

print(">> VVIP STARTED @nakama_asl<<")
client.run_until_disconnected()
