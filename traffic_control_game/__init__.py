
from gymnasium.envs.registration import register

register(
    id='traffic_control-v0',
    entry_point='traffic_control_game.envs:TrafficControlEnv'
)
