all:
	g++ -std=c++11 -o hcstats main.cpp alignments/alignments.cpp data/data.cpp measures/measures.cpp
clean:
	rm hcstats