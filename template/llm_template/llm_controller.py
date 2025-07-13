'''
@Project ：SkyQuant 
@File    ：llm_controller.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/13 10:40 
'''
'''
@Project ：SkyQuant 
@File    ：classify_controller.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/13 10:10 
'''

from fastapi import FastAPI, Form
from fastapi.routing import APIRoute
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


class LLMServer:
    def __init__(self):
        self.app = FastAPI(routes=[
            APIRoute('/predict',
                     self.do_classify,
                     response_class=JSONResponse,
                     methods=['POST']),
        ], log_level='trace', timeout=10000)

        self.app.add_middleware(
            CORSMiddleware, allow_origins=["*"], allow_credentials=True,
            allow_methods=["*"], allow_headers=["*"],
        )

    async def do_predict(self,data: str = Form(...)):
        print(233)

        return {'success':True,'result':'label'}