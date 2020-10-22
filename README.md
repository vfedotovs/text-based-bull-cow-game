## Table of Contents

* [About the Project](#about-the-project)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)



## About The Project

This is example of text based game known as cow-bull or bull-cow  with numbers to practice python coding skills

## Prerequisites

This game rquires that Python 3.x is installed

## Installation

Clone the repo
```sh
git clone https://github.com/vfedotovs/text-based-bull-cow-game.git
```

## Usage

To run game 
```sh
python3 main.py
```

## RULES of the GAME ##
For every digit that you have guessed correctly in the correct place, you have a “cow”.
For every digit that you have  guessed correctly in the wrong place is a “bull.”
Every time you make a guess, we will print how many “cows” and “bulls” you have.
Once the you guess the correct number, the game is over.
Try to quess number in less than 20 attempts.

```sh
Enter 4 numbers:1234
1 1234 bulls: 1 cows: 1

Enter 4 numbers:4567
1 1234 bulls: 1 cows: 1
2 4567 bulls: 1 cows: 0

Enter 4 numbers:2345
1 1234 bulls: 1 cows: 1
2 4567 bulls: 1 cows: 0
3 2345 bulls: 1 cows: 1

```

