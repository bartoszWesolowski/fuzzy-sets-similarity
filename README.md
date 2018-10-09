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

Exaples: 
* `python compare_sets.py -s input/sets.txt -c input/config.txt` - this will compare all sets with each other and print the result to the console
* `python compare_sets.py -s input/sets.txt -c input/config.txt -resultParser excel-result-processor` - using `-resultParser` parameter will allow you to save result in excel file, to specify result file location use `-resultFile`

### Fuzzy similarity measures comparator
Script name: `compare_methods.py`
Script that compares 2 fuzzy sets with list N similarity measures. 

## Requirements to run
Python 2.7	
	
Skrypt compareMethods.py
	- oblicza podobienstwo między dwoma zbioramy zdefiniowanymi w pliku txt, każdy zbiór zdefiniowany jest w osobnej linii pliku, elementy zbioru odzielone powinny być białimy znakami
	- do oblicznia podobieństwa wykorzystuje konfiguracje zdefiniowane w osobnym pliku
	- przykłady plików ze zbiorami oraz konfiguracjami: python\sets.txt oraz python\config.txt
Przykładowe użycie:
	- python compareMethods.py - skrypt wywolany bez parametrow użyje domyślnych nazw dla plików z konfiguracjami sets.txt oraz config.txt
		Wynik z konsoli (testowo)
			Sets file: sets.txt, config file: config.txt
			Parsed sets:
					A: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 1.0]
					B: [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
			Parsing config for minkowski
			Result: 0.823486474191, config: {u'r': 2, u'method': u'minkowski'}
			Parsing config for minkowski
			Result: 0.86760244929, config: {u'r': 3, u'method': u'minkowski'}
			Parsing config for jaccard_index
			Result: 0.56, config: {u'alpha': 1, u'evaluator': u'sup', u'beta': 1, u'gamma': 1, u'method': u'jaccard_index'}
			Parsing config for jaccard_index
			Result: 0.56, config: {u'alpha': 1, u'evaluator': u'sup', u'beta': 1, u'gamma': 1, u'method': u'jaccard_index'}
		
		
	- python compareMethods.py -s customSetsFile.txt -c customConfigFile.txt 
		- parametr -s pozwala na użycie dowolnego pliku zawierającego zbiory rozmyte
		- parametr -c powzwala na użycie dowolnego pliku z konfigracjami.

		
Generating random sets.

Skrypt gerateFuzzySet.py pozwala na automatyczne generowanie zbiorów rozmytych. Przykłady użycia:
	- gerateFuzzySet.py -h -komenda wylistuje wszystkie możliwe parametry wraz z ich znaczeniem oraz wartościami domyślnymi
	- gerateFuzzySet.py --random -min 0.3 -max 0.6 -n 100 --appendToFile -file myResultFile.txt - wywołanie takiej komenty spowoduje wygenerowanie losowego zbioru rozmytego o 100 elementach. Każdy element będzie należał do przedziału [0.3, 0.6]. Dodatkowo wygenerowany zbiór zostanie dopisany do pliku myResultFile.txt (pozwala na to przełącznik --appendToFile - bez niego wynik zostanie tylko wypisany w konsoli)
	- gerateFuzzySet.py --singleton -value 0.4 -n 30 - spowoduje wygenerowanie 30-to elemntowego zbioru składającego się z jednej wartości równej 0.4. Wynik zostanie wyposany na konsolę.
