# `predict` Endpoint

---

**Use an existing classifier to make predictions on new data.**

---

## Arguments

<details style="margin-left:2em">
<summary style="margin-left:-2em">model</summary>


_Model to predict with_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">version</summary>


_Trained instance of the given model to use for prediction_

Argument type: str

Numer of arguments: A single value.

This argument is optional

Default value: most-recent.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">data-query</summary>


_Query used to retrieve issues to predict_

Argument type: query

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

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
