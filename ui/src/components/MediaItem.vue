<template>
    <li class="media-item-li" v-on:click="openWindows(index)">
             <img v-bind:src="item.base_url + item.thumbnail" class="media-item-img nsfw rounded w-100 h-100">
    </li>
</template>

<script>
    export default {
        name: 'MediaItem',
        props: ['item', 'index'],
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
        height: 144px;
        text-align: center;
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
