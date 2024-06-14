#!/bin/sh


case "$RTE" in
    dev )
        echo "** Development mode."
        pip-audit
        coverage run --source="." --omit=coffee_shop.py test --verbosity 2
        coverage report -m
        python coffee_shop.py
        ;;
    test )
        echo "** Test mode."
        pip-audit || exit 1
        coverage run --source="." --omit=coffee_shop.py test --verbosity 2
        coverage report -m --fail-under=80
        ;;
    prod )
        echo "** Production mode."
        pip-audit || exit 1
        python coffee_shop.py check --deploy
        ;;
esac

echo "Starting linting on yml files with yamllint"
yamllint docker-compose.yml

#echo "Starting linting on python files with pylama"
#pylama coffee_shop.py

echo "Starting linting on Dockerfile with hadolint-bin"
hadolint Dockerfile

echo "Starting linting on txt files with proselint"
proselint requirements.txt

echo "Starting linting on the sql files with sqlfluff"
sqlfluff lint --exclude-rules LT02,LT05 dbscripts/provisioning.sql --dialect postgres

echo "Starting safely to check for vulnerabilities in the installed dependencies"
safety check -r requirements.txt --bare

echo "Starting code checking on python files with pyflakes"
pyflakes coffee_shop.py
pyflakes tests/test_http.py

echo "Starting entrypoint script"
python coffee_shop.py
