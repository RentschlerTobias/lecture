
from manim import *
import numpy as np


class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]
        self.edges = [(p1, p2), (p2, p3), (p3, p1)]
        self.circumcircle = self.compute_circumcircle()

    def compute_circumcircle(self):
        # Coordinates of the points
        ax, ay = self.points[0][0], self.points[0][1]
        bx, by = self.points[1][0], self.points[1][1]
        cx, cy = self.points[2][0], self.points[2][1]

        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        if d == 0:
            # Points are colinear; circumcircle is undefined
            return None

        ux = ((ax**2 + ay**2)*(by - cy) + (bx**2 + by**2)
              * (cy - ay) + (cx**2 + cy**2)*(ay - by)) / d
        uy = ((ax**2 + ay**2)*(cx - bx) + (bx**2 + by**2)
              * (ax - cx) + (cx**2 + cy**2)*(bx - ax)) / d

        center = np.array([ux, uy, 0])

        radius = np.linalg.norm(center - self.points[0])

        return (center, radius)

    def contains_point_in_circumcircle(self, p):
        if self.circumcircle is None:
            return False
        center, radius = self.circumcircle
        dist = np.linalg.norm(center - p)
        return dist <= radius


def bowyer_watson(points):
    # Super-triangle that encompasses all the points
    xmin = min(p[0] for p in points)
    xmax = max(p[0] for p in points)
    ymin = min(p[1] for p in points)
    ymax = max(p[1] for p in points)

    dx = xmax - xmin
    dy = ymax - ymin
    delta_max = max(dx, dy)
    midx = (xmax + xmin) / 2
    midy = (ymax + ymin) / 2

    # Create a super-triangle
    p1 = np.array([midx - 20 * delta_max, midy - delta_max, 0])
    p2 = np.array([midx, midy + 20 * delta_max, 0])
    p3 = np.array([midx + 20 * delta_max, midy - delta_max, 0])

    # Initialize the triangulation with the super-triangle
    triangulation = [Triangle(p1, p2, p3)]
    steps = []

    for point in points:
        bad_triangles = []
        for triangle in triangulation:
            if triangle.contains_point_in_circumcircle(point):
                bad_triangles.append(triangle)

        polygon = []
        for triangle in bad_triangles:
            for edge in triangle.edges:
                is_shared = False
                for other_triangle in bad_triangles:
                    if other_triangle == triangle:
                        continue
                    if edge in other_triangle.edges or (edge[1], edge[0]) in other_triangle.edges:
                        is_shared = True
                        break
                if not is_shared:
                    polygon.append(edge)

        for triangle in bad_triangles:
            triangulation.remove(triangle)

        new_triangles = []
        for edge in polygon:
            new_triangle = Triangle(edge[0], edge[1], point)
            new_triangles.append(new_triangle)
            triangulation.append(new_triangle)

        steps.append({
            'point': point,
            'bad_triangles': bad_triangles.copy(),
            'polygon': polygon.copy(),
            'new_triangles': new_triangles.copy(),
            'triangulation': triangulation.copy()
        })

    final_triangulation = []
    for triangle in triangulation:
        if (p1 in triangle.points) or (p2 in triangle.points) or (p3 in triangle.points):
            continue
        final_triangulation.append(triangle)

    return final_triangulation, steps


class DelaunayTriangulation(Scene):
    def construct(self):
        # Define the points
        points = [
            np.array([-2, -1, 0]),
            np.array([0, 2, 0]),
            np.array([2, -1, 0]),
            np.array([-1, 0, 0]),
            np.array([1, 0, 0]),
            np.array([0, -1.5, 0]),
            np.array([1.5, 1, 0]),
            np.array([-1.5, 1, 0])
        ]

        # Draw the points
        point_dots = [Dot(point, color=WHITE) for point in points]
        self.play(*[FadeIn(dot) for dot in point_dots])

        # Compute the triangulation and steps
        final_triangulation, steps = bowyer_watson(points)

        # Animate each step
        for step in steps:
            point = step['point']
            bad_triangles = step['bad_triangles']
            polygon = step['polygon']
            new_triangles = step['new_triangles']

            # Highlight the point being inserted
            point_dot = Dot(point, color=YELLOW)
            self.play(GrowFromCenter(point_dot))

            # Highlight bad triangles
            bad_triangles_mobjects = []
            for triangle in bad_triangles:
                triangle_mobject = Polygon(
                    *[vertex for vertex in triangle.points], color=RED, fill_opacity=0.5)
                bad_triangles_mobjects.append(triangle_mobject)
            self.play(*[FadeIn(triangle_mobject)
                      for triangle_mobject in bad_triangles_mobjects])

            # Show circumcircles of bad triangles
            circles = []
            for triangle in bad_triangles:
                if triangle.circumcircle is not None:
                    center, radius = triangle.circumcircle
                    circle = Circle(radius=radius, color=BLUE).move_to(center)
                    circles.append(circle)
            self.play(*[ShowCreation(circle) for circle in circles])

            # Remove bad triangles
            self.play(*[FadeOut(triangle_mobject)
                      for triangle_mobject in bad_triangles_mobjects])
            self.play(*[FadeOut(circle) for circle in circles])

            # Draw polygonal hole boundary
            polygon_edges = []
            for edge in polygon:
                edge_mobject = Line(edge[0], edge[1], color=GREEN)
                polygon_edges.append(edge_mobject)
            self.play(*[ShowCreation(edge) for edge in polygon_edges])

            # Draw new triangles
            new_triangles_mobjects = []
            for triangle in new_triangles:
                triangle_mobject = Polygon(
                    *[vertex for vertex in triangle.points], color=WHITE, fill_opacity=0.5)
                new_triangles_mobjects.append(triangle_mobject)
            self.play(*[FadeIn(triangle_mobject)
                      for triangle_mobject in new_triangles_mobjects])

            # Remove polygon edges
            self.play(*[FadeOut(edge) for edge in polygon_edges])

            # Remove the inserted point highlight
            self.play(FadeOut(point_dot))

        # Show the final triangulation
        final_triangles_mobjects = []
        for triangle in final_triangulation:
            triangle_mobject = Polygon(
                *[vertex for vertex in triangle.points], color=WHITE, fill_opacity=0.5)
            final_triangles_mobjects.append(triangle_mobject)
        self.play(*[FadeIn(triangle_mobject)
                  for triangle_mobject in final_triangles_mobjects])

        # Show circumcircles of final triangles
        final_circles = []
        for triangle in final_triangulation:
            if triangle.circumcircle is not None:
                center, radius = triangle.circumcircle
                circle = Circle(radius=radius, color=BLUE).move_to(center)
                final_circles.append(circle)
        self.play(*[ShowCreation(circle) for circle in final_circles])

        # Keep the final scene for a few seconds
        self.wait(3)
