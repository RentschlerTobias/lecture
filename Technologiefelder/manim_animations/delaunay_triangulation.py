from manim import *
import numpy as np
from scipy.spatial import Delaunay

boundary_nodes = [
    (0, 0),
    (0, 1),
    (1, 1),
    (1, 0)
]
for node in enumerate(boundary_nodes):
    mapped_nodes = self.ax.coords_to_point(node[0]node[1])
s


class DelaunayTriangulation(Scene):
    def construct(self):
        self.add_axis()
        boundary_nodes = [
            (0, 0),
            (0, 1),
            (1, 1),
            (1, 0)
        ]
        for node in enumerate(boundary_nodes):
            mapped_nodes = self.ax.coords_to_point(node[0]node[1])
        self.add(boundary_square)
        self.wait(1)

    def add_axis(self):
        self.ax = Axes(
            x_range=(-0.1, 1),
            y_range=(-0.1, 1),
            # tips=False,
            axis_config={"include_numbers": True})
        self.add(self.ax)
        self.wait(1)
