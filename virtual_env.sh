#!/bin/bash

virtualenv OCR --python=$(which python3)

source OCR/bin/activate ; pip3 install -r requirements.txt