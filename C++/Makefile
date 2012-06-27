#PROBLEM = library-blitz
#PROBLEM = library-boost
#PROBLEM = library-cblas
#PROBLEM = blitz-small
#PROBLEM = ijk-algorithm
#PROBLEM = ikj-algorithm
PROBLEM = strassen

TESTSET = smallMatrix

make:
	#g++ -std=c++98 -Wall -O3 -g $(PROBLEM).cpp -o $(PROBLEM).out -pedantic
	g++ -std=c++98 -Wall -O0 -g $(PROBLEM).cpp -o $(PROBLEM).out -pedantic

test:
	time ./$(PROBLEM).out -i ../$(TESTSET).in > result.txt
	diff ../$(TESTSET).out result.txt

clean:
	rm -rf  $(TARGET) *.class *.html *.log *.aux *.out
