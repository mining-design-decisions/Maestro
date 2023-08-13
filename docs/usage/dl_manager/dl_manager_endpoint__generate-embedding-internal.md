# `generate-embedding-internal` Endpoint

---

**Internal implementation endpoint for generate-embedding endpoint**

---

_This endpoint is used internally._
_Such endpoints are used as an implementation detail of other endpoints._
_Usually, the outward-facing endpoint retrieves a config from the database, and passes the arguments inside the config to the internal endpoint_

---

## Arguments

<details>
<summary>embedding-id</summary>


_Embedding to train_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>embedding-generator</summary>


_Type of embedding to train._

Argument type: enum (possible values: `Doc2VecGenerator`, `Word2VecGenerator`, `DictionaryGenerator`, `IDFGenerator`)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details>
<summary>embedding-config</summary>


_Config of the embedding_

Argument type: arglist

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

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
<summary>database-url</summary>


_URL of the database (wrapper)_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>
