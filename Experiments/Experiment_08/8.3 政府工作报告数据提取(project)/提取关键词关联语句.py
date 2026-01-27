# 补充你的代码

def has_digit(s):
    return any(c.isdigit() for c in s)

def is_match(match, s):
    return any(word in s for word in match)

def output(match, res):
    for line in res:
        if is_match(match, line):
            print(line)

education = ['高校','培训','基础研究','学生','扩招','培养','教育']  #教育关联词
environment = ['清洁','森林','排放','土地','植被','能耗','湿地','能源','水体','公园','颗粒物','发电'] # 环保关联词
economic = ['就业','消费','市场','失业','工业','农业','费用','债券','土地','措施','汽车','赤字','企业','经济','生产总值','商品','制造','装备','财政','投资','金融','税','支付','销量','外汇','通胀','收入','贫困','预算','贷款','保险','储备','住房','跨境','进口','出口','进出口','自贸','关税','发电']  #经济关联词
medical = ['卫生','医疗','医学','救助','补助','学科']  #医疗卫生关联词
transport = ['交通','运输','汽车','公路','铁路','机场','货物']   #交通运输关联词
science = ['科技','创新','技术','双创','研究','专精特新','学科']  #科技创新关联词

punctuation = ['，', '。', '；']  #中文输入法的逗号，句号及分号

file = '/data/bigfiles/政府工作报告.txt'

with open(file, 'r', encoding = 'utf-8') as f:
    text = f.read()

for item in punctuation:
    text = text.replace(item, ' ')

lines = text.split()
res = [line for line in lines if has_digit(line)]

s = input()

if s == '教育':
    output(education, res)
elif s == '环保':
    output(environment, res)
elif s == '经济':
    output(economic, res)
elif s == '医疗' or s == '卫生':
    output(medical, res)
elif s == '交通' or s == '运输':
    output(transport, res)
elif s == '科技' or s == '创新':
    output(science, res)
elif s == '数据':
    for line in res:
        print(line)
else:
    print('无对应操作')
