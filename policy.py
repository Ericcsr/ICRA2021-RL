from typing import Callable, Dict, List, Optional, Tuple, Type, Union

import gym
import torch
from torch import nn
from stable_baselines3 import PPO
from stable_baselines3.common.policies import ActorCriticPolicy


# This policy will be used as PPO Policy

# Assume input Here is 1-D feature vector
# Use a adjacency List to represent DAG
# Have to assume all decisions are binary
# Do or not do
class DiscreteNode(nn.Module):
    def __init__(self,in_feats):
        super(DiscreteNode,self).__init__()
        self.in_feats = in_feats
        self.action_space = action_space
        self.net = nn.Linear(in_feats,1)


    def attach_children(self,children):
        self.childre

    def forward(self,base_feats,pre_feats):
        x = torch.cat([base_feats]+pre_feats)
        logp = self.net(x)
        return logp


# Assume action dag is an adjacency list which has been topologically sorted
class DAGActor(nn.Module):
    def __init__(self,
                 feature_dim,
                 action_dag):
        super(DAGActor,self).__init__()
        self.feature_dim = feature_dim
        # Construct Policy Dependency Structure
        node_list = []
        for node in reversed(action_dag):
            chlids = 
            

    # logp is the raw logp for each node easy for sampling
    # logp_cond is the conditioned path probability for each action easy for loss evaluation
    def forward(self,base_feature):
        return logp, logp_cond


class DAGActorCritic()