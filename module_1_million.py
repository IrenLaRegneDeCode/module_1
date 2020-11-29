from itertools import combinations

import pandas as pd
import collections

movie = pd.read_csv('data/movie_bd_v5.csv')
print(movie.info())
with pd.option_context('display.max_rows', None, 'display.max_columns', None):


    # Вопрос 1. У какого фильма из списка самый большой бюджет?

    # movie1 = movie.groupby(['original_title'])['budget'].max().sort_values(ascending=False)
    # print('"Задание 1: самый большой бюджет' movie1.head(1))

    # Вопрос 2. Какой из фильмов самый длительный (в минутах)?

    # movie2 = movie.groupby(['original_title'])['runtime'].max().sort_values(ascending=False) #the longest film
    # print('"Задание 2: самый длительный фильм' movie2.head(1))

    # Вопрос 3. Какой из фильмов самый короткий (в минутах)?

    # movie3 = movie.groupby(['original_title'])['runtime'].min().sort_values(ascending=True)
    # print('Задание 3:' movie3.head(1))

    # Вопрос 4. Какова средняя длительность фильмов?
    # movie4 = movie.describe()
    # movie_result=movie4.runtime
    # print('Задание 4:'movie_result)

    # Вопрос 5. Каково медианное значение длительности фильмов?
    # movie5=movie.runtime.median()
    # print('Задание 5:' movie5)

    # Вопрос 6. Какой фильм самый прибыльный?
    # movie6 = movie.copy()

    def calc_profit(row):
        profit = row['revenue']-row['budget']
        return profit

    # movie6['profit'] = movie.apply(calc_profit, axis=1)
    #
    # print('Задание 6:'movie6[movie6.profit == movie6.profit.max()].original_title)

    # Вопрос 7. Какой фильм самый убыточный?

    # print('Задание 7:' movie6[movie6.profit == movie6.profit.min()].original_title)

    # Вопрос 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?
    # movie8 = movie[movie.revenue > movie.budget].value_counts()
    # print('Задание 8:' len(movie8))

    # Вопрос 9. Какой фильм оказался самым кассовым в 2008 году?

    # movie9 = movie.copy()
    #
    # max_profit_2008 = movie9[(movie9.revenue == movie9[movie9.release_year == 2008].revenue.max())].original_title
    # print('Задание 9:', max_profit_2008)


    # Вопрос 10. Самый убыточный фильм за период с 2012 по 2014 годы (включительно)?
    # movie10 = movie.copy()
    #
    # movie10['profit'] = movie.apply(calc_profit, axis=1)
    #
    # movie_profit_min = movie10.profit.min()
    # movie_profit_name = movie10[(movie10.profit == movie_profit_min) & (movie10.release_year >= 2012)
    #                                                       & (movie10.release_year <= 2014)].original_title
    # print("Задание 10: Самый убыточный фильм ", movie_profit_name, " за период с 2012 по 2014 годы, c убытком ",movie_profit_min)

    # Вопрос 11. Какого жанра фильмов больше всего?

    #найти жанры

    # genres_list = ['Comedy', 'Action', 'Adventure', 'Drama', 'Thriller']
    #
    # higher_amount = 0
    #
    # for genre in genres_list:
    #     cur_amt = len(movie[movie.genres.str.contains(genre,na=False)])
    #     if cur_amt > higher_amount:
    #         higher_amount = cur_amt
    #         higher_amount_genre = genre
    # print("Задание 11: Жанр ",higher_amount_genre," у наибольшего количества фильмов ",higher_amount)


    #         # Вопрос 12. Фильмы какого жанра чаще всего становятся прибыльными?
    #
    # # найти жанры фильмов
    # # выбрать прибыльные фильмы
    # # посчитать жанры
    #     movie12 = movie.copy()
    #
    #     movie12['profit'] = movie12.apply(calc_profit, axis=1)
    #     movie12 = movie12[movie12.profit > 0]
    #
    #
    #     c = collections.Counter()
    #     for i in movie12.genres.str.split('|'):
    #         for j in i:
    #             c[j] +=1
    #     print(max(c, key=c.get))
    #
    #        # посчитать жанры
    #     genres_list = ['Comedy', 'Action', 'Adventure', 'Drama', 'Thriller']
    # #
    #     higher_amount = 0
    #
    #     for genre in genres_list:
    #         cur_amt = len(movie[movie.genres.str.contains(genre,na=False)])
    #         if cur_amt > higher_amount:
    #             higher_amount = cur_amt
    #             higher_amount_genre = genre
    #     print(higher_amount_genre)


    # # Вопрос 13. У какого режиссёра самые большие суммарные кассовые сборы?
    #
    # movie13 = movie.copy()
    #
    # movie13.director = movie13.director.str.encode('latin1').str.decode('utf8')
    #
    # #поделить режиссеров
    # movie13['one_director'] = movie13['director'].str.split('|')
    # directors = movie13.explode('one_director')
    # print(movie13.one_director)
    #
    # #отсортировать по режиссеру, найти их суммарную кассу
    #
    # result = directors.groupby(['one_director']).revenue.sum()
    # print(result.sort_values(ascending=False).head(1))

    #
    # # Вопрос 14. Какой режиссер снял больше всего фильмов в стиле Action?
    #
    #
    # movie14 = movie.copy()
    # action_movies = movie14[movie14.genres.str.contains('Action', na=False)]
    #
    # action_movies['one_director'] = action_movies['director'].str.split('|')
    # action_movies = action_movies.explode('one_director')
    #
    # result = action_movies.groupby(['one_director']).one_director.value_counts()
    # print(result.sort_values(ascending=False).head(1))


    # # Вопрос 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?
    #
    # movie15 = movie.copy()
    #
    # movies_2012 = movie15[movie15.release_year == 2012]
    #
    # movies_2012 ['one_actor'] = movies_2012['cast'].str.split('|')
    # movies_2012 = movies_2012.explode('one_actor')
    #
    # result = movies_2012.groupby(['one_actor'])['revenue','original_title'].sum().sort_values(['revenue'],ascending=False)
    #
    # print(result.head(5))

    # # Вопрос 16. Какой актер снялся в большем количестве фильмов?
    # # Примечание: в фильмах, где бюджет выше среднего по данной выборке.
    #
    # movie16 = movie.copy()
    # high_budget_films = movie16[movie16.budget > movie16.budget.mean()]
    # # print(high_budget_films)
    #
    # high_budget_films ['one_actor'] = high_budget_films['cast'].str.split('|')
    # high_budget_films = high_budget_films.explode('one_actor')
    #
    # result = high_budget_films.one_actor.value_counts()
    #
    # print(result)


    # # Вопрос 17. В фильмах какого жанра больше всего снимался Nicolas Cage?
    #
    # movie17 = movie.copy()
    # nic_films = movie17[movie17.cast.str.contains('Nicolas Cage')]
    # # print(high_budget_films)
    #
    # nic_films ['one_genre'] = nic_films['genres'].str.split('|')
    # nic_films = nic_films.explode('one_genre')
    #
    # result = nic_films.one_genre.value_counts()
    #
    # print(result.head(1))
    #
    #
    # # Вопрос 18. Самый убыточный фильм от Paramount Pictures?
    #
    # movie18 = movie.copy()
    # para_pic_films =  movie18[movie18.production_companies.str.contains('Paramount Pictures')]
    #
    # para_pic_films['profit'] = para_pic_films.apply(calc_profit, axis=1)
    #
    # result = para_pic_films[para_pic_films.profit == para_pic_films.profit.min()].original_title
    # print(result)


    # # Вопрос 19. Какой год стал самым успешным по суммарным кассовым сборам?
    #
    # movie19 = movie.copy()
    #
    # result = movie19.groupby(['release_year']).revenue.sum().sort_values(ascending=False)
    #
    # print(result)


    # Вопрос 20. Какой самый прибыльный год для студии Warner Bros?

    # movie20 = movie.copy()
    # wb_movies = movie20[movie20.production_companies.str.contains('Warner Bros')]
    #
    # wb_movies['profit'] = wb_movies.apply(calc_profit, axis=1)
    # result = wb_movies.groupby(['release_year']).profit.sum().sort_values(ascending=False)
    # print(result.head(1))

    # # Вопрос 21. В каком месяце за все годы суммарно вышло больше всего фильмов?
    #
    # movie21 = movie.copy()


    def extract_month(row):
        month = row['release_date'].split('/')
        return month[0]
    #
    #
    # movie21['month'] = movie21.apply(extract_month, axis=1)
    # movie21 = movie21.month.value_counts(sort=True,ascending=False)
    #
    # # print(movie21.month)
    # print(movie21)

    # Вопрос 22. Сколько суммарно вышло фильмов летом (за июнь, июль, август)?

    # movie22=movie.copy()
    # movie22['month'] = movie22.apply(extract_month, axis=1)
    #
    #
    # result = movie22[movie22.month.str.contains('6|7|8')].month.value_counts().sum()
    # print(result)

    # Вопрос 23. Для какого режиссера зима — самое продуктивное время года?

    # movie23 = movie.copy()
    # # movie23['month'] = movie23.apply(extract_month, axis=1)
    #
    # def get_season(row):
    #     month = extract_month(row)
    #     if month in '345':
    #         return 'spring'
    #     elif month in '678':
    #         return 'summer'
    #     elif month in '91011':
    #         return 'autumn'
    #     else:
    #         return 'winter'
    # #
    # movie23['season'] = movie23.apply(get_season,axis=1)
    #
    # movie23['one_director'] = movie23['director'].str.split('|')
    # month_director = movie23.explode('one_director')
    # movie23 = movie23[movie23['season'] == 'winter'].one_director.value_counts()
    # print (movie23)
    # month_director = movie23[movie23['month'].isin(['1','2','12'])].one_director.sort_values(ascending=False)
    # month_director = month_director.groupby(['one_director']).one_director.value_counts(sort=True, ascending = False)
    #
    # pivot = movie23.loc[movie23['release_date'].isin(['12', '1', '2'])].pivot_table(values=['original_title'],
    #                                                                                 index=['one_director'],
    #                                                                                 columns=['release_date'],
    #                                                                                 aggfunc='count', fill_value=0)
    # # #
    # month_director = month_director.groupby(['release_date']).values_count(sort=True, ascending = False)


    # Вопрос 24. Какая студия даёт самые длинные названия своим фильмам по количеству символов?

    # movie24 = movie.copy()
    #
    # movie24['studio'] = movie24['production_companies'].str.split('|')
    # company = movie24.explode('studio')
    #
    # company['name_length'] = company['original_title'].str.len()
    # company = company.groupby(['studio']).name_length.mean().sort_values(ascending=False)
    #
    # print(company.head())

    # Вопрос 25. Описания фильмов какой студии в среднем самые длинные по количеству слов?

    # movie25 = movie.copy()
    #
    # movie25['studios'] = movie25['production_companies'].str.split('|')
    # company = movie25.explode('studios')
    #
    #
    # def count_words(row):
    #     word = 1
    #     for s in row['tagline']:
    #         if s == ' ':
    #             word = word + 1
    #
    #     return word


    # company['quant_words'] = company.apply(count_words, axis=1)
    # company = company[company.studios.str.contains('Universal Pictures|Warner Bros|Midnight Picture Show|Paramount Pictures|Total Entertainment')]
    # print(company[['studios', 'quant_words']].sort_values(['quant_words'],ascending=False).head(20))


    # company = company[company['studios'] == 'Universal Pictures'].quant_words

    # company = company.groupby(['studios']).quant_words.mean().sort_values(ascending=False)
    # print(company)



    # Вопрос 26. Какие фильмы входят в один процент лучших по рейтингу?
    # movie26=movie.copy()
    #
    # movie26 = movie26.loc[movie26['vote_average'] > movie26.quantile(0.99, numeric_only=True)['vote_average']]['original_title']
    # print(movie26)


    # Вопрос 27. Какие актеры чаще всего снимаются в одном фильме вместе?

    movie27 = movie.copy()

    #в каждой строчке дф, в колонке 'cast' из строки создать список актёров.
    # в списке составить пары.
    #Посчитать количество пар. по всему дф.

    movie27 = movie27[(movie27.cast)].list()

    def combo(row):
        for row in movie27['cast']:
            actors_list = movie27['cast']

            for actors in actors_list:
                actor_pairs = combinations(actors,2)

        return actor_pairs

    #Вариант 1
    movie27['actor_pairs'] = movie27.apply(combo, axis=1)
    s = pd.Series(movie27['actor_pairs'])
    # res = movie27.groupby(s).size().nlargest(10)
    res = movie27.groupby(s).value_counts()
    # print(res)
    print(movie27.actor_pairs)
    # #Вариант 2
    # def combo(row):
    #     for actor in row['cast']:
    #
    #         return list(combinations(actor,2))
    # #
    actors_comp = movie27
    # actors_comp ['actors_pair'] = combo(list)
    actors_comp ['actors_pair'] = movie27[movie27(combo(list))]
    actors_comp = actors_comp.actors_pair.value_count()
    #
    # #
    print(actors_comp)




# import itertools
# import pandas as pd
# import numpy as np
# df = pd.read_csv(io.StringIO("""    ID  Top 1 Group  Top 2 Group  Top 3 Group
# 0   1   Supplier A  Supplier B  Supplier C
# 1   2   Supplier B  Supplier A  NaN
# 2   3   Supplier C  Supplier A  NaN
# 3   4   Supplier A  Supplier B  Supplier C
# 4   5   Supplier A  Supplier B  NaN
# 5   6   Supplier B  Supplier C  Supplier A
# 6   7   Supplier B  NaN  NaN
# 7   8   Supplier A  Supplier B  Supplier C
# 8   9   Supplier A  NaN  NaN
# 9   10  Supplier A  Supplier C  Supplier B
# 10  11  Supplier A  Supplier B  Supplier C
# 11  12  Supplier B  Supplier A  NaN
# 12  13  Supplier C  Supplier A  Supplier B
# 13  14  Supplier B  Supplier C  Supplier A
# 14  15  Supplier B  Supplier C  NaN"""), sep="\s\s+", engine="python").replace({None:np.nan, "NaN":np.nan})
#
# # columns that contain suppliers
# cols = [c for c in df.columns if "Top" in c]
# # get unique suppliers
# suppl = np.unique(np.concatenate([df[c].dropna() for c in cols]))
#
# result = []
# for sn in range(len(suppl)):
#     # generate combinations of suppliers
#     for combi in itertools.combinations(suppl, sn+1):
#         # generate a truth matrix and then work out if all rows have been fulfilled
#         result.append({combi:df.loc[:,cols].isin(list(combi)).T.any().all()})




# pivot = df.loc[df['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(values=['Wage'],
#                                                                                                            index=['Nationality'],
#                                                                                                            columns=['Club'],
#                                                                                                            aggfunc='sum')

# df = data.copy()
# df['dirs'] = df['director'].str.split('|')
# dirs_cut = df.explode('dirs')

    # sample.Name.str.match("К", na=False)


# sample.query('City in ["Рига", "Сочи","Чебоксары", "Сургут"] & 21<Age<50 & Profession!="Менеджер"')
    # df['Alone'] = df.apply(alone_check, axis=1)
    # df
    # grouped_df = df.groupby(['Club'])['Wage'].sum().sort_values(ascending=False)
    # df.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean().sort_values(['Wage'],ascending=False).head(10)
    # football[(football.Age < football.Age.mean())&
    #          (football.Club == 'FC Barcelona')].Wage.mean()