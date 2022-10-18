from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from pprint import pprint
from bs4 import BeautifulSoup
import json

def main():
    with open('question_details.pkl','rb') as filehandler: 
        ques_dict=pickle.load(filehandler)
    # pprint(ques_dict)

    browser=webdriver.Chrome()
    # browser.implicitly_wait(30)

    cnt=1
    for ques_no in ques_dict:
        if cnt==50:
            break
        try:
            ques_slug=ques_dict[ques_no]['question_title_slug']
            browser.get("https://leetcode.com/problems/"+ques_slug)
            soup=BeautifulSoup(browser.page_source,'html5lib')
            desc=soup.find("div", {"class": "content__u3I1 question-content__JfgR"})
            ques_dict[ques_no]['description_html']=str(desc)
            with open(f"ques{ques_no}.json", "w") as filehandler:
                json.dump(ques_dict[ques_no], filehandler)
            cnt+=1
        except:
            print(f"failed: {ques_slug=}") #type: ignore
            input()

    browser.quit()

if __name__ == "__main__":
    main()
