import time
import requests
from selenium import webdriver


def get_episode_names(driver, tv_show):
    driver.get(f'https://imsdb.com/TV/{tv_show}.html')
    elements = driver.find_elements_by_css_selector('p > a')
    elements = [e.text for e in elements]
    episode_list = [e.replace(' ', '-') for e in elements]

    return episode_list


def download_transcripts(driver, tv_show, episode_list, filename):
    for i in range(len(episode_list)):
        link = f'https://imsdb.com/transcripts/{tv_show}-{episode_list[i]}.html'
        req = requests.get(link)
        if req.status_code == requests.codes['ok']:
            print(episode_list[i])
            driver.get(link)
            path = '//*[@id="mainbody"]/table[2]/tbody/tr/td[3]/table[1]/tbody/tr/td/pre'
            dos = open(f'{filename}', 'a')
            time.sleep(1)
            try:
                dos.write(driver.find_element_by_xpath(path).text)
                print(episode_list[i], 'completed')
            except UnicodeEncodeError:
                pass


if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    tv_show = 'Seinfeld'
    filename = f'{tv_show}_transcripts.txt'

    episode_list = get_episode_names(driver, tv_show)
    download_transcripts(driver, tv_show, episode_list, filename)
