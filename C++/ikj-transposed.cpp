#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getMatrixN(string filename) {
    std::ifstream inFile(filename.c_str()); 
    return std::count(std::istreambuf_iterator<char>(inFile), 
             std::istreambuf_iterator<char>(), '\n');
}

int getMatrixM(string filename) {
	string line;
	ifstream infile;
	infile.open (filename.c_str());
	getline(infile, line);
	return count(line.begin(), line.end(), '\t') + 1;
}

void read(string filename, vector< vector<double> > &A) {
	string line;
	FILE* matrixfile = freopen(filename.c_str(), "r", stdin);

	int i = 0, j;
    double a;
	while (getline(cin, line) && !line.empty()) {
		istringstream iss(line);
		j = 0;
		while (iss >> a) {
			A[i][j] = a;
			j++;
		}
		i++;
	}

	fclose (matrixfile);
}

vector< vector<double> > ikjalgorithmTranspose(
                                   vector< vector<double> > &J, 
								   vector< vector<double> > &T,
								   vector< vector<double> > &R, 
                                   int n, int m) {
	for (register int i = 0; i < n; i++) {
		for (register int k = 0; k < m; k++) {
			for (register int j = i; j < n; j++) {
				R[i][j] += J[i][k] * T[k][j];
			}
		}
	}

	for (register int i = 0; i < n; i++) {
		for (register int j = 0; j < i; j++) {
			R[i][j] += R[j][i];
		}
	}

	return R;
}

void transpose(vector< vector<double> > &A, 
               vector< vector<double> > &B, int n, int m) {
    for (int i=0; i < n; i++) {
        for (int j=0; j < m; j++) {
            B[j][i] = A[i][j];
        }
    }
}

void printMatrix(vector< vector<double> > &matrix, int n) {
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
		filename = "../Testing/5161x7058.in";
	} else {
		filename = argv[2];
	}

	int n = getMatrixN(filename);
    int m = getMatrixM(filename);
	vector<double> inner (m);
	vector<double> inner2 (n);
	vector< vector<double> > J(n, inner), T(m, inner2), R(n, inner);
	read (filename, J);
    transpose(J, T, n, m);
	ikjalgorithmTranspose(J, T, R, n, m);
	printMatrix(R, n);
	return 0;
}
