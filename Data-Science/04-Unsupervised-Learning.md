# Unsupervised Learning

we are just given output data, without any inputs. The goal is to discover interesting structure in the data

### Discovering clusters

Let $$K$$ denote the number of clusters. Our first goal is to estimate the distribution over the number of clusters, $$p(K|D)$$

$$
K^∗ = argmax_K\space p(K|D)
$$

### Estimating which cluster each point belongs to

Let $$z_i \in \{1, . . . , K\}$$ represent the cluster to which data point i is assigned.

### Real world applications

1. Autoclass system in astronomy
2. Clustering users into groups in e-commerce