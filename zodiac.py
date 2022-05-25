import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (10, 5)

xs_1 = np.array([.2, (9/60 + 30/3600), (1/60 + 30/3600)])
xs_2 = np.array([-30/3600, -(7/60 + 30/3600)])
xs_3 = np.array([-(7/60 + 30/3600), -(7/60 + 30/3600)])
xs_4 = np.array([-(7/60 + 30/3600), -(1/60 + 30/3600)])
xs_5 = np.array([0, 10/60])
xs_6 = np.array([10/60, (12/60 + 30/3600)])

ds_1 = np.array([0, 60, 120])
ds_2 = np.array([120, 180])
ds_3 = np.array([180, 210])
ds_4 = np.array([210, 240])
ds_5 = np.array([240, 300])
ds_6 = np.array([300, 368])

fig, ax = plt.subplots()

ax.plot(ds_1, xs_1, c='black')
ax.plot(ds_2, xs_2, c='black')
ax.plot(ds_3, xs_3, c='black')
ax.plot(ds_4, xs_4, c='black')
ax.plot(ds_5, xs_5, c='black')
ax.plot(ds_6, xs_6, c='black')

ax.plot(np.array([0, 0]), np.array([0, .2]), c='black')
ax.plot(np.array([60, 60]), np.array([0, (9/60 + 30/3600)]), c='black')
ax.plot(np.array([120, 120]), np.array([0, (1/60 + 30/3600)]), c='black')
ax.plot(np.array([120, 120]), np.array([0, -30/3600]), c='black')
ax.plot(np.array([180, 180]), np.array([0, -(7/60 + 30/3600)]), c='black')
ax.plot(np.array([210, 210]), np.array([0, -(7/60 + 30/3600)]), c='black')
ax.plot(np.array([240, 240]), np.array([0, -(1/60 + 30/3600)]), c='black')
ax.plot(np.array([300, 300]), np.array([0, 10/60]), c='black')
ax.plot(np.array([368,368]), np.array([0, (12/60 + 30/3600)]), c='black')
ax.plot(np.array([0, 368]), np.array([0, 0]), c='black')

ds_all = [0, 60, 120, 120, 180, 210, 240, 240, 300, 368]
pairs = [(.2, '0;12'), ((9/60 + 30/3600), '0;9,30'), ((1/60 + 30/3600), '0;1,30'), (-30/3600, '0;30'), (-(7/60 + 30/3600), '0;7,30'), (-(7/60 + 30/3600), '0;7,30'), (-(1/60 + 30/3600), '0;1,30'), (0, '0'), (10/60, '0;10'), ((12/60 + 30/3600), '0;12,30')]
print(len(ds_all), len(pairs))
xvals = [a for (a, b) in pairs]

ax.scatter(ds_all, xvals)
for d, (x_ac, x_s) in zip(ds_all, pairs):
    ax.annotate(x_s, (d, x_ac))

plt.xticks([0, 120, 180, 240, 368])
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
ax.set_xticklabels(['Morning First', 'Morning Station', 'Opposition', 'Evening Station', 'Evening Last'])

plt.title('Motion of Jupiter')
plt.ylabel('Relative Displacement (Speed)')
plt.savefig('zodiacplot.png')
