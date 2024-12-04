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
- Maximize the smallest interior angle.
<!-- .element: class="fragment" data-fragment-index="3"-->
<div class="r-stack">
  <img
          class="fragment fade-in-then-out"
          src="./assets/delaunay_angle_maximization_01.jpg"
          data-fragment-index="4"
        />
  <img
          class="fragment fade-in-then-out"
          src="./assets/delaunay_angle_maximization_02.jpg"
          data-fragment-index="5"
        />
</div>
</div>
<div id="right">
    <div class="r-stack">
    <img
        class="fragment fade-in-then-out"
        src="./assets/delaunay_triangulation_01.png"
        data-fragment-index="1"
      />
<img
        class="fragment fade-in"
        src="./assets/delaunay_triangulation_02.png"
        data-fragment-index="2"
      />
</div>

</div>


### Bowyer-Watson Algorithm
 <div id="left">
  <pre>
    <code  data-trim data-noescape>
function BowyerWatson(pointList)
    add superTriangle to triangulation
    </code>
  </pre>
<!-- .element: class="fragment" data-fragment-index="1"-->
  <pre>
    <code  data-trim data-noescape>
   for point in pointList: 
      for triangle in triangulation: 
        if point is inside circumcircle:
          add triangle to badTriangles
    </code>
  </pre>
<!-- .element: class="fragment" data-fragment-index="2"-->
  <pre>
    <code  data-trim data-noescape>
     for edge in badTriangles:
        if edge not in other badTriangles:
          add edge to polygon
   </code>
  </pre>
<!-- .element: class="fragment" data-fragment-index="4"-->
  <pre>
    <code  data-trim data-noescape>
     for each triangle in badTriangles:
        remove triangle from triangulation
   </code>
  </pre>
<!-- .element: class="fragment" data-fragment-index="5"-->
  <pre>
    <code  data-trim data-noescape>
    reTriangulate(polygonalHole)
    for edge in superTriangle 
      remove edge
    </code>
  </pre>
<!-- .element: class="fragment" data-fragment-index="6"-->
</div>
<div id="right">
    <div class="r-stack">
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_01.jpg"
        data-fragment-index="1"
    />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_02.jpg"
        data-fragment-index="2"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_03.jpg"
        data-fragment-index="3"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_04.jpg"
        data-fragment-index="4"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_05.jpg"
        data-fragment-index="5"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_06.jpg"
        data-fragment-index="6"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_07.jpg"
        data-fragment-index="7"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_08.jpg"
        data-fragment-index="8"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_09.jpg"
        data-fragment-index="9"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_10.jpg"
        data-fragment-index="10"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_11.jpg"
        data-fragment-index="11"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_12.jpg"
        data-fragment-index="12"
      />
<img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_13.jpg"
        data-fragment-index="13"
      />
<img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_14.jpg"
        data-fragment-index="14"
      />
<img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_15.jpg"
        data-fragment-index="15"
      />
<img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_16.jpg"
        data-fragment-index="16"
      />
<img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_17.jpg"
        data-fragment-index="17"
      />
<img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_18.jpg"
        data-fragment-index="18"
      />
<img
        class="fragment fade-in-then-out"
        src="./assets/bowyer_watson_19.jpg"
        data-fragment-index="19"
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


## Indirect Meshing
### Perfect Matching Voronoi Graph

<div id="left">

- Generate triangulated Delaunay mesh
<!-- .element: class="fragment" data-fragment-index="0"-->
- Condition: 
<!-- .element: class="fragment" data-fragment-index="0"-->
  - $n_{\mathrm{triangle}} == \mathrm{even} $
<!-- .element: class="fragment" data-fragment-index="0"-->
  - $n_{\mathrm{nodes,b}} == \mathrm{even}$
<!-- .element: class="fragment" data-fragment-index="0"-->
- Generate Voronoi-Graph
<!-- .element: class="fragment" data-fragment-index="1"-->
- Find perfect matching graph
<!-- .element: class="fragment" data-fragment-index="2"-->
</div>

  <div id="right">
    <div class="r-stack">
      <img
        class="fragment fade-in-then-out"
        src="./assets/indirect_meshing_03.png"
        data-fragment-index="0"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/indirect_meshing_04.png"
        data-fragment-index="1"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/indirect_meshing_05.png"
        data-fragment-index="2"
      />
      <img
        class="fragment fade-in-then-out"
        src="./assets/indirect_meshing_06.png"
        data-fragment-index="3"
      /> 
   <img
        class="fragment fade-in-then-out"
        src="./assets/indirect_meshing_07.png"
        data-fragment-index="4"
      /> 

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
     data-fragment-index = "1"
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
  <div class = "r-stack">
    <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_01.png"
      data-fragment-index = "1"
      />
    <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_02.png"
      data-fragment-index = "2"
      />
    <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_03.png"
      data-fragment-index = "3"
      />
    <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_04.png"
      data-fragment-index = "4"
      />
    <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_05.png"
      data-fragment-index = "5"
      />
    <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_06.png"
      data-fragment-index = "6"
      />
         <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_07.png"
      data-fragment-index = "7"
      />

   <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_08.png"
      data-fragment-index = "8"
      />

   <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_09.png"
      data-fragment-index = "9"
      />

   <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_10.png"
      data-fragment-index = "10"
      />

   <img
      class = "fragment fade-in-then-out"
      src ="./assets/euclidean_data_11.png"
      data-fragment-index = "11"
      />

   <img
      class = "fragment fade-in"
      src ="./assets/euclidean_data_12.png"
      data-fragment-index = "12"
      />
  </div>
</div>
<div id = 'right'>

### GNN
- Non-Euclidean data
<!-- .element: class="fragment" data-fragment-index="1"-->
  <div class = "r-stack">
    <img
      class = "fragment fade-in-then-out"
      src ="./assets/non_euclidean_data_01.png"
      data-fragment-index = "13"
      />
    <img
      class = "fragment fade-in-then-out"
      src ="./assets/non_euclidean_data_02.png"
      data-fragment-index = "14"
      />
    <img
      class = "fragment fade-in-then-out"
      src ="./assets/non_euclidean_data_03.png"
      data-fragment-index = "14"
      />
      <img
      class = "fragment fade-in-then-out"
      src ="./assets/non_euclidean_data_04.png"
      data-fragment-index = "15"
      />

   <img
      class = "fragment fade-in-then-out"
      src ="./assets/non_euclidean_data_05.png"
      data-fragment-index = "16"
      />

   <img
      class = "fragment fade-in"
      src ="./assets/non_euclidean_data_06.png"
      data-fragment-index = "17"
      />

  </div>
</div>


## Graph Theory
### Introduction
<div style="font-size: 0.8em" >
 <ul>
    <li class="fragment" data-fragment-index="0">
      <strong>What is a Graph?</strong>
    </li>
    <li class="fragment" data-fragment-index="1">
      A graph \( G = (V, E) \) consists of:
    </li>
    <ul>
      <li class="fragment" data-fragment-index="2">
        <strong>Nodes (Vertices) \( V \):</strong> Represent entities or data points.
      </li>
      <li class="fragment" data-fragment-index="3">
        <strong>Edges \( E \):</strong> Represent relationships or connections between nodes.
      </li>
    </ul>
  </ul>

  <ul>
    <li class="fragment" data-fragment-index="4">
      <strong>Node Features:</strong>
    </li>
    <li class="fragment" data-fragment-index="5">
      Each node \( v_i \) has an associated feature vector \( \mathbf{x}_i \).
    </li>
    <li class="fragment" data-fragment-index="6">
      The collection of all node features forms the <strong>Feature Matrix</strong> \( X \).
    </li>
  </ul>

  <ul>
    <li class="fragment" data-fragment-index="8">
      <strong>Adjacency Matrix:</strong>
    </li>
    <li class="fragment" data-fragment-index="9">
      The <strong>Adjacency Matrix</strong> \( A \) represents the connections between nodes.
    </li>
    <li class="fragment" data-fragment-index="10">
      \( A \) is an \( n \times n \) matrix where:
    </li>
    <ul>
      <li class="fragment" data-fragment-index="11">
        \( A_{ij} = 1 \) if there is an edge from node \( i \) to node \( j \).
      </li>
      <li class="fragment" data-fragment-index="12">
        \( A_{ij} = 0 \) otherwise.
      </li>
    </ul>
  </ul>

  <div class="fragment fade-in" data-fragment-index="13" style="text-align: center;">
    \[
    A = \begin{bmatrix}
    A_{11} & A_{12} & \cdots & A_{1n} \\
    A_{21} & A_{22} & \cdots & A_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    A_{n1} & A_{n2} & \cdots & A_{nn} \\
    \end{bmatrix}
    \]
  </div>
</div>


## Graph Neutral Network Indirect Meshing
### Introduction 

<img
    src ="./assets/gnn_indirect_meshng.png"
    />


## Edge Prediction
### Example Citation Network 

<div id = "left">
<div class = "r-stack">
<img
    class = "fragment fade-in-then-out"
    src ="./assets/citation_network_01.png"
    data-fragment-index = "0"
    />
<img
    class = "fragment fade-in"
    src ="./assets/citation_network_02.png"
    data-fragment-index = "1"
    />

  </div>
</div>

<div id="right" style="font-size: 0.8em; display: flex; flex-direction: column; align-items: center;">
<div class = "r-stack">
  <div
    class="fragment fade-in-then-out"
    data-fragment-index="0"
    style="font-size: 0.8em; margin: 0 auto;"
  >
    <strong>Feature Matrix N:</strong><br>
    $\begin{array}{c|cccc}
    & \text{word 1} & \text{word 2} & \cdots & \text{word } m \\
    \hline
    \text{paper 1} & 1 & 0 & \cdots & 1 \\
    \text{paper 2} & 0 & 1 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    \text{paper } n & 1 & 1 & \cdots & 0 \\
    \end{array}$
  </div>
  <div
    class="fragment fade-in"
    data-fragment-index="1"
    style="font-size: 0.8em; margin: 0 auto;"
  >
    <strong>Feature Matrix N:</strong><br>
    $\begin{array}{c|cccc}
    & \text{word 1} & \text{word 2} & \cdots & \text{word } m \\
    \hline
    \text{\color{red}{paper 1}} & \color{red}{1} & \color{red}{0} & \color{red}{\cdots} & \color{red}{1} \\
    \text{paper 2} & 0 & 1 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    \text{\color{blue}{paper }}\color{blue}{n} & \color{blue}{1} & \color{blue}{1} & \color{blue}{\cdots} & \color{blue}{0} \\
    \end{array}$

  </div>
  </div>
<br>

- Number of shared words 
<!-- .element: class="fragment" data-fragment-index="2"-->
  - $n_{shared,w} =(\mathbf{n}_i \times \mathbf{n}_j^T)$
<!-- .element: class="fragment" data-fragment-index="2"-->
- Probability of Citation Between Two Papers
<!-- .element: class="fragment" data-fragment-index="3"-->
  - $Z = \mathrm{GNN}(N,A) $
  - $p_{i,j} = \sigma(\mathbf{z}_i \times \mathbf{z}_j^T)$
<!-- .element: class="fragment" data-fragment-index="4"-->
  - $\hat{A} = \sigma(ZZ^\top) = (n \times z) \times (z \times n) = n \times n$
<!-- .element: class="fragment" data-fragment-index="4"-->

</div>


## Graph Neutral Network Indirect Meshing
<div class = "r-stack">
  <img
    class = "fragment fade-in-then-out"
    src ="./assets/gnn_indirect_meshng.png"
    data-fragment-index = "1"
    />
  <img
    class = "fragment fade-in-then-out"
    src ="./assets/gnn_indirect_meshing_01.png"
    data-fragment-index = "2"
    />
  <img
    class = "fragment fade-in"
    src ="./assets/gnn_indirect_meshing_02.png"
    data-fragment-index = "3"
    />

</div>
<div style="text-align: left;">
    <span
      class="fragment fade-in"
      data-fragment-index="3"
      style="font-size: 0.8em;"
    >
      $Z = \mathrm{GNN}(N,A)$
    </span>
</div>
<div style="text-align: left;">
    <span
      class="fragment fade-in"
      data-fragment-index="4"
      style="font-size: 0.8em;"
    >
      $\hat{A} = \sigma(ZZ^\top) = (n_{\text{nodes}} \times f_{\text{latent}}) \times (f_{\text{latent}} \times n_{\text{nodes}}) = n_{\text{nodes}} \times n_{\text{nodes}}$
    </span>
</div>


## Graph Neutral Network Indirect Meshing
### Loss Function

<div id = "left">

- Represent the quality of GNN with one value
<!-- .element: class="fragment" data-fragment-index="1"-->
- Loss function
<!-- .element: class="fragment" data-fragment-index="2"-->
  - Boundary Loss
<!-- .element: class="fragment" data-fragment-index="3"-->
  - Element Loss
<!-- .element: class="fragment" data-fragment-index="4"-->
  - Node Edge Count Loss
<!-- .element: class="fragment" data-fragment-index="5"-->
- Deleting Edge with the lowest predicted probability
<!-- .element: class="fragment" data-fragment-index="6"-->
- Use predicted probability to compute perfect matching Voronoi-Graph
<!-- .element: class="fragment" data-fragment-index="7"-->
</div>

<div id = "right">
<div class = "r-stack">
 <img
    class = "fragment fade-in-then-out"
    src ="./assets/gnn_indirect_meshing_loss_00.png"
    data-fragment-index = "3"
    />
<img
    class = "fragment fade-in-then-out"
    src ="./assets/gnn_indirect_meshing_loss_01.png"
    data-fragment-index = "4"
    />
 <img
    class = "fragment fade-in-then-out"
    src ="./assets/gnn_indirect_meshing_loss_02.png"
    data-fragment-index = "5"
    />
 <img
    class = "fragment fade-in-then-out"
    src ="./assets/gnn_indirect_meshing_prediction.png"
    data-fragment-index = "6"
    />
 <img
    class = "fragment fade-in-then-out"
    src ="./assets/triGraph_vornoiGraph.png"
    data-fragment-index = "7"
    />
 <img
    class = "fragment fade-in-then-out"
    src ="./assets/triGraph_perfectMatching.png"
    data-fragment-index = "8"
    />
 <img
    class = "fragment fade-in-then-out"
    src ="./assets/quadGraph.png"
    data-fragment-index = "9"
    />

  </div>
</div>


## GNN Node Shifting


## GNN Frame Field Prediction

<div style="text-align: left;">
    <span
      class="fragment fade-in"
      data-fragment-index="1"
      style="font-size: 0.8em;"
    >
    1. Generate triangulated mesh.
    </span>
</div>
<div style="text-align: left;">
    <span
      class="fragment fade-in"
      data-fragment-index="2"
      style="font-size: 0.8em;"
    >
  2. Compute crosses at the boundary.
  </span>
</div>
<div style="text-align: left;">
    <span
      class="fragment fade-in"
      data-fragment-index="3"
      style="font-size: 0.8em;"
    >
  3. Mapping cross vector.
  </span>
</div>

<div style="text-align: left;">
    <span
      class="fragment fade-in"
      data-fragment-index="4"
      style="font-size: 0.8em;"
    >
  4. Pass node feature Matrix N to GNN
  </span>
</div>
<div id="bottom" style="position: absolute; bottom: -100; width: 100%; text-align: center;">
<div class = "r-stack">
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/domain_partition_01.png"
     data-fragment-index = "2"
     height = "400"
/>
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/domain_partition_02.png"
     data-fragment-index = "3"
     height = "400"
 />
 <img
     class = "fragment fade-in-then-out"
     src = "./assets/gnn_domain_partition_01.png"
     data-fragment-index = "4"
     height = "400"
  />
  <img
     class = "fragment fade-in-then-out"
     src = "./assets/gnn_domain_partition_02.png"
     data-fragment-index = "5"
     height = "400"
      />
</div>
  </div>


## GNN Frame Field Prediction
### Evaluation

<div id = "left">

<div style="font-size: 0.8em;">

- <strong>Dataset:</strong>
<!-- .element: class="fragment" data-fragment-index="1"-->
  - random scaling factor
<!-- .element: class="fragment" data-fragment-index="2"-->
  - random rotation factor
<!-- .element: class="fragment" data-fragment-index="2"-->
  - 10.000 Meshes
<!-- .element: class="fragment" data-fragment-index="3"-->
    - 7.000 Training
<!-- .element: class="fragment" data-fragment-index="3"-->
    - 2.000 Validation
<!-- .element: class="fragment" data-fragment-index="3"-->
    - 1.000 Test
<!-- .element: class="fragment" data-fragment-index="3"-->
- <strong>Evaluation:</strong>
<!-- .element: class="fragment" data-fragment-index="4"-->
  - Mean angle: $\Delta_{\text{Angle}}$ [rad] = 0.0580
<!-- .element: class="fragment" data-fragment-index="4"-->
  - Median angle: $\Delta_{\text{Angle}}$ [rad] = 0.0267
<!-- .element: class="fragment" data-fragment-index="4"-->
  - Standard deviation: $\Delta_{\text{Angle}}$ [rad] = 0.0996
<!-- .element: class="fragment" data-fragment-index="4"-->
  - Max angle deviation: $\Delta_{\text{Angle,max}}$ [rad] = 3.1408
<!-- .element: class="fragment" data-fragment-index="4"-->
</div>
</div>

<div id = "right">
<div class = "r-stack">
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/Angle_Deviations_Boxplot.png"
     data-fragment-index = "4"
     height = "400"
  />
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/Angle_Deviations_histogram.png"
     data-fragment-index = "5"
     height = "400"
  />

  </div>
</div>


## GNN Frame Field Prediction

<div id = "left">
<div class = "r-stack">
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/predicted_frame_field.png"
     data-fragment-index = "0"
     height = "400"
  />
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/predicted_frame_field.png"
      data-fragment-index = "1"
     height = "400"
  />

  </div>

</div>

<div id = "right">
<div class = "r-stack">
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/true_frame_field.png"
     data-fragment-index = "0"
     height = "400"
  />
    <img
     class = "fragment fade-in-then-out"
     src = "./assets/Angle_Deviations_frame_field.png"
     data-fragment-index = "1"
     height = "400"
  />

  </div>

</div>
