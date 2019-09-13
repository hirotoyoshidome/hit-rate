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

current_dir = str(subprocess.check_output(['pwd'])).replace('b\'', '').replace('\\n\'', '')
os.environ['PATH'] = os.environ.get('PATH') + ':' + current_dir

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

# ブラウザを開かないと画像のパスが読み込まれなかったため、コメントアウト
# opt = selenium.webdriver.ChromeOptions()
# opt.add_argument('--blink-settings=imagesEnabled=false')

url = sys.argv[1]

contents_url = []

driver = webdriver.Chrome(desired_capabilities=caps) # , chrome_options=opt
driver.get(url)

for entry in driver.get_log('performance'):
  str_req_info = entry.get('message')
  dict_req_info = json.loads(str_req_info)
  response_info = dict_req_info.get('message').get('params').get('response')
  if None != response_info:
    contents_url.append(response_info.get('url'))
driver.quit()

# # verify
# # コメントアウト外して、
# # python3 main.py https:google.com > result.txt
# # で対象のリソースの確認ができます
# for x in contents_url:
#   print(x)

total_count = len(contents_url)
hit_count = 0
non_cached_resources = []

for content in contents_url:
  info = requests.get(content)
  val = ""
  if HEADER_TARGET_ITEM in info.headers:
    val = info.headers[HEADER_TARGET_ITEM]

  if JUDGEMENT in val.lower():
    hit_count = hit_count + 1
  else:
    non_cached_resources.append(content)

hit_percentage = (hit_count / total_count * 100)

# output
print('total hit count : ' + str(total_count))
print('hit percentage  : ' + str(hit_percentage))
print('###non cached resources###')
for c in non_cached_resources:
  print(c)
