'''
@Project ：SkyQuant 
@File    ：test_network.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/13 10:50 
'''
import requests

requests.post('http://127.0.0.1:8000/classify',data={"data": "2333"})


