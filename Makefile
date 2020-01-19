#CXX = gcc -Wno-implicit-int	#turn off thie specific warning message - not needed for the g++ compiler

prog1 : main.py functions.py

main.py : main.py
	python3 main.py

functions.py : functions.py
	python3 hw4_functions.py

clean:
	rm -f*.prog
