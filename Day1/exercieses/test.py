from ipywidgets import interact

def test_function(x):
    return x

interact(test_function, x=(0, 10));
