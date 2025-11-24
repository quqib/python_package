"""
高效消息处理的完美结合
    高性能、分布式的消息队列系统
    这玩意儿也有生产者消费者
"""
import json

# 这是配置生产者
from kafka import KafkaProducer

# 配置kafka生产者
producer = KafkaProducer(
    bootstrap_servers = ["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# 发送消息
message = {"key": "value"}
producer.send("test_topic", message)

# 刷新缓冲区
producer.flush()

# 关闭生产者
producer.close()



# 这是配置消费者
from kafka import KafkaConsumer

# 配置kafka消费者
consumer = KafkaConsumer(
    "test_topic",
    bootstrap_servers=["localhost:9092"],
)




