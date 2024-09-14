import matplotlib.pyplot as plt
# import matplotlib as mpl
fig = plt.figure()
ax = fig.add_subplot()
fig1 = plt.figure()
ax1 = fig1.add_subplot()
ax.set_yscale('log')
labels = ["Apples","Banana","Oranges"]
col = ['red','yellow','orange']
ax1.pie([1,2,3], labels=labels, colors=col)
fig.suptitle("Title")
ax.set_xlabel("X axis")
ax.grid(ls=':',c ="#CCCCCC")
ax.bar([1, 2, 3, 4], [1000, 100, 10, 1])
ax.plot([5, 3, 2, 1], [1000, 100, 10, 1],'.', lw = 2, mew = 1.75, mec = '#595959', mfc = '#FFFFFF', ms = 10, ls = '--', c = "#000000")
plt.show()