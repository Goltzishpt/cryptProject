import requests
import pandas as pd
from datetime import datetime


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


def parse_csv(coin_id, name):
    """
    - parse information about chart with the help of magic
    - turn into json file
    - make list with dict(key = column, value = row), convert sec to datetime
    - create dataframe
    - calculate the average(first value rolling = quantity row with digits)
    - convert to csv
    """
    url = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/chart?id={coin_id}&range=7D"
    r = requests.get(url, headers=headers).json()
    data_frame = [{'date': datetime.fromtimestamp(int(k)), 'value': v['v'][0]} for k, v in r['data']['points'].items()]
    df = pd.DataFrame(data_frame)
    df['avg_last_5'] = df.rolling(5, min_periods=1).value.mean()
    df.to_csv(f"{name}_coin_data.csv", encoding='utf-8', index=True)


if __name__ == '__main__':
    parse_csv(2010, 'cardano')
    # parse_csv(11419, 'ton')
