from typing import List
from .plot import Plot

class LinePlot(Plot):

    def __init__(self, n: int = 1, limit: int = 100, update_every=1, close: bool = True):

        super().__init__(close)

        self.x = []
        self.Y = [[] for _ in range(n)]
        self.lines = [self.fig.gca().plot([], [])[0] for _ in range(n)]
        self.slice = slice(0 if limit is None else -limit, None)
        self.update_every = update_every
        self.push_counter = 0

    def with_legend(self, titles: List[str], **kwargs):

        self.fig.gca().legend(titles, **kwargs)
        self.view.set_figure(self.fig)
        return self

    def push(self, x: List[float], Y: List[List[float]]):

        self.push_counter += 1

        self.x = [*self.x, *x][self.slice]
        for i in range(len(self.lines)):
            self.Y[i] = [*self.Y[i], *Y[i]][self.slice]

        if self.push_counter % self.update_every != 0:
            return

        for i in range(len(self.lines)):
            self.lines[i].set_xdata(self.x)
            self.lines[i].set_ydata(self.Y[i])

        flat_y = [y_i for y in self.Y for y_i in y]
        min_x = min(self.x)
        max_x = max(self.x)
        min_y = min(flat_y)
        max_y = max(flat_y)
        pad_x = 0.01 * (max_x - min_x)
        pad_y = 0.01 * (max_y - min_y)
        self.fig.gca().set_xlim(min_x - pad_x, max_x + pad_x)
        self.fig.gca().set_ylim(min_y - pad_y, max_y + pad_y)
        self.view.set_figure(self.fig)