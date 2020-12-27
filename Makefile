all: build
build:
	python3 -m urubu build

serve:
	python3 -m urubu serve

fixbuild:
	find _build -name "*.html" -exec todos -o {} \; 


