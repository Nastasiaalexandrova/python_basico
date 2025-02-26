import sqlite3
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

DB_FILE = "salon_bookings.db"

def init_db():
    """Initialize the database with required tables"""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Create bookings table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            service TEXT NOT NULL,
            sub_option TEXT NOT NULL,
            additional_option TEXT NOT NULL,
            booking_date TEXT NOT NULL,
            booking_time TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        conn.commit()
        conn.close()
        logger.info("Database initialized successfully")
        return True
    except Exception as e:
        logger.error(f"Error initializing database: {e}", exc_info=True)
        return False

def get_available_slots(date_str):
    """
    Get available time slots for a specific date
    
    Args:
        date_str (str): Date in 'YYYY-MM-DD' format
    
    Returns:
        list: List of available time slots
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Get all booked slots for the date
        cursor.execute("SELECT booking_time FROM bookings WHERE booking_date = ?", (date_str,))
        booked_times = [row[0] for row in cursor.fetchall()]
        conn.close()
        
        # Salon working hours from 8:00 to 20:00, each service takes 2 hours
        all_slots = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00"]
        available_slots = [slot for slot in all_slots if slot not in booked_times]
        
        logger.info(f"Available slots for {date_str}: {available_slots}")
        return available_slots
    except Exception as e:
        logger.error(f"Error getting available slots: {e}", exc_info=True)
        return []

def add_booking(name, phone, email, service, sub_option, additional_option, date_str, time_str):
    """
    Add a new booking to the database
    
    Args:
        name (str): Customer name
        phone (str): Customer phone
        email (str): Customer email
        service (str): Selected service
        sub_option (str): Service sub-option
        additional_option (str): Additional service option
        date_str (str): Date in 'YYYY-MM-DD' format
        time_str (str): Time slot
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Check if slot is still available
        cursor.execute(
            "SELECT COUNT(*) FROM bookings WHERE booking_date = ? AND booking_time = ?",
            (date_str, time_str)
        )
        count = cursor.fetchone()[0]
        
        if count > 0:
            logger.warning(f"Slot {date_str} {time_str} is already booked")
            conn.close()
            return False
        
        # Add the booking
        cursor.execute('''
        INSERT INTO bookings (name, phone, email, service, sub_option, additional_option, booking_date, booking_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, phone, email, service, sub_option, additional_option, date_str, time_str))
        
        conn.commit()
        conn.close()
        
        logger.info(f"Added booking for {name} on {date_str} at {time_str}")
        return True
    except Exception as e:
        logger.error(f"Error adding booking: {e}", exc_info=True)
        return False

def get_user_bookings(phone):
    """
    Get all bookings for a specific phone number
    
    Args:
        phone (str): Customer phone number
        
    Returns:
        list: List of bookings
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row  # This enables column access by name
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM bookings 
        WHERE phone = ? 
        ORDER BY booking_date, booking_time
        """, (phone,))
        
        bookings = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return bookings
    except Exception as e:
        logger.error(f"Error getting user bookings: {e}", exc_info=True)
        return []

def cancel_booking(booking_id):
    """
    Cancel a booking by ID
    
    Args:
        booking_id (int): Booking ID
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
        
        if cursor.rowcount == 0:
            logger.warning(f"No booking found with ID {booking_id}")
            conn.close()
            return False
        
        conn.commit()
        conn.close()
        
        logger.info(f"Cancelled booking with ID {booking_id}")
        return True
    except Exception as e:
        logger.error(f"Error cancelling booking: {e}", exc_info=True)
        return False