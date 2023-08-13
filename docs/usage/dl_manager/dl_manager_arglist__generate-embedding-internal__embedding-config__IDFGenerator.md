# Parameters for IDFGenerator options of arglist generate-embedding-internal/embedding-config

---


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

Default value: True



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
<summary style="margin-left:-2em">formatting-handling</summary>


_How to handle formatting in issues._

Argument type: str

This argument has no default value



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">use-ontologies</summary>


_If True, apply ontology classes to the input text._

Argument type: bool

Default value: False



---



Supported hyperparameter specs: values

</details>


<details style="margin-left:2em">
<summary style="margin-left:-2em">ontology-id</summary>


_ID to a file containing ontology classes._

Argument type: str

Default value: 



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
<summary style="margin-left:-2em">min-doc-count</summary>


_Minimum document frequency for a word to be included in the embedding._

Argument type: int (minimum: 0)

This argument has no default value



---



Supported hyperparameter specs: values and range

</details>
