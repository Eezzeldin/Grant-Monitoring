#==============================================================================
#1. IMPORTS
#==============================================================================
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lxml.html
import time
from datetime import datetime
#import sqlite3
#import random
import pandas as pd
#import numpy as np
import re
#import cleaning1 as c
import csv
#==============================================================================
#2. REACHING DESTNATION AND CAPTURING PAGE SOURCE
#==============================================================================
def openbrowser():
    global browser
    current_directory = os.getcwd()
    path_to_chromedriver = current_directory + '/chromedriver'
    #path_to_phantomdriver = current_directory + '/phantomjs'
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)
    #browser  =  webdriver.PhantomJS ( executable_path = path_to_phantomdriver )
    #b.set_window_size(1024, 768) #optional

if __name__ == "__main__":
    url = 'https://volgenau.gmu.edu/research/grants'
    openbrowser()
    browser.get (url)
    myGrants = [element.text for element in browser.find_elements_by_tag_name ('p')]
    for Grant in myGrants :
        print (Grant,'\n')
