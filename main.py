import speech_recognition as sr
from os import path
from pydub import AudioSegment
import time
import urllib
import os
import pydub
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options

#made by client a.k.a Me!
#Copyright Sike Just Kidding


driver  = webdriver.Chrome(executable_path='path to your chrome driver')
driver.get("https://www.google.com/recaptcha/api2/demo")
time.sleep(10)

someframes=driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(someframes[0]);
time.sleep(2)

#click on checkbox to activate recaptcha
driver.find_element_by_class_name("recaptcha-checkbox-border").click()

#to audio control frame
driver.switch_to.default_content()
someframes=driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
driver.switch_to.frame(someframes[0])
time.sleep(2)

#click on audio button
driver.find_element_by_id("recaptcha-audio-button").click()

#to audio frame
driver.switch_to.default_content()
someframes = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(someframes[-1])
time.sleep(2)

#click on the play button
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()
#get the mp3 audio file
src = driver.find_element_by_id("audio-source").get_attribute("src")
print("[INFO] Audio src: %s"%src)
#downloading sound file and changing it to .wav
urllib.request.urlretrieve(src, os.getcwd()+"\\sound.mp3")
sound = pydub.AudioSegment.from_mp3(os.getcwd()+"\\sound.mp3")
sound.export(os.getcwd()+"\\sound.wav", format="wav")
sample_audio = sr.AudioFile(os.getcwd()+"\\sound.wav")

r= sr.Recognizer()

with sample_audio as source:
    audio = r.record(source)

#audio to text
thingy=r.recognize_google(audio)
print("Said: %s"%thingy)

#submitting
driver.find_element_by_id("audio-response").send_keys(thingy.lower())
driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
driver.switch_to.default_content()
time.sleep(2)
driver.find_element_by_id("recaptcha-demo-submit").click()
time.sleep(2)
#delete those sound files
os.remove("sound.mp3")
os.remove("sound.wav")


#made by client a.k.a Me!
#Copyright Sike Just Kidding


