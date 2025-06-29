"""
将RDD结果输出为Python对象的各类方法
collect算子：将RDD各个分区内的数据统一收集到Driver中，形成一个List对象
reduce算子：将RDD数据集按照传入的逻辑进行聚合
take算子：取出RDD前N个元素，组成list返回
count算子：计算RDD有多少条数据，返回是一个数字

saveAsTextFile算子:将RDD的数据写入文本文件中，支持本地写入，hdfs等文件系统，
输出的结果是要给文件夹，有几个分区就输出多少个结果文件
"""
from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:/Program Files/Python311/python.exe"
os.environ["SPARK_HOME"] = "D:/Program Files/Python311/Lib/site-packages/pyspark"

# 创建 SparkConf 对象，配置 Spark 应用程序
conf = SparkConf().setAppName("MySparkApp").setMaster("local[*]")
# 设置属性 全局并行度1 修改rdd分区
conf.set("spark.default.parallelism", "1")

# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
print(rdd)
# collect
print(f"collect: {rdd.collect()}")

# reduce
print(f"reduce: {rdd.reduce(lambda a, b: a + b)}")

# take
print(f"take: {rdd.take(2)}")

# count
print(f"count: {rdd.count()}")

# 需要安装hadoop
# saveAsTextFile算子
rdd = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)
rdd.saveAsTextFile("hdfs://192.168.1.100:9000/test")
rdd.saveAsTextFile("F:/program/python/python-learning/file/13_04_数据输出.text")

print(sc.version)

# 停止
sc.stop()
