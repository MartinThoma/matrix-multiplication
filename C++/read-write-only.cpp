#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getMatrixSize(string filename) {
	string line;
	ifstream infile;
	infile.open (filename.c_str());
	getline(infile, line);
	return count(line.begin(), line.end(), '\t') + 1;
}

void read(string filename, vector< vector<int> > &A, vector< vector<int> > &B) {
	string line;
	FILE* matrixfile = freopen(filename.c_str(), "r", stdin);

	int i = 0, j, a;
	while (getline(cin, line) && !line.empty()) {
		istringstream iss(line);
		j = 0;
		while (iss >> a) {
			A[i][j] = a;
			j++;
		}
		i++;
	}

	i = 0;
	while (getline(cin, line)) {
		istringstream iss(line);
		j = 0;
		while (iss >> a) {
			B[i][j] = a;
			j++;
		}
		i++;
	}

	fclose (matrixfile);
}

void printMatrix(vector< vector<int> > matrix, int n) {
	for (int i=0; i < n; i++) {
		for (int j=0; j < n; j++) {
			if (j != 0) {
				cout << "\t";
			}
			cout << matrix[i][j];
		}
		cout << endl;
	}
}

int main (int argc, char* argv[]) {
	string filename;
	if (argc < 3) {
		filename = "bigMatrix.in";
	} else {
		filename = argv[2];
	}

	int n = getMatrixSize(filename);
	vector<int> inner (n);
	vector< vector<int> > A(n, inner), B(n, inner), C(n, inner);
	read (filename, A, B);
	// do something with the matrices
	printMatrix(C, n);
	return 0;
}
