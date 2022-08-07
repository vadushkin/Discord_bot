# Библиотеки Python
import math
import re
import time
import json
import random
import sqlite3
import asyncio
import datetime
import platform

# Файлы
import game_2048
from photo_demotivator import servant
from smail import *
from questions import *
from config import TOKEN

# Сторонние библиотеки
import discord
import bs4
import requests
from pyrandmeme import *
from deepface import DeepFace
from googletrans import Translator
from fake_useragent import UserAgent
from simpledemotivators import Quote

your_channel = 10000000000
your_server = 10000000000

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

translator = Translator()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

screen_for_game = "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"


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


def to_return_a_random_anime_picture():
    """Выбирает фотографию"""
    page = random.randint(1, 5000)
    url = f'https://anime-pictures.net/pictures/view_posts/{page}'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    number_random_picture = random.randint(1, 60)
    photo_url = soup.find_all('span', class_='img_block_big')[number_random_picture].find('a').get('href')
    url = f"https://anime-pictures.net{photo_url}"
    response = requests.get(url=url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    full_photo_url = soup.find_all('img', id='big_preview')[0].get('src')
    url_photo = f"https:{full_photo_url}"
    embed = discord.Embed(
        title='Аниме',
        color=0xff9900,
    )
    embed.set_image(url=url_photo)
    return embed


def to_return_a_random_hentai():
    """Возвращает рандомное видео"""
    while True:
        number_page = random.randint(1, 158)
        url = f"https://gifsauce.com/r/HENTAI_GIF?page={number_page}"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'}
        response = requests.get(url=url, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        videos = soup.find_all("div", class_="itemgif relative pb-13/12 group bg-palette-1")
        random_number_video = random.randint(1, len(videos) - 1)
        video = videos[random_number_video].find('a').get('href')
        video_full_url = f"https://gifsauce.com{video}"
        response2 = requests.get(url=video_full_url, headers=headers)
        soup2 = bs4.BeautifulSoup(response2.text, 'lxml')
        video_block = soup2.find_all('div', class_='absolute h-full w-full object-cover block')[0].find('video')
        url_video = re.findall(r'src="(.*?)"', str(video_block))[0]
        if url_video[:23] == 'https://i.gifsauce.com/':
            continue
        else:
            return url_video


def face_analyze(img_path):
    """Анализ лица"""
    try:
        today = datetime.datetime.today()
        result_dict = DeepFace.analyze(img_path=img_path, actions=('age', 'gender', 'race', 'emotion'))
        result_dict['img1'] = img_path
        with open(f"json_image_analyze/{today.strftime('%Y-%m-%d-%H.%M.%S').replace('.', '-')}.json", 'a') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        age = result_dict.get("age")
        gender = result_dict.get("gender")
        sorted_tuples = sorted(result_dict.get('race').items(), key=lambda item: item[1], reverse=True)
        sorted_dict = {key: value for key, value in sorted_tuples}
        for item, value in sorted_dict.items():
            sorted_dict[item] = round(value, 1)
        race = sorted_dict
        sorted_tuples = sorted(result_dict.get('emotion').items(), key=lambda item: item[1], reverse=True)
        sorted_dict2 = {key: value for key, value in sorted_tuples}
        for item, value in sorted_dict2.items():
            sorted_dict2[item] = round(value, 1)
        emotions = sorted_dict2
        listik = [age, gender, race, emotions]
        return listik

    except ValueError:
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
            complete = 'Проверка пройдена. Эти фотографии похожих людей'
            embed = discord.Embed(
                title='Complete',
                description=complete,
                color=5763719,
            )
            return embed

        problem = 'Проверка не прошла. Эти фотографии не одного человека'
        embed = discord.Embed(
            title='Complete',
            description=problem,
            color=15158332,
        )
        return embed

    except ValueError:
        embed = discord.Embed(
            title='Error',
            description="Не могу распознать лицо, пожалуйста повторите попытку с другими фотографиями :)",
            color=15158332,
        )
        return embed


def check(message):
    return lambda m: m.author == message.author and m.channel == message.channel


def photo(string, msg2):
    return f'https://some-random-api.ml/canvas/{photo_changes[msg2]}' \
           f'?avatar=https://media.discordapp.net/attachments/{string[39:]}'


def random_anecdotes():
    """Рандомный анекдот"""
    url = 'https://anekdoty.ru/'
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    try:
        response = requests.get(url, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        names_categories = soup.find("div", class_="drop").find_all('a')
        list_names = []
        for name in names_categories:
            list_names.append(name.get('href'))
        random_anecdote_url_category = random.choice(list_names)
        response = requests.get(random_anecdote_url_category, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        number_all_anecdotes = int(soup.find("div", class_="pagination-holder-result").text.split()[1]) // 20
        category = soup.find("div", class_='description content-blocks').text.strip()
        number_pagination = random.randint(1, number_all_anecdotes)
        random_anecdote_url = random_anecdote_url_category + 'page/' + str(number_pagination) + '/'
        response = requests.get(random_anecdote_url, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        anecdote = soup.find("div", class_="content-block section").find_all(
            'div', class_='holder-body')[0].text.strip()
        return [anecdote, category]

    except Exception as _ex:
        print(_ex)
        return "Нету анекдотов ((("


async def get_input_of_type(func, message):
    while True:
        try:
            msg = await client.wait_for('message', check=check(message))
            return func(msg.content)
        except ValueError:
            break
            
@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji

    if user.bot:
        return

    if emoji in ['⬇', '⬆', '➡', '⬅']:
        fixed_channel = client.get_channel(reaction.message.channel.id)
        message = await fixed_channel.fetch_message(reaction.message.id)
        base.execute(
            'CREATE TABLE IF NOT EXISTS games (server_id INT, open STRING, screen TEXT, score INT,  '
            'moved BOOLEAN, move BOOLEAN)')
        base.commit()
        cursor.execute(f"SELECT * FROM games WHERE open = 'Открыта' AND server_id = {fixed_channel.guild.id}")
        records = cursor.fetchone()
        if records:
            screen, score, moved, move = game_2048.key_handler(emoji, records[2],
                                                               records[3], records[4], records[5])
            check_lose_or_win = game_2048.to_check_win_or_lose(screen)
            screen, score, moved, move = game_2048.add_new_field(screen, score, moved, move)
            screen, score, animal_stile = game_2048.prtScreen(screen, score)
            cursor.execute(
                f"UPDATE games SET screen = '{screen}', score = {score}, moved = {moved}, move = {move} "
                f"WHERE (open == 'Открыта') AND (server_id == {fixed_channel.guild.id})")
            base.commit()
            if check_lose_or_win == "Win":
                cursor.execute(f"UPDATE games SET open = 'Выигрыш' "
                               f"WHERE server_id = {fixed_channel.guild.id} AND (open == 'Открыта')")
                base.commit()
                await message.edit(content="Score: " + str(score) + "\n" + animal_stile + "Вы выиграли, поздравляю!!!")
            elif check_lose_or_win == "Lose":
                cursor.execute(f"UPDATE games SET open = 'Проигрыш' "
                               f"WHERE server_id = {fixed_channel.guild.id} AND (open == 'Открыта')")
                base.commit()
                await message.edit(content="Score: " + str(
                    score) + "\n" + animal_stile + "Вы проиграли... Я болел за вас(\nМожете попробовать еще раз!")
            else:
                await message.edit(content="Score: " + str(score) + "\n" + animal_stile)
        else:
            await fixed_channel.send("Создайте игру с помощью $start_game")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    global base, cursor
    base = sqlite3.connect('Аркадий.sqlite3')
    cursor = base.cursor()
    if base:
        print('DataBase connected...OK')


@client.event
async def on_member_join(member):
    if member.guild.id == your_server:
        channel = client.get_channel(your_channel)
    else:
        channel = client.get_channel(your_channel)
    embed = discord.Embed(
        title=f"Приветик {member.name}!",
        description="Здесь весело :)",
    )
    embed.set_image(
        url="https://fotointeres.ru/wp-content/uploads/2012/04/0_827f9_58eba125_orig.jpg")
    await channel.send("Добро пожаловать на сервер!", embed=embed)


@client.event
async def on_member_remove(member):
    if member.guild.id == your_channel:
        channel = client.get_channel(your_channel)
    else:
        channel = client.get_channel(your_channel)
    embed = discord.Embed(
        title=f"{member.name}! Покидает сервер...",
    )
    embed.set_image(url=member.avatar_url)
    await channel.send(f"Ушёл в далёкий путь, удачи ему!", embed=embed)


@client.event
async def on_message(message):
    if message.author:

        today = datetime.datetime.today()

        message_content_lower_with_prefix = message.content.lower()
        message_content = message.content
        message_content_lower = message_content_lower_with_prefix[1:]
        message_attachments = message.attachments
        message_guild_name = message.guild.name
        message_guild_id = message.guild.id
        message_author = message.author

        if message_attachments:
            if message_content:
                print(f"Сервер: {message_guild_name}, Дата: {time.ctime()}, {message_author} : {message_content}")
            for urls in re.findall(r'https?://\S+\'', str(message_attachments)):
                print(f"Сервер: {message_guild_name}, Дата: {time.ctime()}, {message_author} : {urls[:-1]}")
        else:
            print(f"Сервер: {message_guild_name}, Дата: {time.ctime()}, {message_author} : {message_content}")

        if not (message_content[
                :1] in startswith_word) and not message_author.bot and message_content != '<@"Your discord bot id">':
            
            base.execute('CREATE TABLE IF NOT EXISTS messages (userid INT, content STRING, links INT)')
            base.commit()
            
            if len(re.findall(r'https?://\S+.png|.jpeg|.jpg\'', str(message_attachments))) == 1:
                url = re.findall(r'https?://\S+\'', str(message_attachments))
                cursor.execute('INSERT INTO messages VALUES(?, ?, ?)', (message_author.id, url[0][:-1], 1))
                
            elif len(re.findall(r'https?://\S+.png|.jpeg|.jpg\'', str(message_attachments))) > 1:
                for urls in re.findall(r'https?://\S+\'', str(message_attachments)):
                    cursor.execute('INSERT INTO messages VALUES(?, ?, ?)', (message_author.id, urls[:-1], 1))
                    
            elif len(re.findall(r'https?://\S+', str(message_content))) == 1:
                for urls in re.findall(r'https?://\S+', str(message_content)):
                    cursor.execute('INSERT INTO messages VALUES(?, ?, ?)', (message_author.id, urls[:-1], 0))
                    
            elif message_content != '':
                cursor.execute('INSERT INTO messages VALUES(?, ?, ?)', (message_author.id, message_content, 2))
                
            base.commit()
                
        if message_content_lower == 'start_game':
            base.execute(
                'CREATE TABLE IF NOT EXISTS games (server_id INT, open STRING, screen TEXT, score INT,  '
                'moved BOOLEAN, move BOOLEAN)')
            base.commit()
            cursor.execute(f"SELECT * FROM games WHERE open = 'Открыта' AND server_id = {message_guild_id}")
            records = cursor.fetchone()
            if records:
                screen, score, moved, move = game_2048.key_handler('none', records[2],
                                                                   records[3], records[4], records[5])
                screen, score, animal_stile = game_2048.prtScreen(screen, score)
                message = await message.channel.send("Score: " + str(score) + "\n" + animal_stile)
                reactions = ['⬅', '⬆', '⬇', '➡']
                for reaction in reactions:
                    await message.add_reaction(reaction)
            else:
                cursor.execute("INSERT INTO games VALUES (?, ?, ?, ?, ?, ?)",
                               (int(message_guild_id), str('Открыта'), screen_for_game, int(0), True, True))
                base.commit()
                screen, score, moved, move = game_2048.start_game_2048(screen_for_game, 0, True, True)
                screen, score, animal_stile = game_2048.prtScreen(screen, score)
                cursor.execute(f"UPDATE games SET screen = '{screen}', score = {score}, moved = {moved}, move = {move} "
                               f"WHERE (open == 'Открыта') AND (server_id == {message_guild_id})")
                base.commit()
                message = await message.channel.send("Score: " + str(score) + "\n" + animal_stile)
                reactions = ['⬇', '⬆', '➡', '⬅']
                for reaction in reactions:
                    await message.add_reaction(reaction)

        if message_content_lower == 'stat_games':
            base.execute(
                'CREATE TABLE IF NOT EXISTS games (server_id INT, open STRING, screen TEXT, score INT,  '
                'moved BOOLEAN, move BOOLEAN)')
            base.commit()
            cursor.execute(f"SELECT * FROM games WHERE server_id = {message_guild_id} ORDER BY score DESC LIMIT 10")
            records = cursor.fetchall()
            if records:
                masters = ""
                for number, item in enumerate(records, start=1):
                    masters += f"Игра №{number}:\n" + "Статус: " + str(item[1]) + ". " + "Очки: " + str(item[3]) + "\n"
                cursor.execute(
                    f"SELECT COUNT(*) FROM games WHERE (open == 'Выигрыш') AND server_id = {message_guild_id}")
                records = cursor.fetchone()
                winners = "Количество побед: "
                if records:
                    winners += str(records[0])
                await message.channel.send(masters + winners)
            else:
                await message.channel.send("Пока что игр не создано")

        if client.user.mentioned_in(message) or random.randint(0, 20) == 10:
            if random.randint(0, 10) == 1:
                url = servant.looking_for_a_link()
                img_data = requests.get(url).content
                time_now = today.strftime("%Y-%m-%d-%H.%M.%S").replace('.', '-')
                with open(f'photo_demotivator/{time_now}.jpeg', 'wb') as handler:
                    handler.write(img_data)
                photos = servant.photo_change('', f'photo_demotivator/{time_now}.jpeg')
                with open(f'{photos}', 'rb') as file:
                    picture = discord.File(file)
                    await message.channel.send(file=picture)
            else:
                sqlite_select_query = """SELECT * from messages ORDER BY RANDOM() LIMIT 1;"""
                cursor.execute(sqlite_select_query)
                records = cursor.fetchone()
                await message.channel.send(records[1])

        if message_content_lower == 'anime':
            embed = to_return_a_random_anime_picture()
            await message.channel.send(embed=embed)

        if message_content_lower_with_prefix == "$hentai":
            url = to_return_a_random_hentai()
            await message.channel.send(url)

        if message_content_lower[:3] == 'dem' or message_content_lower[:5] == 'r_dem':
            if len(re.findall(r'https?://\S+\'', str(message_attachments))) == 1 and message_content_lower[:3] == 'dem':
                url = re.findall(r'https?://\S+\'', str(message_attachments))
                img_data = requests.get(url[0][:-1]).content
                content = message_content[4:]
            elif message_content_lower[:5] == 'r_dem':
                url = servant.looking_for_a_link()
                img_data = requests.get(url).content
                content = message_content[6:]
            else:
                content = ''
                img_data = ''
                await message.channel.send("Приложите одну фотографию, пожалуйста!")
            time_now = today.strftime("%Y-%m-%d-%H.%M.%S").replace('.', '-')
            with open(f'photo_demotivator/{time_now}.jpeg', 'wb') as handler:
                handler.write(img_data)
            photos = servant.photo_change(content.split(','), f'photo_demotivator/{time_now}.jpeg')
            with open(f'{photos}', 'rb') as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)

        if message_content_lower[:10] == 'your_quote':
            content = message_content[12:]
            avatar = message_author.avatar_url
            if len(content.split()) >= 1:
                dem = Quote(str(content), str(message_author)[:-5])
            else:
                dem = Quote('Я забыл написать тут текст!', str(message_author)[:-5])
            nickname_file = 'quote_demotivator/' + today.strftime("%Y-%m-%d-%H.%M.%S").replace('.', '-') + '.png'
            dem.create(str(avatar), use_url=True, result_filename=nickname_file)
            with open(nickname_file, 'rb') as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)

        if message_content_lower == 'quote':
            await message.channel.send(embed=quote())

        if random.randint(0, 20) == 1:
            await message.add_reaction(emoticons[random.randint(0, len(emoticons) - 1)])

        if message_content_lower_with_prefix in dict_help_bot:
            await message.channel.send(dict_help_bot[message_content_lower_with_prefix])

        if message_content_lower_with_prefix in question_for_kek_dela and not message_author.bot:
            await message.reply(kak_dela_from_bot[random.randint(0, len(kak_dela_from_bot) - 1)])

        if message_content_lower_with_prefix in word_for_hi and not message_author.bot:
            await message.reply(hi_from_bot[random.randint(0, len(hi_from_bot) - 1)])

        if message_content_lower[:13] == 'analyze_photo':
            if len(re.findall(r'https?://\S+\'', str(message_attachments))) == 1:
                url = re.findall(r'https?://\S+\'', str(message_attachments))
                url += []
                picture = face_analyze(url[0][:-1])
                if picture:
                    age, floor, race, emotion = picture[0], picture[1], picture[2], picture[3]
                    race = race.items()
                    emotion = emotion.items()
                    floor = translator.translate(floor, dest='ru').text.title()
                    embed = discord.Embed(
                        title=f"Пол: {floor}",
                        colour=16705372,
                    )
                    race = [str(item) + ' ' + str(content) for item, content in race][0]
                    emotion = [str(item) + ' ' + str(content) for item, content in emotion][0]
                    race = translator.translate(race, dest='ru').text.title()
                    emotion = translator.translate(emotion, dest='ru').text.title()
                    embed.set_image(url=url[0][:-1])
                    embed.add_field(name='Раса', value=race + "%")
                    embed.add_field(name='Эмоция', value=emotion + "%")
                    embed.set_author(name=f"Возраст: {age}")
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send(
                        "Не могу распознать лицо на фотографии, можете попробовать еще раз с другим фото!")
            else:
                await message.channel.send("Приложите одну фотографию для исследования!")

        if message_content_lower[:9] == 'id_photos':
            if len(re.findall(r'https?://\S+\'', str(message_attachments))) == 2:
                urls = re.findall(r'https?://\S+\'', str(message_attachments))
                embed = face_verify(img_1=urls[0][:-1], img_2=urls[1][:-1])
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Укажите 2 фотографии, пожалуйста! :(")

        if message_content_lower[:15] == 'youtube_comment' or message_content_lower[:5] == 'tweet':
            if len(message_content_lower.split()) >= 3:
                string = str(*message_attachments)
                user = message_content_lower.split()[1].title()
                comment = '%20'.join(message_content.split()[2:])
                if comment[-1] in [',', '.']:
                    comment = comment[:-1]
                if string and message_content_lower.split()[0] in sites:
                    await message.channel.send(
                        f'https://some-random-api.ml/canvas/{sites[message_content_lower.split()[0]]}?avatar=https' +
                        f'://cdn.discordapp.com/attachments/{string[39:]}&username={user}&displayname=' +
                        f'{user}&comment={comment}')
                else:
                    await message.channel.send("Приложите фотографию")
            else:
                await message.channel.send(
                    "Укажите: $tweet/$youtube_comment <User> <Comment> <Img>" + "\n" +
                    "Например: $tweet/$youtube_comment Ваня Я прошёл марио пати! (+фото его аватарки)")

        if message_content_lower in photo_changes:
            string = str(*message_attachments)
            if string != '':
                await message.channel.send(photo(string, message_content_lower))
            else:
                await message.channel.send("Приложите фотографию, пожалуйста")

        if message_content_lower[:6] == 'binary':
            response = requests.get(
                f"https://some-random-api.ml/binary?encode={translator.translate(message_content_lower[6:]).text}")
            if response.status_code == 200:
                json_data = json.loads(response.text)
                embed = discord.Embed(color=0xff9900, title=json_data['binary'])
                await message.channel.send(embed=embed)
            else:
                await message.channel.send('После "$binary" укажите строку')

        if message_content_lower == 'anime_quote':
            response = requests.get('https://some-random-api.ml/animu/quote')
            json_data = json.loads(response.text)
            embed = discord.Embed(
                title=translator.translate(json_data['character'], dest='ru').text,
                description=translator.translate(json_data['sentence'], dest='ru').text,
                color=0xff9900,
            )
            embed.set_author(name=translator.translate(json_data['anime'], dest='ru').text, )
            await message.channel.send(embed=embed)

        if message_content_lower in dict_links_for_img:
            response = requests.get(f'https://some-random-api.ml/{dict_links_for_img[message_content_lower]}')
            json_data = json.loads(response.text)
            title = translator.translate(message_content_lower, dest='ru').text
            embed = discord.Embed(color=0xff9900, title=title.title())
            embed.set_image(url=json_data['link'])
            await message.channel.send(embed=embed)

        if message_content_lower in dict_animal:
            response = requests.get(f'https://some-random-api.ml/{dict_animal[message_content_lower]}')
            json_data = json.loads(response.text)
            title = translator.translate(message_content_lower, dest='ru').text
            fact = translator.translate(json_data['fact'], dest='ru')
            embed = discord.Embed(color=0xff9900, title=title.title(), description=fact.text)
            embed.set_image(url=json_data['image'])
            await message.channel.send(embed=embed)

        if message_content_lower == 'joke' or message_content_lower == 'шутка':
            try:
                response = requests.get(f'https://some-random-api.ml/joke')
                json_data = json.loads(response.text)
                result = translator.translate(json_data['joke'], dest='ru').text
                embed = discord.Embed(color=0xff9900, title=result)
                await message.channel.send(embed=embed)
            except KeyError:
                await message.channel.send("Попробуйте ещё раз")
        
        if message_content_lower == 'meme':
            await message.channel.send(embed=await pyrandmeme())
            
        if message_content_lower in word_from_anekdot:
            anecdote, category = random_anecdotes()
            await message.channel.send(f"Категория: {category}\nАнекдот: {anecdote}")

        if message_content_lower_with_prefix == 'умница' or message_content_lower_with_prefix == 'умничка':
            await message.channel.send("Знаю)")


client.run(TOKEN)
