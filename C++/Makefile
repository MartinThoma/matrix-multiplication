#PROBLEM = library-blitz
#PROBLEM = library-boost
#PROBLEM = library-cblas
#PROBLEM = blitz-small
#PROBLEM = ijk-algorithm
#PROBLEM = ikj-algorithm
#PROBLEM = strassen
PROBLEM = strassen-mixed
#PROBLEM = read-write-only

TESTSET = 2000

CFLAGS          = -std=c++98 -Wall -pedantic
DEBUGFLAGS      = -O0 -D _DEBUG -g
RELEASEFLAGS    = -O3 -D NDEBUG -DBOOST_UBLAS_NDEBUG

make:
	g++ $(CFLAGS) $(RELEASEFLAGS) $(PROBLEM).cpp -o $(PROBLEM).out
	
debug:
	g++ $(CFLAGS) $(DEBUGFLAGS) $(PROBLEM).cpp -o $(PROBLEM).out

test:
	time -f "%U" ./$(PROBLEM).out -i ../Testing/$(TESTSET).in > result.txt
	diff ../Testing/$(TESTSET).out result.txt

clean:
	rm -rf  $(TARGET) *.class *.html *.log *.aux *.out
