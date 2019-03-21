import tensorflow as tf
hello = tf.constant("agnaljasg")
sess = tf.Session()
result = sess.run(hello)
sess.close()
print(result)