.PHONY: generate test

generate:
	bash scripts/generate.sh

test:
	python -m pytest
