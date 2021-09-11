# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr cfc-*.dist-info
	@rm -fr cfc.egg-info

install:
	@pip install . -U	

all: clean install test

run_api:
	@uvicorn app.main:app --reload


# ----------------------------------
#          AWS Lambda
# ----------------------------------
build-ScraperAPI:
	cp *.py $(ARTIFACTS_DIR)
	cp requirements.txt $(ARTIFACTS_DIR)
	python -m pip install -r requirements.txt -t $(ARTIFACTS_DIR)
	rm -rf $(ARTIFACTS_DIR)/bin