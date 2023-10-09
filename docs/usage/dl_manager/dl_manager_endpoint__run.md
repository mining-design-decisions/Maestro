# `run` Endpoint

---

**Train a classifier and store the results**

---

_This endpoint is used internally._
_Such endpoints are used as an implementation detail of other endpoints._
_Usually, the outward-facing endpoint retrieves a config from the database, and passes the arguments inside the config to the internal endpoint_

---

## Arguments

<details style="margin-left:2em">
<summary style="margin-left:-2em">input-mode</summary>


_Generator to use._

Argument type: enum (possible values: `Doc2Vec`, `OntologyFeatures`, `Word2Vec`, `KateAutoEncoder`, `BOWFrequency`, `BOWNormalized`, `Bert`, `TfidfGenerator`, `AutoEncoder`, `Metadata`)

Numer of arguments: A list of one or more values.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">output-mode</summary>


_Output mode to use._

Argument type: enum (possible values: `Detection`, `Classification3Simplified`, `Classification3`, `Classification8`)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">params</summary>


_Generator params. Items in the name=value format._

Argument type: [arglist](./dl_manager_arglist__run__params.md)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">ontology-classes</summary>


_ID of the DB-file containing ontology classes._

Argument type: str

Numer of arguments: A single value.

This argument is optional

Default value: .

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.apply-ontology-classes, run.classifiers and run.ontology-classes</summary>



If `run.apply-ontology-classes == True or 'OntologyFeatures' in run.classifiers`, then the following are not allowed:

- `run.ontology-classes == ''`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">apply-ontology-classes</summary>


_Enable application of ontology classes_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.apply-ontology-classes, run.classifiers and run.ontology-classes</summary>



If `run.apply-ontology-classes == True or 'OntologyFeatures' in run.classifiers`, then the following are not allowed:

- `run.ontology-classes == ''`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">classifier</summary>


_Classifier to use. Use `list` for options_

Argument type: enum (possible values: `LinearRNNModel`, `Bert`, `LinearConv1Model`, `FullyConnectedModel`)

Numer of arguments: A list of one or more values.

This argument is mandatory and must be given.

This argument has no default value.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.classifier and run.input_mode</summary>



The following condition must hold:

`len(run.classifier) == len(run.input_mode)`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">epochs</summary>


_Amount of training epochs_

Argument type: int

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">split-size</summary>


_Size of testing and validation splits. Ignored when k-cross > 0_

Argument type: float

Numer of arguments: A single value.

This argument is optional

Default value: 0.2.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">max-train</summary>


_Maximum amount of training items. -1 for infinite_

Argument type: int

Numer of arguments: A single value.

This argument is optional

Default value: -1.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">k-cross</summary>


_Enable k-fold cross-validation._

Argument type: int

Numer of arguments: A single value.

This argument is optional

Default value: 0.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.store-model, run.k-cross and run.cross-project</summary>



The following conditions are mutually exclusive:

- `run.store-model == True`

- `run.k-cross != 0`

- `run.cross-project == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.cross-project and run.k-cross</summary>



The following conditions are mutually exclusive:

- `run.cross-project == True`

- `run.k-cross != 0`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.quick-cross and run.k-cross</summary>



If `run.quick-cross == True`, then the following are not allowed:

- `run.k-cross == 0`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.analyze-keywords, run.k-cross and run.cross-project</summary>



If `run.analyze-keywords == True`, then the following are not allowed:

- `run.k-cross != 0`

- `run.cross-project == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.k-cross and run.analyze-keywords</summary>



If `run.k-cross != 0`, then the following are not allowed:

- `run.analyze-keywords == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.k-cross and test-with-training-data</summary>



If `run.k-cross == True`, then the following are not allowed:

- `test-with-training-data == False`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: test-with-training-data and run.k-cross</summary>



If `test-with-training-data == False`, then the following are not allowed:

- `run.k-cross == True`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">quick-cross</summary>


_Enable k-fold cross validation_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.quick-cross and run.k-cross</summary>



If `run.quick-cross == True`, then the following are not allowed:

- `run.k-cross == 0`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">cross-project</summary>


_Run cross project validation._

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.store-model, run.k-cross and run.cross-project</summary>



The following conditions are mutually exclusive:

- `run.store-model == True`

- `run.k-cross != 0`

- `run.cross-project == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.cross-project and run.k-cross</summary>



The following conditions are mutually exclusive:

- `run.cross-project == True`

- `run.k-cross != 0`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.analyze-keywords, run.k-cross and run.cross-project</summary>



If `run.analyze-keywords == True`, then the following are not allowed:

- `run.k-cross != 0`

- `run.cross-project == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.cross-project and run.analyze-keywords</summary>



If `run.cross-project == True`, then the following are not allowed:

- `run.analyze-keywords == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.cross-project and test-with-training-data</summary>



If `run.cross-project == True`, then the following are not allowed:

- `test-with-training-data == False`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: test-with-training-data and run.cross-project</summary>



If `test-with-training-data == False`, then the following are not allowed:

- `run.cross-project == True`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">cache-features</summary>


_Force caching of features. NOTE: the pipeline does not handle cache invalidation!_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.store-model and run.cache-features</summary>



If `run.store-model == True`, then the following are not allowed:

- `run.cache-features == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.cache-features and run.store-model</summary>



If `run.cache-features == True`, then the following are not allowed:

- `run.store-model == True`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">architectural-only</summary>


_If specified, only architectural issues are used_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">hyper-params</summary>


_Hyper-parameters params. Items in the name=value format._

Argument type: [arglist](./dl_manager_arglist__run__hyper-params.md)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">class-balancer</summary>


_Enable Class-Balancing_

Argument type: enum (possible values: `none`, `upsample`, `class-weights`)

Numer of arguments: A single value.

This argument is optional

Default value: none.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">upsampler</summary>


_Upsampler to use_

Argument type: enum (possible values: `SynonymUpSampler`, `SmoteUpSampler`, `RandomUpSampler`)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `class-balancer` is equal to `upsample`

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">upsampler-params</summary>


_Parameters for the upsampler_

Argument type: [arglist](./dl_manager_arglist__run__upsampler-params.md)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `class-balancer` is equal to `upsample`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">batch-size</summary>


_Specify the batch size used during training_

Argument type: int

Numer of arguments: A single value.

This argument is optional

Default value: 32.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">combination-strategy</summary>


_Strategy used to combine models. Use `combination-strategies` for more information._

Argument type: enum (possible values: `add`, `subtract`, `average`, `min`, `max`, `multiply`, `dot`, `concat`)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `ensemble-strategy` is equal to `combination`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">combination-model-hyper-params</summary>


_Hyper-parameters for the creation of a combined model_

Argument type: [arglist](./dl_manager_arglist__run__combination-model-hyper-params.md)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `ensemble-strategy` is equal to `combination`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">ensemble-strategy</summary>


_Strategy used to combine models. Use `combination-strategies` for more information._

Argument type: enum (possible values: `stacking`, `voting`, `combination`, `none`)

Numer of arguments: A single value.

This argument is optional

Default value: none.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.ensemble-strategy and run.test-separately</summary>



The following conditions are mutually exclusive:

- `run.ensemble-strategy == 'none'`

- `run.test-separately == True`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">stacking-meta-classifier</summary>


_Classifier to use as meta-classifier in stacking._

Argument type: enum (possible values: `LinearRNNModel`, `Bert`, `LinearConv1Model`, `FullyConnectedModel`)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `ensemble-strategy` is equal to `stacking`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">stacking-meta-classifier-hyper-parameters</summary>


_Hyper-parameters for the meta-classifier_

Argument type: [arglist](./dl_manager_arglist__run__stacking-meta-classifier-hyper-parameters.md)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `ensemble-strategy` is equal to `stacking`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">stacking-use-concat</summary>


_Use simple concatenation to create the input for the meta classifier_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">stacking-no-matrix</summary>


_Disallow the use of matrices for meta classifier input_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">voting-mode</summary>


_Mode for the voting ensemble. Either hard of sort voting_

Argument type: enum (possible values: `soft`, `hard`)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `ensemble-strategy` is equal to `voting`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">use-early-stopping</summary>


_If specified, use early stopping._

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">early-stopping-patience</summary>


_Patience used when using early stopping_

Argument type: int

Numer of arguments: A single value.

This argument is optional

Default value: 5.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">early-stopping-min-delta</summary>


_Minimum delta used when using early stopping. One entry for every attribute used._

Argument type: float

Numer of arguments: A list of one or more values.

This argument is optional

Default value: [0.001].

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.early-stopping-min-delta and run.early-stopping-attribute</summary>



The following condition must hold:

`len(run.early-stopping-min-delta) == len(run.early-stopping-attribute)`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">early-stopping-attribute</summary>


_Attribute(s) to use for early stopping (from the validation set)_

Argument type: str

Numer of arguments: A list of one or more values.

This argument is optional

Default value: ['loss'].

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.early-stopping-min-delta and run.early-stopping-attribute</summary>



The following condition must hold:

`len(run.early-stopping-min-delta) == len(run.early-stopping-attribute)`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">test-separately</summary>


_If given, disable combining multiple classifiers. In stead, test them separately on the same data._

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.ensemble-strategy and run.test-separately</summary>



The following conditions are mutually exclusive:

- `run.ensemble-strategy == 'none'`

- `run.test-separately == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.store-model and run.test-separately</summary>



The following conditions are mutually exclusive:

- `run.store-model == True`

- `run.test-separately == True`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">store-model</summary>


_If given, store the trained model. Can only be used when training a single model._

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.store-model and run.test-separately</summary>



The following conditions are mutually exclusive:

- `run.store-model == True`

- `run.test-separately == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.store-model, run.k-cross and run.cross-project</summary>



The following conditions are mutually exclusive:

- `run.store-model == True`

- `run.k-cross != 0`

- `run.cross-project == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.store-model and run.model-id</summary>



If `run.store-model == True`, then the following are not allowed:

- `run.model-id == ''`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.store-model and run.cache-features</summary>



If `run.store-model == True`, then the following are not allowed:

- `run.cache-features == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.cache-features and run.store-model</summary>



If `run.cache-features == True`, then the following are not allowed:

- `run.store-model == True`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">model-id</summary>


_ID of the model being trained. Must be present in the database. (passed automatically be `train` endpoint)_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.store-model and run.model-id</summary>



If `run.store-model == True`, then the following are not allowed:

- `run.model-id == ''`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">analyze-keywords</summary>


_Compute a list of important keywords (convolutional mode only)_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:



<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.analyze-keywords and run.classifiers</summary>



If `run.analyze-keywords == True`, then the following are not allowed:

- `'LinearConv1Model' not in run.classifiers`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.classifiers and run.analyze-keywords</summary>



If `'LinearConv1Model' not in run.classifiers`, then the following are not allowed:

- `run.analyze-keywords == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.analyze-keywords, run.k-cross and run.cross-project</summary>



If `run.analyze-keywords == True`, then the following are not allowed:

- `run.k-cross != 0`

- `run.cross-project == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.k-cross and run.analyze-keywords</summary>



If `run.k-cross != 0`, then the following are not allowed:

- `run.analyze-keywords == True`

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">Constraint on arguments: run.cross-project and run.analyze-keywords</summary>



If `run.cross-project == True`, then the following are not allowed:

- `run.analyze-keywords == True`

</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">training-data-query</summary>


_Query to obtain data from the database for training_

Argument type: query

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">test-data-query</summary>


_Query to obtain data from the database for performance evaluation_

Argument type: query

Numer of arguments: A single value.

This argument is optional

This argument should be `null` if `test-with-training-data` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">database-url</summary>


_URL of the database (wrapper)_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">test-with-training-data</summary>


_Draw testing data from training data using train/test split_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">seed</summary>


_Seed to use to initialize all the RNG related stuff. -1 means no seed is used_

Argument type: int

Numer of arguments: A single value.

This argument is optional

Default value: -1.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">perform-tuning</summary>


_Enable hyperparameter tuning_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">tuner-type</summary>


_Select the hyperparameter optimization strategy._

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">tuner-objective</summary>


_Select the metric to optimize for._

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">tuner-max-trials</summary>


_Select the number of hyperparameter combinations that are tried._

Argument type: int

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">tuner-executions-per-trial</summary>


_Select the number of executions per trial, to mitigate randomness._

Argument type: int

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">tuner-hyperband-iterations</summary>


_Select the number of iterations for the HyperBand algorithm._

Argument type: int

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">tuner-hyper-params</summary>


_Hyper-parameters params for the Keras Tuner. Items in the name=value format._

Argument type: [hyper_arglist](./dl_manager_arglist__run__tuner-hyper-params.md)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">tuner-combination-model-hyper-params</summary>


_Hyper-parameters for the creation of a combined model for keras tuner_

Argument type: [hyper_arglist](./dl_manager_arglist__run__tuner-combination-model-hyper-params.md)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: {'CombinedModel.0': {}}.

There are no additional constraints on this argument.

</details>
