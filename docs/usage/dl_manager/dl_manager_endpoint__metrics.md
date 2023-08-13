# `metrics` Endpoint

---

**Endpoint to calculate various metrics based on predictions**

---

## Arguments

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
<summary>model-id</summary>


_ID of the model from which predictions must be fetched_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>version-id</summary>


_ID of the model version from which predictions must be fetched_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>metrics</summary>


_JSON describing which metrics should be calculated_

Argument type: object

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>classification-as-detection</summary>


_Evaluate detection performance of a classification model_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>


<details>
<summary>epoch</summary>


_Epoch to evaluate metrics at. Either an epoch, `last`, `stopping-point`, or `all`_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>include-non-arch</summary>


_Include the non-architectural class as a class in Classification3_

Argument type: bool

Numer of arguments: A single value.

This argument is optional

Default value: False.

There are no additional constraints on this argument.

</details>
