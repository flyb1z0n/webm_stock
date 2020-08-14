<template>
    <div>
        <nav class="navbar navbar-light bg-light">
            <span class="navbar-brand mb-0 h1">WebmStock</span>
        </nav>
        <div class="container">
            <MediaList/>
        </div>
    </div>

</template>

<script>

    import MediaList from '@/components/MediaList'

    export default {
        name: 'App',
        components: {
            MediaList
        }
    }
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
