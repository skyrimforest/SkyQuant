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


class ClassifyServer:
    def __init__(self):
        self.app = FastAPI(routes=[
            APIRoute('/classify',
                     self.do_classify,
                     response_class=JSONResponse,
                     methods=['POST']),
        ], log_level='trace', timeout=10000)

        self.app.add_middleware(
            CORSMiddleware, allow_origins=["*"], allow_credentials=True,
            allow_methods=["*"], allow_headers=["*"],
        )

    async def do_classify(self,data: str = Form(...)):
        print(233)

        return {'success':True,'result':'label'}