# Randomized Treap

Python implementation of the Randomized [Treap](https://en.wikipedia.org/wiki/Treap#Randomized_binary_search_tree), a tree data structure that combines properties of BSTs and Heaps with a guarantee to be balanced on average.

Guidance and inspiration from the book [Advanced Algorithms and Data Structures](https://github.com/mlarocca/AlgorithmsAndDataStructuresInAction) by Marcello La Rocca.

## How to setup
```bash
# clone the project
git clone https://github.com/damien-neveu/randomized-treap
cd randomized-treap/

# create a virtual environment for the project (new folder .venv/)
python3 -m venv .venv

# install dependencies in the virtual environment only
source .venv/bin/activate
pip install -r requirements.txt
deactivate
```

## How to run tests
```bash
source .venv/bin/activate
export PYTHONPATH="${PYTHONPATH}:/absolute/path/to/randomized-treap"
python -m pytest
deactivate
```
