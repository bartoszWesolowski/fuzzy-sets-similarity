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