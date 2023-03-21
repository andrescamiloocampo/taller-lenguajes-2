<template>
  <main>
    <cabecera></cabecera>
    <CardComp></CardComp>
  </main>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import cabecera from './components/CabeceraPrincipal.vue';
import CardComp from './components/CardComp.vue'

export default {
  name: 'App',
  components: {
    cabecera,
    CardComp
  }
}
</script>

<style>
  *{
    margin: 0%;
    padding: 0%;
  }
</style>
