#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <blitz/matrix.h>
#include <algorithm>

#define N 2000
 
using namespace std;

struct Result {
	blitz::Matrix<int> A, B;
};

int getMatrixSize(string filename) {
	string line;
	ifstream infile;
	infile.open (filename.c_str());
	getline(infile, line);
	return count(line.begin(), line.end(), '\t') + 1;
}

Result read(string filename) {
	Result ab;
	string line;
	ifstream infile;
	infile.open (filename.c_str());

	// get dimension
	blitz::Matrix<int> A, B;

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

void printMatrix(blitz::Matrix<int> matrix, int n) {
	for (unsigned int i=0; i < n; i++) {
		for (unsigned int j=0; j < n; j++) {
			cout << matrix(i, j);
			if(j+1 != N) {
				cout << "\t";
			}	
		}
		cout << endl;
	}
}

int main(int argc, char* argv[]) {
	string filename;
	if (argc < 3) {
		filename = "bigMatrix.in";
	} else {
		filename = argv[2];
	}
	Result a;

	n = getMatrixSize(filename);
	a = read (filename);

	blitz::Matrix<int> A, B, C;

	C = blitz::product(A, B);

	cout << C << endl;
}
