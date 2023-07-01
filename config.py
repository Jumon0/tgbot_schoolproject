import telebot
import pytz
from datetime import datetime
bot = telebot.TeleBot( '6273175972:AAGzCPX9VcOoyUhXZjbUzM8U_4hhX7572LE' )
API = 'cd24020961e80c6698c7401f2ab9817f'
def time(x):
    if x == 1:
        tz = pytz.timezone( 'Europe/London' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 2:
        tz = pytz.timezone( 'Europe/Berlin' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 3:
        tz = pytz.timezone( 'Europe/Minsk' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 4:
        tz = pytz.timezone( 'Asia/Yerevan' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 5:
        tz = pytz.timezone( 'Asia/Dushanbe' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 6:
        tz = pytz.timezone( 'Asia/Dhaka' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 7:
        tz = pytz.timezone( 'Asia/Bangkok' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 8:
        tz = pytz.timezone( 'Asia/Singapore' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 9:
        tz = pytz.timezone( 'Asia/Tokyo' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 10:
        tz = pytz.timezone( 'Asia/Vladivostok' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 11:
        tz = pytz.timezone( 'Asia/Magadan' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 12:
        tz = pytz.timezone( 'Asia/Kamchatka' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == 0:
        tz = pytz.timezone( 'Atlantic/Azores' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == -3:
        tz = pytz.timezone( 'America/Sao_Paulo' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == -4:
        tz = pytz.timezone( 'America/Manaus' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == -5:
        tz = pytz.timezone( 'America/Chicago' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == -6:
        tz = pytz.timezone( 'America/Denver' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == -7:
        tz = pytz.timezone( 'America/Los_Angeles' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    if x == -8:
        tz = pytz.timezone( 'America/Anchorage' )
        currtime = datetime.now( tz ).strftime( '%H:%M:%S' )
    return currtime
def pog(x):
    if 0 <= int( x ) <= 10:
        x = 'Ясно'
    elif 11 <= int( x ) <= 58:
        x = 'Облачно'
    elif int( x ) > 58:
        x = 'Пасмурно'
    return x

