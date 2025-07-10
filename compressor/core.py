'''
@Project ：SkyQuant 
@File    ：core.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/10 17:52 
'''
# compressor/core.py

class Compressor:
    def __init__(self, model):
        self.model = model
        self.modules = []

    def enable(self, module_class, config=None):
        module = module_class(self.model, config=config)
        self.modules.append(module)

    def run(self, calibration_data=None, teacher_model=None):
        model = self.model
        for module in self.modules:
            model = module.apply(calibration_data=calibration_data, teacher_model=teacher_model)
        return model
