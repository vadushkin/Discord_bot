from smail import *
from questions import *
from googletrans import Translator
from deepface import DeepFace
from photo_demotivator import servant
from config import TOKEN
import time
import sqlite3
import json
import random
import discord
import bs4
import requests
import re
import datetime
import platform
import asyncio

your_channel = "Токен вашего канала int"

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
today = datetime.datetime.today()
translator = Translator()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


def quote():
    """Выбирает цитату"""
    url_link = random.randint(0, 10)
    if url_link > 0:
        url = f'https://quotes.toscrape.com/page/{url_link}'
    else:
        url = 'https://quotes.toscrape.com'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    random_int = random.randint(0, len(quotes) - 1)
    embed = discord.Embed(
        title=translator.translate(authors[random_int].text, dest='ru').text,
        description=translator.translate(quotes[random_int].text, dest='ru').text,
        color=0xff9900,
    )
    return embed


def face_analyze(img_path):
    """Анализ лица"""
    try:
        today = datetime.datetime.today()
        result_dict = DeepFace.analyze(img_path=img_path, actions=['age', 'gender', 'race', 'emotion'])
        result_dict['img1'] = img_path
        with open(f"json_image_analyze/{today.strftime('%Y-%m-%d-%H.%M.%S').replace('.', '-')}.json", 'a') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        age = result_dict.get("age")
        gender = result_dict.get("gender")
        sorted_tuples = sorted(result_dict.get('race').items(), key=lambda item: item[1], reverse=True)
        sorted_dict = {k: v for k, v in sorted_tuples}
        for k, v in sorted_dict.items():
            sorted_dict[k] = round(v, 1)
        race = sorted_dict
        sorted_tuples = sorted(result_dict.get('emotion').items(), key=lambda item: item[1], reverse=True)
        sorted_dict2 = {k: v for k, v in sorted_tuples}
        for k, v in sorted_dict2.items():
            sorted_dict2[k] = round(v, 1)
        emotions = sorted_dict2
        listik = [age, gender, race, emotions]
        return listik

    except Exception as _ex:
        return None


def face_verify(img_1, img_2):
    """Сравнение лиц"""
    try:
        today = datetime.datetime.today()
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)
        result_dict['img1'] = img_1
        result_dict['img2'] = img_2
        with open(f"json_image_check/{today.strftime('%Y-%m-%d-%H.%M.%S').replace('.', '-')}.json", 'a') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        # return result_dict
        if result_dict.get('verified'):
            b = 'Проверка пройдена. Эти фотографии похожих людей'
            embed = discord.Embed(
                title='Complete',
                description=b,
                color=5763719,
            )
            return embed

        d = 'Проверка не прошла. Эти фотографии не одного человека'
        embed = discord.Embed(
            title='Complete',
            description=d,
            color=15158332,
        )
        return embed

    except Exception as _ex:
        embed = discord.Embed(
            title='Error',
            description="Не могу распознать лицо, пожалуйста повторите попытку с другими фотографиями :)",
            color=15158332,
        )
        return embed


def check(ctx):
    return lambda m: m.author == ctx.author and m.channel == ctx.channel


def photo(string, msg2):
    return f'https://some-random-api.ml/canvas/{photo_changes[msg2]}?avatar=https://media.discordapp.net/attachments/{string[39:]}'


def random_anecdotes():
    # """Рандомный анекдот"""
    # string_for_anecdote = ''
    # text = ''
    # link = requests.get('http://anekdotme.ru/random')
    # b = bs4.BeautifulSoup(link.text, "html.parser")
    # text_for_anecdote = b.select('.anekdot_text')
    # for symbol in text_for_anecdote:
    #     text = (symbol.getText().strip())
    #     string_for_anecdote = string_for_anecdote + text + '\n\n'
    #
    # return text
    return "К сожалению анекдотов нету("

async def get_input_of_type(func, ctx):
    while True:
        try:
            msg = await client.wait_for('message', check=check(ctx))
            return func(msg.content)
        except ValueError:
            break


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    global base, cur
    base = sqlite3.connect('DiscordBase.sqlite3')
    cur = base.cursor()
    if base:
        print('DataBase connected...OK')


@client.event
async def on_member_join(member):
    channel = client.get_channel(your_channel)
    embed = discord.Embed(
        title="Добро пожаловать на сервер!",
    )
    await channel.send(f"Приветик {member.name}!", embed=embed)


@client.event
async def on_member_remove(member):
    channel = client.get_channel(your_channel)
    await channel.send(f"Прощай {member.name}!")


@client.event
async def on_message(message):
    if message.author:
        msg = message.content.lower()
        msg_upper = message.content
        msg2 = msg[1:]
        mes_atr = message.attachments
        if not (message.content[:1] in startswith_word) and not message.author.bot:
            base.execute('CREATE TABLE IF NOT EXISTS messages (userid INT, content STRING, links INT)')
            base.commit()
            print(msg_upper)
            if len(re.findall(r'(https?://[^\s]+.png|.jpeg|.jpg\')', str(mes_atr))) == 1:
                url = re.findall(r'(https?://[^\s]+\')', str(mes_atr))
                cur.execute('INSERT INTO messages VALUES(?, ?, ?)', (message.author.id, url[0][:-1], 1))
            elif len(re.findall(r'(https?://[^\s]+.png|.jpeg|.jpg\')', str(mes_atr))) > 1:
                for urls in re.findall(r'(https?://[^\s]+\')', str(mes_atr)):
                    cur.execute('INSERT INTO messages VALUES(?, ?, ?)', (message.author.id, urls[:-1], 1))
            elif len(re.findall(r'(https?://[^\s]+)', str(msg_upper))) == 1:
                for urls in re.findall(r'(https?://[^\s]+)', str(msg_upper)):
                    cur.execute('INSERT INTO messages VALUES(?, ?, ?)', (message.author.id, urls[:-1], 0))
            elif message.content != '':
                cur.execute('INSERT INTO messages VALUES(?, ?, ?)', (message.author.id, message.content, 2))
            base.commit()
        if client.user.mentioned_in(message) or random.randint(0, 15) == 12:
            sqlite_select_query = """SELECT * from messages ORDER BY RANDOM() LIMIT 1;"""
            cur.execute(sqlite_select_query)
            records = cur.fetchone()
            await message.channel.send(records[1])
        print(f"Дата: {time.ctime()}, {message.author} : {message.content}")
        if msg2[:3] == 'dem' or msg2[:5] == 'r_dem':
            if len(re.findall(r'(https?://[^\s]+\')', str(mes_atr))) == 1 and msg2[:3] == 'dem':
                url = re.findall(r'(https?://[^\s]+\')', str(mes_atr))
                img_data = requests.get(url[0][:-1]).content
                msg3 = msg_upper[4:]
            elif msg2[:5] == 'r_dem':
                url = servant.looking_for_a_link()
                img_data = requests.get(url).content
                msg3 = msg_upper[6:]
            else:
                await message.channel.send("Приложите одну фотографию, пожалуйста!")
            now = today.strftime("%Y-%m-%d-%H.%M.%S").replace('.', '-')
            with open(f'photo_demotivator\{now}.jpeg', 'wb') as handler:
                handler.write(img_data)
            photos = servant.photo_change(msg3.split(','), f'photo_demotivator\{now}.jpeg')
            with open(f'{photos}', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
        if msg2 == 'quote':
            await message.channel.send(embed=quote())
        if random.randint(0, 20) == 1:
            await message.add_reaction(emoticons[random.randint(0, len(emoticons) - 1)])
        if msg in dict_help_bot:
            await message.channel.send(dict_help_bot[msg])
        if msg in question_for_kek_dela and not message.author.bot:
            await message.reply(kak_dela_from_bot[random.randint(0, len(kak_dela_from_bot) - 1)])
        if msg in word_for_hi and not message.author.bot:
            await message.reply(hi_from_bot[random.randint(0, len(hi_from_bot) - 1)])
        if msg2[:13] == 'analyze_photo':
            if len(re.findall(r'(https?://[^\s]+\')', str(mes_atr))) == 1:
                url = re.findall(r'(https?://[^\s]+\')', str(mes_atr))
                url += []
                picture = face_analyze(url[0][:-1])
                if picture:
                    a, b, c, d = picture[0], picture[1], picture[2], picture[3]
                    c = c.items()
                    d = d.items()
                    b = translator.translate(b, dest='ru').text.title()
                    embed = discord.Embed(
                        title=f"Пол: {b}",
                        colour=16705372,
                    )
                    c = [str(i) + ' ' + str(k) for i, k in c][0]
                    d = [str(f) + ' ' + str(s) for f, s in d][0]
                    c = translator.translate(c, dest='ru').text.title()
                    d = translator.translate(d, dest='ru').text.title()
                    embed.set_image(url=url[0][:-1])
                    embed.add_field(name='Раса', value=c + "%")
                    embed.add_field(name='Эмоция', value=d + "%")
                    embed.set_author(name=f"Возраст: {a}")
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send(
                        "Не могу распознать лицо на фотографии, простите, но вы можете попробовать еще раз :))) Но уже с другим фото!!!!")
            else:
                await message.channel.send("Приложите одну фотографию для исследования!")
        if msg2[:9] == 'id_photos':
            if len(re.findall(r'(https?://[^\s]+\')', str(mes_atr))) == 2:
                urls = re.findall(r'(https?://[^\s]+\')', str(mes_atr))
                embed = face_verify(img_1=urls[0][:-1], img_2=urls[1][:-1])
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Укажите 2 фотографии, пожалуйста! :(")
        if msg2[:15] == 'youtube_comment' or msg2[:5] == 'tweet':
            if len(msg2.split()) >= 3:
                string = str(*message.attachments)
                user = msg2.split()[1].title()
                comment = '%20'.join(msg_upper.split()[2:])
                if comment[-1] in [',', '.']:
                    comment = comment[:-1]
                if string and msg2.split()[0] in sites:
                    await message.channel.send(
                        f'https://some-random-api.ml/canvas/{sites[msg2.split()[0]]}?avatar=https://cdn.discordapp.com/attachments/{string[39:]}&username={user}&displayname={user}&comment={comment}')
                else:
                    await message.channel.send("Приложите фотографию")
            else:
                await message.channel.send(
                    f"Укажите: $tweet/$youtube_comment <User> <Comment> <Img>\nНапример:\n$tweet/$youtube_comment Барак Я ненавижу черных! (+фото)")
        if msg2 in photo_changes:
            string = str(*message.attachments)
            if string != '':
                await message.channel.send(photo(string, msg2))
            else:
                await message.channel.send("Приложите фотографию, пожалуйста")
        if msg2[:6] == 'binary':
            response = requests.get(
                f"https://some-random-api.ml/binary?encode={translator.translate(msg2[6:]).text}")
            if response.status_code == 200:
                json_data = json.loads(response.text)
                embed = discord.Embed(color=0xff9900, title=json_data['binary'])
                await message.channel.send(embed=embed)
            else:
                await message.channel.send('После "$binary" укажите строку')
        if msg2 == 'anime_quote':
            response = requests.get('https://some-random-api.ml/animu/quote')
            json_data = json.loads(response.text)
            embed = discord.Embed(
                title=translator.translate(json_data['character'], dest='ru').text,
                description=translator.translate(json_data['sentence'], dest='ru').text,
                color=0xff9900,
            )
            embed.set_author(name=translator.translate(json_data['anime'], dest='ru').text, )
            await message.channel.send(embed=embed)
        if msg2 in dict_links_for_img:
            response = requests.get(f'https://some-random-api.ml/{dict_links_for_img[msg2]}')
            json_data = json.loads(response.text)
            title = translator.translate(msg2, dest='ru').text
            embed = discord.Embed(color=0xff9900, title=title.title())
            embed.set_image(url=json_data['link'])
            await message.channel.send(embed=embed)
        if msg2 in dict_animal:
            response = requests.get(f'https://some-random-api.ml/{dict_animal[msg2]}')
            json_data = json.loads(response.text)
            title = translator.translate(msg2, dest='ru').text
            fact = translator.translate(json_data['fact'], dest='ru')
            embed = discord.Embed(color=0xff9900, title=title.title(), description=fact.text)
            embed.set_image(url=json_data['image'])
            await message.channel.send(embed=embed)
        if msg2 == 'joke' or msg2 == 'шутка':
            response = requests.get(f'https://some-random-api.ml/joke')
            json_data = json.loads(response.text)
            result = translator.translate(json_data['joke'], dest='ru').text
            embed = discord.Embed(color=0xff9900, title=result)
            await message.channel.send(embed=embed)
        if msg2 in word_from_anekdot:
            await message.channel.send(random_anecdotes())
        if msg == 'умница' or msg == 'умничка':
            await message.channel.send("Знаю)")


client.run(TOKEN)
