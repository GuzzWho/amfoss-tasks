import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables 
yourkey = "8c54c419"
bot_id = "5622491549:AAFYCkTx90SsvOelzXqSWQC1hydVgBAj9Qw"

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    # TODO: 1.2 Get movie information from the API
    MOVIE_NAME = message.text
    MOVIE_NAME = str(MOVIE_NAME.split(' ', 1)[1])
    response = requests.get(f"http://www.omdbapi.com/?apikey=8c54c419&t={MOVIE_NAME}")
    mv_data = response.json()
    #print(json.dumps(mv_data, indent=4, sort_keys=True))
    info = []
    for key, value in mv_data.items():
          if key != "Ratings":
              print(key, ' : ', value)
              sam = key +' : '+value
              info.append(sam)
    #print("\n".join(info))
    bot.reply_to(message, "\n".join(info))
    #print(f'Title: {mv_data["Title"]}')
    with open("mv_data.csv", 'w',encoding ='UTF8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(info)
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    try:
    	chat_id = message.chat.id
    	
    except Exception as e:
    	print(e)
    mv_csv=open('mv_data.csv','rb')
    bot.send_document(chat_id,mv_csv)
    
    #TODO: 2.2 Send downlodable CSV file to telegram chat

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
