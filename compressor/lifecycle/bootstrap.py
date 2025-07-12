'''
@Project ：SkyQuant 
@File    ：bootstrap.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/12 13:05 
'''

from compressor.config.config_reader import config_user_reader

# 进行工具本身的生命周期管理
def bootstrap():
    # 获得初始配置 会指定使用cli还是frontend
    config = config_user_reader()
    # 从命令行或者前端获取指令
    get_input()

    # 获得对应输入

    # 开始压缩流程

    # 进行模板的构造

    # 最终输出

def get_input():
    pass

