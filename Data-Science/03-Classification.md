# Classification

### Need of probabilistic predictions

We will denote the probability distribution over possible labels, given the input vector $$x$$ and training set $$D$$ by $$p(y|x, D)$$

Given a probabilistic output, we can always compute our best guess as to the true label using

$$
\hat{y} = \hat{f}(x) = 	argmax\space p(y = c|x, D)
$$

### Real world applications

1. Email spam filtering
2. Image classification and handwriting recognition
3. Face detection and recognition