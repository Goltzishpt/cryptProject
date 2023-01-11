import requests
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


def parse_csv(coin_id, name):
    """
    parse information about chart with the help of magic
    turn into json file
    get column
    convert to csv
    """
    url = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/chart?id={coin_id}&range=7D"
    r = requests.get(url, headers=headers).json()
    df = pd.DataFrame(r['data'])
    df.to_csv(f"{name}_coin_data.csv", encoding='utf-8', index=True)


parse_csv(2010, 'cardano')

parse_csv(11419, 'ton')
