import gym
import torch
from stable_baselines3 import PPO
from kuka_env import KukaGymEnv

env = KukaGymEnv(renders=True)

model = PPO('MlpPolicy',env,verbose=1)
model.learn(total_timesteps=30000)


# Show case
print("Training Finished ...")
#env = KukaGymEnv(renders=True) # rebuild the env to enable the rendering
obs,done = env.reset(),False
total_reward = 0
cnt = 0
while not done:
    if cnt % 10 == 0:
        env.render()
    cnt += 1
    env.render()
    action,_states = model.predict(obs,deterministic=True)
    obs,rew,done,_ = env.step(action)
    total_reward += rew
