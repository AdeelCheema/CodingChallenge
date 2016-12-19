# Coding Challenge (Project Euler)


This repository contains solutions to three Project Euler Problems

  - [Problem 102: Triangle Containment](https://projecteuler.net/problem=102)
  - [Problem 119: Digit Power Sum](https://projecteuler.net/problem=119)
  - [Problem 107: Minimum Network](https://projecteuler.net/problem=107)



### Usage

Each solution was coded in Python

The solutions are located in the main CodingChallenge folder and are directly runnable.

Tests for each solution are provided in the tests folder.

```sh
$ nosetests -v --with-coverage --cover-package=CodingChallenge \
              --cover-inclusive --cover-erase tests
```

### Extra

Problem 102 has a supplemental API hosted at http://ep102.herokuapp.com. The backend code is located in [app.py](https://github.com/AdeelCheema/CodingChallenge/blob/master/app.py)

Simply enter comma separated triangle vertices to test origin containment
