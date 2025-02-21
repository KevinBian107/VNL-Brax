import mujoco
from mujoco import mjx
import jax
from jax import numpy as jp

'''BraxData Class'''

# This is the direct inherent data class just like mjx.Data
# Essentially we are plugging in a mid step to store all the data and then in the network function give ppo's original data concatinated form

class BraxData(mujoco.mjx._src.dataclasses.PyTreeNode):
    proprioception: jax.Array
    vision:jax.Array
    shape:tuple
    
    # for the shape function in calling, attribute directly, not a method
    # after shape[-1] should be int
    # at obs level, data should be a concatenated jax array