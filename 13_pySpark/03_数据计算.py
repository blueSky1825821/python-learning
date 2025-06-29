"""
map：将RDD的数据一条条处理（处理的逻辑基于map算子中接收的处理函数），返回新的RDD
"""
from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:/Program Files/Python311/python.exe"
os.environ["SPARK_HOME"] = "D:/Program Files/Python311/Lib/site-packages/pyspark"

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
print(f"lambda: {rdd.map(lambda x: x * 10).map(lambda x: x + 5).collect()}")

# flatmap 拍平 解除嵌套
lst = [[1, 2, 3], [4, 5, 6]]
rdd = sc.parallelize(lst)
rdd_flatmap = rdd.flatMap(lambda x: x)
print(f"rdd_flatmap: {rdd_flatmap.collect()}")

# reduceByKey 针对KV型RDD，自动按照key分组，然后聚合逻辑完成组内数据value的聚合操作
dict_data = [("a", 1), ("b", 1), ("a", 3), ("b", 4), ("c", 5)]
rdd = sc.parallelize(dict_data)
rdd_reduce_by_key = rdd.reduceByKey(lambda x, y: x + y)
print(f"rdd_reduce_by_key: {rdd_reduce_by_key.collect()}")

# filter 过滤想要的数据进行保留
rdd = sc.parallelize([1, 2, 3, 4, 5])
print(f"filter: {rdd.filter(lambda x: x % 2 == 0).collect()}")
print(f"rdd:{rdd.collect()}")

# distinct 去重
rdd = sc.parallelize([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(f"distinct: {rdd.distinct().collect()}")

#sortBy 排序
rdd = sc.parallelize([5, 4, 3, 2, 1])
print(f"sortBy: {rdd.sortBy(lambda x: x, ascending=False, numPartitions=1).collect()}")
rdd = sc.parallelize([("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)])
print(f"sortBy: {rdd.sortBy(lambda x: x[1]).collect()}")


print(sc.version)

# 停止
sc.stop()
