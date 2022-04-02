# encoding=utf-8


def big_camel_case(text):
    '''大驼峰'''
    arr = list(filter(None, text.lower().split('_')))
    return "".join(map(lambda x: x.capitalize(), arr))


def get_class_name(cls):
    '''获取class的类名'''
    return cls.__name__