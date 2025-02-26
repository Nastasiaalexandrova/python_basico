from aiogram import Bot
import asyncio

async def check_token():
    bot = Bot(token="7690334241:AAGrVRJP-6zQR4CnMoUaFAMs2GuiRbyI-k0")
    try:
        print(await bot.get_me())
    finally:
        await bot.session.close()  # Ensure the client session is closed

asyncio.run(check_token())



# from aiogram import Bot
# import asyncio

# async def check_token():
#     bot = Bot(token="7690334241:AAGrVRJP-6zQR4CnMoUaFAMs2GuiRbyI-k0")
#     print(await bot.get_me())

# asyncio.run(check_token())
