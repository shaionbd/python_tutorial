import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

minist = input_data.read_data_sets("/temp/data/", one_hot=True)

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_sizes = 100

# height x width
x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')

def neural_network_model(data):
    #(input_data * weights) + biases
    hidden_layer_1 = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl1))}

    hidden_layer_2 = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl2))}

    hidden_layer_3 = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl3))}

    output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                      'biases': tf.Variable(tf.random_normal(n_classes))}

    l1 = tf.add(tf.matmul(data, hidden_layer_1['weights'])+ hidden_layer_1['biases'])
    l1 = l1.nn.relu(l1)

    l2 = tf.add(tf.matmul(data, hidden_layer_2['weights']) + hidden_layer_2['biases'])
    l2 = l1.nn.relu(l2)

    l3 = tf.add(tf.matmul(data, hidden_layer_3['weights']) + hidden_layer_3['biases'])
    l3 = l1.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']

    return output