'''
@Project ：SkyQuant 
@File    ：config_reader.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/12 12:26 
'''
import yaml

config_file_path = 'user_config.yaml'

def config_user_reader():
    """
    读取全局配置文件
    :return:
    """
    with open(config_file_path, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config['config']

def config_advance_reader():
    """
    读取专门的高级配置,配置文件将在不同工具链的config中指定
    :return:
    """
    pass

def check_user_config():
    """
    检查每个用户配置是否合法
    :return:
    """
    pass

def check_advance_config():
    """
    检查每个高级配置是否合法
    :return:
    """
    pass


if __name__ == '__main__':
    result = config_user_reader()
    print(result)