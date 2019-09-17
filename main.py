import os
import subprocess
import json
import sys
import requests

import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# execute command
# python3 main.py https://google.com/

# consts
JUDGEMENT = 'hit'
HEADER_TARGET_ITEM = 'X-Cache'
ALLOWED_EXTENSIONS = ['js', 'png', 'jpg', 'css', 'gif', 'jpeg', 'html', 'htm']

# function definition
def check_exteensions(content):
  for ext in ALLOWED_EXTENSIONS:
    if ext in content:
      return False
  return True

# set env
current_dir = str(subprocess.check_output(['pwd'])).replace('b\'', '').replace('\\n\'', '')
os.environ['PATH'] = os.environ.get('PATH') + ':' + current_dir

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

opt = selenium.webdriver.ChromeOptions()
## comment out because it did not work without opening a browser
# opt.add_argument('--blink-settings=imagesEnabled=false')
opt.add_argument('--headless')
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-dev-shm-usage')

url = sys.argv[1]
contents_url = []

# run selenium with chrome
try:
  driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=opt)
  driver.get(url)

  for entry in driver.get_log('performance'):
    str_req_info = entry.get('message')
    dict_req_info = json.loads(str_req_info)
    response_info = dict_req_info.get('message').get('params').get('response')
    if None != response_info:
      contents_url.append(response_info.get('url'))
  driver.quit()
except:
  raise Exception('Chrome Driver ERROR.')

## verify
## if you want to check all static resources, please add this comments .
## python3 main.py https:google.com > result.txt
# for x in contents_url:
#   print(x)

total_count = len(contents_url)
hit_count = 0
exclusion_count = 0
non_cached_resources = []
error_count = 0

# run requests with selenium result
for content in contents_url:
  try:
    info = requests.get(content)
  except:
    error_count = error_count + 1
    continue
  val = ""
  if HEADER_TARGET_ITEM in info.headers:
    val = info.headers[HEADER_TARGET_ITEM]

  if JUDGEMENT in val.lower():
    hit_count = hit_count + 1
  elif check_exteensions(content):
    exclusion_count = exclusion_count + 1
  else:
    non_cached_resources.append(content)

# post processing
try:
  hit_percentage = (hit_count / (total_count - exclusion_count) * 100)
except ZeroDivisionError:
  raise Exception('Could not divide by 0.')  

# output
print('total hit count : ' + str(total_count - exclusion_count))
print('hit percentage  : ' + str(hit_percentage))
print('error count : ' + str(error_count))

## if you want to check non cached resources, please add this comments .
# print('###non cached resources###')
# for c in non_cached_resources:
#   print(c)
