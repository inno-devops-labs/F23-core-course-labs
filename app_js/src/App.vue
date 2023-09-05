<template>
  <div>
    <h1>Current Time in Moscow</h1>
    <p>{{ currentTime }}</p>
  </div>
</template>

<script>
import { getCurrentTime } from './getCurrentTime';
export default {
  data() {
    return {
      currentTime: ''
    }
  }, 
  mounted() {
     this.currentTime = getCurrentTime();
     setInterval(() => {
       this.currentTime = getCurrentTime();
     }, 1000);
   }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>