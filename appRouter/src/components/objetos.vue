<template>
    <div id="principal">
        <h2>Ejercicios JavaScript 2</h2>
        <section class="s1">
            <h2>Objetos</h2>
            <article class="a1">
                <h3>Cambiar atributos</h3>
                <section class="obj">
                    <h4>Marca:{{ car.brand }}</h4>
                    <h4>Modelo:{{ car.model }}</h4>
                    <h4>Año:{{ car.year }}</h4>
                </section>
                <input type="text" placeholder="Ingrese marca" v-model="marca">
                <input type="text" placeholder="Ingrese modelo" v-model="modelo">
                <input type="number" placeholder="Ingrese año" v-model="year">
                <button @click="ingresarDatos">Ingresar datos</button>
            </article>

            <article class="a1">
                <h3>Eliminar atributos</h3>
                <section class="obj">

                    <article class="obj1">
                        <h4>Marca:{{ car.brand }}</h4>
                        <button @click="removerAtributo(0)">X</button>
                    </article>

                    <article class="obj1">
                        <h4>Modelo:{{ car.model }}</h4>
                        <button @click="removerAtributo(1)">X</button>       
                    </article>

                    <article class="obj1">
                        <h4>Año:{{ car.year }}</h4>
                        <button @click="removerAtributo(2)">X</button>
                    </article>

                </section>
                <button @click="removerAtributos()">Quitar atributos</button>
            </article>

            <article class="a1">
                <h3>Crear atributos</h3>
                <section class="obj">
                    <!-- <h4>Marca:{{ car.brand }}</h4>
                    <h4>Modelo:{{ car.model }}</h4>
                    <h4>Año:{{ car.year }}</h4> -->
                    <h4 v-for="[atributo,valor] in Object.entries(car)" v-bind:key="atributo">
                        {{ atributo }} : {{ valor }}
                    </h4>
                </section>
                <input type="text" placeholder="Nombre atributo" v-model="nombre">
                <input type="text" placeholder="Valor atributo" v-model="valor">
                <button @click="ingresarAtributo">Agregar Atributo</button>
            </article>
        </section>
    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
    props: {
    },
    data(){
        return{
            car:{
                brand:'Ford',
                model:'Mustang',
                year:1964
            },
            marca:'',
            modelo:'',
            year:0,
            nombre:'',
            valor:''
        }
    },
    methods:{
        ingresarDatos(){
            this.car.year = this.year
            this.car.brand = this.marca
            this.car.model = this.modelo
        },
        removerAtributo(p:number){
            switch(p){
                case 0:{
                    delete(this.car.brand)
                    break
                }
                case 1:{
                    delete(this.car.model)
                    break
                }
                case 2:{
                    delete(this.car.year)
                    break
                }
            }
        },
        removerAtributos(){
            delete(this.car.brand)
            delete(this.car.model)
            delete(this.car.year)
        },
        ingresarAtributo(){
            let nom = this.nombre,
            val = this.valor
            this.car[nom] = val
            console.log('Hola')
        }
    },
})
export default class objetos extends Vue {
}

</script>

<style>
  .obj{
    background-color: black;
    display: flex;
    width: 50%;
    padding: 2%;
    border-radius: 10px;
    flex-direction: column;
  }

  .obj1{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }

  .obj1 button{
    width: 20px;
    border-radius: 50%;
    background-color: red;
  }

  .obj1 button:hover{
    background-color: rgb(241, 85, 85);
  }
</style>