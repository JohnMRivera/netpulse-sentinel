<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import axios from 'axios';
import { ref, onMounted } from 'vue';

const status = ref('Cargando...')

onMounted(() => {
  console.log("Cargando...")

  axios.get('http://localhost:5000/status').then( response => {
    status.value = response.data

    console.log(`El código de status es de ${status.value.status}\nMensaje: ${status.value.message}`)
  }).catch( error => {
    status.value = "¡Error al intentar conectar!"
  })
})
// export default {
//   data(){
//     return { status: "Cargando..." }
//   },
//   mounted(){
//     axios.get('http://localhost:5000/status')
//     .then( response => {
//       this.status = response.data.message
//     })
//     .catch( error => {
//       this.status = "Error al intentar conectar"
//     })
//   }
// }
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div> -->
  </header>

  <main>
    <!-- <TheWelcome /> -->
    <h1> Bienvenida </h1>
    <ul>
      <li>
        <p> Código de status {{ status.status }}</p>
      </li>
      <li>
        <p> {{ status.message }} </p>
      </li>
    </ul>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>