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

void read(string &filename, vector< vector<int> > &A, vector< vector<int> > &B) {
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

vector< vector<int> > ikjalgorithm(vector< vector<int> > A, 
									vector< vector<int> > B) {
	int n = A.size();

	// initialise C with 0s
	vector<int> tmp(n, 0);
	vector< vector<int> > C(n, tmp);

	for (register int i = 0; i < n; i++) {
		for (register int k = 0; k < n; k++) {
			for (register int j = 0; j < n; j++) {
				C[i][j] += A[i][k] * B[k][j];
			}
		}
	}
	return C;
}

void printMatrix(vector< vector<int> > matrix) {
	vector< vector<int> >::iterator it;
	vector<int>::iterator inner;
	for (it=matrix.begin(); it != matrix.end(); it++) {
		for (inner = it->begin(); inner != it->end(); inner++) {
			cout << *inner;
			if(inner+1 != it->end()) {
				cout << "\t";
			}
		}
		cout << endl;
	}
}

int main (int argc, char* argv[]) {
	string filename;
	if (argc < 3) {
		filename = "bigMatrix.txt";
	} else {
		filename = argv[2];
	}

	int n = getMatrixSize(filename);
	vector<int> inner (n);
	vector< vector<int> > A(n, inner), B(n, inner);
	read (filename, A, B);
	vector< vector<int> > C = ikjalgorithm(A, B);
	printMatrix(C);
	return 0;
}
