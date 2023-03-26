<template>
  <div id="app">
    <nav>
      <h1>Pagina principal</h1>
      <section>
        <router-link to="/" class="link">Listas</router-link>
        <router-link to="/object" class="link">Objetos</router-link>
        <router-link to="/class" class="link">Clases</router-link>
      </section>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
export default {
  name: 'App'
}
</script>

<style lang="scss">
* {
  margin: 0%;
  padding: 0%;
}

html,
body {
  font-family: sans-serif;
  width: 100%;
  height: 100%;
}

nav{
  width: 100%;
  height: 60px;
  color: white;
  background-color: black;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}

nav section{
  display: flex;
  flex-direction: row;
  justify-content: center;
  justify-content: space-around;
  margin-top: .5%;
  width:30%;
  margin-left: 35%;
}

.link{
  text-decoration: none;
  color: white;
}
.link:hover{
  text-decoration: underline;
}
</style>
