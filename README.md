Fuzzy sets similarity calculator

Project created for calculating fuzzy sets similarity using following methods:
	- Minkowski
	- Jaccard
	- Angular Distance
	


Config file creation using config.py script.

Parameters:
	- fn (file name) - path or name of file that config will be appended to
	- m (method) - name of a method that config will be created for
	
Example usage:
	- python config.py -r 2 -m minkowski -fn C:/Users/Lenovo/config.txt
	- python config.py -r 2 -m minkowski -fn config.txt
	- python config.py -r 3 -alpha 1 -beta 1 -gamma 1 -m jaccard_index -evaluator sup (if no fn argument is present the default value equal to config.txt is used)
	
	
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
		