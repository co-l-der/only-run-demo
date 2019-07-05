#!/usr/bin/env python
# encoding: utf-8
__author__ = "han"


class ClassTool(object):

    @staticmethod
    def get_all_classes(parent):
        """
        功能：获取其父类下的所有直接子类
        :param parent: 父类名称
        :return:
        """
        all_subclasses = list()
        for subclass in parent.__subclasses__():
            if (not subclass in all_subclasses):
                all_subclasses.append(subclass)
        return all_subclasses

    # 由文件获取当前父目录, 父目录不跟随调用改变
    # current_dir = os.path.dirname(os.path.realpath(__file__))
