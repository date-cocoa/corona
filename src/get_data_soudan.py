from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import chromedriver_binary
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_text_data(url):
    """
    東京都のサイトにアクセスしてテクスト形式で相談件数データを取得
    """
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div/div/div/div[5]/div/div/div[6]/div/div/button/div/i').click()
    text = driver.find_element_by_xpath('/html/body/div/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div/div/div/div[5]/div/div/div[6]/div/div/div/div/div/div/table/tbody').text
    driver.close()

    return text

def make_df_from_text(text):
    """
    textデータを整形してデータフレーム化
    """
    text_list = text.replace('\n', ' ').split(' ')

    date = []
    number = []

    for idx in range(len(text_list)):
        if '日' in text_list[idx]:
            date.append('2020年' + text_list[idx])
            number.append(int(text_list[idx+1]))

    df = pd.DataFrame({
        'date': date,
        'number': number
    })

    return df

def add_week_to_df(df):
    """
    データフレームに曜日カラムを追加
    """
    df['date'] = pd.to_datetime(df['date'], format ='%Y年%m月%d日')

    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    weeks = week * (len(df) // 7)
    diff = len(df) - len(weeks)
    for idx in range(diff):
        weeks.append(week[idx])
    weeks.reverse()
    df['week']= weeks

    return df

if __name__ == '__main__':
    url = 'https://stopcovid19.metro.tokyo.lg.jp/'
    text = get_text_data(url)
    df = make_df_from_text(text)
    df = add_week_to_df(df)
    df.to_csv('./data/data_sodan.csv', index=False)
