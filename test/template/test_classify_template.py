'''
@Project ：SkyQuant 
@File    ：test_classify_template.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/13 10:07 
'''
from template.classify_template.classify_controller import ClassifyServer
import uvicorn

# 实例化服务并暴露 app
server = ClassifyServer()
app = server.app
# uvicorn test.template.test_classify_template:app --reload --port 8000

