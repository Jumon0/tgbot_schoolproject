import requests
import json
from config import API, bot, time, pog
from PIL import Image,ImageDraw,ImageFont

@bot.message_handler( commands = [ 'start' ] )
def start( message ):
    bot.send_message( message.chat.id,'Привет, рад тебя видеть! Напиши название города' )


@bot.message_handler( content_types = [ 'text' ] )
def get_weather( message ):
    moon = Image.open( 'Moon.jpg' )
    sun = Image.open( 'Sun.jpg' )
    vecher = Image.open( 'Blood.jpg' )
    city = message.text.strip( )
    idraw1 = ImageDraw.Draw( sun )
    idraw2 = ImageDraw.Draw( moon )
    idraw3 = ImageDraw.Draw( vecher )
    if len( city ) > 16:
        fontcity = ImageFont.truetype( "Montserrat-Bold.ttf",size = 45 )
        font = ImageFont.truetype( "Montserrat-Bold.ttf",size = 45 )
    else:
        font = ImageFont.truetype( "Montserrat-Bold.ttf",size = 75 )
        fontcity = ImageFont.truetype( "Montserrat-Bold.ttf",size = 75 )

    res = requests.get( f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ru' )

    if res.status_code == 200:
        data = json.loads( res.text )
        humidity = data[ 'main' ][ 'humidity' ]
        pressure = data[ 'main' ][ 'pressure' ]
        speed = data[ 'wind' ][ 'speed' ]
        temp = data[ "main" ][ "temp" ]
        pogoda = data[ "clouds" ][ "all" ]
        pogoda=pog(pogoda)
        timezone = data[ 'timezone' ]

        x=timezone//3600
        times=time(x)
        zxc = int( times[ :2 ] )
        if len( city ) > 16:
            if 6 <= zxc <= 18:
                idraw1.text( (0,350),f'{city}',font = fontcity )
                idraw1.text( (0,450),f'{temp}°',font = font )
                idraw1.text( (0,400),f'{pogoda} ',font = font )
                sun.save( 'test_text.jpg' )
                bot.send_photo( message.chat.id,sun )
            if 18 < zxc <= 24:
                idraw3.text( (0,350),f'{city}',font = fontcity )
                idraw3.text( (0,450),f'{temp}°',font = font )
                idraw3.text( (0,400),f'{pogoda} ',font = font )
                vecher.save( 'test_text.jpg' )
                bot.send_photo( message.chat.id,vecher )
            if 0 <= zxc < 6:
                idraw2.text( (0,350),f'{city}',font = fontcity )
                idraw2.text( (0,450),f'{temp}°',font = font )
                idraw2.text( (0,400),f'{pogoda} ',font = font )
                moon.save( 'test_text.jpg' )
                bot.send_photo( message.chat.id,moon )
        if len( city ) < 16:
            if 6 <= zxc <= 18:
                idraw1.text( (0,320),f'{city}',font = fontcity )
                idraw1.text( (0,475),f'{temp}°',font = font )
                idraw1.text( (0,400),f'{pogoda} ',font = font )
                sun.save( 'test_text.jpg' )
                bot.send_photo( message.chat.id,sun )
            if 18 < zxc <= 24:
                idraw3.text( (0,320),f'{city}',font = fontcity )
                idraw3.text( (0,475),f'{temp}°',font = font )
                idraw3.text( (0,400),f'{pogoda} ',font = font )
                vecher.save( 'test_text.jpg' )
                bot.send_photo( message.chat.id,vecher )
            if 0 <= zxc < 6:
                idraw2.text( (0,320),f'{city}',font = fontcity )
                idraw2.text( (0,475),f'{temp}°',font = font )
                idraw2.text( (0,400),f'{pogoda} ',font = font )
                moon.save( 'test_text.jpg' )
                bot.send_photo( message.chat.id,moon )
        bot.reply_to( message,f'В городе {city} 'f'температура : {temp}°  \n'
                                      f'{pogoda} \n'
                                      f'Влажность: {humidity} % \n'
                                      f'Давление: {pressure} гПа \n'
                                      f'Ветер: {speed} м.с.\n'
                                      f'Время: {times} \n' )

    else:
        bot.reply_to( message,f'Город указан неверно' )


bot.polling( none_stop = True )
