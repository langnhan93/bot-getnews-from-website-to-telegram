from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup


# define function
def hi(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.last_name}')


# kinh doanh
def getnews_kd():
    list_news = []
    r = requests.get("https://vnexpress.net/kinh-doanh")

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
    data = getnews_kd()
    str1 = ""

    for item in data:
        #str1 += item["title"] + "\n"
        update.message.reply_text(f'{item["title"]}')

# so hoa
def getnews_sh():
    list_news = []
    r = requests.get("https://vnexpress.net/so-hoa")

    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news
#
def news_sh(update: Update, context: CallbackContext) -> None:
    data = getnews_sh()
    str1 = ""

    for item in data:
        #str1 += item["title"] + "\n"
        update.message.reply_text(f'{item["title"]}')

# khoa hoc
def getnews_kh():
    list_news = []
    r = requests.get("https://vnexpress.net/khoa-hoc")

    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news
#
def news_kh(update: Update, context: CallbackContext) -> None:
    data = getnews_kh()
    str1 = ""

    for item in data:
        #str1 += item["title"] + "\n"
        update.message.reply_text(f'{item["title"]}')

# the gioi
def getnews_tg():
    list_news = []
    r = requests.get("https://vnexpress.net/the-gioi")

    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news
#
def news_tg(update: Update, context: CallbackContext) -> None:
    data = getnews_tg()
    str1 = ""

    for item in data:
        #str1 += item["title"] + "\n"
        update.message.reply_text(f'{item["title"]}')

# suc khoe
def getnews_sk():
    list_news = []
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
def news_sk(update: Update, context: CallbackContext) -> None:
    data = getnews_sk()
    str1 = ""

    for item in data:
        #str1 += item["title"] + "\n"
        update.message.reply_text(f'{item["title"]}')



# tienao
def getnews_tienao():
    list_news = []
    r = requests.get("https://blogtienao.com/tin-tuc-crypto/")

    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("div", {"class": "td-module-thumb"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news
#
def news_tienao(update: Update, context: CallbackContext) -> None:
    data = getnews_tienao()
    str1 = ""

    for item in data:
        str1 += item["title"] + "\n"
        update.message.reply_text(f'{item["title"]}')

# news_tienao1
def getnews_tienao1():
    list_news = []
    r = requests.get("https://tapchibitcoin.io/tin-tuc")

    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("div", {"class": "td-module-thumb"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

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
def news_tienao1(update: Update, context: CallbackContext) -> None:
    data = getnews_tienao1()
    str1 = ""

    for item in data:
        str1 += item["title"] + "\n"
        update.message.reply_text(f'{item["title"]}')


# news
def getnews_news():
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
def news_news(update: Update, context: CallbackContext) -> None:
    data = getnews_news()
    str1 = ""

    for item in data:
        #str1 += item["title"] + "\n"
        update.message.reply_text(f'{item["title"]}')


# TECH
def getnews_tech():
    list_news = []
    r = requests.get("https://techcrunch.com/")

    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("h2", {"class": "post-block__title"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.get("href")
        newdict["title"] = new.a.get("title")
        list_news.append(newdict)

    return list_news
#
def news_tech(update: Update, context: CallbackContext) -> None:
    data = getnews_tech()
    str1 = ""

    for item in data:
        #str1 += item["title"] + "\n"
        update.message.reply_text(f'{item["link"]}')


# token
updater = Updater('1145431553:AAHfGqlo9HAB852nEsh-ifJc9BGCg3XV2eM')

# handler
updater.dispatcher.add_handler(CommandHandler('hi', hi))
updater.dispatcher.add_handler(CommandHandler('kd', news_kd))
updater.dispatcher.add_handler(CommandHandler('sh', news_sh))
updater.dispatcher.add_handler(CommandHandler('kh', news_kh))
updater.dispatcher.add_handler(CommandHandler('tg', news_tg))
updater.dispatcher.add_handler(CommandHandler('sk', news_sk))
updater.dispatcher.add_handler(CommandHandler('news', news_news))
updater.dispatcher.add_handler(CommandHandler('tech', news_tech))
updater.dispatcher.add_handler(CommandHandler('tienao', news_tienao))
updater.dispatcher.add_handler(CommandHandler('tienao1', news_tienao1))



# end
updater.start_polling()
updater.idle()