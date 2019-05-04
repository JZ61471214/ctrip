import yaml
import inspect


def getData(funcname):
    """
    设置参数化，
    :param filename:  指定要打开的yml路径
    :param funcname:  yml中定义的与script脚本中对应py文件实际调用函数同名的字典的键名，仅是为了方便查找 yml中第二层表示含一条测试用例用到的所有数据的一个字典
    :return:
    """
    # 注意pytest是从项目根目录开始，
    # 注意filename定义时引号与包含文件路径的引号一致
    # 适配单属性和多属性参数化
    fileinfo = inspect.stack()[1]
    fileName = fileinfo.filename
    dotIndex = fileName.rfind(".")
    underlineIndex = fileName.rfind("_")
    fileName = fileName[underlineIndex:dotIndex]

    with open("./data/data"+fileName+".yml", "r", encoding="utf-8") as f:
        data = yaml.load(f)

    res_arr = []
    for i in data[funcname].values():
        tem_arr = []
        for j in i.values():
            tem_arr.append(j)
        res_arr.append(tem_arr)
    return res_arr


# print(getData("search", "test_fn2"))

# {
#     'search1': {
#         'name': 'xiaoming', 'age': 18, 'hob': 'sing'
#     },
#     'search2': {
#         'name': 'xiaoming', 'age': 18, 'hob': 'sing'
#     }
# }
