<template>
    <div>
        <div v-for="item in articles" :key="item.id">
            {{ item.title }}
            <br>
            {{item.article}}
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            articles: null,
            endpoint: 'http://127.0.0.1:8000/api/v1/articles/'
        }
    },
    mounted() {
        axios.get(this.endpoint).then(response => {this.articles = response.data})
    },
}
</script>

<style scoped>

</style>