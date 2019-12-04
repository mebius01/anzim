<template>
    <div>
        <div v-for="item in articles" :key="item.id">
            {{ item.title }}
            <hr>
            <div v-html="item.article"></div>
        </div>
    </div>
</template>

<script>

import axios from 'axios'
// import { response } from 'express';

export default {
    data() {
        return {
            articles: null,
            endpoint: 'http://127.0.0.1:8000/api/v1/articles/',
        }
    },
    mounted() {
      axios.get(this.endpoint).then(response => {this.articles = response.data})
  }
}
</script>

<style scoped>

</style>