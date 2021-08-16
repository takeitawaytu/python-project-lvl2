build:
	poetry build

publish:
	poetry publish --dry-run

install:
	poetry install

package-install:
	python -m pip install --user dist/hexlet_code-0.1.4-py3-none-any.whl

lint:
	poetry run flake8 brain_games

install-requirements:
	python -m pip install --user --upgrade pip
	python -m pip install poetry