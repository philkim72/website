import logging
import confluent_kafka
from util import VideoCamera, ThreadedVideoCamera
import time


def pub(message):
    kafka.produce(topic, value=message)
    kafka.flush(timeout=1./120.)
    logging.info("message published.")


if __name__ == "__main__":
    # set producer config
    topic = 'Video'
    address = '192.168.1.134'  # 'localhost'
    zookeeper_port = 9092
    bootstrap_servers = '{}:{}'.format(address, zookeeper_port)
    max_messages = 1
    conf = {
        'bootstrap.servers': bootstrap_servers,
    }

    logging.info(conf)

    # set up logging
    logging_level = logging.getLevelName('INFO')
    logging.getLogger().setLevel(logging_level)

    # build the consumer
    kafka = confluent_kafka.Producer(**conf)

    # consume messages
    start = time.time(); count = 0.
    for message in ThreadedVideoCamera().messages():
        count += 1
        pub(message)
        logging.info("Publishing at {} fps.".format(count / (time.time() - start)))