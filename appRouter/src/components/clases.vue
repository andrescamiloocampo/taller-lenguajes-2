<template>
    <div id="principal">
        <h2>Ejercicios JavaScript 2</h2>
        <section class="s1">
            <h2>Clases</h2>
            <article class="a1">
                <h3>Creación de clases</h3>
                <section class="texto">
                    <p>En vue los componentes son considerados clases
                        esto implica algunos cambios con respecto a la sintaxis
                        JavaScript tradicional.
                    </p>
                </section>

                <section class="texto">
                    <h4>Sintaxis de una clase en JavaScript</h4>
                    <pre>
        class Person{
            constructor(name,age){
                this.name = name
                this.age = age
                }
        }
        </pre>
                </section>

                <section class="texto">
                    <h4>Sintaxis de una clase como un componente Vue</h4>
                    <pre>

    import { Options, Vue }
    from 'vue-class-component';

    @Options({
        props: {
        },
        data() {
            return {
            }
        },
        methods: {
        },
    })
    export default class clase extends Vue 
    {
    }
                        </pre>
                </section>
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
        }
    },
    methods: {
    },
})
export default class clases extends Vue {
}

</script>

<style>
.texto {
    background-color: white;
    color: black;
    width: 60%;
    padding: 2%;
    margin-bottom: 25px;
    border-radius: 10px;
}

.texto h4 {
    margin-bottom: 15px;
}

.texto pre {
    background-color: lightgray;
    padding: 1%;
    border-radius: 5px;
}
</style>


