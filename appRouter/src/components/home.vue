<template>
    <div id="principal">
        <h2>Ejercicios JavaScript 2</h2>
        <section class="s1">
            <h1>Listas</h1>

            <article class="a1">
                <h3>Indices</h3>
                <h4 v-for="fruit in fruits" v-bind:key="fruit">{{ fruit }}</h4>
                <input type="number" placeholder="Ingrese un indice" v-model="index">
                <button @click="select = fruits[index]">Buscar</button>
                <h4 style="margin-bottom: 2%;">{{ select }}</h4>
            </article>

            <article class="a1">
                <h3>Ingresar datos</h3>
                <h4 v-for="fruit in fruits" v-bind:key="fruit">{{ fruit }}</h4>
                <input type="text" placeholder="Ingrese un nuevo elemento" v-model="nuevo">
                <button @click="fruits.push(nuevo)">Ingresar Elemento</button>
            </article>

            <article class="a1">
                <h3>Ingresar datos en un indice</h3>
                <h4 v-for="fruit in fruits" v-bind:key="fruit">{{ fruit }}</h4>
                <input type="number" placeholder="Ingrese un indice" v-model="indice">
                <input type="text" placeholder="Ingrese un elemento" v-model="nuevo">
                <button @click="ingresarElemento()">Ingresar elemento</button>
            </article>

            <article class="a1">
                <h3>Imprimir en un rango</h3>
                <h4 v-for="fruit in fruits" v-bind:key="fruit">{{ fruit }}</h4>
                <section id="rango">
                    <input type="number" placeholder="limite inferior" v-model="inferior">
                    <input type="number" placeholder="limite superior" v-model="superior">
                </section>
                <button @click="imprimirRango()">Rango</button>
                <h4 v-for="fruit in fruitsR" v-bind:key="fruit">{{ fruit }}</h4>
            </article>

            <article class="a1">
                <h3>Buscar un elemento</h3>
                <h4 v-for="fruit in fruits" v-bind:key="fruit">{{ fruit }}</h4>
                <input type="text" placeholder="Ingrese una fruta" v-model="fruit">
                <button @click="buscar">Buscar</button>
            </article>

            <article class="a1">
                <h3>Unir listas "forEach"</h3>
                <section class="l2">
                    <div>
                        <h4 v-for="fruit in fruits" v-bind:key="fruit">{{ fruit }}</h4>
                    </div>

                    <div>
                        <h4 v-for="fruit in fruits2" v-bind:key="fruit">{{ fruit }}</h4>
                    </div>
                </section>
                <button @click="unir">Unir Listas</button>
            </article>

            <article class="a1">
                <h3>Eliminar elemento</h3>
                <h4 v-for="fruit in fruits" v-bind:key="fruit">{{ fruit }}</h4>
                <input type="text" placeholder="Ingrese un elemento" v-model="fruit">
                <button @click="eliminar">Eliminar</button>
            </article>

        </section>

    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
    props: {
    },
    data() {
        return {
            fruits: ['Apple', 'Banana', 'Cherry'],
            fruits2: ['Orange', 'Mango', 'Grapes'],
            index: 0,
            select: '',
            nuevo: '',
            indice: 0,
            inferior: 0,
            superior: 0,
            fruitsR: [],
            fruit: ''
        };
    },
    methods: {
        ingresarElemento() {
            this.fruits.splice(this.indice, 0, this.nuevo)
        },
        imprimirRango() {
            this.fruitsR = []
            for (let i = this.inferior; i <= this.superior; i++) {
                this.fruitsR.push(this.fruits[i])
            }
        },
        buscar() {
            (this.fruits.includes(this.fruit)) ? alert(`${this.fruit} es una fruta`) : alert(`${this.fruit} no es una fruta`)
        },
        unir() {
            this.fruits2.forEach((fruit: string) => {
                this.fruits.push(fruit)
            })
        },
        eliminar() {
            if (this.fruits.indexOf(this.fruit) > -1) {
                this.fruits.splice(this.fruits.indexOf(this.fruit), 1)
            } else {
                console.log('El elemento no existe en la lista')
            }
        }
    }
})
export default class home extends Vue {
    // fruits: object = {};
    // fruits2:object = {};
    // index: number = 0;
    // select: string = '';
    // nuevo: string = '';
    // indice: number = 0;
    // inferior: number = 0;
    // superior: number = 0;
    // fruitsR: object = {};
    // fruit: string = '';
}

</script>

<style>
#principal {
    width: 80%;
    height: fit-content;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: lightgray;
    margin-left: 10%;
}

#principal h2 {
    margin-top: 2%;
}

.s1 {
    display: flex;
    width: 80%;
    height: fit-content;
    background-color: #282a35;
    border-radius: 5px;
    color: white;
    margin-top: 20px;
    flex-direction: column;
    align-items: center;
}

.s1 h1 {
    margin-top: 20px;
}

.a1 {
    width: 60%;
    height: fit-content;
    margin-top: 2%;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 5px;
    background-color: rgb(17, 198, 230);
}

.a1 h3 {
    margin-top: 20px;
    margin-bottom: 20px;
}

.a1 input {
    margin-top: 3%;
    width: 50%;
    padding: 1%;
    border: none;
    border-radius: 30px;
}

.a1 button {
    background-color: #04aa6d;
    width: 50%;
    padding: 1%;
    border: none;
    margin-top: 2%;
    border-radius: 30px;
    margin-bottom: 2%;
    color: white;
    cursor: pointer;
}

.a1 button:hover {
    background-color: #0be293;
}

.l2 {
    display: flex;
    flex-direction: row;
    width: 50%;
    justify-content: space-between;
}

.l2 div {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
}

#rango {
    display: flex;
    justify-content: space-evenly;
}

#rango input {
    width: 20%;
}
</style>