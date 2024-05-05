# Define the name of the Python script
PYTHON_SCRIPT = partie_1.py

# Define the list of input files for each question
FILES_1_2_3_4 = RAM_1_2_3_4.txt
FILE_5_PUISSANCE = RAM_5_puissance.txt
FILE_5_TRI = RAM_5_tri.txt
FILES_6_7 = RAM_6_7.txt

# Define the targets for each question
all: Question1 Question2 Question3 Question4 Question5.1 Question5.2 Question6 Question7

Question1:
	@echo "Building and executing RAM for Question 1..."
	@python3 $(PYTHON_SCRIPT) $(FILES_1_2_3_4)

Question2:
	@echo "Building and executing RAM for Question 2..."
	@python3 $(PYTHON_SCRIPT) $(FILES_1_2_3_4)

Question3:
	@echo "Building and executing RAM for Question 3..."
	@python3 $(PYTHON_SCRIPT) $(FILES_1_2_3_4)

Question4:
	@echo "Building and executing RAM for Question 4..."
	@python3 $(PYTHON_SCRIPT) $(FILES_1_2_3_4)

Question5.1:
	@echo "Building and executing RAM for Question 5.1..."
	@python3 $(PYTHON_SCRIPT) $(FILE_5_PUISSANCE)

Question5.2:
	@echo "Building and executing RAM for Question 5.2..."
	@python3 $(PYTHON_SCRIPT) $(FILE_5_TRI)

Question6:
	@echo "Building and executing RAM for Question 6..."
	@python3 $(PYTHON_SCRIPT) $(FILES_6_7)

Question7:
	@echo "Building and executing RAM for Question 7..."
	@python3 $(PYTHON_SCRIPT) $(FILES_6_7)

clean:
	@echo "Cleaning up..."
	@rm -f *.pyc
	@rm -rf __pycache__

.PHONY: all Question1 Question2 Question3 Question4 Question5.1 Question5.2 clean
