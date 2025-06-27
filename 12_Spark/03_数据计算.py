"""
map：将RDD的数据一条条处理（处理的逻辑基于map算子中接收的处理函数），返回新的RDD
"""
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/Program Files/Python/Python312/python.exe"

# 创建 SparkConf 对象，配置 Spark 应用程序
conf = SparkConf().setAppName("MySparkApp").setMaster("local[*]")
# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

# RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
# 通过map将全部数据都乘以10
def func(data):
    return data * 10

rdd_map = rdd.map(func)
print(rdd_map.collect())


# (T) -> U
# (T) -> T
print(sc.version)

# 停止
sc.stop()
