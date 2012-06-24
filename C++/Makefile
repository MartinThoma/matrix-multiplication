#PROBLEM = library-blitz
PROBLEM = library-boost
#PROBLEM = blitz-small
PROBLEM = ikj-algorithm
#PROBLEM = ijk-algorithm
#PROBLEM = library-cblas

make:
	g++ -std=c++98 -Wall -O3 -g $(PROBLEM).cpp -o $(PROBLEM).out -pedantic
	#meld result-cpp.txt ../smallResult.txt

test:
	time ./$(PROBLEM).out -i ../bigMatrix.txt > result-cpp.txt
	diff ../bigResult.txt result-cpp.txt

clean:
	rm -rf  $(TARGET) *.class *.html *.log *.aux *.out
