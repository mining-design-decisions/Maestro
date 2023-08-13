# Parameters for Bert options of arglist run/stacking-meta-classifier-hyper-parameters

---


<details>
<summary>number-of-frozen-layers</summary>


_Number of layers to freeze._

Argument type: int (minimum: 0, maximum: 12)

This argument has no default value



---



No supported hyperparameter specs.

</details>


<details>
<summary>optimizer</summary>


_Optimizer to use. Special case: use sgd_XXX to specify SGD with momentum XXX_

Argument type: str

This argument has no default value



---



No supported hyperparameter specs.

</details>


<details>
<summary>optimizer-params</summary>


_Hyper-parameters for the optimizer_

Argument type: nested arglist.

Default values are inherited from contained child arguments.

Hyper-parameter specs are inherited from nested child arguments.

**Nested arguments:**



<details>

<summary>adam</summary>





<details>

<summary>beta-1</summary>



_Beta-1 value for the Adam optimizer_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>





<details>

<summary>beta-2</summary>



_Beta-2 value for the Adam optimizer_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>





<details>

<summary>epsilon</summary>



_Epsilon value for the Adam optimizer_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>





<details>

<summary>weight-decay</summary>



_Weight decay_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>



</details>





<details>

<summary>nadam</summary>





<details>

<summary>beta-1</summary>



_Beta-1 value for the Nadam optimizer_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>





<details>

<summary>beta-2</summary>



_Beta-2 value for the Nadam optimizer_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>





<details>

<summary>epsilon</summary>



_Epsilon value for the Nadam optimizer_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>





<details>

<summary>weight-decay</summary>



_Weight decay_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>



</details>





<details>

<summary>adamw</summary>





<details>

<summary>beta-1</summary>



_Beta-1 value for the Nadam optimizer_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>





<details>

<summary>beta-2</summary>



_Beta-2 value for the Nadam optimizer_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>





<details>

<summary>epsilon</summary>



_Epsilon value for the Nadam optimizer_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>





<details>

<summary>weight-decay</summary>



_Weight decay_

Argument type: float (no restrictions)

This argument has no default value



---



No supported hyperparameter specs.

</details>



</details>





<details>

<summary>sgd</summary>





<details>

<summary>momentum</summary>



_Momentum value for the SGD optimizer_

Argument type: float (minimum: 0.0, maximum: 1.0)

This argument has no default value



---



No supported hyperparameter specs.

</details>





<details>

<summary>use-nesterov</summary>



_Whether to use Nesterov momentum in the SGD optimizer_

Argument type: bool

This argument has no default value



---



No supported hyperparameter specs.

</details>



</details>



</details>


<details>
<summary>loss</summary>


_Loss to use in the training process_

Argument type: str

This argument has no default value



---



No supported hyperparameter specs.

</details>


<details>
<summary>learning-rate-start</summary>


_Initial learning rate for the learning process_

Argument type: float (minimum: 0.0)

This argument has no default value



---



No supported hyperparameter specs.

</details>


<details>
<summary>learning-rate-stop</summary>


_Learnign rate after "learning-rate-steps" steps_

Argument type: float (minimum: 0.0)

This argument has no default value



---



No supported hyperparameter specs.

</details>


<details>
<summary>learning-rate-steps</summary>


_Amount of decay steps requierd to go from start to stop LR_

Argument type: int (minimum: 1)

This argument has no default value



---



No supported hyperparameter specs.

</details>


<details>
<summary>learning-rate-power</summary>


_Degree of the polynomial to use for the learning rate._

Argument type: float (minimum: 0.0)

This argument has no default value



---



No supported hyperparameter specs.

</details>


<details>
<summary>batch-size</summary>


_Batch size used during training_

Argument type: int (minimum: 1)

This argument has no default value



---



No supported hyperparameter specs.

</details>


<details>
<summary>use-trainable-embedding</summary>


_Whether to make the word-embedding trainable._

Argument type: bool

This argument has no default value



---



No supported hyperparameter specs.

</details>
