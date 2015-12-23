# pylint: skip-file
""" data iterator for imagnet"""
import sys
sys.path.insert(0, "../../python/")
import mxnet as mx

def ilsvrc12_iterator(batch_size, input_shape):
    """return train and val iterators for imagenet"""
    train_dataiter = mx.io.ImageRecordIter(
		path_imgrec        = "Z:/mxnet/train.bin",
		mean_r			   = 104,
		mean_g 			   = 117,
		mean_b			   = 123,
        rand_crop          = True,
        rand_mirror        = True,
        prefetch_buffer    = 4,
        preprocess_threads = 4,
        data_shape         = input_shape,
        batch_size         = batch_size)
    val_dataiter = mx.io.ImageRecordIter(
		path_imgrec        = "Z:/mxnet/val.bin",
		mean_r			   = 104,
		mean_g 			   = 117,
		mean_b			   = 123,
		rand_crop          = False,
        rand_mirror        = False,
        prefetch_buffer    = 4,
        preprocess_threads = 4,
        data_shape         = input_shape,
        batch_size         = batch_size)

    return (train_dataiter, val_dataiter)
