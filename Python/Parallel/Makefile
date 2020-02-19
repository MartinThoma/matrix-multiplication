ALGORITHM = ikjMultiplication

TESTSET = 2000

test:
	time -f "%U" python $(ALGORITHM).py --threads 4 -i ../../Testing/$(TESTSET).in > result.txt
	diff ../../Testing/$(TESTSET).out result.txt
