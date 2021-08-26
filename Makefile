build:
	poetry build

publish:
	poetry publish --dry-run

install:
	poetry install

package-install:
	python -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall

lint:
	poetry run flake8 gendiff

install-requirements:
	python -m pip install --user --upgrade pip
	python -m pip install poetry

test:
	poetry run pytest
