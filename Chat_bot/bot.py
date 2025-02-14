import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from datetime import datetime, timedelta
from database import add_booking, get_available_slots
from email_utils import send_email

TOKEN = "7690334241:AAGrVRJP-6zQR4CnMoUaFAMs2GuiRbyI-k0"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Define FSM states
class BookingState(StatesGroup):
    name = State()
    phone = State()
    email = State()
    service = State()
    option = State()
    date = State()
    time = State()

# 1️⃣ Start Command
from aiogram.filters import Command

@dp.message(Command("start"))

async def start(message: types.Message):
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

    # Create a keyboard with two buttons
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Button 1"), KeyboardButton(text="Button 2")]
        ],
        resize_keyboard=True
    )

    keyboard.add(KeyboardButton("📅 Book an Appointment"))
    await message.answer("Welcome to the Beauty Salon! Click below to start booking:", reply_markup=keyboard)

# 2️⃣ Begin Booking Process
@dp.message(lambda msg: msg.text == "📅 Book an Appointment")
async def ask_name(message: types.Message, state: FSMContext):
    await state.set_state(BookingState.name)
    await message.answer("Please enter your full name:")

@dp.message(BookingState.name)
async def ask_phone(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookingState.phone)
    await message.answer("Enter your phone number:")

@dp.message(BookingState.phone)
async def ask_email(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(BookingState.email)
    await message.answer("Enter your email address:")

# 3️⃣ Choose Service
@dp.message(BookingState.email)
async def ask_service(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    keyboard = InlineKeyboardMarkup(row_width=2)
    services = ["Manicure", "Pedicure", "Haircut", "Hair Coloring", "Keratin", "Eyelash Extensions"]
    for service in services:
        keyboard.add(InlineKeyboardButton(service, callback_data=f"service_{service}"))
    await message.answer("Choose a service:", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data.startswith("service_"))
async def ask_option(callback: types.CallbackQuery, state: FSMContext):
    service = callback.data.split("_")[1]
    await state.update_data(service=service)

    if service in ["Haircut", "Hair Coloring", "Keratin"]:
        keyboard = InlineKeyboardMarkup()
        for length in ["Up to 15cm", "Up to 30cm", "Longer"]:
            keyboard.add(InlineKeyboardButton(length, callback_data=f"option_{length}"))
        await callback.message.answer("Choose hair length:", reply_markup=keyboard)
    else:
        await state.update_data(option="-")
        await ask_date(callback.message, state)

@dp.callback_query(lambda c: c.data.startswith("option_"))
async def ask_date(callback: types.CallbackQuery, state: FSMContext):
    option = callback.data.split("_")[1]
    await state.update_data(option=option)

    keyboard = InlineKeyboardMarkup()
    today = datetime.today()
    for i in range(1, 90):  
        date = (today + timedelta(days=i)).strftime("%Y-%m-%d")
        keyboard.add(InlineKeyboardButton(date, callback_data=f"date_{date}"))
    await callback.message.answer("Choose a date:", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data.startswith("date_"))
async def ask_time(callback: types.CallbackQuery, state: FSMContext):
    date = callback.data.split("_")[1]
    await state.update_data(date=date)

    available_times = get_available_slots(date)
    keyboard = InlineKeyboardMarkup(row_width=3)
    for time in available_times:
        keyboard.add(InlineKeyboardButton(time, callback_data=f"time_{time}"))

    if available_times:
        await callback.message.answer("Choose a time:", reply_markup=keyboard)
    else:
        await callback.message.answer("No available slots for this day. Choose another date.")

@dp.callback_query(lambda c: c.data.startswith("time_"))
async def confirm_booking(callback: types.CallbackQuery, state: FSMContext):
    time = callback.data.split("_")[1]
    data = await state.get_data()

    add_booking(data["name"], data["phone"], data["email"], data["service"], data["option"], data["date"], time)

    email_body = f"Hello {data['name']}, your booking is confirmed for {data['service']} on {data['date']} at {time}."
    await send_email(data["email"], "Booking Confirmation", email_body)

    await callback.message.answer("✅ Your booking is confirmed! Check your email.")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
