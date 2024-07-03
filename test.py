# import tensorflow as tf
# import matplotlib.pyplot as plt
# import numpy as np
# # import tensorflow_datasets as tfds
# print(tf.config.list_physical_devices('GPU'))
# # print(tfds.__version__)
#
# print(tf.__version__)
#
#
import tensorflow_datasets as tfds

builder = tfds.builder('imdb_reviews/subwords8k')
builder.download_and_prepare(download_dir='/path/to/downloads', download_config=tfds.download.DownloadConfig(delete_downloaded=True))

