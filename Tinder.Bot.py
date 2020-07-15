from selenium import webdriver
import pyautogui 
from encrypted import username,password
from time import sleep

class TinderBot():
    import time
    def __init__(self):
        self.driver=webdriver.Chrome()

    def login(self):
        self.driver.get("https://tinder.com/")
        sleep(10)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()
        base_window = self.driver.window_handles[0]

        self.driver.switch_to_window(self.driver.window_handles[1])
        email_id=self.driver.find_element_by_xpath('//*[@id="email"]')
        email_id.send_keys(username)

        pw_id=self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_id.send_keys(password)

        login_btn=self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(5)

        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[z@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):

        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')

        dislike_btn.click()
       
    def auto_swipe(self):
            while True:
                sleep(1)
                try:
                    self.like()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        self.get_tinderplus_popup()
                        self.close_match()

                    
                   

                
                    

                

               
                        

    def close_popup(self):

        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')

        popup_3.click()



    def close_match(self):

        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')

        match_popup.click()


    def get_tinderplus_popup(self):
        plus_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]/span')
        plus_popup.click()

        
    
Bot=TinderBot()
Bot.login()
Bot.like()
Bot.dislike()
Bot.auto_swipe()



        
        




