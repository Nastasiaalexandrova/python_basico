# import logging
# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from datetime import datetime, timedelta
# from database import add_booking, get_available_slots
# from email_utils import send_email
# from aiogram.filters import Command
# # from email_utils import executor
# # from aiogram.types.message import ParseMode


# TOKEN = "7690334241:AAGrVRJP-6zQR4CnMoUaFAMs2GuiRbyI-k0"

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=TOKEN)
# dp = Dispatcher(storage=MemoryStorage())

# # Define FSM states
# class BookingState(StatesGroup):
#     name = State()
#     phone = State()
#     email = State()
#     service = State()
#     option = State()
#     date = State()
#     time = State()

# # 1️⃣ Start Command
# from aiogram.filters import Command

# @dp.message(Command("start"))
# async def start(message: types.Message):
#     # Create a keyboard with two buttons
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="Button 1"), KeyboardButton(text="Button 2")],
#             [KeyboardButton("📅 Book an Appointment")]
#         ],
#         resize_keyboard=True
#     )
#     await message.answer("Welcome to the Beauty Salon Romashka! Click below to start booking:", reply_markup=keyboard)


# # 2️⃣ Begin Booking Process
# @dp.message(lambda msg: msg.text == "📅 Book an Appointment")
# async def ask_name(message: types.Message, state: FSMContext):
#     await state.set_state(BookingState.name)
#     await message.answer("Please enter your full name:")

# @dp.message(BookingState.name)
# async def ask_phone(message: types.Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(BookingState.phone)
#     await message.answer("Enter your phone number:")

# @dp.message(BookingState.phone)
# async def ask_email(message: types.Message, state: FSMContext):
#     await state.update_data(phone=message.text)
#     await state.set_state(BookingState.email)
#     await message.answer("Enter your email address:")

# # 3️⃣ Choose Service
# @dp.message(BookingState.email)
# async def ask_service(message: types.Message, state: FSMContext):
#     await state.update_data(email=message.text)
#     keyboard = InlineKeyboardMarkup(row_width=2)
#     services = ["Manicure", "Pedicure", "Haircut", "Hair Coloring", "Keratin", "Eyelash Extensions"]
#     for service in services:
#         keyboard.add(InlineKeyboardButton(service, callback_data=f"service_{service}"))
#     await message.answer("Choose a service:", reply_markup=keyboard)

# @dp.callback_query(lambda c: c.data.startswith("service_"))
# async def ask_option(callback: types.CallbackQuery, state: FSMContext):
#     service = callback.data.split("_")[1]
#     await state.update_data(service=service)

#     if service in ["Haircut", "Hair Coloring", "Keratin"]:
#         keyboard = InlineKeyboardMarkup()
#         for length in ["Up to 15cm", "Up to 30cm", "Longer"]:
#             keyboard.add(InlineKeyboardButton(length, callback_data=f"option_{length}"))
#         await callback.message.answer("Choose hair length:", reply_markup=keyboard)
#     else:
#         await state.update_data(option="-")
#         await ask_date(callback.message, state)

# @dp.callback_query(lambda c: c.data.startswith("option_"))
# async def ask_date(callback: types.CallbackQuery, state: FSMContext):
#     option = callback.data.split("_")[1]
#     await state.update_data(option=option)

#     keyboard = InlineKeyboardMarkup()
#     today = datetime.today()
#     for i in range(1, 90):  
#         date = (today + timedelta(days=i)).strftime("%Y-%m-%d")
#         keyboard.add(InlineKeyboardButton(date, callback_data=f"date_{date}"))
#     await callback.message.answer("Choose a date:", reply_markup=keyboard)

# @dp.callback_query(lambda c: c.data.startswith("date_"))
# async def ask_time(callback: types.CallbackQuery, state: FSMContext):
#     date = callback.data.split("_")[1]
#     await state.update_data(date=date)

#     available_times = get_available_slots(date)
#     keyboard = InlineKeyboardMarkup(row_width=3)
#     for time in available_times:
#         keyboard.add(InlineKeyboardButton(time, callback_data=f"time_{time}"))

#     if available_times:
#         await callback.message.answer("Choose a time:", reply_markup=keyboard)
#     else:
#         await callback.message.answer("No available slots for this day. Choose another date.")

# @dp.callback_query(lambda c: c.data.startswith("time_"))
# async def confirm_booking(callback: types.CallbackQuery, state: FSMContext):
#     time = callback.data.split("_")[1]
#     data = await state.get_data()

#     add_booking(data["name"], data["phone"], data["email"], data["service"], data["option"], data["date"], time)

#     email_body = f"Hello {data['name']}, your booking is confirmed for {data['service']} on {data['date']} at {time}."
#     await send_email(data["email"], "Booking Confirmation", email_body)

#     await callback.message.answer("✅ Your booking is confirmed! Check your email.")
#     await state.clear()

# async def main():
#     # await dp.start_polling(bot)
#     await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


# if __name__ == "__main__":
#     asyncio.run(main())







# import logging
# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from datetime import datetime, timedelta
# from database import add_booking, get_available_slots
# from email_utils import send_email
# from aiogram.filters import Command

# # Configure logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler("bot_debug.log", encoding="utf-8"),
#         logging.StreamHandler()
#     ]
# )

# logger = logging.getLogger(__name__)

# TOKEN = "7690334241:AAGrVRJP-6zQR4CnMoUaFAMs2GuiRbyI-k0"
# bot = Bot(token=TOKEN)
# dp = Dispatcher(storage=MemoryStorage())

# # Define FSM states
# class BookingState(StatesGroup):
#     name = State()
#     phone = State()
#     email = State()
#     service = State()
#     option = State()
#     date = State()
#     time = State()

# # 1️⃣ Start Command with error handling
# @dp.message(Command("start"))
# async def start(message: types.Message):
#     try:
#         logger.info(f"Received /start command from user_id: {message.from_user.id}")
#         # Create a keyboard with buttons - FIXED SYNTAX
#         keyboard = ReplyKeyboardMarkup(
#             keyboard=[
#                 [KeyboardButton(text="Button 1"), KeyboardButton(text="Button 2")],
#                 [KeyboardButton(text="📅 Book an Appointment")]
#             ],
#             resize_keyboard=True
#         )
#         await message.answer("Welcome to the Beauty Salon Romashka! Click below to start booking:", reply_markup=keyboard)
#         logger.info(f"Successfully sent welcome message to user_id: {message.from_user.id}")
#     except Exception as e:
#         logger.error(f"Error in /start command: {e}", exc_info=True)

# # 2️⃣ Begin Booking Process - FIXED SYNTAX
# @dp.message(lambda msg: msg.text == "📅 Book an Appointment")
# async def ask_name(message: types.Message, state: FSMContext):
#     try:
#         await state.set_state(BookingState.name)
#         await message.answer("Please enter your full name:")
#         logger.info(f"Asked for name from user_id: {message.from_user.id}")
#     except Exception as e:
#         logger.error(f"Error in ask_name: {e}", exc_info=True)

# @dp.message(BookingState.name)
# async def ask_phone(message: types.Message, state: FSMContext):
#     try:
#         await state.update_data(name=message.text)
#         await state.set_state(BookingState.phone)
#         await message.answer("Enter your phone number:")
#         logger.info(f"Asked for phone from user_id: {message.from_user.id}")
#     except Exception as e:
#         logger.error(f"Error in ask_phone: {e}", exc_info=True)

# @dp.message(BookingState.phone)
# async def ask_email(message: types.Message, state: FSMContext):
#     try:
#         await state.update_data(phone=message.text)
#         await state.set_state(BookingState.email)
#         await message.answer("Enter your email address:")
#         logger.info(f"Asked for email from user_id: {message.from_user.id}")
#     except Exception as e:
#         logger.error(f"Error in ask_email: {e}", exc_info=True)

# # 3️⃣ Choose Service - FIXED SYNTAX
# @dp.message(BookingState.email)
# async def ask_service(message: types.Message, state: FSMContext):
#     try:
#         await state.update_data(email=message.text)
#         keyboard = InlineKeyboardMarkup(inline_keyboard=[])
#         services = ["Manicure", "Pedicure", "Haircut", "Hair Coloring", "Keratin", "Eyelash Extensions"]
        
#         # Build keyboard in rows of 2 buttons
#         for i in range(0, len(services), 2):
#             row = []
#             row.append(InlineKeyboardButton(text=services[i], callback_data=f"service_{services[i]}"))
#             if i + 1 < len(services):
#                 row.append(InlineKeyboardButton(text=services[i+1], callback_data=f"service_{services[i+1]}"))
#             keyboard.inline_keyboard.append(row)
        
#         await message.answer("Choose a service:", reply_markup=keyboard)
#         logger.info(f"Asked for service from user_id: {message.from_user.id}")
#     except Exception as e:
#         logger.error(f"Error in ask_service: {e}", exc_info=True)

# # General message handler to catch all messages
# @dp.message()
# async def echo_all(message: types.Message):
#     logger.info(f"Received message: '{message.text}' from user_id: {message.from_user.id}")
#     if message.text and message.text.startswith('/'):
#         logger.warning(f"Received unhandled command: {message.text}")
#         await message.answer(f"Received command {message.text}, but it wasn't properly processed. Try /start instead.")

# async def main():
#     try:
#         logger.info("Starting the bot...")
#         await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
#     except Exception as e:
#         logger.critical(f"Critical error when starting the bot: {e}", exc_info=True)

# if __name__ == "__main__":
#     asyncio.run(main())
# worked 26/02


import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from datetime import datetime, timedelta
import calendar
from aiogram.filters import Command
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot_debug.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

TOKEN = "7690334241:AAGrVRJP-6zQR4CnMoUaFAMs2GuiRbyI-k0"
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Email configuration
EMAIL_SENDER = "salon.romashka@example.com"
EMAIL_PASSWORD = "your_email_password"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

# Define FSM states
class BookingState(StatesGroup):
    name = State()
    phone = State()
    email = State()
    service = State()
    sub_option = State()
    additional_option = State()
    date = State()
    time = State()
    confirmation = State()

# Database setup
def init_db():
    conn = sqlite3.connect("salon_bookings.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT,
        email TEXT,
        service TEXT,
        sub_option TEXT,
        additional_option TEXT,
        booking_date TEXT,
        booking_time TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()
    logger.info("Database initialized")

# Get available time slots for a specific date
def get_available_slots(date_str):
    conn = sqlite3.connect("salon_bookings.db")
    cursor = conn.cursor()
    
    # Get all booked slots for the date
    cursor.execute("SELECT booking_time FROM bookings WHERE booking_date = ?", (date_str,))
    booked_times = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    # Salon working hours from 8:00 to 20:00, each service takes 2 hours
    all_slots = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00"]
    available_slots = [slot for slot in all_slots if slot not in booked_times]
    
    return available_slots

# Add a booking to the database
def add_booking(name, phone, email, service, sub_option, additional_option, date_str, time_str):
    conn = sqlite3.connect("salon_bookings.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO bookings (name, phone, email, service, sub_option, additional_option, booking_date, booking_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, phone, email, service, sub_option, additional_option, date_str, time_str))
    
    conn.commit()
    conn.close()
    logger.info(f"Added booking for {name} on {date_str} at {time_str}")
    return True

# Send confirmation email
def send_email(recipient, name, service, sub_option, additional_option, date_str, time_str):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = recipient
        msg['Subject'] = "Beauty Salon Romashka - Booking Confirmation"
        
        body = f"""
        Dear {name},
        
        Thank you for booking with Beauty Salon Romashka!
        
        Your appointment details:
        Service: {service}
        Option: {sub_option}
        Additional: {additional_option}
        Date: {date_str}
        Time: {time_str}
        
        We look forward to seeing you!
        
        Best regards,
        Beauty Salon Romashka
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_SENDER, recipient, text)
        server.quit()
        
        logger.info(f"Confirmation email sent to {recipient}")
        return True
    except Exception as e:
        logger.error(f"Error sending email: {e}", exc_info=True)
        return False

# Start Command
@dp.message(Command("start"))
async def start(message: types.Message):
    try:
        logger.info(f"Received /start command from user_id: {message.from_user.id}")
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📅 Записаться на прием")]
            ],
            resize_keyboard=True
        )
        await message.answer("Добро пожаловать в салон красоты Ромашка! Нажмите на кнопку ниже, чтобы записаться:", reply_markup=keyboard)
        logger.info(f"Successfully sent welcome message to user_id: {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in /start command: {e}", exc_info=True)

# Begin Booking Process
@dp.message(lambda msg: msg.text == "📅 Записаться на прием")
async def ask_service(message: types.Message, state: FSMContext):
    try:
        await state.set_state(BookingState.service)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[])
        services = ["Маникюр", "Педикюр", "Стрижка", "Покраска волос", "Кератин", "Наращивание ресниц"]
        
        # Build keyboard in rows of 2 buttons
        for i in range(0, len(services), 2):
            row = []
            row.append(InlineKeyboardButton(text=services[i], callback_data=f"service_{services[i]}"))
            if i + 1 < len(services):
                row.append(InlineKeyboardButton(text=services[i+1], callback_data=f"service_{services[i+1]}"))
            keyboard.inline_keyboard.append(row)
        
        await message.answer("Выберите услугу:", reply_markup=keyboard)
        logger.info(f"Asked for service from user_id: {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in ask_service: {e}", exc_info=True)

# Handle service selection
@dp.callback_query(lambda c: c.data.startswith("service_"))
async def process_service(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        service = callback_query.data.split("_")[1]
        await state.update_data(service=service)
        
        # Different options based on service type
        keyboard = InlineKeyboardMarkup(inline_keyboard=[])
        
        if service in ["Стрижка", "Покраска волос", "Кератин"]:
            # Hair length options
            options = ["До 15 см", "До 30 см", "Длиннее 30 см"]
            for option in options:
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(text=option, callback_data=f"sub_{option}")
                ])
                
        elif service in ["Маникюр", "Педикюр"]:
            # Manicure/pedicure options
            options = ["Аппаратный", "Классический"]
            for option in options:
                keyboard.inline_keyboard.append([
                    InlineKeyboardButton(text=option, callback_data=f"sub_{option}")
                ])
        else:
            # For eyelash extensions, go directly to name
            await state.update_data(sub_option="Стандартный", additional_option="Стандартный")
            await state.set_state(BookingState.name)
            await bot.send_message(callback_query.from_user.id, "Введите ваше полное имя:")
            await callback_query.answer()
            return
            
        await state.set_state(BookingState.sub_option)
        await bot.send_message(callback_query.from_user.id, "Выберите вариант:", reply_markup=keyboard)
        
        await callback_query.answer()
        logger.info(f"Selected service: {service} for user_id: {callback_query.from_user.id}")
    except Exception as e:
        logger.error(f"Error in process_service: {e}", exc_info=True)

# Handle sub-option selection
@dp.callback_query(lambda c: c.data.startswith("sub_"))
async def process_sub_option(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        sub_option = callback_query.data.split("_")[1]
        await state.update_data(sub_option=sub_option)
        user_data = await state.get_data()
        
        if user_data["service"] in ["Маникюр", "Педикюр"]:
            # For manicure/pedicure, ask about permanent/without color
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="С покрытием", callback_data="add_permanent")],
                [InlineKeyboardButton(text="Без покрытия", callback_data="add_without")]
            ])
            await state.set_state(BookingState.additional_option)
            await bot.send_message(callback_query.from_user.id, "Выберите дополнительный вариант:", reply_markup=keyboard)
        else:
            # For hair services, go to name input
            await state.update_data(additional_option="Стандартный")
            await state.set_state(BookingState.name)
            await bot.send_message(callback_query.from_user.id, "Введите ваше полное имя:")
        
        await callback_query.answer()
        logger.info(f"Selected sub-option: {sub_option} for user_id: {callback_query.from_user.id}")
    except Exception as e:
        logger.error(f"Error in process_sub_option: {e}", exc_info=True)

# Handle additional option selection
@dp.callback_query(lambda c: c.data.startswith("add_"))
async def process_additional_option(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        additional_option = callback_query.data.split("_")[1]
        await state.update_data(additional_option=additional_option)
        
        # Move to collecting personal info
        await state.set_state(BookingState.name)
        await bot.send_message(callback_query.from_user.id, "Введите ваше полное имя:")
        
        await callback_query.answer()
        logger.info(f"Selected additional option: {additional_option} for user_id: {callback_query.from_user.id}")
    except Exception as e:
        logger.error(f"Error in process_additional_option: {e}", exc_info=True)

# Handle name input
@dp.message(BookingState.name)
async def process_name(message: types.Message, state: FSMContext):
    try:
        await state.update_data(name=message.text)
        await state.set_state(BookingState.phone)
        await message.answer("Введите ваш номер телефона:")
        logger.info(f"Received name: {message.text} from user_id: {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in process_name: {e}", exc_info=True)

# Handle phone input
@dp.message(BookingState.phone)
async def process_phone(message: types.Message, state: FSMContext):
    try:
        await state.update_data(phone=message.text)
        await state.set_state(BookingState.email)
        await message.answer("Введите ваш email для получения подтверждения:")
        logger.info(f"Received phone: {message.text} from user_id: {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in process_phone: {e}", exc_info=True)

# Handle email input
@dp.message(BookingState.email)
async def process_email(message: types.Message, state: FSMContext):
    try:
        await state.update_data(email=message.text)
        await state.set_state(BookingState.date)
        
        # Generate calendar for next 3 months
        current_date = datetime.now()
        keyboard = InlineKeyboardMarkup(inline_keyboard=[])
        
        # Generate dates for the next 3 months
        for month_offset in range(3):
            month_date = current_date + timedelta(days=month_offset*30)
            month_name = month_date.strftime('%B')
            month_year = month_date.strftime('%Y-%m')
            
            keyboard.inline_keyboard.append([
                InlineKeyboardButton(text=f"{month_name} {month_date.year}", callback_data=f"month_{month_year}")
            ])
        
        await message.answer("Выберите месяц для записи:", reply_markup=keyboard)
        logger.info(f"Received email: {message.text} from user_id: {message.from_user.id}")
    except Exception as e:
        logger.error(f"Error in process_email: {e}", exc_info=True)

# Handle month selection
@dp.callback_query(lambda c: c.data.startswith("month_"))
async def process_month(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        month_year = callback_query.data.split("_")[1]
        year, month = map(int, month_year.split('-'))
        
        # Generate calendar for selected month
        keyboard = InlineKeyboardMarkup(inline_keyboard=[])
        
        # Get the number of days in the month
        _, num_days = calendar.monthrange(year, month)
        
        current_date = datetime.now()
        
        # Build calendar in rows of 7 days
        day_buttons = []
        for day in range(1, num_days + 1):
            date_obj = datetime(year, month, day)
            
            # Skip past dates
            if date_obj.date() < current_date.date():
                continue
                
            date_str = date_obj.strftime('%Y-%m-%d')
            
            # Check if there are available slots for this date
            available_slots = get_available_slots(date_str)
            if not available_slots:
                continue  # Skip days with no available slots
                
            day_buttons.append(
                InlineKeyboardButton(text=str(day), callback_data=f"date_{date_str}")
            )
            
            # Create rows of 7 buttons (for 7 days of week)
            if len(day_buttons) == 7:
                keyboard.inline_keyboard.append(day_buttons)
                day_buttons = []
        
        # Add any remaining days
        if day_buttons:
            keyboard.inline_keyboard.append(day_buttons)
            
        # Add back button
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(text="« Назад к выбору месяца", callback_data="back_to_months")
        ])
        
        await bot.send_message(
            callback_query.from_user.id, 
            f"Выберите день для записи (показаны только дни со свободным временем):",
            reply_markup=keyboard
        )
        
        await callback_query.answer()
        logger.info(f"Selected month: {month_year} for user_id: {callback_query.from_user.id}")
    except Exception as e:
        logger.error(f"Error in process_month: {e}", exc_info=True)

# Handle back to months
@dp.callback_query(lambda c: c.data == "back_to_months")
async def back_to_months(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        # Generate calendar for next 3 months
        current_date = datetime.now()
        keyboard = InlineKeyboardMarkup(inline_keyboard=[])
        
        # Generate dates for the next 3 months
        for month_offset in range(3):
            month_date = current_date + timedelta(days=month_offset*30)
            month_name = month_date.strftime('%B')
            month_year = month_date.strftime('%Y-%m')
            
            keyboard.inline_keyboard.append([
                InlineKeyboardButton(text=f"{month_name} {month_date.year}", callback_data=f"month_{month_year}")
            ])
        
        await bot.send_message(
            callback_query.from_user.id,
            "Выберите месяц для записи:",
            reply_markup=keyboard
        )
        
        await callback_query.answer()
    except Exception as e:
        logger.error(f"Error in back_to_months: {e}", exc_info=True)

# Handle date selection
@dp.callback_query(lambda c: c.data.startswith("date_"))
async def process_date(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        date_str = callback_query.data.split("_")[1]
        await state.update_data(date=date_str)
        
        # Get available time slots for the selected date
        available_slots = get_available_slots(date_str)
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=[])
        for slot in available_slots:
            keyboard.inline_keyboard.append([
                InlineKeyboardButton(text=slot, callback_data=f"time_{slot}")
            ])
            
        # Add back button
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(text="« Назад к выбору дня", callback_data=f"back_to_days")
        ])
        
        formatted_date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%d.%m.%Y')
        await bot.send_message(
            callback_query.from_user.id,
            f"Выберите удобное время для записи на {formatted_date}:",
            reply_markup=keyboard
        )
        
        await state.set_state(BookingState.time)
        await callback_query.answer()
        logger.info(f"Selected date: {date_str} for user_id: {callback_query.from_user.id}")
    except Exception as e:
        logger.error(f"Error in process_date: {e}", exc_info=True)

# Handle back to days
@dp.callback_query(lambda c: c.data == "back_to_days")
async def back_to_days(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        user_data = await state.get_data()
        if "date" in user_data:
            date_obj = datetime.strptime(user_data["date"], '%Y-%m-%d')
            month_year = date_obj.strftime('%Y-%m')
            
            # Trigger the month selection handler with the current month
            callback_query.data = f"month_{month_year}"
            await process_month(callback_query, state)
        else:
            # If no date is stored, go back to months
            await back_to_months(callback_query, state)
            
        await callback_query.answer()
    except Exception as e:
        logger.error(f"Error in back_to_days: {e}", exc_info=True)

# Handle time selection
@dp.callback_query(lambda c: c.data.startswith("time_"))
async def process_time(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        time_str = callback_query.data.split("_")[1]
        await state.update_data(time=time_str)
        
        # Get all booking details for confirmation
        user_data = await state.get_data()
        
        formatted_date = datetime.strptime(user_data["date"], '%Y-%m-%d').strftime('%d.%m.%Y')
        
        confirmation_text = f"""
Пожалуйста, подтвердите вашу запись:

Имя: {user_data['name']}
Телефон: {user_data['phone']}
Email: {user_data['email']}
Услуга: {user_data['service']}
Вариант: {user_data['sub_option']}
Дополнительно: {user_data['additional_option']}
Дата: {formatted_date}
Время: {time_str}
        """
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm_booking")],
            [InlineKeyboardButton(text="❌ Отменить", callback_data="cancel_booking")]
        ])
        
        await bot.send_message(
            callback_query.from_user.id,
            confirmation_text,
            reply_markup=keyboard
        )
        
        await state.set_state(BookingState.confirmation)
        await callback_query.answer()
        logger.info(f"Selected time: {time_str} for user_id: {callback_query.from_user.id}")
    except Exception as e:
        logger.error(f"Error in process_time: {e}", exc_info=True)

# Handle booking confirmation
@dp.callback_query(lambda c: c.data == "confirm_booking")
async def confirm_booking(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        user_data = await state.get_data()
        
        # Add booking to database
        booking_success = add_booking(
            user_data['name'], 
            user_data['phone'], 
            user_data['email'],
            user_data['service'],
            user_data['sub_option'],
            user_data['additional_option'],
            user_data['date'],
            user_data['time']
        )
        
        if booking_success:
            # Send confirmation email
            email_sent = send_email(
                user_data['email'],
                user_data['name'],
                user_data['service'],
                user_data['sub_option'],
                user_data['additional_option'],
                user_data['date'],
                user_data['time']
            )
            
            email_status = "Письмо с подтверждением отправлено на ваш email." if email_sent else "Не удалось отправить письмо с подтверждением."
            
            formatted_date = datetime.strptime(user_data["date"], '%Y-%m-%d').strftime('%d.%m.%Y')
            
            await bot.send_message(
                callback_query.from_user.id,
                f"""
Ваша запись успешно подтверждена!

Имя: {user_data['name']}
Услуга: {user_data['service']} ({user_data['sub_option']}, {user_data['additional_option']})
Дата и время: {formatted_date}, {user_data['time']}

{email_status}

Спасибо за запись в салон красоты Ромашка!
                """
            )
        else:
            await bot.send_message(
                callback_query.from_user.id,
                "К сожалению, произошла ошибка при создании записи. Пожалуйста, попробуйте снова или свяжитесь с нами по телефону."
            )
        
        # Reset state
        await state.clear()
        
        # Offer to book again
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📅 Записаться на прием")]
            ],
            resize_keyboard=True
        )
        await bot.send_message(
            callback_query.from_user.id,
            "Хотите записаться на еще одну услугу?",
            reply_markup=keyboard
        )
        
        await callback_query.answer()
        logger.info(f"Booking confirmed for user_id: {callback_query.from_user.id}")
    except Exception as e:
        logger.error(f"Error in confirm_booking: {e}", exc_info=True)

# Handle booking cancellation
@dp.callback_query(lambda c: c.data == "cancel_booking")
async def cancel_booking(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.clear()
        
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📅 Записаться на прием")]
            ],
            resize_keyboard=True
        )
        
        await bot.send_message(
            callback_query.from_user.id,
            "Запись отменена. Вы можете начать новую запись в любое время.",
            reply_markup=keyboard
        )
        
        await callback_query.answer()
        logger.info(f"Booking cancelled for user_id: {callback_query.from_user.id}")
    except Exception as e:
        logger.error(f"Error in cancel_booking: {e}", exc_info=True)

# General message handler to catch all messages
@dp.message()
async def echo_all(message: types.Message):
    logger.info(f"Received message: '{message.text}' from user_id: {message.from_user.id}")
    if message.text and message.text.startswith('/'):
        logger.warning(f"Received unhandled command: {message.text}")
        await message.answer(f"Получена команда {message.text}, но она не была обработана. Попробуйте /start.")

async def main():
    try:
        # Initialize database
        init_db()
        
        logger.info("Starting the bot...")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logger.critical(f"Critical error when starting the bot: {e}", exc_info=True)

if __name__ == "__main__":
    asyncio.run(main())