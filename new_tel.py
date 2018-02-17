from getpass import getpass
import sys, traceback, time, telebot,random
import wget, os
from telebot import types
from telethon.tl.types import UpdateShortMessage, PeerUser, PeerChannel
from telethon.tl.functions.channels import *
import threading
import shutil
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import SetBotCallbackAnswerRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.tl.functions.messages import SendInlineBotResultRequest
from telethon.tl.functions.messages import GetInlineBotResultsRequest

#1200 символов
#pool_bot_id=129782279
client=None;
emoji_send="👍😐👎"

def check_exist(path):
    try:
        file = open(path)
    except IOError as e:
        return False;
    else:
        return True;

def main():
    global client
    session_name = 'session'#environ.get('TG_SESSION', 'session')
    user_phone = '+380666123545'#environ['TG_PHONE']
    client = TelegramClient(session_name,
                            187706,#int(environ['TG_API_ID']),
                            'a1c5bae7b04067f397f4f96400be8718',
                             update_workers=4)

    print('INFO: Connecting to Telegram Servers...', end='', flush=True)
    err=client.connect()
    print(err)
    print('Done!')

    if not client.is_user_authorized():
        print('INFO: Unauthorized user')
        client.send_code_request(user_phone)
        code_ok = False
        while not code_ok:
            code = input('Enter the auth code: ')
            try:
                code_ok = client.sign_in(user_phone, code)
            except SessionPasswordNeededError:
                password = getpass('Two step verification enabled. Please enter your password: ')
                code_ok = client.sign_in(password=password)
    print('INFO: Client initialized succesfully!')
    client.add_update_handler(update_handler)
    input('Press Enter to stop this!\n')

def update_handler(update):
    #print(client)
    global client
    #print(update.stringify())
    #print('Press Enter to stop this!')
    if update.message=="Отправляй украинский":
        print("react")
        directory="md_question/Ukrainian/not_sended/"
        files=os.listdir(directory)
        try:
            fl=random.choice(files)
            client.send_file(entity="@QuanBot", file=directory+fl)
            shutil.move(directory+fl,"md_question/Ukrainian/sended/"+fl)
        except Exception as e:
            print(e)
    if update.message=="Отправляй биологию":
        print("react")
        directory="md_question/Biology/not_sended/"
        files=os.listdir(directory)
        #print(files)
        try:
            fl=random.choice(files)
            client.send_file(entity="@QuanBot", file=directory+fl)
            shutil.move(directory+fl,"md_question/Biology/sended/"+fl)
        except Exception as e:
            print(e)
    if update.message=="Отправляй историю":
        print("react")
        directory="md_question/History/not_sended/"
        files=os.listdir(directory)
        #print(files)
        try:
            fl=random.choice(files)
            client.send_file(entity="@QuanBot", file=directory+fl)
            shutil.move(directory+fl,"md_question/History/sended/"+fl)
        except Exception as e:
            print(e)
    if update.message=="Отправляй географию":
        print("react")
        directory="md_question/Geography/not_sended/"
        files=os.listdir(directory)
        #print(files)
        try:
            fl=random.choice(files)
            client.send_file(entity="@QuanBot", file=directory+fl)
            shutil.move(directory+fl,"md_question/Geography/sended/"+fl)
        except Exception as e:
            print(e)
    if update.message=="Факт украинский":
        print("react")
        directory="md_question/Ukrainian/pictures_facts_not_send/"
        files=os.listdir(directory)
        #print(files)
        try:
            fl=random.choice(files)
            client.send_file(entity="@like", file=directory+fl)
            client.send_message("@like","👍😐👎")
            shutil.move(directory+fl,"md_question/Ukrainian/pictures_facts_sended/"+fl)
        except Exception as e:
            print(e)
    print(update.message.from_id)
    if update.message.from_id==190601014:
        print("!!! - message from like bot")
        for i in update.message.reply_markup.rows:
            for j in i.buttons:
                try:
                    if j.query!="":
                        bot_results = client(GetInlineBotResultsRequest(bot="@like", peer="@forevka", query=j.query, offset=''))
                        client(SendInlineBotResultRequest(peer="t.me/prepare_zno", query_id=bot_results.query_id, id=bot_results.results[0].id))
                except:
                    pass
    if update.message.from_id==219282912:
        print("!!! - message from quan bot")
        for i in update.message.reply_markup.rows:
            for j in i.buttons:
                try:
                    if j.query!="":
                        bot_results = client(GetInlineBotResultsRequest(bot="@QuanBot", peer="@forevka", query=j.query, offset=''))
                        client(SendInlineBotResultRequest(peer="t.me/prepare_zno", query_id=bot_results.query_id, id=bot_results.results[0].id))
                except:
                    pass
                if j.text.find('Завершити')>=0:
                    client(GetBotCallbackAnswerRequest(
                            "@QuanBot",
                            update.message.id,
                            data=j.data
                            ))
                if j.text.find('Поділитися')>=0:
                    client(GetBotCallbackAnswerRequest(
                            "@QuanBot",
                            update.message.id,
                            data=j.data
                            ))


if __name__ == '__main__':
    main()
