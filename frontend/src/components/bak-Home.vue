// Home.vue
<template>
  <div>
    <p>Home page</p>
    <p>Random number from backend: {{ randomNumberB }}</p>
    <p>Random number: {{ randomNumber1 }}</p>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      randomNumber1: 0
    }
  },
  methods: {
    getRandomInt (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandom () {
	// this.randomNumber = this.getRandomInt(1, 100)
	this.randomNumberB = this.getRandomFromBackend()
    },
    getRandomFromBackend() {
	const path = `http://localhost:5000/api/random`
        axios.get(path)
	    .then(response => {
		    this.randomNumberB = response.data.randomNumber
		})
	    .catch(error => {
		    console.log(error)
		})
    }
  },
  created () {
      this.getRandom()
      //      this.randomNumberB = this.getRandomFromBackend();
      //      this.randomNumber1 = this.getRandomInt(1, 100);
  }
}
</script>