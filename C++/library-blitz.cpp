#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <blitz/matrix.h>
#include <algorithm>

#define FILENAME "/home/moose/Desktop/matrix-multiplication/bigMatrix.txt"
#define N 2000
 
using namespace std;

struct Result {
	blitz::Matrix<int> A, B;
};

int getMatrixSize() {
	string line;
	ifstream infile;
	infile.open (FILENAME);
	getline(infile, line);
	return count(line.begin(), line.end(), '\t') + 1;
}

Result read() {
	Result ab;
	string line;
	ifstream infile;
	infile.open (FILENAME);

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

void printMatrix(blitz::Matrix<int> matrix) {
	for (unsigned int i=0; i < N; i++) {
		for (unsigned int j=0; j < N; j++) {
			cout << matrix(i, j);
			if(j+1 != N) {
				cout << "\t";
			}	
		}
		cout << endl;
	}
}

int main() {
	Result a;
	a = read ();

	blitz::Matrix<int> A, B, C;

	C = blitz::product(A, B);

	cout << C << endl;
}
