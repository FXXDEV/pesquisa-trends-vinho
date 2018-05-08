                                                     
from db import Banco
from pytrends.request import TrendReq
# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq(hl='en-US', tz=360)

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
kw_list = ['Vinho branco', 'Vinho tinto', 'Vinhos'] #Lista de plavras chaves a serem pesquisadas
fonte_pesquisa = ['news','youtube','froogle','images'] # Lugares pesquisados [Noticias, youtube, shopping google, imagens]

pytrend.build_payload(kw_list, cat=0, timeframe='2018-05-08 2018-01-01',geo='BR-SC',gprop=fonte_pesquisa)

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.head())

# Interest by Region
interest_by_region_df = pytrend.interest_by_region(resulution='COUNTRY')
print(interest_by_region_df.head())

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print(related_queries_dict)

# Get Google Hot Trends data
rending_searches_df = pytrend.trending_searches()
print(trending_searches_df.head())

# Get Google Top Charts
top_charts_df = pytrend.top_charts(cid='actors', date=201805)
print(top_charts_df.head())

# Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword='vinho')
print(suggestions_dict)

