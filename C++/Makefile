#PROBLEM = library-blitz
PROBLEM = library-boost
#PROBLEM = blitz-small
#PROBLEM = ikj-algorithm
#PROBLEM = ijk-algorithm

make:
	g++ -std=c++98 -Wall -O3 -g $(PROBLEM).cpp -o $(PROBLEM).out -pedantic
	#meld result-cpp.txt ../smallResult.txt

clean:
	rm -rf  $(TARGET) *.class *.html *.log *.aux *.out
