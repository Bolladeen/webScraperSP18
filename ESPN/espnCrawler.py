from bs4 import BeautifulSoup
import requests
import datetime



def run_entire_thing(espn_link):
    espn = requests.get(espn_link).text
    soup = BeautifulSoup(espn, "html5lib")

    def get_source():
        return "ESPN"
    def get_url():
        return espn_link

    def get_tags():
        return True

    def get_title():
        title_tag = (soup.find_all("header", class_="article-header")[0])
        return title_tag.h1.string

    def get_author_and_date():
        author_and_date = list()
        info = (soup.find_all("div",class_ = "article-meta")[0])

        author = next(info.ul.li.contents[1].children)
        date = info.span.span.string
        if(check_if_today(date)):
            date = datetime.date.today()

        to_return = (author,date)
        author_and_date.extend(to_return)
        return author_and_date

    def get_image_caption():
        captions = soup.find_all("figcaption", class_ = "photoCaption")
        if(len(captions) == 0):
            return None

        captions_list = list()
        for i in range(0,len(captions)):
            captions_list.append(captions[i].contents[0])

        return captions_list

    def return_article_contents():
        text = soup.find_all("p")
        total_story = ""

        for part in text:
            if(part.string is not None):
                total_story += part.string

        return total_story


    def check_if_today(date):
        for i in range(0,len(date)):
            if(date[i] == ","):
                return False
        return True

run_entire_thing("http://www.espn.com/nfl/draft2018/story/_/id/22645316/shaquem-griffin-central-florida-runs-fastest-lb-40-more-decade")
