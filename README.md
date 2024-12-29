# bashicu-matrix-system
Some python classes for BM2.3=BM4. <br>Thanks to [Fish](https://github.com/kyodaisuu) for the notation. <br>Live at <https://greatcoder1000.github.io/bashicu-matrix-system>
TODO:
re-add the ci.yml file in .github/workflows, ```
name: CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip

    - name: Run tests
      run: |
      ```
