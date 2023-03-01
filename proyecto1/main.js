const app = {
    data(){
        return{
            variable:'',
            bloque:'',
            constante:'',
            x:0,
            y:0,
            resultado:0
        }
    },
    mounted(){
        
    },
    methods:{
        mensajeConsola(){
            console.log("Hello world")
        },
        //Asi se hace un comentario 
        tiposDeVariables(){
            let variable = 10
            const variable2 = 15
        },
        suma(){
            this.resultado =  this.x + this.y
        }
    }
}

var mountedApp = Vue.createApp(app).mount('#app')


