import telebot
import mysql.connector

import myToken

from datetime import date
from datetime import datetime

TOKEN = myToken.TOKEN
myBot = telebot.TeleBot(TOKEN)
database = mysql.connector.connect(host='localhost', user='root', passwd='', database='db_belajarbot')
sql = database.cursor()
from telebot import apihelper

time = datetime.now()


class Mybot:
    def __init__(self):
        self.message
 
    @myBot.message_handler(commands=['start'])
    def start(message):
        photo = open('img/bot2.jpg', 'rb')
        myBot.send_photo(message.from_user.id, photo)
        text = myToken.deskripsi + "\nCreate by @Rosiyana" + "\n" \
                                                             "Waktu 🗓 : " + str(time)
        myBot.reply_to(message, text)

    @myBot.message_handler(commands=['help'])
    def bantu(message):
        bantu = myToken.bantuan + "\nCreate by @Rosiyana" + "\n" \
                                                             "Waktu 🗓 : " + str(time)
        myBot.reply_to(message, bantu)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "SELECT `nipd`,`nama`,`kelas` FROM `tabel_siswa`"
        sql.execute(query)
        data =sql.fetchall()
        totaldata = sql.rowcount
        kumpuldata=''
        if (totaldata > 0):
            pass
            # print(data)
        no = 0
        for x in data:
            no += 1
            kumpuldata = kumpuldata + str(x) +'\n'
            print(kumpuldata)
            kumpuldata = kumpuldata.replace('(', '')
            kumpuldata = kumpuldata.replace(')', '')
            kumpuldata = kumpuldata.replace("'", '')
            kumpuldata = kumpuldata.replace(",", '')
        else:
            print('Empty Data')

        myBot.reply_to(message, str(kumpuldata))


print(database)
print("-- Running --")
myBot.polling(none_stop=True)
