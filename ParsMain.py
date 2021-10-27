from typing import Text
import requests
from bs4 import BeautifulSoup
import json

def get_info_first():

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    }


    url = "https://web2.bbiz.info/forums/sxemy-zarabotka-deneg-v-internete.13/"

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    information_posts = soup.find("ol", class_ = "discussionListItems").findAll(class_ = "PreviewTooltip")

    new_dict = {}

    for info in information_posts:
        get_link = f'https://web2.bbiz.info/{info.get("href")}'
        get_discription = info.get_text("data-previewurl")

        inf_id = get_link.split(".")[-1]
        inf_id = inf_id[:-1]

        new_dict[inf_id] = {
            "get_link": get_link,
            "get_discription": get_discription
        }

    with open("new_dict.json", "w") as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)
        
        #print(f"{get_discription}: {get_link}" # test

def get_info_fresh():

    with open("new_dict.json") as file:
        new_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    }


    url = "https://web2.bbiz.info/forums/sxemy-zarabotka-deneg-v-internete.13/"

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    information_posts = soup.find("ol", class_ = "discussionListItems").findAll(class_ = "PreviewTooltip")

    fresh_dict = {}

    for inf in information_posts:
        get_link = f'https://web2.bbiz.info/{inf.get("href")}'
        get_discription = inf.get_text("data-previewurl")

        inf_id = get_link.split(".")[-1]
        inf_id = inf_id[:-1]

        if inf_id in new_dict:
            continue
        else:
            get_link = f'https://web2.bbiz.info/{inf.get("href")}'
            get_discription = inf.get_text("data-previewurl")

            inf_id = get_link.split(".")[-1]
            inf_id = inf_id[:-1]

            new_dict[inf_id] = {
                "get_link": get_link,
                "get_discription": get_discription
            }

            fresh_dict[inf_id] = {
                "get_link": get_link,
                "get_discription": get_discription
            }
    
    with open("new_dict.json", "w") as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)
    
    return fresh_dict    

    

def main():
    get_info_first()

if __name__ == "__main__":
    main()
