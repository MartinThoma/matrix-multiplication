#include <sstream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <gsl/gsl_cblas.h>

extern C
{
   #include <cblas.h>
}

using namespace std;

struct Result {
	vector< vector<int> > A;
	vector< vector<int> > B;
};

Result read(string filename) {
	vector< vector<int> > A, B;
	Result ab;
	string line;
	ifstream infile;
	infile.open (filename.c_str());

	int i = 0;
	while (getline(infile, line) && !line.empty()) {
		istringstream iss(line);
		A.resize(A.size() + 1);
		int a, j = 0;
		while (iss >> a) {
			A[i].push_back(a);
			j++;
		}
		i++;
	}

	i = 0;
	while (getline(infile, line)) {
		istringstream iss(line);
		B.resize(B.size() + 1);
		int a;
		int j = 0;
		while (iss >> a) {
			B[i].push_back(a);
			j++;
		}
		i++;
	}

	infile.close();
	ab.A = A;
	ab.B = B;
	return ab;
}

vector< vector<int> > ikjalgorithm(vector< vector<int> > A, 
									vector< vector<int> > B) {
	int n = A.size();

	// initialise C with 0s
	vector<int> tmp(n, 0);
	vector< vector<int> > C(n, tmp);

	for (int i = 0; i < n; i++) {
		for (int k = 0; k < n; k++) {
			for (int j = 0; j < n; j++) {
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
		filename = "bigMatrix.in";
	} else {
		filename = argv[2];
	}
	Result result = read (filename);
	int n = result.A.size();
    float *A = new float[n*n];
    float *B = new float[n*n];
    float *C = new float[n*n];
	for (int i=0; i < n; i++) {
		for (int j=0; j < n; j++) {
			A[i*n+j] = result.A[i][j];
			B[i*n+j] = result.B[i][j];
		}
	}
	
	 cblas_sgemm(CblasRowMajor, 
                CblasNoTrans,
                CblasNoTrans, 
                n,
                n,
                n,
                1.0,
                A, n,
                B, n,
                0.0,
                C, n);

    //printf ("[ %i, %i]\n", C[0], C[1]);
	//printMatrix(C);
	return 0;
}
