# `run` Endpoint

---

**Train a classifier and store the results**

---

_This endpoint is used internally._
_Such endpoints are used as an implementation detail of other endpoints._
_Usually, the outward-facing endpoint retrieves a config from the database, and passes the arguments inside the config to the internal endpoint_

---

## Arguments

<details>
<summary>input-mode</summary>


_Generator to use._

Argument type: enum (possible values: `BOWNormalized`, `Word2Vec`, `Bert`, `OntologyFeatures`, `Metadata`, `Doc2Vec`, `TfidfGenerator`, `AutoEncoder`, `KateAutoEncoder`, `BOWFrequency`)

Numer of arguments: A list of one or more values.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>output-mode</summary>


_Output mode to use._

Argument type: enum (possible values: `Detection`, `Classification3Simplified`, `Classification3`, `Classification8`)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>params</summary>


_Generator params. Items in the name=value format._

Argument type: [arglist](./dl_manager_arglist__run__params.md)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>ontology-classes</summary>


_ID of the DB-file containing ontology classes._

Argument type: str

Numer of arguments: A single value.

This argument is optional

Default value: .

Additional constraints:

- Constraint on run.ontology-classes, run.apply-ontology-classes and run.classifier: Ontology class file must be given when applying ontology classes or using ontology features

</details>


<details>
<summary>apply-ontology-classes</summary>


_Enable application of ontology classes_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:

- Constraint on run.ontology-classes, run.apply-ontology-classes and run.classifier: Ontology class file must be given when applying ontology classes or using ontology features

</details>


<details>
<summary>classifier</summary>


_Classifier to use. Use `list` for options_

Argument type: enum (possible values: `LinearConv1Model`, `LinearRNNModel`, `Bert`, `FullyConnectedModel`)

Numer of arguments: A list of one or more values.

This argument is mandatory and must be given.

This argument has no default value.

Additional constraints:

- Constraint on run.classifier and run.input_mode: Argument lists must have equal length.

- Constraint on run.analyze-keywords, run.classifier and #config: Can only analyze keywords when using a convolutional model

- Constraint on run.ontology-classes, run.apply-ontology-classes and run.classifier: Ontology class file must be given when applying ontology classes or using ontology features

</details>


<details>
<summary>epochs</summary>


_Amount of training epochs_

Argument type: int

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>split-size</summary>


_Size of testing and validation splits. Ignored when k-cross > 0_

Argument type: float

Numer of arguments: A single value.

This argument is optional

Default value: 0.2.

There are no additional constraints on this argument.

</details>


<details>
<summary>max-train</summary>


_Maximum amount of training items. -1 for infinite_

Argument type: int

Numer of arguments: A single value.

This argument is optional

Default value: -1.

There are no additional constraints on this argument.

</details>


<details>
<summary>k-cross</summary>


_Enable k-fold cross-validation._

Argument type: int

Numer of arguments: A single value.

This argument is optional

Default value: 0.

Additional constraints:

- Constraint on run.store-model and run.k-cross: Cannot store model when using k-fold cross validation

- Constraint on run.cross-project and run.k-cross: Cannot use --k-cross and --cross-project at the same time.

- Constraint on run.k-cross and run.quick-cross: Must specify k when running with --quick-cross

- Constraint on run.k-cross and run.cross-project: k-cross must be 0 when running with --cross-project

- Constraint on run.store-model, run.k-cross, run.cross-project and run.quick-cross: Cannot run cross validation (or cross study) scheme when saving a model.

- Constraint on run.k-cross and run.test-with-training-data: Must test with training data when performing cross validation!

</details>


<details>
<summary>quick-cross</summary>


_Enable k-fold cross validation_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:

- Constraint on run.k-cross and run.quick-cross: Must specify k when running with --quick-cross

- Constraint on run.store-model, run.k-cross, run.cross-project and run.quick-cross: Cannot run cross validation (or cross study) scheme when saving a model.

</details>


<details>
<summary>cross-project</summary>


_Run cross project validation._

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:

- Constraint on run.cross-project and run.k-cross: Cannot use --k-cross and --cross-project at the same time.

- Constraint on run.k-cross and run.cross-project: k-cross must be 0 when running with --cross-project

- Constraint on run.store-model, run.k-cross, run.cross-project and run.quick-cross: Cannot run cross validation (or cross study) scheme when saving a model.

</details>


<details>
<summary>cache-features</summary>


_Force caching of features. NOTE: the pipeline does not handle cache invalidation!_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:

- Constraint on run.store-model and run.cache-features: May not use --cache-features when using --store-model.

</details>


<details>
<summary>architectural-only</summary>


_If specified, only architectural issues are used_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details>
<summary>hyper-params</summary>


_Hyper-parameters params. Items in the name=value format._

Argument type: [arglist](./dl_manager_arglist__run__hyper-params.md)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>class-balancer</summary>


_Enable Class-Balancing_

Argument type: enum (possible values: `none`, `upsample`, `class-weights`)

Numer of arguments: A single value.

This argument is optional

Default value: none.

There are no additional constraints on this argument.

</details>


<details>
<summary>upsampler</summary>


_Upsampler to use_

Argument type: enum (possible values: `RandomUpSampler`, `SmoteUpSampler`, `SynonymUpSampler`)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `class-balancer` is equal to `upsample`

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>upsampler-params</summary>


_Parameters for the upsampler_

Argument type: [arglist](./dl_manager_arglist__run__upsampler-params.md)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `class-balancer` is equal to `upsample`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>batch-size</summary>


_Specify the batch size used during training_

Argument type: int

Numer of arguments: A single value.

This argument is optional

Default value: 32.

There are no additional constraints on this argument.

</details>


<details>
<summary>combination-strategy</summary>


_Strategy used to combine models. Use `combination-strategies` for more information._

Argument type: enum (possible values: `add`, `subtract`, `average`, `min`, `max`, `multiply`, `dot`, `concat`)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `ensemble-strategy` is equal to `combination`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>combination-model-hyper-params</summary>


_Hyper-parameters for the creation of a combined model_

Argument type: [arglist](./dl_manager_arglist__run__combination-model-hyper-params.md)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `ensemble-strategy` is equal to `combination`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>ensemble-strategy</summary>


_Strategy used to combine models. Use `combination-strategies` for more information._

Argument type: enum (possible values: `stacking`, `voting`, `combination`, `none`)

Numer of arguments: A single value.

This argument is optional

Default value: none.

Additional constraints:

- Constraint on run.ensemble-strategy and run.test-separately: Cannot use ensemble when using separate testing mode.

</details>


<details>
<summary>stacking-meta-classifier</summary>


_Classifier to use as meta-classifier in stacking._

Argument type: enum (possible values: `LinearConv1Model`, `LinearRNNModel`, `Bert`, `FullyConnectedModel`)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `ensemble-strategy` is equal to `stacking`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>stacking-meta-classifier-hyper-parameters</summary>


_Hyper-parameters for the meta-classifier_

Argument type: [arglist](./dl_manager_arglist__run__stacking-meta-classifier-hyper-parameters.md)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `ensemble-strategy` is equal to `stacking`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>stacking-use-concat</summary>


_Use simple concatenation to create the input for the meta classifier_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details>
<summary>stacking-no-matrix</summary>


_Disallow the use of matrices for meta classifier input_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details>
<summary>voting-mode</summary>


_Mode for the voting ensemble. Either hard of sort voting_

Argument type: enum (possible values: `soft`, `hard`)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `ensemble-strategy` is equal to `voting`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>use-early-stopping</summary>


_If specified, use early stopping._

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details>
<summary>early-stopping-patience</summary>


_Patience used when using early stopping_

Argument type: int

Numer of arguments: A single value.

This argument is optional

Default value: 5.

There are no additional constraints on this argument.

</details>


<details>
<summary>early-stopping-min-delta</summary>


_Minimum delta used when using early stopping. One entry for every attribute used._

Argument type: float

Numer of arguments: A list of one or more values.

This argument is optional

Default value: [0.001].

Additional constraints:

- Constraint on run.early-stopping-min-delta and run.early-stopping-attribute: Argument lists must have equal length.

</details>


<details>
<summary>early-stopping-attribute</summary>


_Attribute(s) to use for early stopping (from the validation set)_

Argument type: str

Numer of arguments: A list of one or more values.

This argument is optional

Default value: ['loss'].

Additional constraints:

- Constraint on run.early-stopping-min-delta and run.early-stopping-attribute: Argument lists must have equal length.

</details>


<details>
<summary>test-separately</summary>


_If given, disable combining multiple classifiers. In stead, test them separately on the same data._

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:

- Constraint on run.ensemble-strategy and run.test-separately: Cannot use ensemble when using separate testing mode.

- Constraint on run.store-model and run.test-separately: Cannot store model when using separate testing mode.

</details>


<details>
<summary>store-model</summary>


_If given, store the trained model. Can only be used when training a single model._

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:

- Constraint on run.store-model and run.test-separately: Cannot store model when using separate testing mode.

- Constraint on run.store-model and run.k-cross: Cannot store model when using k-fold cross validation

- Constraint on run.store-model and run.model-id: --model-id must be given when storing a model.

- Constraint on run.store-model and run.cache-features: May not use --cache-features when using --store-model.

- Constraint on run.store-model, run.k-cross, run.cross-project and run.quick-cross: Cannot run cross validation (or cross study) scheme when saving a model.

</details>


<details>
<summary>model-id</summary>


_ID of the model being trained. Must be present in the database. (passed automatically be `train` endpoint)_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

Additional constraints:

- Constraint on run.store-model and run.model-id: --model-id must be given when storing a model.

</details>


<details>
<summary>analyze-keywords</summary>


_Compute a list of important keywords (convolutional mode only)_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:

- Constraint on run.analyze-keywords, run.classifier and #config: Can only analyze keywords when using a convolutional model

- Constraint on run.analyze-keywords and #config: Can not perform cross validation when extracting keywords

</details>


<details>
<summary>training-data-query</summary>


_Query to obtain data from the database for training_

Argument type: query

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>test-data-query</summary>


_Query to obtain data from the database for performance evaluation_

Argument type: query

Numer of arguments: A single value.

This argument is optional

This argument should be `null` if `test-with-training-data` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>database-url</summary>


_URL of the database (wrapper)_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>test-with-training-data</summary>


_Draw testing data from training data using train/test split_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

Additional constraints:

- Constraint on run.k-cross and run.test-with-training-data: Must test with training data when performing cross validation!

</details>


<details>
<summary>seed</summary>


_Seed to use to initialize all the RNG related stuff. -1 means no seed is used_

Argument type: int

Numer of arguments: A single value.

This argument is optional

Default value: -1.

There are no additional constraints on this argument.

</details>


<details>
<summary>perform-tuning</summary>


_Enable hyperparameter tuning_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details>
<summary>tuner-type</summary>


_Select the hyperparameter optimization strategy._

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>tuner-objective</summary>


_Select the metric to optimize for._

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>tuner-max-trials</summary>


_Select the number of hyperparameter combinations that are tried._

Argument type: int

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>tuner-executions-per-trial</summary>


_Select the number of executions per trial, to mitigate randomness._

Argument type: int

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>tuner-hyperband-iterations</summary>


_Select the number of iterations for the HyperBand algorithm._

Argument type: int

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>tuner-hyper-params</summary>


_Hyper-parameters params for the Keras Tuner. Items in the name=value format._

Argument type: [hyper_arglist](./dl_manager_arglist__run__tuner-hyper-params.md)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: None.

There are no additional constraints on this argument.

</details>


<details>
<summary>tuner-combination-model-hyper-params</summary>


_Hyper-parameters for the creation of a combined model for keras tuner_

Argument type: [hyper_arglist](./dl_manager_arglist__run__tuner-combination-model-hyper-params.md)

Numer of arguments: A single value.

This argument is optional

This argument should be `null` unless `perform-tuning` is equal to `True`

Default value: {'CombinedModel.0': {}}.

There are no additional constraints on this argument.

</details>
