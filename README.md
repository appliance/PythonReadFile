# PythonReadFile
python文件读取
/# 读取test.rlabelclass文件中记录，以[(text_name,tag),]形式保存

'''

try:

    # r表示 读
    
    # open('url','r')
    
    f = open('C:/Users/Administrator/Desktop/NLP/review_sentiment.v1/test2.rlabelclass', 'r')
    
    print(f.read())
    
finally:

    # 文件使用完毕后必须关闭，文件对象会占用操作系统的资源
   
    # 为了保证文件读写错误还能调用后续的关闭 一般使用try finally
    
    if f:
    
        f.close()
        
'''


\# try...finally方法比较复杂，一般使用with语句，with语句会自动帮我们调用close()方法


with open('C:/Users/Administrator/Desktop/NLP/review_sentiment.v1/test2.rlabelclass', 'r') as f:

    # 注: read()会一次性读取文件的全部内容，超过n个g内存就爆炸了。
    
    # 保险起见，反复调用read(size)方法，设定每次读取的字节数，或者readline()可以读取一行内容，或者readlines()一次读取所有内容并按行返回list
    
    for line in f.readlines():
    
        print(line.strip())         # line.strip()将每行末尾的\n换行给剔除掉
