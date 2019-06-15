"""
把.csv格式的数据，转化成标注工具需要的.json数据
把.csv文件也放在这个目录下，运行程序后，.json会生成在data文件夹下
"""
from utils import file2file
f2f = file2file.file2file()

# 固定参数
outpath = '../data/'
# 可变参数
infilename = 'GuangQing_10w_V1.csv'
outfilename = 'GuangQing_10w_V1_BiaoZhu.json'
# 不变语句
f2f.csv2json(inpath=infilename,outpath=outpath+outfilename)
# 对生成好的json外面嵌套一层{'data:'my.json}
datas = open(outpath + outfilename,'r').read()
new_datas = '{"data": ' + datas + '}'
open(outpath + outfilename,'w').write(new_datas)
print('==========Translate Over==========')
