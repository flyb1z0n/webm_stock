<template>
    <div>
        <nav class="navbar navbar-light bg-light">
            <span class="navbar-brand mb-0 h1">WebmStock [{{mode}}]</span>
          <NsfwWidget/>
        </nav>

        <div class="container-xxl p-1">
            <MediaList/>
        </div>
    </div>

</template>

<script>
    import MediaList from '@/components/MediaList'
    import NsfwWidget from '@/components/NsfwWidget'

    export default {
        name: 'App',
        components: {
            MediaList,
            NsfwWidget
        },
        data() {
            return {
                mode: process.env.NODE_ENV
            }
        },
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

    .container-xxl{
      width: 100%;
      padding-right: 15px;
      padding-left: 15px;
      margin-right: auto;
      margin-left: auto;
    }

    .container-xxl{
      width: 100%;
      padding-right: 15px;
      padding-left: 15px;
      margin-right: auto;
      margin-left: auto;
    }

    @media (min-width: 1200px)
    {
      .container-xxl {
        max-width: 1320px;
      }
    }


</style>
