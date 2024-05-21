# Parameters for Bert options of arglist run/stacking-meta-classifier-hyper-parameters

---


<details style="margin-left:2em">
<summary style="margin-left:-2em">number-of-frozen-layers</summary>


_Number of layers to freeze._

Argument type: int (minimum: 0, maximum: 12)

Default value: 10



---



Supported hyperparameter specs: values and range

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">optimizer</summary>


_Optimizer to use. Special case: use sgd_XXX to specify SGD with momentum XXX_

Argument type: str

Default value: adam



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">optimizer-params</summary>


_Hyper-parameters for the optimizer_

Argument type: nested arglist.

Default values are inherited from contained child arguments.

Hyper-parameter specs are inherited from nested child arguments.

**Nested arguments:**



<details style="margin-left:2em">

<summary style="margin-left:-2em">adam</summary>





<details style="margin-left:2em">

<summary style="margin-left:-2em">beta-1</summary>



_Beta-1 value for the Adam optimizer_

Argument type: float (no restrictions)

Default value: 0.9



---



Supported hyperparameter specs: values and floats

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">beta-2</summary>



_Beta-2 value for the Adam optimizer_

Argument type: float (no restrictions)

Default value: 0.999



---



Supported hyperparameter specs: values and floats

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">epsilon</summary>



_Epsilon value for the Adam optimizer_

Argument type: float (no restrictions)

Default value: 1e-07



---



Supported hyperparameter specs: values and floats

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">weight-decay</summary>



_Weight decay_

Argument type: float (no restrictions)

Default value: 0.0



---



Supported hyperparameter specs: values and floats

</details>



</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">nadam</summary>





<details style="margin-left:2em">

<summary style="margin-left:-2em">beta-1</summary>



_Beta-1 value for the Nadam optimizer_

Argument type: float (no restrictions)

Default value: 0.9



---



Supported hyperparameter specs: values and floats

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">beta-2</summary>



_Beta-2 value for the Nadam optimizer_

Argument type: float (no restrictions)

Default value: 0.999



---



Supported hyperparameter specs: values and floats

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">epsilon</summary>



_Epsilon value for the Nadam optimizer_

Argument type: float (no restrictions)

Default value: 1e-07



---



Supported hyperparameter specs: values and floats

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">weight-decay</summary>



_Weight decay_

Argument type: float (no restrictions)

Default value: 0.0



---



Supported hyperparameter specs: values and floats

</details>



</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">adamw</summary>





<details style="margin-left:2em">

<summary style="margin-left:-2em">beta-1</summary>



_Beta-1 value for the Nadam optimizer_

Argument type: float (no restrictions)

Default value: 0.9



---



Supported hyperparameter specs: values and floats

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">beta-2</summary>



_Beta-2 value for the Nadam optimizer_

Argument type: float (no restrictions)

Default value: 0.999



---



Supported hyperparameter specs: values and floats

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">epsilon</summary>



_Epsilon value for the Nadam optimizer_

Argument type: float (no restrictions)

Default value: 1e-07



---



Supported hyperparameter specs: values and floats

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">weight-decay</summary>



_Weight decay_

Argument type: float (no restrictions)

Default value: 0.0



---



Supported hyperparameter specs: values and floats

</details>



</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">sgd</summary>





<details style="margin-left:2em">

<summary style="margin-left:-2em">momentum</summary>



_Momentum value for the SGD optimizer_

Argument type: float (minimum: 0.0, maximum: 1.0)

Default value: 0.0



---



Supported hyperparameter specs: values and floats

</details>





<details style="margin-left:2em">

<summary style="margin-left:-2em">use-nesterov</summary>



_Whether to use Nesterov momentum in the SGD optimizer_

Argument type: bool

Default value: False



---



Supported hyperparameter specs: values

</details>



</details>



</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">loss</summary>


_Loss to use in the training process_

Argument type: str

Default value: crossentropy



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">learning-rate-start</summary>


_Initial learning rate for the learning process_

Argument type: float (minimum: 0.0)

Default value: 0.005



---



Supported hyperparameter specs: values and floats

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">learning-rate-stop</summary>


_Learnign rate after "learning-rate-steps" steps_

Argument type: float (minimum: 0.0)

Default value: 0.0005



---



Supported hyperparameter specs: values and floats

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">learning-rate-steps</summary>


_Amount of decay steps requierd to go from start to stop LR_

Argument type: int (minimum: 1)

Default value: 470



---



Supported hyperparameter specs: values and range

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">learning-rate-power</summary>


_Degree of the polynomial to use for the learning rate._

Argument type: float (minimum: 0.0)

Default value: 1.0



---



Supported hyperparameter specs: values and floats

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">batch-size</summary>


_Batch size used during training_

Argument type: int (minimum: 1)

Default value: 32



---



Supported hyperparameter specs: values and range

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">use-trainable-embedding</summary>


_Whether to make the word-embedding trainable._

Argument type: bool

Default value: False



---



Supported hyperparameter specs: values

</details>
