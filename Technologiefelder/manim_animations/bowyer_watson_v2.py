from manim import *

class BowyerWatsonVisualization(Scene):
    def construct(self):
        # Step 1: Highlight the domain
        domain = Rectangle(width=2, height=2, color=BLUE).shift(UP + RIGHT)
        domain_label = Text("Domain", font_size=24).next_to(domain, UP)
        self.play(Create(domain), Write(domain_label))
        self.wait(1)

        # Step 2: Show the super-triangle
        super_triangle = Polygon(
            [-1, -1, 0], [3, -1, 0], [1, 3, 0], color=GREEN
        )
        self.play(Create(super_triangle))
        self.wait(1)

        # Step 3: Add the first point and highlight it in red
        point1 = Dot(point=[0.5, 0.5, 0], color=RED)
        point1_label = Text("Point 1", font_size=24).next_to(point1, UP)
        self.play(FadeIn(point1), Write(point1_label))
        self.wait(1)

        # Step 4: Triangulation visualization
        # Initial triangles
        triangle1 = Polygon(
            [-1, -1, 0], [3, -1, 0], [0.5, 0.5, 0], color=YELLOW
        )
        triangle2 = Polygon(
            [3, -1, 0], [1, 3, 0], [0.5, 0.5, 0], color=YELLOW
        )
        triangle3 = Polygon(
            [1, 3, 0], [-1, -1, 0], [0.5, 0.5, 0], color=YELLOW
        )
        self.play(Create(triangle1), Create(triangle2), Create(triangle3))
        self.wait(1)

        # Highlight the circumcircle of a "bad triangle"
        circumcircle = Circle(radius=1, color=RED).move_to([0.5, 0.5, 0])
        self.play(Create(circumcircle))
        self.wait(1)

        # Highlight and remove edges of bad triangles
        edge1 = Line([-1, -1, 0], [3, -1, 0], color=RED)
        edge2 = Line([3, -1, 0], [1, 3, 0], color=RED)
        edge3 = Line([1, 3, 0], [-1, -1, 0], color=RED)
        self.play(Create(edge1), Create(edge2), Create(edge3))
        self.wait(1)
        self.play(FadeOut(edge1), FadeOut(edge2), FadeOut(edge3))
        self.wait(1)

        # Add new edges one by one
        new_edge1 = Line([-1, -1, 0], [0.5, 0.5, 0], color=GREEN)
        new_edge2 = Line([3, -1, 0], [0.5, 0.5, 0], color=GREEN)
        new_edge3 = Line([1, 3, 0], [0.5, 0.5, 0], color=GREEN)
        self.play(Create(new_edge1))
        self.wait(0.5)
        self.play(Create(new_edge2))
        self.wait(0.5)
        self.play(Create(new_edge3))
        self.wait(1)

        # Finalize the visualization
        self.play(FadeOut(circumcircle), Write(Text("Triangulation Complete").shift(2 * UP)))
        self.wait(2)
