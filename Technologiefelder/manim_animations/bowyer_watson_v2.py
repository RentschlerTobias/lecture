from manim import *

class BowyerWatsonVisualization(Scene):
    def construct(self):
        # Step 1: Create a coordinate system
        axes = Axes(
            x_range=[0, 1.5, 0.2],
            y_range=[0, 1.5, 0.2],
            axis_config={"include_numbers": True},
            tips=False,
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)

        # Step 2: Highlight the domain
        domain = Rectangle(
            width=1, height=1, color=BLUE, fill_opacity=0.1
        ).move_to(axes.c2p(0.5, 0.5))
        domain_label = Text("Domain", font_size=24).next_to(domain, UP)
        self.play(Create(domain), Write(domain_label))
        self.wait(1)

        # Step 3: Add the super-triangle
        super_triangle = Polygon(
            axes.c2p(-0.5, -0.5),
            axes.c2p(1.5, -0.5),
            axes.c2p(0.5, 1.5),
            color=GREEN,
        )
        self.play(Create(super_triangle))
        self.wait(1)

        # Step 4: Add the first node and highlight it
        point1 = Dot(axes.c2p(0.5, 0.5), color=RED)
        point1_label = Text("Point 1", font_size=18).next_to(point1, UP)
        self.play(FadeIn(point1), Write(point1_label))
        self.wait(1)

        # Step 5: Triangulation visualization
        # Initial triangles
        triangle1 = Polygon(
            axes.c2p(-0.5, -0.5),
            axes.c2p(1.5, -0.5),
            axes.c2p(0.5, 0.5),
            color=YELLOW,
            fill_opacity=0.2,
        )
        triangle2 = Polygon(
            axes.c2p(1.5, -0.5),
            axes.c2p(0.5, 1.5),
            axes.c2p(0.5, 0.5),
            color=YELLOW,
            fill_opacity=0.2,
        )
        triangle3 = Polygon(
            axes.c2p(0.5, 1.5),
            axes.c2p(-0.5, -0.5),
            axes.c2p(0.5, 0.5),
            color=YELLOW,
            fill_opacity=0.2,
        )
        self.play(Create(triangle1), Create(triangle2), Create(triangle3))
        self.wait(1)

        # Highlight the circumcircle of a "bad triangle"
        circumcircle = Circle(
            radius=0.7, color=RED
        ).move_to(axes.c2p(0.5, 0.5))
        self.play(Create(circumcircle))
        self.wait(1)

        # Highlight and remove edges of bad triangles
        edge1 = Line(axes.c2p(-0.5, -0.5), axes.c2p(1.5, -0.5), color=RED)
        edge2 = Line(axes.c2p(1.5, -0.5), axes.c2p(0.5, 1.5), color=RED)
        edge3 = Line(axes.c2p(0.5, 1.5), axes.c2p(-0.5, -0.5), color=RED)
        self.play(Create(edge1), Create(edge2), Create(edge3))
        self.wait(1)
        self.play(FadeOut(edge1), FadeOut(edge2), FadeOut(edge3))
        self.wait(1)

        # Add new edges one by one
        new_edge1 = Line(axes.c2p(-0.5, -0.5), axes.c2p(0.5, 0.5), color=GREEN)
        new_edge2 = Line(axes.c2p(1.5, -0.5), axes.c2p(0.5, 0.5), color=GREEN)
        new_edge3 = Line(axes.c2p(0.5, 1.5), axes.c2p(0.5, 0.5), color=GREEN)
        self.play(Create(new_edge1))
        self.wait(0.5)
        self.play(Create(new_edge2))
        self.wait(0.5)
        self.play(Create(new_edge3))
        self.wait(1)

        # Finalize the visualization
        self.play(FadeOut(circumcircle), Write(Text("Triangulation Complete").shift(2 * UP)))
        self.wait(2)
