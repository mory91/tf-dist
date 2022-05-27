import json
import os
import sys
import time

import tensorflow as tf

import mnist_setup

WORKER_BATCH_SIZE = 64


def main():
    tf_config = json.loads(os.environ['TF_CONFIG'])
    num_workers = len(tf_config['cluster']['worker'])

    strategy = tf.distribute.MultiWorkerMirroredStrategy()

    global_batch_size = WORKER_BATCH_SIZE * num_workers
    multi_worker_dataset = mnist_setup.mnist_dataset(global_batch_size)

    with strategy.scope():
        # Model building/compiling need to be within `strategy.scope()`.
        multi_worker_model = mnist_setup.build_and_compile_cnn_model()

    multi_worker_model.fit(multi_worker_dataset, epochs=20, steps_per_epoch=100)


if __name__ == '__main__':
    main()
