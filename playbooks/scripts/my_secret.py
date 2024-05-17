#!/usr/bin/python3

import os

dynatrace_secret_api_key = os.environ['DYNATRACE_API_KEY']

print(f'My dynatrace api secret is *** {dynatrace_secret_api_key} ***')