# # 导入相关库
# import pyecharts
# # pyecharts.globals._WarningControl.ShowWarning = False
# import pandas as pd
# from pyecharts.charts import Map
# from pyecharts import options as opts
# import json

# # # 中文到英文的省份映射字典
# # province_map = {
# #     "北京市": "Beijing",
# #     "天津市": "Tianjin",
# #     "河北省": "Hebei",
# #     "山西省": "Shanxi",
# #     "内蒙古自治区": "Inner Mongolia",
# #     "辽宁省": "Liaoning",
# #     "吉林省": "Jilin",
# #     "黑龙江省": "Heilongjiang",
# #     "上海市": "Shanghai",
# #     "江苏省": "Jiangsu",
# #     "浙江省": "Zhejiang",
# #     "安徽省": "Anhui",
# #     "福建省": "Fujian",
# #     "江西省": "Jiangxi",
# #     "山东省": "Shandong",
# #     "河南省": "Henan",
# #     "湖北省": "Hubei",
# #     "湖南省": "Hunan",
# #     "广东省": "Guangdong",
# #     "广西壮族自治区": "Guangxi",
# #     "海南省": "Hainan",
# #     "重庆市": "Chongqing",
# #     "四川省": "Sichuan",
# #     "贵州省": "Guizhou",
# #     "云南省": "Yunnan",
# #     "西藏自治区": "Tibet",
# #     "陕西省": "Shaanxi",
# #     "甘肃省": "Gansu",
# #     "青海省": "Qinghai",
# #     "宁夏回族自治区": "Ningxia",
# #     "新疆维吾尔自治区": "Xinjiang",
# #     "香港特别行政区": "Hong Kong",
# #     "澳门特别行政区": "Macau",
# #     "台湾省": "Taiwan",
# #     "南海诸岛": "South China Sea islands",
# # }

# # 为了美化图表，我们将部分省份简写
# province_map = {"香港特别行政区": "香港",
#     "澳门特别行政区": "澳门",
# }


# file_path = r'2024.10Total value of the location of the consignee or consignor of import and export commodities.xlsx'
# df = pd.read_excel(file_path, sheet_name = '终版数据')
# df.head()

# # # 将文件中中文省份名称转换为英文
# # df['province_en'] = df['province'].map(province_map)

# # # 将map中省份名称从中文替换为英文
# # province_data = [list(z) for z in zip(df['province_en'], df['Oct_export'])]

# # # 读取 GeoJSON 数据
# # with open('China.json', 'r', encoding='utf-8') as f:
# #     geo_data = json.load(f)
# #
# # # 遍历 GeoJSON 中的省份，将中文名称替换为英文名称
# # for feature in geo_data['features']:
# #     province_name = feature['properties']['name']
# #     if province_name in province_map:
# #         feature['properties']['name'] = province_map[province_name]
# #
# # # 保存修改后的 GeoJSON 文件
# # with open('China_English.json', 'w', encoding='utf-8') as f:
# #     json.dump(geo_data, f, ensure_ascii=False, indent=4)


# # # 读取修改后的英文地图 GeoJSON 数据
# # with open('China_English.json', 'r', encoding='utf-8') as f:
# #     geo_data = json.load(f)



# '''
# 导入地图和数据
# '''

# m1=Map()
# m1.add("Value of Export", [list(z) for z in zip(df['province'], df['export_value'])], "china",is_map_symbol_show=True,name_map = province_map)


# '''
# 自适应间隔图例
# '''

# population_data = df['export_value']

# # 设置图例最大最小值
# min_population = 0
# max_population = population_data.max()

# interval_base = 10 ** (len(str(int(max_population))) - 3)
# interval_size = interval_base * ((max_population - min_population) // interval_base // 6 + 1)

# pieces = [
#     {'min': min_population, 'max': min_population + interval_size, 'label': f'{min_population:.0f}-{min_population + interval_size:.0f} billion USD'},
#     {'min': min_population + interval_size, 'max': min_population + 2 * interval_size, 'label': f'{min_population + interval_size:.0f}-{min_population + 2 * interval_size:.0f} billion USD'},
#     {'min': min_population + 2 * interval_size, 'max': min_population + 3 * interval_size, 'label': f'{min_population + 2 * interval_size:.0f}-{min_population + 3 * interval_size:.0f} billion USD'},
#     {'min': min_population + 3 * interval_size, 'max': min_population + 4 * interval_size, 'label': f'{min_population + 3 * interval_size:.0f}-{min_population + 4 * interval_size:.0f} billion USD'},
#     {'min': min_population + 4 * interval_size, 'max': min_population + 5 * interval_size, 'label': f'{min_population + 4 * interval_size:.0f}-{min_population + 5 * interval_size:.0f} billion USD'},
#     {'min': min_population + 5 * interval_size, 'label': f'over {min_population + 5 * interval_size:.0f} billion USD'}
# ]

# ''' 
# 全局设置
# '''
# m1.set_global_opts(
#              title_opts=opts.TitleOpts('Distribution of the Locations of Consigners'),#设置图标题
#             visualmap_opts=opts.VisualMapOpts(is_piecewise=True,pieces=pieces))#热力图相关设置
# m1.render("heatchart.html")


# 玫瑰图
from pyecharts import options as opts
from pyecharts.charts import Pie
l1 = ['教授','副教授','讲师','助教','其它']
num = [20,30,10,12,8]
c = Pie()
c.add('',[list(z) for z in zip(l1,num)],radius=['40%','55%'],center=[240,220],rosetype='radius')
c.add('',[list(z) for z in zip(l1,num)],radius=['40%','55%'],center=[620,220],rosetype='area')

# # 设置颜色列表
# color_list = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FFA500']
# c.set_colors(color_list)

c.set_global_opts(title_opts=opts.TitleOpts(title='玫瑰图'))
c.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}'))
c.render('a.html')
