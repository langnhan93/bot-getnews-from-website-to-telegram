from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup

# token
updater = Updater('1145431553:AAHfGqlo9HAB852nEsh-ifJc9BGCg3XV2eM')

###########################
# def all
def getnews(getfn):
    list_news = []
    r = ""

    if getfn == "kd":
        r = requests.get("https://vnexpress.net/kinh-doanh")
    elif getfn =="sh":
        r = requests.get("https://vnexpress.net/so-hoa")
    elif getfn == "kh":
        r = requests.get("https://vnexpress.net/khoa-hoc")
    elif getfn == "tg":
        r = requests.get("https://vnexpress.net/the-gioi")
    elif getfn == "sk":
        r = requests.get("https://vnexpress.net/suc-khoe")

    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)
    return list_news

#
def news_kd(update: Update, context: CallbackContext) -> None:
    data = getnews("kd")
    for item in data:
        update.message.reply_text(f'{item["title"]}')
#
def news_sh(update: Update, context: CallbackContext) -> None:
    data = getnews("sh")
    for item in data:
        update.message.reply_text(f'{item["title"]}')
#
def news_kh(update: Update, context: CallbackContext) -> None:
    data = getnews("kh")
    for item in data:
        update.message.reply_text(f'{item["title"]}')
#
def news_tg(update: Update, context: CallbackContext) -> None:
    data = getnews("tg")
    for item in data:
        update.message.reply_text(f'{item["title"]}')
#
def news_sk(update: Update, context: CallbackContext) -> None:
    data = getnews("sk")
    for item in data:
        update.message.reply_text(f'{item["title"]}')


###########################
# tienao
def getcoin(getfn):
    list_news = []
    r = ""

    if getfn == "coin":
        r = requests.get("https://blogtienao.com/tin-tuc-crypto/")
    elif getfn == "ta":
        r = requests.get("https://tapchibitcoin.io/tin-tuc")
        
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("div", {"class": "td-module-thumb"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    if getfn == "ta":
        r = requests.get("https://goctienao.com")
    
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("div", {"class": "td-module-thumb"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news
#
def news_coin(update: Update, context: CallbackContext) -> None:
    data = getcoin("coin")
    for item in data:
        update.message.reply_text(f'{item["title"]}')

#
def news_ta(update: Update, context: CallbackContext) -> None:
    data = getcoin("ta")
    for item in data:
        update.message.reply_text(f'{item["title"]}')


###########################
# news
def getEnews():
    list_news = []
    r = requests.get("https://e.vnexpress.net/news/world")

    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h2", {"class": "title_news_site"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news
#
def news_Enews(update: Update, context: CallbackContext) -> None:
    data = getEnews()
    for item in data:
        update.message.reply_text(f'{item["title"]}')


# handler
updater.dispatcher.add_handler(CommandHandler('kd', news_kd))
updater.dispatcher.add_handler(CommandHandler('sh', news_sh))
updater.dispatcher.add_handler(CommandHandler('kh', news_kh))
updater.dispatcher.add_handler(CommandHandler('tg', news_tg))
updater.dispatcher.add_handler(CommandHandler('sk', news_sk))

updater.dispatcher.add_handler(CommandHandler('coin', news_coin))
updater.dispatcher.add_handler(CommandHandler('ta', news_ta))
updater.dispatcher.add_handler(CommandHandler('news', news_Enews))

# end
updater.start_polling()
updater.idle()
