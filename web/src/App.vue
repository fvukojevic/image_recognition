<template>
    <div id="app" class="container">
        <h1 class="header"> Image Recognition </h1>
        <Home/>
    </div>
</template>

<script>
    import Home from './components/Home.vue'

    export default {
        name: 'App',
        components: {
            Home
        }
    }
</script>

<style>
    @font-face {
        font-family: 'charlize';
        src: url('./fonts/charlize.regular.ttf');
    }

    body {
        background-color: #F6F6F8 !important;
    }

    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }

    .header {
        font-family: charlize;
        color: #C60021;
        font-size: 4em;
    }
</style>
