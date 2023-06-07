import gym
from black_jack_agent import Agent


if __name__ == '__main__':

    env = gym.make('Blackjack-v1')
    agent = Agent()
    n_episodes = 500000
    for i in range(n_episodes):
        if i % 50000 == 0:
            print('starting episode', i)
        observation = env.reset()[0]
        done = False

        while not done:
            action = agent.policy(observation)
            observation_, reward, done, info, _ = env.step(action)
            agent.memory.append((observation, reward))
            observation = observation_

        agent.update_V()
    print(agent.V[(21, 3, True)])
    print(agent.V[(4, 1, False)])
