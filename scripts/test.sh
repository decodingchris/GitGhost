#!/bin/bash
set -e

PYTHONPATH=. coverage run --source=gitghost -m pytest
coverage report -m
coverage html