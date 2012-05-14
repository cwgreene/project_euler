problem_files=$(shell ls problem*.cpp | grep -o 'problem[0-9]*')
problems:
	@$(foreach problem,$(problem_files), echo $(problem); g++ -o build/$(problem) $(problem).cpp;)

problem:
ifneq ("X"$(N), "X")
	g++ problem$(N).cpp -o build/problem$(N).cpp
else
	@echo "Need to specify N"
endif


