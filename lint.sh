#!/bin/bash
if [ -z "$CI" ]
then
  # shellcheck source=/dev/null
  source ~/.venvs/i3/bin/activate
  BASH_FILES=$(find . -name "*.sh")
fi
black --check --config i3.toml .
flake8 --ignore=E501 .
# shellcheck disable=SC2086
shellcheck $BASH_FILES

if [ -z "$CI" ]
then
  deactivate
fi