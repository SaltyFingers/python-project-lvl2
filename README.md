### Hexlet tests and linter status:
[![Actions Status](https://github.com/SaltyFingers/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/SaltyFingers/python-project-lvl2/actions) [![Python CI](https://github.com/SaltyFingers/python-project-lvl2/actions/workflows/tests.yml/badge.svg)](https://github.com/SaltyFingers/python-project-lvl2/actions/workflows/tests.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/bc4768616c2143e6fa4a/maintainability)](https://codeclimate.com/github/SaltyFingers/python-project-lvl2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/bc4768616c2143e6fa4a/test_coverage)](https://codeclimate.com/github/SaltyFingers/python-project-lvl2/test_coverage)

### What is does:
This package allows You get difference between two ``json`` or ``yaml/yml`` files.

### How to install:
To install this package from GitHub on Your PC use command

.. code::bash

    pip install git+https://github.com/SaltyFingers/python-project-lvl2

in your terminal.

### How to use:
You can get help by using:

.. code:: bash

    gendiff -h

To get difference you can use command:

.. code:: bash

    gendiff path/to/file1 path/to/file2

You will get differense in ``stylish`` format as default.

To get difference in ``plain`` format use:

    gendiff -f plain path/to/file1 path/to/file2

And to get difference in ``json`` format use:

    gendiff -f json path/to/file1 path/to/file2

### Demonstration

Stylish demo:
[![asciicast](https://asciinema.org/a/JM913EloUWzhUi4udFoZIOHTj.svg)](https://asciinema.org/a/JM913EloUWzhUi4udFoZIOHTj)

Plain demo:
[![asciicast](https://asciinema.org/a/qZBrOG4E7Gc1d0JG2rVzyjTIX.svg)](https://asciinema.org/a/qZBrOG4E7Gc1d0JG2rVzyjTIX)

Json demo:
[![asciicast](https://asciinema.org/a/Anep3jBkqvvxRMoB9cazCfLB9.svg)](https://asciinema.org/a/Anep3jBkqvvxRMoB9cazCfLB9)