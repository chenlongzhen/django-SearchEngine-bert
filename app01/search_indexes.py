## 定义索引类
#from haystack import indexes
## 导入模型类
#from . import models
#
## https://www.cnblogs.com/SR-Program/p/12535309.html
## https://www.jianshu.com/p/f50c684d6a8f
#
## 对某个类的 某些数据 建立索引
## 索引类 类名 的格式：模型类名+Index !!!
#class PublisherIndex(indexes.SearchIndex, indexes.Indexable):
#    # text: 索引字段。document=True: 指定 该text为 索引字段。
#    # use_template=True 指定 对表中的哪些字段进行关键词分析 建立索引文件。对字段的说明，是 放在一个文件中的。
#    text = indexes.CharField(document=True, use_template=True)
#
#    def get_model(self):
#        # 返回 需要检索的 模型类
#        return models.SearchDB
#
#    # 返回 数据。对该数据 建立索引。
#    def index_queryset(self, using=None):
#        return self.get_model().objects.all() # 对key字段建立索引