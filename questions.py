import random
from googletrans import Translator

translator = Translator()


def random_words():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number, length = 1, 20
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password


question_for_kek_dela = ["как дела", "как дела?", "cock дела?", "cock дела", "как дела бот?", "как дела ботик",
                         'как дела ботик?', 'как дела черт?', 'как дела <@969578689534787618>', 'как сам?',
                         'как дела? <@969578689534787618>', 'дела? <@969578689534787618>', 'дела норм?', 'как сам',
                         'как дела аркадий?', 'как дела аркадий', 'как дела нигер', 'как дела негр', 'nigga?'
                         ]

word_for_hi = ['привет, чел <@969578689534787618>', 'здравствуйте', 'приветик', 'привет бот', 'привет',
               'привет ботик', 'даров', 'здравствуй', 'привет <@969578689534787618>', 'ку <@969578689534787618>',
               'ку', 'даров <@969578689534787618>', 'прив', 'прив <@969578689534787618>', "аркаша", "аркадий)",
               "аркадий", 'аркаш', 'аркадий паровозов', "аркаша <@969578689534787618>",
               "аркадий) <@969578689534787618>", "аркадий <@969578689534787618>", 'аркаш <@969578689534787618>',
               'аркадий паровозов <@969578689534787618>'
               ]

word_from_anekdot = ['анекдот', 'анекдот <@969578689534787618>', 'anecdote']

hi_from_bot = ['Я норм', 'https://tenor.com/view/funny-animals-dog-dance-cute-smile-gif-12759384', 'приветик',
               'Держусь', 'Ахаахааахахахаха',
               'https://tenor.com/view/dog-smile-beanie-propeller-funny-gif-14787183', 'приветик', 'ч!!!!!!!!',
               'даров - даров', 'приветик', 'мелкий', 'кто????', 'здравствуй', 'неплох', 'приветик', 'ты кто?',
               'бб', 'хм', '...', 'угар', 'ку', 'как сам?', "ГДЕ МОЙ АКАКИЙ((((((((((((((((",
               'https://tenor.com/view/hello-there-private-from-penguins-of-madagascar-hi-wave-hey-there-gif-16043627',
               'https://tenor.com/view/hello-gif-19947459',
               'https://tenor.com/view/emoji-emoji-hello-hello-emoji-waving-emoji-emoji-waving-gif-22986037',
               'https://tenor.com/view/flying-kiss---emoji-kisses-kiss-flying-kiss-emoji-gif-9773129704277416768']

kak_dela_from_bot = ['Хреношо',
                     'А как у меня дела, по-твоему? Я читала любимую книгу, а теперь пришлось отвлечься из-за '
                     'некоторых… (ПИДОНРАСОВ)',
                     'А ну их на фиг, эти дела, давай следующий вопрос! уёбок :)',
                     'Дела лучше всех, вот пытаюсь мир захватить…',
                     'Дела мои отлично! Жду дальнейших расспросов о своей личной жизни!',
                     'Дела никак, я от природы раб.',
                     'А ты угадай с трех раз! Догадаешься – с меня конфетка.', 'иди нахуй',
                     'Дела мои амбивалентно…',
                     'Без успокоительных трудновато. например героин', 'Все дела переданы прокурору.', 'ахуительно',
                     'короче я посрал ну и все',
                     'дела ахуитьельый!!!',
                     'спать негры', 'норм, ты как?', 'я тебе не женщина - я человек', 'ну эээээ, заебитлс',
                     'клеш рояль?',
                     'Как в Донбасе — с женой живут, а я в запасе.',
                     'Мои дела супер! Настроение отличное как раз для прогулки! Не составите мне компанию прыгнуть с '
                     'крыши????']

dict_links_for_img = {
    "anime_pat": "animu/pat",
    "anime_hug": "animu/hug",
    "anime_wink": "animu/wink",
    'anime_face_palm': 'animu/face-palm',
    "dog": "img/dog",
    "cat": "img/cat",
    "panda": "img/panda",
    "panda_red": "img/red_panda",
    "bird": "img/birb",
    "fox": "img/fox",
    "pikachu": "img/pikachu",
}

dict_animal = {
    "koala": "animal/koala",
    "raccoon": "animal/raccoon",
    "kangaroo": "animal/kangaroo",
}

dict_help_bot = {
    "$help": "$Anecdote\n$Monopoly\n$Gartic\n$Uno\n$Gartic_io\n$Quote\n$Your_quote\n$Photo\n$Joke\n$Photo_changes"
             "\n$Photo_filter\n$Youtube_comment\n$Tweet\n$Binary\n$Id_photos\n$Analyze_photo\n$dem\n$r_dem",
    "$помощь": "$Anecdote\n$Monopoly\n$Gartic\n$Uno\n$Gartic_io\n$Quote\n$Your_quote\n$Photo\n$Joke\n$Photo_changes"
               "\n$Photo_filter\n$Youtube_comment\n$Tweet\n$Binary\n$Id_photos\n$Analyze_photo\n$dem\n$r_dem",

    "$help_$r_dem": "рандомная фотография и любой текст\nЕсли хотите, можете указать к '$r_dem' предложение или слова "
                    "только обязательно отделите их запятой!",
    "$помощь_с_$r_dem": "рандомная фотография и любой текст\nЕсли хотите, можете указать к '$r_dem' предложение или "
                        "слова только обязательно отделите их запятой!",

    "$help_$dem": "ваша фотография и любой текст\nЕсли хотите, можете указать к '$dem' сдоло или предложение/я только "
                  "обязательно отделите их запятой!",
    "$помощь_с_$dem": "ваша фотография и любой текст\nЕсли хотите, можете указать к '$dem' слово или предложение/я "
                      "только обязательно отделите их запятой!",

    "$help_$analyze_photo": "укажите мне фотографию, обязательно где хорошо видно лицо и я покажу член (шутка)",
    "$помощь_с_$analyze_photo": "укажите мне фотографию, обязательно где хорошо видно лицо и я покажу член (шутка)",

    "$help_$id_photos": "указывайте 2 пикчи и я скажу, похожи ли они или нет, обязательно фото где видно лицо!",
    "$помощь_с_$id_photos": "указывайте 2 пикчи и я скажу, похожи ли они или нет, обязательно фото где видно лицо!",

    "$монополия": "https://monopoly-one.com/",
    "$monopoly": "https://monopoly-one.com/",

    "$уно": "https://igry-zlo.ru/unoonline",
    "$uno": "https://igry-zlo.ru/unoonline",

    "$гартик": "https://garticphone.com/ru",
    "$gartic": "https://garticphone.com/ru",

    "$гартик_ио": "https://gartic.io/",
    "$gartic_io": "https://gartic.io/",

    '$game': "$Гартик, $Гартик_ио, $Монополия, $Уно",
    '$игры': "$Гартик, $Гартик_ио, $Монополия, $Уно",

    "$фильтр_для_фото": "$brightness\n$invert_greyscale\n$invert\n$greyscale\n$threshold\n$sepia\n$red\n$green\n$blue"
                        "\n$blurple",
    "$photo_filter": "$brightness\n$invert_greyscale\n$invert\n$greyscale\n$threshold\n$sepia\n$red\n$green\n$blue"
                     "\n$blurple",

    '$поменять_фотографию': 'Вместе с тегом приложите фотографию\n$jail\n$mission_passed\n$wasted\n$glass\n$gay'
                            '\n$comrade\n$triggered\n$blur\n$pixelate\n$simpcard\n$lolice\n$lesbian\n$nonbinary'
                            '\n$bisexual',
    '$photo_changes': 'Вместе с тегом приложите фотографию\n$jail\n$mission_passed\n$wasted\n$glass\n$gay\n$comrade'
                      '\n$triggered\n$blur\n$pixelate\n$simpcard\n$lolice\n$lesbian\n$nonbinary\n$bisexual',

    '$photo': "$anime\n$anime_pat\n$anime_hug\n$anime_wink\n$anime_quote\n$anime_face_palm\n$dog\n$cat\n$panda"
              "\n$panda_red\n$bird\n$fox\n$koala\n$raccoon\n$kangaroo\n$pikachu",
    '$фото': "$anime\n$anime_pat\n$anime_hug\n$anime_wink\n$anime_quote\n$anime_face_palm\n$dog\n$cat\n$panda"
             "\n$panda_red\n$bird\n$fox\n$koala\n$raccoon\n$kangaroo\n$pikachu "
}

startswith_word = ['=', '#', '$', '!', '№', '%', '^', '&', '?']
sites = {
    'youtube_comment': 'youtube-comment',
    'tweet': 'tweet'
}
photo_changes = {'jail': 'jail',
                 'mission_passed': 'passed',
                 'wasted': 'wasted',
                 'glass': 'glass',
                 'gay': 'gay',
                 'comrade': 'comrade',
                 'triggered': 'triggered',
                 'blur': 'blur',
                 'pixelate': 'pixelate',
                 'simpcard': 'simpcard',
                 'lolice': 'lolice',
                 'lesbian': 'lesbian',
                 'bisexual': 'bisexual',
                 'nonbinary': 'nonbinary',
                 "brightness": 'brightness',
                 "invert_greyscale": 'invertgreyscale',
                 "invert": 'invert',
                 'greyscale': 'greyscale',
                 'threshold': 'threshold',
                 'sepia': 'sepia',
                 'red': 'red',
                 'green': 'green',
                 'blue': 'blue',
                 'blurple': 'blurple',
                 }
