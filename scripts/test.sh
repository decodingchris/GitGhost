#!/bin/bash
set -e

PYTHONPATH=. coverage run --source=gitvault -m pytest
coverage report -m
coverage html