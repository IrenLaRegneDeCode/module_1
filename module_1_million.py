from itertools import combinations

import pandas as pd
import collections

movie = pd.read_csv('data/movie_bd_v5.csv')
print(movie.info())
with pd.option_context('display.max_rows', None, 'display.max_columns', None):

    # Вопрос 1. У какого фильма из списка самый большой бюджет?

    movie1 = movie.copy()  # копия основной таблицы, номерной код копии равен номеру задания

    movie1 = movie1.groupby(['original_title'])['budget'].max().sort_values(ascending=False)

    print('"Задание 1: самый большой бюджет: ', movie1.head(1))

    # Вопрос 2. Какой из фильмов самый длительный (в минутах)?

    movie2 = movie.copy()

    movie2 = movie2.groupby(['original_title'])['runtime'].max().sort_values(ascending=False)  # the longest film

    print('"Задание 2: самый длительный фильм', movie2.head(1))

    # Вопрос 3. Какой из фильмов самый короткий (в минутах)?

    movie3 = movie.copy()

    movie3 = movie3.groupby(['original_title'])['runtime'].min().sort_values(ascending=True)

    print('Задание 3:', movie3.head(1))

    # Вопрос 4. Какова средняя длительность фильмов?

    movie4 = movie.copy()

    movie_result = movie4.runtime.mean()

    print('Задание 4:', movie_result)

    # Вопрос 5. Каково медианное значение длительности фильмов?

    movie5 = movie.copy()

    movie5 = movie5.runtime.median()

    print('Задание 5:', movie5)

    # Вопрос 6. Какой фильм самый прибыльный?

    movie6 = movie.copy()

    # подсчет прибыли
    def calc_profit(row):
        profit = row['revenue']-row['budget']
        return profit


    movie6['profit'] = movie6.apply(calc_profit, axis=1)

    result = movie6[movie6.profit == movie6.profit.max()].original_title

    print('Задание 6:', result)

    # Вопрос 7. Какой фильм самый убыточный?

    movie7 = movie.copy()

    movie7['profit'] = movie7.apply(calc_profit, axis=1)
    min_profit = movie7[movie7.profit == movie7.profit.min()].original_title

    print('Задание 7:', min_profit)

    # Вопрос 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

    movie8 = movie.copy()

    result = movie8[movie8.revenue > movie8.budget].value_counts()

    print('Задание 8:', len(result))

    # Вопрос 9. Какой фильм оказался самым кассовым в 2008 году?

    movie9 = movie.copy()

    max_profit_2008 = movie9[(movie9.revenue == movie9[movie9.release_year == 2008].revenue.max())].original_title

    print('Задание 9:', max_profit_2008)

    # Вопрос 10. Самый убыточный фильм за период с 2012 по 2014 годы (включительно)?

    movie10 = movie.copy()

    movie10['profit'] = movie.apply(calc_profit, axis=1)

    movie_profit_min = movie10.profit.min()  # переменная для обозначения минимальной прибыли

    # определение самого убыточного фильма
    movie_profit_name = movie10[(movie10.profit == movie_profit_min) & (movie10.release_year >= 2012)
                           & (movie10.release_year <= 2014)].original_title

    print("Задание 10: Самый убыточный фильм ", movie_profit_name, " за период с 2012 по 2014 годы ")

    # Вопрос 11. Какого жанра фильмов больше всего?

    # создание списка жанров:
    genres_list = ['Comedy', 'Action', 'Adventure', 'Drama', 'Thriller']

    higher_amount = 0

    # найти жанры

    for genre in genres_list:
        cur_amt = len(movie[movie.genres.str.contains(genre, na=False)])
        if cur_amt > higher_amount:
            higher_amount = cur_amt
            higher_amount_genre = genre

    print("Задание 11: Жанр ", higher_amount_genre, " у наибольшего количества фильмов ", higher_amount)

    # Вопрос 12. Фильмы какого жанра чаще всего становятся прибыльными?
    movie12 = movie.copy()

    # выбрать прибыльные фильмы

    movie12['profit'] = movie12.apply(calc_profit, axis=1)
    movie12 = movie12[movie12.profit > 0]

    c = collections.Counter()
    for i in movie12.genres.str.split('|'):
        for j in i:
            c[j] += 1
    print(max(c, key=c.get))

    # найти жанры фильмов
    genres_list = ['Comedy', 'Action', 'Adventure', 'Drama', 'Thriller']

    higher_amount = 0

    # посчитать жанры

    for genre in genres_list:
        cur_amt = len(movie[movie.genres.str.contains(genre, na=False)])
        if cur_amt > higher_amount:
            higher_amount = cur_amt
            higher_amount_genre = genre

    print("Задание 12: ", higher_amount_genre)

    # Вопрос 13. У какого режиссёра самые большие суммарные кассовые сборы?

    movie13 = movie.copy()

    movie13.director = movie13.director.str.encode('latin1').str.decode('utf8')

    # поделить режиссеров (split)
    movie13['one_director'] = movie13['director'].str.split('|')
    directors = movie13.explode('one_director')
    print(movie13.one_director)

    # отсортировать по режиссеру, найти их суммарную кассу

    result = directors.groupby(['one_director']).revenue.sum()
    print("Задание 13: ", result.sort_values(ascending=False).head(1))

    # Вопрос 14. Какой режиссер снял больше всего фильмов в стиле Action?

    movie14 = movie.copy()
    action_movies = movie14[movie14.genres.str.contains('Action', na=False)]

    # поделить режиссеров (split) и размножить строчки
    action_movies['one_director'] = action_movies['director'].str.split('|')
    action_movies = action_movies.explode('one_director')

    # посчитать суммарную кассу режиссеров (split)
    result = action_movies.groupby(['one_director']).one_director.value_counts()

    print("Задание 14: ", result.sort_values(ascending=False).head(1))

    # Вопрос 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?

    movie15 = movie.copy()

    # выделить фильмы 2012 года
    movies_2012 = movie15[movie15.release_year == 2012]

    # разделить актеров на строчки
    movies_2012['one_actor'] = movies_2012['cast'].str.split('|')
    movies_2012 = movies_2012.explode('one_actor')

    # отсортировать по кассовым сборам
    result = movies_2012.groupby(['one_actor'])['revenue', 'original_title'].sum().sort_values(['revenue'], ascending=False)

    print("Задание 15: ", result.head(5))

    # Вопрос 16. Какой актер снялся в большем количестве фильмов?
    # Примечание: в фильмах, где бюджет выше среднего по данной выборке.

    movie16 = movie.copy()

    high_budget_films = movie16[movie16.budget > movie16.budget.mean()]

    # разделить актеров на строчки
    high_budget_films['one_actor'] = high_budget_films['cast'].str.split('|')
    high_budget_films = high_budget_films.explode('one_actor')

    result = high_budget_films.one_actor.value_counts()

    print("Задание 16: ", result)

    # Вопрос 17. В фильмах какого жанра больше всего снимался Nicolas Cage?

    movie17 = movie.copy()

    # отобрать фильмы Н. Кейджа
    nic_films = movie17[movie17.cast.str.contains('Nicolas Cage')]

    # выделить жанры
    nic_films['one_genre'] = nic_films['genres'].str.split('|')
    nic_films = nic_films.explode('one_genre')

    # посчитать жанры
    result = nic_films.one_genre.value_counts()

    print("Задание 17: ", result.head(1))

    # Вопрос 18. Самый убыточный фильм от Paramount Pictures?
    #
    movie18 = movie.copy()

    # отобрать фильмы Paramount Pictures
    para_pic_films = movie18[movie18.production_companies.str.contains('Paramount Pictures')]

    # вызвать функцию calc_profit
    para_pic_films['profit'] = para_pic_films.apply(calc_profit, axis=1)

    # найти самый убыточный фильм
    result = para_pic_films[para_pic_films.profit == para_pic_films.profit.min()].original_title

    print("Задание 18: ", result)

    # Вопрос 19. Какой год стал самым успешным по суммарным кассовым сборам?

    movie19 = movie.copy()

    result = movie19.groupby(['release_year']).revenue.sum().sort_values(ascending=False)

    print("Задание 19: ", result)

    # Вопрос 20. Какой самый прибыльный год для студии Warner Bros?

    movie20 = movie.copy()

    # отобрать фильмы Warner Bros.
    wb_movies = movie20[movie20.production_companies.str.contains('Warner Bros')]

    # вызвать функцию calc_profit
    wb_movies['profit'] = wb_movies.apply(calc_profit, axis=1)

    # сгруппировать по годам
    result = wb_movies.groupby(['release_year']).profit.sum().sort_values(ascending=False)
    print("Задание 20: ", result.head(1))

    # Вопрос 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

    movie21 = movie.copy()

    # функция, выделяющая месяц из release_date
    def extract_month(row):
        month = row['release_date'].split('/')
        return month[0]

    # вызов функции, находим месяц, считаем количество
    movie21['month'] = movie21.apply(extract_month, axis=1)
    movie21 = movie21.month.value_counts(sort=True, ascending=False)

    print("Задание 21: ", movie21)

    # Вопрос 22. Сколько суммарно вышло фильмов летом (за июнь, июль, август)?

    movie22 = movie.copy()

    # вызов функции extract_month
    movie22['month'] = movie22.apply(extract_month, axis=1)

    # считаем летние месяцы
    result = movie22[movie22.month.str.contains('6|7|8')].month.value_counts().sum()

    print("Задание 22: ", result)

    # Вопрос 23. Для какого режиссера зима — самое продуктивное время года?

    movie23 = movie.copy()

    # функция, выделяющая сезоны
    def get_season(row):
        month = extract_month(row)
        if month in '345':
            return 'spring'
        elif month in '678':
            return 'summer'
        elif month in '91011':
            return 'autumn'
        else:
            return 'winter'


    movie23['season'] = movie23.apply(get_season, axis=1)

    # разделяем режиссеров, выделяем в отдельную колонку
    movie23['one_director'] = movie23['director'].str.split('|')
    month_director = movie23.explode('one_director')

    # определяем зимних рекордсменов
    movie23 = movie23[movie23['season'] == 'winter'].one_director.value_counts()
    print("Задание 23: ", movie23.head())

    # Вопрос 24. Какая студия даёт самые длинные названия своим фильмам по количеству символов?

    movie24 = movie.copy()

    # выделяем студии в отдельную колонку
    movie24['studio'] = movie24['production_companies'].str.split('|')
    company = movie24.explode('studio')

    # считаем длину названий фильмов, сортиоуем по длине
    company['name_length'] = company['original_title'].str.len()
    company = company.groupby(['studio']).name_length.mean().sort_values(ascending=False)

    print("Задание 24: ", company.head())

    # Вопрос 25. Описания фильмов какой студии в среднем самые длинные по количеству слов?

    movie25 = movie.copy()

    # выделяем студии в отдельную колонку
    movie25['studios'] = movie25['production_companies'].str.split('|')
    company = movie25.explode('studios')

    # функция, считающая слова
    def count_words(row):
        word = 1
        for s in row['tagline']:
            if s == ' ':
                word = word + 1
        return word


    company['quant_words'] = company.apply(count_words, axis=1)

    # считаем компании
    company = company[company.studios.str.contains('Universal Pictures|Warner Bros|'
                                                   'Midnight Picture Show|Paramount Pictures|Total Entertainment')]
    print(company[['studios', 'quant_words']].sort_values(['quant_words'], ascending=False).head())

    company = company.groupby(['studios']).quant_words.mean().sort_values(ascending=False)
    print("Задание 25: ", company)

    # Вопрос 26. Какие фильмы входят в один процент лучших по рейтингу?

    movie26 = movie.copy()

    # отбираем фильмы по рейтингу
    movie26 = movie26.loc[movie26['vote_average'] >
                          movie26.quantile(0.99, numeric_only=True)['vote_average']]['original_title']

    print("Задание 26: ", movie26)

    # Вопрос 27. Какие актеры чаще всего снимаются в одном фильме вместе?

    movie27 = movie.copy()

    def combo(row):

        for row in movie27['cast']:
            # в каждой строчке дф, в колонке 'cast' из строки создать список актёров.

            # actors_list = (movie27[movie27.cast]).row.to_list()
            actors_list = row['cast'].UserString()

            # в списке составить пары.
            for actors in actors_list:
                actor_pairs = combinations(actors_list, 2)
        return actor_pairs


    # Посчитать количество пар. по всему дф.
    movie27['actor_pairs'] = movie27.apply(combo, axis=1)
    s = pd.Series(movie27['actor_pairs']).value_counts()

    print("Задание 27: ", s)

    # actors_pairs = movie27
    # actors_pairs['actors_pair'] = combo(list)
    # actors_comp['actors_pair'] = movie27[movie27(combo(list))]
    # actors_pairs = movie27.actors_pairs.value_count()
    #
    # print("Задание 27: ", actors_pairs)