'''
    已有json文件，对其内容进行整合
'''
# 读取json文件
import json
import codecs

# 打开要写入的文件
save_file = codecs.open("C:/Users/Administrator/Desktop/自动爬取网页/mydataPro.json", "wb", encoding="utf-8")
with open("C:/Users/Administrator/Desktop/自动爬取网页/mydata.json", "r" ,encoding="utf-8") as f:
    temp = json.loads(f.read())
    for i in range(len(temp["name"])):
        product = {"name": temp["name"][i], "price": temp["price"][i], "link": temp["link"][i]}
        # 将字典型数据转化为json型数据，注意ensure_ascii来处理中文乱码问题
        product_json = json.dumps(product, ensure_ascii=False)
        save_file.write(product_json+"\n")
    save_file.close()

with open("C:/Users/Administrator/Desktop/自动爬取网页/mydataPro.json","r",encoding="utf-8") as f:
    for line in f.readlines():
        temp = json.loads(line)
        print(temp)
