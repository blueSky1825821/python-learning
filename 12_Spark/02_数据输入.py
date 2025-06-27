"""
RDD：弹性分布式数据集（Resilient Distributed Datasets）
"""
from pyspark import SparkConf, SparkContext

# 创建 SparkConf 对象，配置 Spark 应用程序
conf = SparkConf().setAppName("MySparkApp").setMaster("local[*]")
# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

# 加载为RDD对象
#容器
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize("abcde")
rdd4 = sc.parallelize({1, 2, 3, 4, 5})
rdd5 = sc.parallelize({"key1": 1, "key2": 2, "key3": 3, "key4": 4})
#文本
rdd6 = sc.textFile("E:/study/py/code/python-learning/testfile.text")

# 打印RDD内容
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())
print(rdd6.collect())
# 停止
sc.stop()
