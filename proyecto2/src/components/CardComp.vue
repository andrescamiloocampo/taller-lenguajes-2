<template>
    <main>
        <section class="f1">
            <h2 style="margin-left: 2%; margin-top: 20px;">Listas</h2>
            <article class="f2">
                <h2>Indices en las listas</h2>
                <ol id="frutas">
                    <li v-for="fruta in fruits" v-bind:key="fruta">
                       <h2>{{ fruta }}</h2>
                    </li>
                </ol>
                <input type="number" placeholder="Ingrese un indice de la lista" v-model="indice">
                <button @click="fruit = fruits[indice]">Consultar Lista</button>
                <h2>{{ fruit }}</h2>
            </article>
        </section>
    </main>
</template>

<script>
  export default {
    name: 'CardComp',
    props: {
    },
    data(){
        return{
            fruits:["Apple","Banana","Cherry"],
            indice:0,
            fruit:''
        }
    },
    methods:{

    }
  }

</script>

<style>
 *{
    margin: 0%;
    padding: 0%;
    font-family: monospace;
 }

 main{
    width: 100%;
    height: 100%;
 }
 .f1{
    width:50%;
    height: 300px;
    margin-left: 25%;
    margin-top: 3%;
    background-color: lightgray;
    border-radius: 5px;
 }

 .f2{
    width: 60%;
    margin-left: 20%;
    height: 90%;
    background-color: #0a0a23;
    display: flex;
    justify-content: center;
    text-align: center;
    flex-direction: column;
    justify-content: space-evenly;
    color:white;
    border-radius:5px;
 }

 .f2 ol{
    list-style: none;
 }

 .f2 input,button{
    padding: 2%;
    width: 60%;
    margin-left: 20%;
    border-radius: 30px;
    border: none;
 }

 .f2 button{
    background-color: #feac32;
    margin-left: 22%;
    cursor: pointer;
 }

 .f2 button:hover{
    background-color: lightyellow;
 }

</style>