# -*- coding: utf-8 -*-
"""
@Author : quentin.chen
@File   : GrapClimate.py
@Project: WebGrap1
@Time   : 2022-06-15 09:22:08
@Desc   : The file is ...
@Version: v1.0
"""
import requests  # 导入requests
from bs4 import BeautifulSoup  # 导入bs4中的BeautifulSoup
import os
import re
import csv
import pandas as pd
import numpy as np
import time
import json



if __name__ == '__main__':
    request_url = 'https://lishi.tianqi.com/'
    hearders = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
    }
    result_df = ''