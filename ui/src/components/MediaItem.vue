<template>
    <li class="media-item-li" v-on:click="openWindows(index)">
             <img v-bind:src="item.base_url + item.thumbnail" class="media-item-img  rounded w-100 h-100" v-bind:class = "nsfw?'nsfw':''" v-bind:alt="item.fullname">
    </li>
</template>

<script>
    import {mapState} from "vuex";

    export default {
        name: 'MediaItem',
        props: ['item', 'index'],
        computed: mapState({
          nsfw: state => state.nsfw,
        }),
        methods: {
            openWindows: function(index)
            {
                this.$emit('open-media', index)
            }
        }
    }

</script>

<style>
    .media-item-li {
        list-style-type: none;
        display: inline-block;
        height: calc((100vw)/8);
        text-align: center;
    }
    @media (min-width: 1200px)
    {
      .media-item-li {
        height: calc((100vw)/8);
      }
    }
    .nsfw {
        filter: blur(4px);
        -webkit-filter: blur(4px);
        opacity: 0.5
    }
    .media-item-li:hover .nsfw{
        opacity: 1;
        filter: none;
        -webkit-filter: none;
    }
</style>
