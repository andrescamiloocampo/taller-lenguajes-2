const app = {
    data(){
        return{
            medida:0,
            variable:'',
            bloque:'',
            constante:'constante=5',
            x:0,
            y:0,
            num:0,
            num1:0,
            im:'',
            booleano:false,
            text:'',
            tipo:'',
            fruits:['Apple','Banana','Cherry'],
            cadena:'...',
            texto:'Hello world',
            texto1:'    Hello world     ',
            texto2:'Hello world',
            caracter:'',
            caracter1:'',
            caracter2:'',
            inf:0,
            sup:0,
            name:'',
            validar:false,
            exp:'',
            resultados:[]
        }
    },
    computed(){
        this.medir()
    },
    watch:{
    
    },
    methods:{
        mensajeConsola(){
            console.log("Hello world")
        },
        //Asi se hace un comentario 
        tiposDeDatos(x){
            this.tipo = typeof(x)
        },
        cambiarTipo(x,op){
            switch(op){
                case 0:
                   x = parseFloat(x)
                   console.log(x,typeof(x))
                break;

                case 1:
                    x = parseInt(x)
                    console.log(x,typeof(x))
                break;
                
                case 2:
                    this.pasarComplejo(x,i)
                break;
            }
        },
        pasarComplejo(x,i){
            if(i==''){
              alert("Ingrese la parte imaginaria")
            }else{
                let complejo = (function(real,imag){
                    return{real:real,imag:imag}
                })(x,i)
                console.log(complejo.real, '+' ,complejo.imag, 'i')
            }
        },
        medir(){
            this.medida = this.cadena.length
        },
        quitarEspacios(){
            console.log(this.texto1)
            this.texto1 = this.texto1.trim()
            console.log(this.texto1)
        },
        letras(x){
            switch(x){
                case 0:{
                    this.texto2 = this.texto2.toUpperCase()
                    console.log(this.texto2)
                    break;
                }
                case 1:{
                    this.texto2 = this.texto2.toLowerCase()
                    console.log(this.texto2)
                    break;
                }
            }
        },
        reemplazar(){
            this.texto2 = this.texto2.replace(this.caracter1,this.caracter2)
        },
        interpretar(exp){
            this.validar = eval(exp)
        },
        operaciones(x){
            switch(x){
                case 1:{
                    const input1 = document.getElementById('inputS')
                    const input2 = document.getElementById('inputS1')
                    this.resultados[0] = parseFloat(input1.value) + parseFloat(input2.value)
                    break;
                }
                case 2:{
                    const input1 = document.getElementById('inputR')
                    const input2 = document.getElementById('inputR1')
                    this.resultados[1] = parseFloat(input1.value) - parseFloat(input2.value)
                    break;
                }
                case 3:{
                    const input1 = document.getElementById('inputM')
                    const input2 = document.getElementById('inputM1')
                    this.resultados[2] = parseFloat(input1.value) * parseFloat(input2.value)
                    break;
                }
                case 4:{
                    const input1 = document.getElementById('inputD')
                    const input2 = document.getElementById('inputD1')
                    this.resultados[3] = parseFloat(input1.value) / parseFloat(input2.value)
                    break;
                }
            }
        },
        incluye(){
            const fruta = document.getElementById('fruitInput')
            if(this.fruits.includes(fruta.value))
               alert("La fruta se encuentra en la lista") 
            else
               alert("La fruta no se encuentra en la lista")
        }
    }
}

var mountedApp = Vue.createApp(app).mount('#app')


