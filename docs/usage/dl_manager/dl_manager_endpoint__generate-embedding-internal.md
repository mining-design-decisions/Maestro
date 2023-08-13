# `generate-embedding-internal` Endpoint

---

**Internal implementation endpoint for generate-embedding endpoint**

---

_This endpoint is used internally._
_Such endpoints are used as an implementation detail of other endpoints._
_Usually, the outward-facing endpoint retrieves a config from the database, and passes the arguments inside the config to the internal endpoint_

---

## Arguments

<details style="margin-left:2em">
<summary style="margin-left:-2em">embedding-id</summary>


_Embedding to train_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">embedding-generator</summary>


_Type of embedding to train._

Argument type: enum (possible values: `IDFGenerator`, `Doc2VecGenerator`, `DictionaryGenerator`, `Word2VecGenerator`)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">embedding-config</summary>


_Config of the embedding_

Argument type: [arglist](./dl_manager_arglist__generate-embedding-internal__embedding-config.md)

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

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
<summary style="margin-left:-2em">database-url</summary>


_URL of the database (wrapper)_

Argument type: str

Numer of arguments: A single value.

This argument is mandatory and must be given.

This argument has no default value.

There are no additional constraints on this argument.

</details>
