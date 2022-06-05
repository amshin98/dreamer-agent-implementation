# CSC 570 Final Project: Transferring Algorithms to Master Atari
Professor: Dr. Rodrigo "Tío Rodrigo" Canaan
California Polytechnic State University - San Luis Obispo

The work done in this repository was part of a class project done with @Melinal23, @khanmzeeshan, and @patrickrperrine.

## Acknowledgements

The original DreamerV2 repository can be found [here](https://github.com/danijar/dreamerv2).

## Instructions

Install dependencies:
```sh
pip install -r requirements.txt
```

Import an Atari ROM (note: create a `roms` directory and add Atari ROMS to it. We used Breakout):
```sh
ale-import-roms ./roms
```

Train the agent:
```sh
python driver.py
```

Monitor results:
```sh
tensorboard --logdir logdir
```
