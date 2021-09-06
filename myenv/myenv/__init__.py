import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='TwoArmBandit-v0',
    entry_point='myenv.env:twoArmBandit',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)

register(
    id='TenArmBandit-v0',
    entry_point='myenv.env:tenArmBandit',
    timestep_limit=1000,
    reward_threshold=10.0,
    nondeterministic = True,
)

register(
    id='RandomWalk-v0',
    entry_point='gym.envs:SoccerAgainstKeeperEnv',
    timestep_limit=1000,
    reward_threshold=8.0,
    nondeterministic = True,
)