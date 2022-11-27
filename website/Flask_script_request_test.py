# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 05:49:29 2022

@author: João Araújo
"""

import requests
dicToSend = {'sdsd': 1234}
res = requests.post('http://127.0.0.1:5000/',json=dicToSend)
print(res)