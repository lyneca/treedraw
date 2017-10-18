# Treedraw
Generate diagrams of trees from your text editor


## Usage
```
$ pip install treedraw
$ python -m treedraw [input file] [output file]
```
See `python -m treedraw --help` for more options.


## Language
`.tree` files have the following syntax:

Defining node labels:
```
label: value
```

Setting the root node of the tree:
```
:: root [label]
```

Defining children of a node
```
label > label [, label ...]
```

Semicolons are optional and can be used to chain together multiple expressions.
