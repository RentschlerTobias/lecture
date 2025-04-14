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


# Technische Strömungslehre 
___
## Vortragsübung 1


# Organisation

- Ilias: Aufbau der Lehrveranstaltung
   - Termine, Hörsaal, etc.
   - Forum
- 10x Vortragsübungen 
   - Verantwortliche: Frau Ma & Herr Rentschler
   - Present und Online 
- 9x Tutorien
   - Verantwortlicher: Herr Raj
- Online Sprechstunde


## Termine Vortragsübung

| Thema                        | Datum          | Uhrzeit       | Hörsaal |
|-----------------------------:|:--------------:|:-------------:|:-------:|
| Hydrostatik                  | Mo. 05.12.2025 | 11:30–13:00   | V53.01  |
| Hydrostatik                  | Mo. 12.05.2025 | 11:30–13:00   | V53.01  |
| Erhaltungsgleichungen        | Mo. 26.05.2025 | 11:30–13:00   | V53.01  |
| Erhaltungsgleichungen        | Di. 27.05.2025 | 15:45–17:15   | V47.01  |
| Erhaltungsgleichungen        | Mo. 16.06.2025 | 11:30–13:00   | V53.01  |
| Rohrhydraulik                | Di. 17.06.2025 | 15:45–17:15   | V47.01  |
| Rohrhydraulik                | Mi. 30.06.2025 | 11:30–13:00   | V53.01  |
| Differentialgleichungen/Spalt| Mo. 14.07.2025 | 11:30–13:00   | V53.01  |
| Prüfungsaufgaben 2025F       | Di. 15.07.2025 | 15:45–17:15   | V47.01  |
| Prüfungsaufgaben 2025F       | Mo. 21.07.2025 | 11:30–13:00   | V47.04  |


# Statik der Fluide 
## Teil 1


# Grundbegriffe
- Statik: 
   - $\sum{\vec{F}} = m \cdot \vec{a} = \frac{\partial \left(m \vec{v}\right)}{\partial t} \stackrel{!}{=} 0$
   - Keine relative bewegung zwischen den Fluidteilchen 

- Druck: 
   - Einheit: $ Pa = \left[\frac{N}{m^2}\right]$ 
   - Skalarer Wert => Richtungsunabhängig
<div class="r-stack">
<img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/HydrostatischerDruck.png"
   data-fragment-index="1"
   />
 <img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/hydrostatik_03.png"
   data-fragment-index="4"
   /> 
</div>


# Grundbegriffe
- Druckverlauf: $p(h)$
<div class="r-stack">
<img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/druckverlauf_01.png"
   data-fragment-index="1"
   />
<img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/druckverlauf_02.png"
   data-fragment-index="2"
   /> 
<img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/druckverlauf_03.png"
   data-fragment-index="3"
   /> 
<img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/druckverlauf_04.png"
   data-fragment-index="4"
   /> 
<img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/druckverlauf_05.png"
   data-fragment-index="5"
   /> 
<img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/druckverlauf_06.png"
   data-fragment-index="6"
   /> 
<img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/druckverlauf_07.png"
   data-fragment-index="7"
   /> 
<img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/druckverlauf_08.png"
   data-fragment-index="8"
   /> 
<img
   class="fragment fade-in-then-out"
   src="./assets/StatikDerFluide/druckverlauf_09.png"
   data-fragment-index="9"
   /> 
</div>


- Druckkraft: $ \vec{F} = - \int{p\ d\vec{A}} =  - \int{p\vec{n}\ dA}$
   - Vektor => Richtungsabhängig
