<style>

#left {
    left:-8.33%;
  text-align: left;
  float: left;
  width:50%;
  z-index:-10;
}

#right {
  left:31.25%;
  top: 75px;
  float: right;
  text-align: right;
  z-index:-10;
  width:50%;
}
#fs-size {
  font-size:2px;
}

</style>
## Why do we need a Mesh?


## Let's Analyze the Fluid Flow in a Bottle
<div id ="left" >

- Fluid Flow Microscopic Scale
<!-- .element: class="fragment" data-fragment-index="1"-->
- Molecules are in constant motion.
<!-- .element: class="fragment" data-fragment-index="2"-->
- Molecules interacts with others.
<!-- .element: class="fragment" data-fragment-index="3"-->
- Molecules collid.
<!-- .element: class="fragment" data-fragment-index="3"-->
- Tracking every individual molecule is impossible!
<!-- .element: class="fragment" data-fragment-index="4"-->
</div>

<div id ="right">
  <div class="r-stack">
      <img
      class="fragment fade-out"
      data-fragment-index="1"
      src="assets/water_bottle.png"
    />
    <img
      class="fragment current-visible"
      data-fragment-index="1"
      src="assets/water_bottle_zoom_particles_init.png"
    /> 
    <img
      class="fragment current-visible"
      data-fragment-index="2"
      src="assets/water_bottle_zoom_particles_init_shake.png"
    /> 
    <img
      class="fragment current-visible" 
      data-fragment-index="3"
      src="assets/water_bottle_zoom_particles_crash.png"
    />
    <img
      class="fragment current-visible"
      data-fragment-index="4"
      src="assets/water_bottle_zoom_particles_new.png"
    />
    <img
      class="fragment"
      data-fragment-index="5"
      src="assets/water_bottle_zoom_particles_many.png"
    />
  </div>
</div>

<div style="margin-top:450px; text-align: center;">
  <p style="font-size: 1em;">
    \[
    \text{Number of molecules} = \left( \frac{\text{Volume} \times \text{Density}}{\text{Molar Mass}} \right) \times N_A
    \]
    Approximately \(3.35 \times 10^{25}\) molecules
    <!-- .element: class="fragment" data-fragment-index="3"-->
  </p>
</div>


## Fluid as Continuum
 
Description of the Fluid via Navier-Stokes-Equation
<div class = "r-stack" >
  <img 
    class="fragment fade-in-then-out"
    src="./assets/fv001.png"
    data-fragment-index="1"
    height= "450"
  />
  <img 
    class="fragment fade-in-then-out"
    src="./assets/fv002.png"
    data-fragment-index="2"
    height= "450"
  />
  <img 
    class="fragment fade-in-then-out"
    src="./assets/fv003.png"
    data-fragment-index="3"
    height= "450"
  />
  <img 
    class="fragment fade-in-then-out"
    src="./assets/fv004.png"
    data-fragment-index="4"
    height= "450"
  />
 <img 
    class="fragment fade-in"
    src="./assets/fv0066.png"
    data-fragment-index="5"
    height= "450"
  />

</div>
<div style="margin-top:-125px; text-align: center;">

`$$
\begin{aligned}
  \textcolor{blue}{\frac{\partial{}}{\partial{t}} \underline{u}} + 
  \textcolor{orange}{\underline{u} \cdot \left( \nabla \cdot \underline{u} \right)}
  & =
  \textcolor{magenta}{\nu \nabla \cdot \left( \nabla \cdot \underline{u} \right)} -
  \textcolor{green}{\frac{1}{\rho} \nabla p}
  \\
  \nabla \cdot \underline{u} 
  & = 
  0
\end{aligned}
$$`
<!-- .element: class="fragment fade-in" data-fragment-index="5" -->

</div>



## Triangulated Mesh


### Delaunay Triangulation

<div id = 'left'>

- Subdivides the convex hull of a point-cloud into triangles.
<!-- .element: class="fragment" data-fragment-index="1"-->
- Circumcircles of the triangles do not contain any of the points.
<!-- .element: class="fragment" data-fragment-index="2"-->
</div>
<div id="right">
    <div class="r-stack">
      <img
        class="fragment fade-in"
        src="./assets/triangulation_01.png"
        data-fragment-index="0"
      />
</div>
</div>


### Bowyer-Watson Algorithm
<div id="right">
    <div class="r-stack">
      <img
        class="fragment fade-in-then-out"
        src="./assets/triangulation_01.png"
        data-fragment-index="0"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/triangulation_02.png"
        data-fragment-index="2"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/triangulation_03.png"
        data-fragment-index="3"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/triangulation_04.png"
        data-fragment-index="4"
      />
       <img
        class="fragment fade-in-then-out"
        src="./assets/triangulation_05.png"
        data-fragment-index="5"
      />
         <img
        class="fragment fade-in-then-out"
        src="./assets/triangulation_05.png"
        data-fragment-index="5"
      />
</div>
  </div>



## Quadrilateral Mesh 


### Triangulation vs Quadrilateral Methods

<div id = 'left'>

- Quadrilateral mesh generation difficult task
<!-- .element: class="fragment" data-fragment-index="1"-->
- Geometrical "stiff" structure
<!-- .element: class="fragment" data-fragment-index="2"-->
- Inserting Node
<!-- .element: class="fragment" data-fragment-index="3"-->
  - 2D: Possible, but not good
<!-- .element: class="fragment" data-fragment-index="4"-->
  - 3D: Impossible!
<!-- .element: class="fragment" data-fragment-index="5"-->
</div>

<div id= 'right'>
  <div class = 'r-stack'>
      <img
        class="fragment fade-in"
        src="./assets/tri_vs_quad_insert.png"
        data-fragment-index="1"
      />
</div>
</div>


## Indirect Meshing
### Triangle Merge

  <div id="left">
    <ul>
      <li class="fragment fade-in" data-fragment-index="0">Generate a Triangulated Mesh.</li>
      <li class="fragment fade-in" data-fragment-index="1">Delete an Edge between two Triangles to Generate a Quad.</li>
    </ul>
  </div>

  <div id="right">
    <div class="r-stack">
      <img
        class="fragment fade-in-then-out"
        src="./assets/indirect_meshing_01.png"
        data-fragment-index="0"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/indirect_meshing_02.png"
        data-fragment-index="1"
      />
      <video
        class="fragment fade-in"
        autoplay
        loop
        controls
        src="./assets/IndirectMeshTransformation.mp4"
        data-fragment-index="2"
      >
      </video>
    </div>
  </div>


## Cross Fields for Quadrilateral Meshes
### Introduction 
<div id = "right">
  <div class = "r-stack">
    <img
      class = "fragment fade-in-then-out"
      src = "./assets/cross-field_01.png"
      data-fragment-index = "0"
      />
    <img
      class = "fragment fade-in-then-out"
      src = "./assets/cross-field_02.png"
      data-fragment-index = "1"
      />
     <img
      class = "fragment fade-in-then-out"
      src = "./assets/cross-field_03.png"
      data-fragment-index = "2"
      />
     <img
      class = "fragment fade-in-then-out"
      src = "./assets/cross-field_04.png"
      data-fragment-index = "3"
      />
     <img
      class = "fragment fade-in-then-out"
      src = "./assets/cross-field_05.png"
      data-fragment-index = "4"
      />
  </div>
</div>

<div id = "left">

- Define Geometry.
<!-- .element: class="fragment" data-fragment-index="0" -->
- Assume a Quadrilateral Mesh Structure.
<!-- .element: class="fragment" data-fragment-index="1" -->
- Abstract Mesh: Nodes as Line Intersections.
<!-- .element: class="fragment" data-fragment-index="2" -->
- Abstract Mesh: At Each Node Four Orthogonal Vectors.
<!-- .element: class="fragment" data-fragment-index="3" -->
- Crosses Known Along the Boundary.
  <!-- .element: class="fragment" data-fragment-index="4"-->
</div>


## Cross Fields for Quadrilateral Meshes
### Overall Approch

<div id ="left">

- Calculate Normal and Tangent Vectors Along the Boundary.
<!-- .element: class="fragment" data-fragment-index="0"-->
- Simplify Cross-Field to Frame-Field
<!-- .element: class="fragment" data-fragment-index="1"-->
 <img
     class = "fragment fade-in"
     src   = "./assets/cross-field_06.png"
     data-fragment-index = "1"
     />
- Propagate Information from Boundary to the domain's interior. 
<!-- .element: class="fragment" data-fragment-index="2"-->
- Mapping Frame-Field to Cross-Field. 
<!-- .element: class="fragment" data-fragment-index="3"-->
</div>

<div id = "right">
  <div class = "r-stack">
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/domain_partition_01.png"
     data-fragment-index = "0"
     />
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/domain_partition_02.png"
     data-fragment-index = "1"
     />
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/domain_partition_03.png"
     data-fragment-index = "2"
     />
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/domain_partition_04.png"
     data-fragment-index = "3"
     />
  </div>
</div>


## Cross Fields for Quadrilateral Meshes
### Irregularities Identification

<div id = "left">

- Singularities: Locations where Frame Field is not defined.
<!-- .element: class="fragment" data-fragment-index="0"-->
- <img
     class = "fragment fade-in"
     src   = "./assets/Streamline_02.png"
     data-fragment-index = "0"
     height= "300"
     /> 
- Marks Locations Where the Mesh needs Special Treatment
<!-- .element: class="fragment" data-fragment-index="2"-->
  
</div>

<div id = "right">
  <div class = "r-stack">
 <img
     class = "fragment fade-in-then-out"
     src = "./assets/Streamline_01.png"
     data-fragment-index = "0"
    />
 <img
     class = "fragment fade-in-then-out"
     src = "./assets/cross-field_10.png"
     data-fragment-index = "1"
      height = "200"
        />
<img
     class = "fragment fade-in-then-out"
     src = "./assets/Streamlines_03.png"
     data-fragment-index = "2"
       />
 <img
     class = "fragment fade-in-then-out"
     src = "./assets/cross-field_12.png"
     data-fragment-index = "3"
       height = "200"
       />
 </div>
</div>



## Neural Networks


### Neural Networks (NN) vs Graph Neural Networks (GNN)

<div id = 'left'>

### NN
- Euclidean data
<!-- .element: class="fragment" data-fragment-index="1"-->
<img
  class = "fragment fade-in"
  src ="./assets/euclidean_data.png"
  data-fragment-index = "1"
  />
</div>

<div id = 'right'>

### GNN
- Non-Euclidean data
<!-- .element: class="fragment" data-fragment-index="1"-->
<img
  class = "fragment fade-in"
  src ="./assets/non_euclidean_data.png"
  data-fragment-index = "1"
  />

</div>


## Graph Neutral Network Indirect Meshing

<img
  class = "fragment fade-in"
  src ="./assets/indirect_meshing_02.png"
  data-fragment-index = "1"
  />
<img
  class = "fragment fade-in"
  src ="./assets/gnn_indirect_meshng.png"
  data-fragment-index = "2"
  />


## Overall Approch



