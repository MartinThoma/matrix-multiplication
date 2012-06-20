#include <iostream>
#include <blitz/tinymat.h>
#include <blitz/matrix.h>

int main()
{
  using namespace blitz;

  TinyMatrix<int,3,3> A, B, C;
  Matrix<int> D;

  A = 1, 2, 3,
      4, 5, 6,
      7, 8, 9;

	B(0,0) = 5;

  C = product(A, B);

  std::cout << C << std::endl;
}
