<template>
    <li class="media-item-li" v-on:click="openWindows(item)">
        <img v-bind:src="item.base_url + item.thumbnail" class="media-item-img nsfw">
    </li>
</template>

<script>
    export default {
        name: 'MediaItem',
        props: ['item'],
        methods: {
            openWindows: function(item)
            {
                this.$emit('open-media', item)
            }
        }
    }

</script>

<style>
    .media-item-li {
        list-style-type: none;
        display: inline-block;
        width:310px;
        height: 174px;
        background: #3B666B;
        border-radius: 8px;
        margin: 5px;
        text-align: center;
    }

    .media-item-img {
        height: 100%;
        width: 100%;
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
