# Variables
GRAMMAR_DIR = grammar
GRAMMAR_FILE = $(GRAMMAR_DIR)/g.g4
CLASSES_DIR = classes

.PHONY: all clean

# Main target
all:
	@echo "Generating ANTLR files..."
	@antlr4 -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR_FILE)
	@echo "Generation completed"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -f $(GRAMMAR_DIR)/gLexer.py
	@rm -f $(GRAMMAR_DIR)/gParser.py
	@rm -f $(GRAMMAR_DIR)/gVisitor.py  # Limpia gVisitor.py
	@rm -f $(GRAMMAR_DIR)/*.tokens
	@rm -f $(GRAMMAR_DIR)/*.interp
	@echo "Cleaning completed"