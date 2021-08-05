import numpy as np
np.random.seed(1234)

def random_walk(N):
    """
    Simulates a discrete random walk
    :param int N : the number of steps to take
    """
    # event space: set of possible increments
    increments = np.array([1, -1])
    # the probability to generate 1
    p=0.5

    # the epsilon values
    random_increments = np.random.choice(increments, N, p)
    # calculate the random walk
    random_walk = np.cumsum(random_increments)

    # return the entire walk and the increments
    return random_walk, random_increments

# generate a random walk
N = 500
X, epsilon = random_walk(N)

# normalize the random walk using the Central Limit Theorem
X = X * np.sqrt(1./N)

import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('seaborn')

#general figure options
fig = plt.figure(figsize=(15, 7))
ax = plt.axes(xlim=(0, N), ylim=(np.min(X) - 0.5, np.max(X) + 0.5))
line, = ax.plot([], [], lw=2)
ax.set_title('2D Random Walk', fontsize=18)
ax.set_xlabel('Steps', fontsize=16)
ax.set_ylabel('Value', fontsize=16)
ax.tick_params(labelsize=12)

# initialization function
def init():
    # creating an empty plot/frame
    line.set_data([], [])
    return line,

# lists to store x and y axis points
xdata, ydata = [], []

# animation function
def animate(i):
    # x, y values to be plotted
    y = X[i]

    # appending new points to x, y axes points list
    xdata.append(i)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,

# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=N, interval=20, blit=True)
# save the animation as mp4 video file
anim.save('random_walk.gif',writer='SurajitAnemie')