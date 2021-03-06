# Fuzzy sets similarity calculator
Simple tool for calculating fuzzy sets similarity using different similarity measures.


## Similarity measure interface
Each similarity measure have to extend `AbstractSimilarityCalculator` from `simcalculators` package. This class has one abstract method with signature:
```
def calculateSimilarity(self, A, B, configuration):
```
where A, B represents fuzzy sets as lists of numbers and configuration is a key-value map containing all parameters required by given similarity measure.

## Supported Similarity Measures

This tool supports currently few selected similarity measures OOTB. List of all supported similarity measures can be found in `simcalculators` package. 

List of all supported measures with descriptions listed below.

#### Minkowski
Measure based on a distance calculated with Minkowski metric. This is implemented in `MinkowskiSimilarityCalculator` (minkowski_similarity_calculator.py).

Similarity is calculated with the following formula:

![Minkowski](docs/images/minkowski-formula.PNG?raw=true "Title")


**Configuration:**

Configuration map requires one parameter `r` with integer grater than zero, for example:
```
{
  "r": 2
}
```

#### Angular Distance
Similarity based on angular distance between two fuzzy sets represented as vectors. 

Similarity is calculated with the following formula:


![Angular distance](docs/images/angular-distance-formula.PNG?raw=true "Title")


**Configuration:**

This measure does not require any configuration. An empty mam can be passed.

#### Ko-Implication
Measure based on fuzzy implication.

Similarity is calculated with the following formula:

![Ko-implication](docs/images/implication-formula-1.PNG?raw=true "Title")
* f is a function that aggregates vector in single value. All implemented aggregators are available in `aggregators` package. To register new aggregator have a look on `aggregators_factory.py`
* t stands for t-norm. All t-norms are available in `tnorms` package. To register new t-norm have a look in `t_norm_factory.py`
* fuzzy implication is represented by the following formula: `a => b = s(v(a), b)` where s is a t-konorm and v is a fuzzy negation. This similarity measure uses the following negation: `v(a) = 1 - a`. List of all available implications is available in `implications` package.

**Configuration:**

Requires three parameters: 'aggregator', 'implication', 'tnorm'. To see all available values for this parameters please run `config.py -h`. Below you can find an example config map:

```
{
  'aggregator': 'average',
  'implication': 'lukasiewicz',
  'tnorm': 'lukasiewicz'
}
```
#### Jaccard Index
Measure based on classic set theory calculated with the following formula:
![Jaccard](docs/images/jaccard-formula.PNG?raw=true "Title")
* g represents scalar evaluator of fuzzy set
* intersection of fuzzy set calculated with t-normy minimum
* complement of a fuzzy set calculated with the following negation: `v(a) = 1 - a`


**Configuration:**

Requires four parameters: 'alpha', 'beta', 'gamma' and 'evaluator'. First three are numbers grater or equal to zero. A list of implemented evaluators can bo found in `fuzzysetevaluator.py`. And example configuration included below.
```
{
  'evaluator': 'average',
  'alpha': 1,
  'beta': 0,
  'gamma': 0
}
```

#### Simplified Jaccard Index
Measure based on classic set theory calculated with the following formula: 

![Simplified jaccard](docs/images/simiplified-jaccard-formula.PNG?raw=true "Title")

* f is a function that aggregates fuzzy set in single value.
* sum and intersection of fuzzy sets are calculated based on configurable t-norm and t-konorm


**Configuration:**

Requires three parameters: 'aggregator', 'tknorm', 'tnorm'.  To see all available values for those parameters please run `config.py -h`. Example configuration:
```
{
    "aggregator": "average",
    "tknorm": "probabilistic",
    "tnorm": "algebraic"
}
``` 
## Main Scripts
All executable scripts are placed under `executables` package. Each script contains simple manual which can be displayed by running it with `-h` parameter, for example:
 * `python compare_sets.py - h`

Below you can find list of all available executables with a brief description.

### Similarity measure configuration generator
Script name: `config.py`

Each similarity measure requires some parameters. To make it unified along all measures arguments are represented as a key-value map.
This script was created to allow automatic generation of wide ranges of configurations. Running this script will generate a json that represents similarity measure configuration and save it in result file. 
This script takes all parameters like: `-parameterName parameterValue` and pare them as an entry in generated configuration map.
Example usages (for more information use `-h` parameter):
* `python config.py -r 2 -m minkowski -fn config.txt` - this will generate the following json `{"r": 2, "method": "minkowski"}` and save it in `config.txt` file (passing `config.txt` is not required as this is a default value)
* `python config.py -method implication-similarity -aggregator maximum -implication lukasiewicz -tnorm lukasiewicz` will generate the following configuration: `{"aggregator": "maximum", "implication": "lukasiewicz", "tnorm": "lukasiewicz", "method": "implication-similarity"}`
* `python config.py -r 2` will throw an exception because no similarity measure method is defined, this will also happen if method name is not valid.
* `python config.py -r not-valid-type -m minkowski` will throw an exception as r parameter in minkowski similarity measure must be a number

### Fuzzy Sets Generator
Script name: `generate_fuzzy_sets.py`

This script is a tool for automatic generating fuzzy sets. Run it wiht `-h` parameter to show current manual.
Examples:
* `python generate_fuzzy_sets.py -h` - Help
* `python generate_fuzzy_sets.py --random -min 0.3 -max 0.6 -n 100 --appendToFile -file myResultFile.txt` 
 This will create fuzzy set containing 100 elements, each element will be a randomly generated value between 0.3 and 0.6. Because of `--apendToFile` generated fuzzy set will be appended to end of the file provided by `-file` parameter. Without the `--appendToFile` result would be printed to console.
* `python generate_fuzzy_sets.py --singleton -value 0.4 -n 30`
 Running this command will generate a fuzzy set with 30 elements, each with value equal to 0.4 

### Fuzzy Sets Comparator
Script name: `compare_sets.py`
Script that allows to compare list of `N` fuzzy sets using one similarity method. It generates a `NxN` matrix R which cell R[i, j] represents a similarity of sets with indexes `i` and `j` calculated with given similarity measure.
It takes two files as an input:
 * file containing list of sets, configurable by `-s` param, each set represented by list of numbers separated by any white character or `,` sign, each set in new line, for example: 
    ```
     1.0 1.0 1.0 0.4 0.2 0.1 0 0 1
     0.5 0.5 0.5 0.0 0.4 0.5 1 1 0
     0 0 0
    ```
 * file containing JSON with similarity measure configuration, use `config.py` to generate sample config. Only configuration from first line of the file is used. 

Examples: 
* `python compare_sets.py -s input/sets.txt -c input/config.txt` - this will compare all sets with each other and print the result to the console
* `python compare_sets.py -s input/sets.txt -c input/config.txt -resultParser excel-result-processor` - using `-resultParser` parameter will allow you to save result in excel file, to specify result file location use `-resultFile`

### Fuzzy similarity measures comparator
Script name: `compare_methods.py`

Script that compares 2 fuzzy sets with list N similarity measures. Running this script will generate a list of N numbers where number `i` is a similarity between defined sets calculated with similarity measure with index `i`.
It takes two files as an input:
* file containing two sets, each in separate line (same format as for Fuzzy Sets Comparator), only first two sets are used.
* file containing list of similarity measures configurations, each configuration represented by JSON placed in separate line of file. Sample configurations can be generated using `config.py` script.

In case of invalid configuration or sets definition program will be terminated with exception describing what happened.
Examples: 
* `python compare_methods.py -s fileContainingSets.txt -c fileContainingConfgs.txt`
* TODO: add different result processors that will be configurable - currently result will be printed to console
ToDO

### Compare N fuzzy sets using M similarity measures
Script `multi-compare.py`

This script will compare N fuzzy sets same as for `Fuzzy Sets Comparator` using each of M provided similarity measures configurations.
Running this script will result with M matrices, each matrix representing result of comparing N sets with one of similarity measures.

## Flask api endpoint
Along with a standard console python scripts a flask server script that expose several REST endpoints is provided. To run this server simply execute `python flaskapp.py`. This command will start a server at: `http://127.0.0.1:5000/`

This server provides few REST endpoint listed below

###REST Similarity Calculator
* Endpoint path: /fuzzy/similarity
* Method: POST

This endpoints allows to check similarity between two fuzzy sets. It takes JSON as a payload. And example payload for calculating similarity with Minkowski method is presented below:
```
{
    "method": "minkowski",
    "setA": [0, 0.5, 1],
    "setB": [1, 0.5, 0],
    "r": 2
}

```
First three parameters are always required:
* `method` stands for similarity measure method that will be used
* `setA` and `setB` stand for fuzzy sets that will be compared.

Because `minkowski` measure requires one additional parameter it's added at the end of the payload. Payload should contain all configuration parameters that referenced similarity measure requires. Below you can find example payload used to compare sets with simplified jaccard similarity measure:
```
{
    "method": "simplified-jaccard-index",
    "setA": [0.71, 0.7437, 0.698, 0.7241, 0.7196, 0.7019],
    "setB": [0.31, 0.7437, 0.698, 0.7241, 0.7196, 0.7019],
    "aggregator: "average",
    "tknorm": "lukasiewicz",
    "tnorm": "lukasiewicz"
}
```

In case of validation failure an error response with `400` code will be returned. Below you can find example response for invalid method name:

```
{
  "message": "Unrecognized method: 'not-supported-method' found while parsing configuration object. List of supported methods: ['angular-distance', 'minkowski', 'jaccard-index', 'implication-similarity', 'simplified-jaccard-index']",
  "status": "FAILURE"
}
```
## Implementing custom similarity measure
Implementing new similarity measure is fairly simple - it require creating two classes:
1. Custom similarity calculator. This class have to extend AbstractSimilarityCalculator available in
abstract_similarity_calculator.py. Extending class must override the `calculateSimilarity` method which will
calculate the similarity between 2 fuzzy sets. For more info look on the provided documentation.

2. Custom similarity configuration parser. This class should extend `AbstractConfigurationParser` and implement 
`parse` method. This method should parse raw configuration map that contains string -> string value pairs to format 
supported by custom similarity calculator implemented in step 1. Map returned by this method should be a valid 
configuration for similarity calculator. For more info have a look on this method documentation.

The last step to perform is to register calculator and config parser in `SimilarityFacade` by adding entry to 
`similarityMethods` list. Each entry is a `SimilarityMethod` object that is basically a triple connecting similarity 
calculator, config parser with unique name. This name is used as identifier of previous objects - this name is 
basically the same name present as value of `method` attribute in JSON configuration (see Similarity measure 
configuration generator section) 

By doing those three steps custom similarity measure will be plugged in for REST server and local executable scripts.
  

## Requirements to run
Python 2.7	

To install all required dependencies run `python setup.py install`.

To run flask server run `python flaskapp.py`


