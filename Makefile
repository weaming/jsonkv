build:
	rm -rf dist && python3 setup.py sdist bdist_wheel

publish:
	TWINE_USERNAME=weaming TWINE_PASSWORD=$$PASSWORD twine upload dist/*

.PHONY: build publish
