import tensorflow as tf
import os
from Model import checkpoint, checkpoint_dir, train, predict


# train()
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))

res, str = predict("我们曾有失去生命的危险 。")

print('Input: %s' % str)
print('Predicted translation: {}'.format(res))
