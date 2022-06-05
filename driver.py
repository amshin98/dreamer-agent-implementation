from ale_py import ALEInterface, SDL_SUPPORT
import gym

import dreamerv2.api as dv2

ale = ALEInterface()

# Get & Set the desired settings
ale.setInt("random_seed", 123)

# If you get errors about the SDL failing to initialize, comment out this
# entire if statement. It's used for displaying the game as the agent trains,
# so you only actually need this if you use the gym.make statement below with
# render_mode='human'
if SDL_SUPPORT:
    ale.setBool("sound", True)
    ale.setBool("display_screen", True)

# Load the ROM file. Requires ale-import-roms to be run first, or comment out the
# line below and change Breakout in the line below that one to a file path to a ROM
from ale_py.roms import Breakout
ale.loadROM(Breakout)

config = dv2.defaults.update({
    'logdir': './logdir/breakout',
    'log_every': 1e3,
    'train_every': 10,
    'prefill': 1e5,
    'actor_ent': 3e-3,
    'loss_scales.kl': 1.0,
    'discount': 0.99,
})

# To display the screen (if this is possible on your machine) uncomment first line below
# and comment out the one below that
#env = gym.make('Breakout-v4', render_mode='human')
env = gym.make('Breakout-v4')

dv2.train(env, config)
