import jieba

file_path = "E:/fenci.txt"  # 需要分词的数据集：上海自来水来自海上
dict_path = "E:/cidian.txt"  # 词频表(词语 词频<可省略> 词性<可省略>): 上海自来水

# jieba.cut(sequence, cut_all=False, HMM=True)
with open(file_path, 'r', encoding='utf-8') as fp:
    content = fp.read()
    seg_generator = jieba.cut(content)  # 默认参数cut_all=False,HMM=True 返回generator
    seg_list = [item for item in seg_generator]
    print(seg_list)  # ['上海', '自来水', '来自', '海上', '。']

# jieba.lcut(sequence, cut_all=False, HMM=True)
with open(file_path, 'r', encoding='utf-8') as fp:
    content = fp.read()
    seg_list = jieba.lcut(content)  # jieba.lcut直接返回list
    print(seg_list)  # ['上海', '自来水', '来自', '海上', '。']

# jieba.load_userdict(dict)
with open(file_path, 'r', encoding='utf-8') as fp:
    content = fp.read()
    jieba.load_userdict(dict_path)  # 加载自定义词典
    seg_list = jieba.lcut(content)
    print(seg_list)  # ['上海自来水', '来自', '海上', '。']

# jieba.add_word(word, freq=None, tag=None)
# jieba.del_word(word)
with open(file_path, 'r', encoding='utf-8') as fp:
    content = fp.read()
    jieba.add_word('来自海上')  # 添加自定义词汇
    seg_list = jieba.lcut(content)
    print(seg_list)  # ['上海自来水', '来自海上', '。']
    jieba.del_word('来自海上')  # 删除自定义词汇
    seg_list = jieba.lcut(content)
    print(seg_list)  # ['上海自来水', '来自', '海上', '。']


