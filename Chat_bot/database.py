# import sqlite3

# DB_NAME = "bookings.db"

# def init_db():
#     """ Initializes the database and creates the bookings table. """
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS bookings (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             phone TEXT,
#             email TEXT,
#             service TEXT,
#             option TEXT,
#             date TEXT,
#             time TEXT
#         )
#     """)
#     conn.commit()
#     conn.close()

# def add_booking(name, phone, email, service, option, date, time):
#     """ Adds a new booking to the database. """
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     cursor.execute("""
#         INSERT INTO bookings (name, phone, email, service, option, date, time)
#         VALUES (?, ?, ?, ?, ?, ?, ?)
#     """, (name, phone, email, service, option, date, time))
#     conn.commit()
#     conn.close()

# def get_available_slots(date):
#     """ Returns available time slots for a given date. """
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#     cursor.execute("SELECT time FROM bookings WHERE date = ?", (date,))
#     booked_times = {row[0] for row in cursor.fetchall()}
#     conn.close()

#     all_slots = [f"{hour}:00" for hour in range(8, 20, 2)]
#     return [slot for slot in all_slots if slot not in booked_times]

# init_db()



