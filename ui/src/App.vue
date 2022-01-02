<template>
    <div>
        <nav class="navbar navbar-light bg-light">
            <span class="navbar-brand mb-0 h1">WebmStock [{{mode}}]</span>
          <b-form-checkbox
              id="nsfw-switch"
              :value.sync="nsfw"
              value="true"
              unchecked-value="false"
              @change="check($event)"
              switch>
            NSFW
          </b-form-checkbox>
        </nav>

        <div class="container p-2">
            <MediaList/>
        </div>
    </div>

</template>

<script>

    import MediaList from '@/components/MediaList'
    import {mapState} from "vuex";

    export default {
        name: 'App',
        components: {
            MediaList
        },
        computed: mapState({
          nsfw: state => state.nsfw,
        }),
        methods: {
          check: function(e) {
            this.$store.dispatch('toggleNSFW');
          }
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
</style>
