# -*- coding: utf-8 -*-
# @Time :   19-3-20 下午3:18 
# @Author :     HaiYang Gao
# @OS：  ubuntu 16.04
# @File :   file2file.py
import pandas as pd
import re
import jieba
"""
file2file类，是自己写的常用的文件类型转化函数，
在实际处理自己的文件时，有时要灵活调整code
"""

class file2file:
    def gbk_csv2utf8_csv(self, inpath, outpath, splitchar=','):
        """国标csv文件-->utf-8csv文件（处理乱码）"""
        all_datas = []
        with open(inpath, mode='r') as f:
            for line in f:
                # ,分行
                data = line.strip().split(splitchar)
                # 添加数据
                all_datas.append(data)
                # 每行转为指定编码的字符串
                str1 = ','.join(data).encode('utf-8')
                # 解码写入，添加写：a+
                open(outpath, mode='a+').write('\n' + str1.decode('utf-8'))

    def csv2json(self,inpath,outpath,orient_str='index'):
        """以csv列号为key，构建对应的json数据,默认orient='index'"""
        # 读入csv文件
        data = pd.read_csv(inpath)
        # 指定orient及其他参数
        data.to_json(outpath, orient=orient_str, force_ascii=False)

    def csv2pickle(self,inpath,outpath):
        """csv文件转为pickle文件"""
        tempdata = pd.read_csv(inpath)
        tempdata.to_pickle(outpath)

    def full_csv2part_csv_bycolumn(self,inpath,outpath,column_number_list,head_name_list,index=False):
        """column_number_list,head_name_list大小相同，列号与名字一一对应"""
        data = pd.read_csv(inpath, usecols=column_number_list)
        data.to_csv(outpath, encoding="utf-8-sig", index=index,header=head_name_list)

    def full_csv2part_csv_byrows(self,inpath,outpath,skiprow,nrow):
        """读取指定行，skiprow表示跳过多少行，nrow表示读多少行，第一行header不计入行数"""
        data = pd.read_csv(inpath, skiprows=skiprow, nrows=nrow)
        data.to_csv(outpath)

    def full_csv2part_txt(self,inpath,outpath,column_name_list):
        """从csv中提取出某几列，构造新的txt，column_name_list指定列名"""
        data = pd.read_csv(inpath)
        content = []
        # 自定义正则，去掉括号及内容
        pattern = '\\（.*?\\）|\\{|\\}|\\[.*?]|\\<.*?>'
        column_num = len(column_name_list)
        for i in range(column_num):
            content.append(list(data[column_name_list[i]]))
        # csv文件：每列长度是一样的
        length = len(content[0])
        for i in range(0, length):
            temp_str = ''
            for j in range(column_num):
                if j > 0:
                    # '+x+'给后面的空格占个位置,if控制位置，不要占错
                    temp_str = temp_str + '+×+' + str(content[j][i])
                else:
                    temp_str = temp_str + str(content[j][i])
            # 去掉乱七八糟的字符，手动定义
            temp_str = temp_str.replace('\r', '').replace('\n', '').replace('&nbsp;', '').replace(' ','' )
            temp_str = re.sub(pattern,'',temp_str)
            # 加上换行符
            temp_str = temp_str + '\n'
            # 更换占位符为' '
            temp_str = temp_str.replace('+×+', ' ')
            # 每次写入1行，io没有优化
            open(outpath, 'a+').write(temp_str)

    def txt2csv(self,inpath,outpath,columnnamelist,index=False,splitchar = ' '):
        """读取txt文件，按txt的列，转为csv文件，手动指定csv各列列名list"""
        datas = self.readtxt(inpath,splitchar=splitchar)
        columns = columnnamelist
        # 构造DataFrame格式数据
        csvdatas = pd.DataFrame(columns=columns, data=datas)
        csvdatas.to_csv(outpath,index=index, sep='\t')

    def txt2pickle(self,inpath,outpath,columnnamelist):
        """读取txt文件，按txt的列，转为pickle文件，手动指定pickle各列列名list"""
        datas = self.readtxt(inpath,splitchar=' ')
        columns = columnnamelist
        # 构造DataFrame格式数据
        pkdatas = pd.DataFrame(columns=columns,data=datas)
        pkdatas.to_pickle(outpath)

    def readjson(self,inpath,orient_str):
        """读json数据，不同格式的json数据，orient_str不一样"""
        data = pd.read_json(inpath, orient=orient_str)
        return data

    def readtxt(self,inpath,splitchar=' '):
        """读取txt，返回list，txt默认以‘空格’分行"""
        datas = []
        with open(inpath, 'r') as f:
            for line in f:
                content = line.strip().split(splitchar)
                # 不空
                if content:
                    datas.append(content)
        return datas

    def readcsv(self,inpath):
        """读取csv，返回DataFrame"""
        data = pd.read_csv(inpath)
        return data

    def readpickle(self,inpath):
        """读取pickle，返回DataFrame"""
        data = pd.read_pickle(inpath)
        return data

    def twoDlist2txt(self,twoDlist, outpath, linesplitor=' ', joinlink=','):
        temp = ''
        count = 0
        for i in twoDlist:
            # 每个子list字符化，构成字符串
            temp = temp + joinlink.join(i) + '\n'
            count += 1
            # 分批写入，注意temp重置
            if count % 200 == 0:
                open(outpath, 'a+').write(temp)
                temp = ''
        open(outpath, 'a+').write(temp)

    def txt2jieba_stopwords(self,txtinpath,stopwordspath,outpath):
        # 读入待处理数据
        datas = self.readtxt(txtinpath, splitchar=' ')
        # 读入停用词，并且使list一维化
        stopwords = set(sum(self.readtxt(stopwordspath), []))
        labels = []
        contents = []
        # 循环处理
        for i in datas:
            labels.append(i[0])

            # 分词
            content = jieba.lcut(i[1])
            k = []
            for each in content:
                k.append(each.encode('utf-8'))
            # 去停用词
            cut_data = [word for word in k if word not in stopwords]
            contents.append(' '.join(cut_data))
        # 写入本地
        write_txt = ''
        for i in range(len(labels)):
            write_txt = write_txt + labels[i] + ' ' + contents[i] + '\n'
        open(outpath, 'w').write(write_txt)


if __name__ == '__main__':
    f = file2file()
    """
    自己处理文件，生成.txt或.csv对应的.json文件，
    所有利用代码生成的.json文件，还不是最后可以标注的文件，
    需要手动在该.json文件外部嵌套上一层"data:"，形式如下：
    {
        "data":
              { 
                我的json文件
              }
    }
    """
    print ('file2file.py is running...')

