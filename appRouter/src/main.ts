// import { createApp } from 'vue'
// import App from './App.vue'
// import store from './store'
// import home from './components/home.vue'
// import { createRouter, createWebHashHistory } from 'vue-router'

// const Home = home
// const Detail = {template:'<h1>Detalles</h1>'}

// const routes = [
//     {
//         path:'/',
//         component:Home
//     },
//     {
//         path:'/detail',
//         component:Detail,
//     }
// ]

// const VueRouter = createRouter({
//     history: createWebHashHistory(),
//     routes
// })

// const app = createApp(App).use(store).use(VueRouter).mount('#app')

import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
// import home from './components/home.vue'
import home from '@/components/home.vue'
import object from '@/components/objetos.vue'
import clases from '@/components/clases.vue'
import { createRouter, createWebHashHistory } from 'vue-router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
library.add(faUserSecret)

const Home = home,
Object = object,
Clases = clases 

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/object',
    component: Object
  },
  {
    path: '/class',
    component:Clases
  }
]

const vueRouter = createRouter({
  history: createWebHashHistory(),
  routes
})

const app = createApp(App)
  .component('font-awesome-icon', FontAwesomeIcon)
  .use(store)
  .use(vueRouter)
  .mount('#app')

