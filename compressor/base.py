'''
@Project ：SkyQuant 
@File    ：base.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/10 17:52 
'''
# compressor/base.py

from abc import ABC, abstractmethod

class CompressionModule(ABC):
    def __init__(self, model, config=None):
        """
        :param model: nn.Module - 待压缩模型
        :param config: dict - 该压缩方法的参数配置
        """
        self.model = model
        self.config = config or {}

    @abstractmethod
    def apply(self, calibration_data=None, teacher_model=None):
        """
        执行压缩操作
        :param calibration_data: 可选，用于量化或剪枝的校准数据
        :param teacher_model: 可选，用于蒸馏
        :return: 压缩后的模型
        """
        pass

    def report(self):
        """
        可选：返回压缩报告（如精度变化、参数量对比等）
        """
        return {}

    def requires_training(self) -> bool:
        """
        指示该压缩模块是否需要训练过程
        """
        return False
