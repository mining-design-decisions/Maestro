# Deep Learning Manager -- Parameter Types 

---

## Common Types 

We do not explain the types `str` (string), `int`, and `float`.

## Enum

A string which must exactly one of a set of possible values.

## Class

Sometimes, arguments have a Python class as their type (e.g. `pathlib.Path`).
In such cases, the argument must be a value which is valid input for the 
constructor of that class. 
For instance, for the `pathlib.Path` class, this would be a string.

## arglist 

Arglists are the most important parameter type in the deep learning manager.
They are always tied to another argument, usually of type enum. For instance, 
for the training command, we have 

- `input-mode` <-> `params`
- `classifier` <-> `hyper-params`

We will use the `classifier` and `hyper-params` as a running example.
Suppose that we are training an ensemble of classifiers. Specifically, 
we have three different classifiers: one CNN, and two FNN. 
The config of this ensemble model would have the following value for `"classifier"`:

```json
[
        "LinearConv1Model",
        "FullyConnectedModel",
        "FullyConnectedModel"
]
```

The `hyper-params` are then a means of configuring the hyperparameters 
for each model. Consider the following set of hyperparameters:

```json
{
    "LinearConv1Model.0": {
        "filters": 8,
        "number-of-convolutions": 1,
        "convolution-1-size": 8,
        "fully-connected-layer-size": 0
    },
    "FullyConnectedModel.0": {
        "layer-activation": "sigmoidal"
    },
    "FullyConnectedModel.1": {
        "layer-activation": "relu"
    },
    "FullyConnectedModel": {
        "number-of-hidden-layers": 2,
        "hidden-layer-1-size": 64,
        "hidden-layer-2-size": 32
    },
    "default": {
        "optimizer": "adam",
        "optimizer-params": {
            "beta_1": 0.99,
            "beta_2": 0.99
        },
        "loss": "crossentropy"
    }
}
```

Here, `LinearConv1Model.0` contains the parameters for the CNN,
`FullyConnectedModel.0` for the first FNN, and `FullyConnectedModel.1` for the second FNN.
`FullyConnectedModel` contains parameter shared by _all_ `FullyConnectedModel` models
(i.e. `FullyConnectedModel.0` and `FullyConnectedModel.1`).
`default` contains parameters shared by all models.

## hyper arglist

Hyper arglists are a special type of arglist used when optimising the hyper-parameters of a
model. In this case, for every entry in the arglist, not a single value, but a range 
of possible values must be specified. This must be done using a so-called 
"hyperparameter specifier." 

A specifier has the general form 

```json 
{"type": "specifier-type", "options":  {...}}
```

We have three basic types of specifiers: `range`, `floats`, and `values`.

#### `range`

The range specifier is used to specify a range of integer values. 
It has four possible options: `start`, `stop`, `step`, and `sampling`.

`start` and `stop` are mandatory and specify the range (endpoints included).
`step` determines the step size, with the default being 1 is not specified.

The sampling can be one of `linear`, `log`, or `reverse_log`.
For more details check [here](https://keras.io/api/keras_tuner/hyperparameters/#int-method).
The default is `linear`.

For `linear` sampling, the `step` is the minimum additive difference between values; 
for `log` sampling, it is the minimum multiplier between values.

For example, the following example defines the list of numbers `[0, 1, 2, 3, 4, 5]`:

```json 
{
    "type": "range",
    "options": {
        "start": 0,
        "stop": 5
    }
}
```

The following defines the list of numbers `[0, 2, 4, 6, 8, 10]`:

```json 
{
    "type": "range",
    "options": {
        "start": 0,
        "stop": 10,
        "step": 2
    }
}
```

Finally, the following examples defines the list of possible values `[1, 2, 4, 8, 16]`:

```json 
{
    "type": "range",
    "options": {
        "start": 1,
        "stop": 16,
        "sampling": "log"
    }
}
```

#### `floats`

Completely analogous to the `range` specifier, but for `float` values.

#### `values`

A hard-coded set of values for the hyperparameter tuning. There is only 
a single option, called `values`, which is a list of values.
This option should be used for enum values or ranges of values 
which cannot easily be expressed using the other specifiers. 
The following is an example, specifying the set of numbers 
`{2, 4, 8, 16}`:

```json 
{
    "type": "values",
    "options": {
        "values": [2, 4, 8, 16]
    }
}
```

