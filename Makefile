all: build
build:
	python -m urubu build

serve:
	python -m urubu serve

fixbuild:
	find _build -name "*.html" -exec todos -o {} \;
