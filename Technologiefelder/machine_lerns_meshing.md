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
<!-- .element: class="fragment" data-fragment-index="0"-->
- Molecules are in constant motion.
<!-- .element: class="fragment" data-fragment-index="1"-->
- Molecules interacts with others.
<!-- .element: class="fragment" data-fragment-index="2"-->
- Molecules collid.
<!-- .element: class="fragment" data-fragment-index="2"-->
- Tracking every individual molecule is impossible!
<!-- .element: class="fragment" data-fragment-index="3"-->
</div>

<div id ="right">
  <div class="r-stack">
      <img
      class="fragment fade-out"
      data-fragment-index="0"
      src="assets/water_bottle.png"
    />
    <img
      class="fragment current-visible"
      data-fragment-index="0"
      src="assets/water_bottle_zoom_particles_init.png"
    /> 
    <img
      class="fragment current-visible"
      data-fragment-index="1"
      src="assets/water_bottle_zoom_particles_init_shake.png"
    /> 
    <img
      class="fragment current-visible" 
      data-fragment-index="2"
      src="assets/water_bottle_zoom_particles_crash.png"
    />
    <img
      class="fragment current-visible"
      data-fragment-index="3"
      src="assets/water_bottle_zoom_particles_new.png"
    />
    <img
      class="fragment"
      data-fragment-index="4"
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

