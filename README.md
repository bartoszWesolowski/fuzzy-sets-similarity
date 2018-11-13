#Fuzzy sets similarity calculator
Simple tool for calculating fuzzy sets similarity using different similarity measures.
## Supported Similarity Measures

#### Minkowski
TODO
#### Angular Distance
TODO
#### Implication
TODO

#### Jaccard Index
TODO

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
* `python config.py -r 2 -m minkowski -fn config.txt` - this will generate the following json `{"r": 4, "method": "minkowski"}` and save it in `config.txt` file (passing `config.txt` is not required as this is a default value)
* `python config.py -method implication-similarity -aggregator maximum -implication lukasiewicz -tnorm lukasiewicz` will generate the following configuration: `{"aggregator": "maximum", "implication": "lukasiewicz", "tnorm": "lukasiewicz", "method": "implication-similarity"}`
* `python config.py -r 2` will throw an exception because no similarity measure method is defined, this will also happen if method name is not valid.
* `python config.py -r not-valid-type -m minkowski` will throw an exception as r parameter in minkowski similarity measure must be a number

### Fuzzy Sets Generator
Script name: `generateFuzzySet.py`

This script is a tool for automatic generating fuzzy sets. Run it wiht `-h` parameter to show current manual.
Examples:
* `python gerateFuzzySet.py -h` - Help
* `python gerateFuzzySet.py --random -min 0.3 -max 0.6 -n 100 --appendToFile -file myResultFile.txt` 
 This will create fuzzy set containing 100 elements, each element will be a randomly generated value between 0.3 and 0.6. Because of `--apendToFile` generated fuzzy set will be appended to end of the file provided by `-file` parameter. Without the `--appendToFile` result would be printed to console.
* `python gerateFuzzySet.py --singleton -value 0.4 -n 30`
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
TODO

##Implementing next similarity measure
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

By doing those three steps 
  

## Requirements to run
Python 2.7	
