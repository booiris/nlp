import os
import time

import jieba
import tensorflow as tf

from Decoder import Decoder
from Encoder import Encoder
from Prestep import load_dataset, max_length, preprocess_sentence

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# config = tf.compat.v1.ConfigProto()
# config.gpu_options.allow_growth = True
# session = tf.compat.v1.InteractiveSession(config=config)

jieba.enable_paddle()
jieba.set_dictionary('File/dict.txt.big')

path_to_file = "File/train_data.txt"

BATCH_SIZE = 64
embedding_dim = 256
units = 1024
EPOCHS = 16

input_tensor_train, target_tensor_train, inp_lang, targ_lang = load_dataset(path_to_file, None)
max_length_targ, max_length_inp = max_length(target_tensor_train), max_length(input_tensor_train)

BUFFER_SIZE = len(input_tensor_train)
steps_per_epoch = len(input_tensor_train)  # BATCH_SIZE
vocab_inp_size = len(inp_lang.word_index) + 1
vocab_tar_size = len(targ_lang.word_index) + 1

dataset = tf.data.Dataset.from_tensor_slices((input_tensor_train, target_tensor_train)).shuffle(BUFFER_SIZE)
dataset = dataset.batch(BATCH_SIZE, drop_remainder=True)

encoder = Encoder(vocab_inp_size, embedding_dim, units, BATCH_SIZE)
decoder = Decoder(vocab_tar_size, embedding_dim, units, BATCH_SIZE)

optimizer = tf.keras.optimizers.Adam()
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(
    from_logits=True, reduction='none')


def loss_function(real, pred):
    mask = tf.math.logical_not(tf.math.equal(real, 0))
    loss_ = loss_object(real, pred)

    mask = tf.cast(mask, dtype=loss_.dtype)
    loss_ *= mask

    return tf.reduce_mean(loss_)


checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(optimizer=optimizer,
                                 encoder=encoder,
                                 decoder=decoder)


def train():
    @tf.function
    def train_step(inp, targ, enc_hidden):
        loss = 0

        with tf.GradientTape() as tape:
            enc_output, enc_hidden = encoder(inp, enc_hidden)

            dec_hidden = enc_hidden

            dec_input = tf.expand_dims([targ_lang.word_index['<start>']] * BATCH_SIZE, 1)

            # 教师强制 - 将目标词作为下一个输入
            for t in range(1, targ.shape[1]):
                # 将编码器输出 （enc_output） 传送至解码器
                predictions, dec_hidden = decoder(dec_input, dec_hidden, enc_output)

                loss += loss_function(targ[:, t], predictions)

                # 使用教师强制
                dec_input = tf.expand_dims(targ[:, t], 1)

        batch_loss = (loss / int(targ.shape[1]))

        variables = encoder.trainable_variables + decoder.trainable_variables

        gradients = tape.gradient(loss, variables)

        optimizer.apply_gradients(zip(gradients, variables))

        return batch_loss

    for epoch in range(EPOCHS):
        start = time.time()

        enc_hidden = encoder.initialize_hidden_state()
        total_loss = 0

        for (batch, (inp, targ)) in enumerate(dataset.take(steps_per_epoch)):
            batch_loss = train_step(inp, targ, enc_hidden)
            total_loss += batch_loss

            if batch % 100 == 0:
                print('Epoch {} Batch {} Loss {:.5f}'.format(epoch + 1,
                                                             batch,
                                                             batch_loss.numpy()))
        # 保存检查点
        if epoch == EPOCHS - 1:
            checkpoint.save(file_prefix=checkpoint_prefix)

        print('Epoch {} Loss {:.5f}'.format(epoch + 1,
                                            total_loss / steps_per_epoch))
        print('Time taken for 1 epoch {} sec\n'.format(time.time() - start))


def predict(sentence, ):
    str_list = jieba.cut(sentence, use_paddle=True)
    str = " ".join(list(str_list))
    str = preprocess_sentence(str)
    temp = str.split(" ")
    temp = filter(None, temp)
    inputs = [inp_lang.word_index[i] for i in temp]
    inputs = tf.keras.preprocessing.sequence.pad_sequences([inputs],
                                                           maxlen=max_length_inp,
                                                           padding='post')
    inputs = tf.convert_to_tensor(inputs)

    result = ''

    hidden = [tf.zeros((1, units))]
    enc_out, enc_hidden = encoder(inputs, hidden)

    dec_hidden = enc_hidden
    dec_input = tf.expand_dims([targ_lang.word_index['<start>']], 0)

    for t in range(max_length_targ):
        predictions, dec_hidden = decoder(dec_input,
                                          dec_hidden,
                                          enc_out)

        predicted_id = tf.argmax(predictions[0]).numpy()

        result += targ_lang.index_word[predicted_id] + ' '

        if targ_lang.index_word[predicted_id] == '<end>':
            return result, str

        # 预测的 ID 被输送回模型
        dec_input = tf.expand_dims([predicted_id], 0)

    return result, str
