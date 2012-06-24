#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>

using namespace std;

struct Result {
	boost::numeric::ublas::matrix<int> A;
	boost::numeric::ublas::matrix<int> B;
};

int getMatrixSize(string filename) {
	string line;
	ifstream infile;
	infile.open (filename.c_str());
	getline(infile, line);
	return count(line.begin(), line.end(), '\t') + 1;
}

void printMatrix(boost::numeric::ublas::matrix<int> matrix) {
	for (unsigned int i=0; i < matrix.size1(); i++) {
		for (unsigned int j=0; j < matrix.size2(); j++) {
			cout << matrix(i, j);
			if(j+1 != matrix.size2()) {
				cout << "\t";
			}	
		}
		cout << endl;
	}
}

Result read(string filename) {
	Result ab;
	string line;
	ifstream infile;
	infile.open (filename.c_str());

	// get dimension
	getline(infile, line);
	int n = getMatrixSize(filename);

	boost::numeric::ublas::matrix<int> A(n,n), B(n,n);

	// process first line
	istringstream iss(line);
	int a, i = 0, j = 0;
	while (iss >> a) {
		A(i,j) = a;
		j++;
	}
	i++;

	while (getline(infile, line) && !line.empty()) {
		istringstream iss(line);
		j = 0;
		while (iss >> a) {
			A(i,j) = a;
			j++;
		}
		i++;
	}

	i = 0;
	while (getline(infile, line)) {
		istringstream iss(line);
		j = 0;
		while (iss >> a) {
			B(i,j) = a;
			j++;
		}
		i++;
	}

	infile.close();
	ab.A = A;
	ab.B = B;
	return ab;
}

int main (int argc, char* argv[]) {
	string filename;
	if (argc < 3) {
		filename = "bigMatrix.txt";
	} else {
		filename = argv[2];
	}
	Result result = read (filename);

	boost::numeric::ublas::matrix<int> C;
	C = boost::numeric::ublas::prod(result.A, result.B);
	printMatrix(C);

	return 0;
}
