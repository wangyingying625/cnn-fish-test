import tensorflow as tf
if __name__ == '__main__':
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph('./model/fish.ckpt.meta')
        saver.restore(sess,tf.train.latest_checkpoint('./model'))
        print(sess.run('train_op:0'))
    ##Model has been restored. Above statement will print the saved value