"""
pyspark 执行环境入口对象：SparkContext

编程模型：
数据输入：通过SparkContext完成数据读取
数据计算：读取到的数据转换为RDD对象，调用RDD的成员方法完成计算
数据输出：调用RDD的数据输出相关成员方法，将结果输出到list、tuple、dict、文本文件、数据库等
"""
from pyspark import SparkConf, SparkContext

# 创建 SparkConf 对象，配置 Spark 应用程序
conf = SparkConf().setAppName("MySparkApp").setMaster("local[*]")
#基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf = conf)
#打印版本
print(sc.version)

#停止
sc.stop()