Matrix multiplication
=====================

Some scripts in Python, Java and C++ for matrix multiplication.

Read this blogpost for some explanations:
http://martin-thoma.com/matrix-multiplication-python-java-cpp/

How you can test the programs
=============================
I have created a Bash-Script for testing. You can use it like this:

$ ./test.sh -i Testing/100.in -p "./C++/strassen.out" -n 100

Or

$ ./test.sh -i Testing/100.in -p "python Python/simple-ikj-multiplication.py" -n 100
