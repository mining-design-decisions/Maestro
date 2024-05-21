# Parameters for KateAutoEncoder options of arglist run/params

---


<details style="margin-left:2em">
<summary style="margin-left:-2em">max-len</summary>


_words limit of the issue text. Set to -1 to disable._

Argument type: int (minimum: -1)

Default value: -1



---



Supported hyperparameter specs: values and range

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">disable-lowercase</summary>


_transform words to lowercase_

Argument type: bool

Default value: False



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">disable-stopwords</summary>


_remove stopwords from text_

Argument type: bool

Default value: False



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">use-stemming</summary>


_stem the words in the text_

Argument type: bool

Default value: False



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">use-lemmatization</summary>


_Use lemmatization on words in the text_

Argument type: bool

Default value: False



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">use-pos</summary>


_Enhance words in the text with part of speech information_

Argument type: bool

Default value: False



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">class-limit</summary>


_limit the amount of items per class. Set to -1 to disable_

Argument type: int (minimum: -1)

Default value: -1



---



Supported hyperparameter specs: values and range

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">metadata-attributes</summary>


_Comma-separated list of metadata attributes to fetch for use in feature generation_

Argument type: str

Default value: 



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">formatting-handling</summary>


_How to handle formatting_

Argument type: str

Default value: markers



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">replace-this-technology-mapping</summary>


_If given, should be a file mapping project keys to project names. Project names in text will be replacement with `this-technology-replacement`._

Argument type: str

Default value: 



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">this-technology-replacement</summary>


_See description of `replace-this-technology-mapping`_

Argument type: str

Default value: 



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">replace-other-technologies-list</summary>


_If given, should be a file containing a list of project names. Project names will be replaced with `other-technology-replacement`_

Argument type: str

Default value: 



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">other-technology-replacement</summary>


_See description of `replace-other-technology-list`._

Argument type: str

Default value: 



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">text-features-no-formatting-removal</summary>


_If True, formatting is not removed for features of type `Text`._

Argument type: bool

Default value: False



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">training-data-query</summary>


_Query to retrieve data used to train the auto-encoder_

Argument type: Query

This argument has no default value



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">bow-min-count</summary>


_Minimum document count for bag of words_

Argument type: int (minimum: 0)

Default value: 0



---



Supported hyperparameter specs: values and range

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">inner-generator</summary>


_Feature generator to transform issues to text_

Argument type: str

This argument has no default value



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">hidden-layer-size</summary>


_Size of the hidden layer_

Argument type: int (minimum: 2)

This argument has no default value



---



Supported hyperparameter specs: values and range

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">k-competitive</summary>


_Size of the K-Competitive layer_

Argument type: int (minimum: 2)

This argument has no default value



---



Supported hyperparameter specs: values and range

</details>
