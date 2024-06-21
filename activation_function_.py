from tensorflow import keras
import tensorflow as tf

def y_x(x):
    return x

def junsung_activation(x):
    x = tf.cast(x, dtype=tf.float32)
    return tf.multiply(2.0, x) / (tf.square(x) + 1.0)

def gamma_factorial(x):
    x = tf.cast(x, dtype=tf.float32)
    abs_x = tf.abs(x)
    return tf.math.exp(tf.math.lgamma(abs_x + 1))

def volcano_function(x):
    x = tf.cast(x, dtype=tf.float32)
    abs_x = tf.abs(x)
    fuck = tf.math.exp(tf.math.lgamma(abs_x + 1))
    return tf.divide(1.0, fuck)

def MadeInChina(x):
    x = tf.cast(x, dtype=tf.float32)
    result = tf.where(x < 0, tf.math.pow(5.0, x) - 1, x)
    return result