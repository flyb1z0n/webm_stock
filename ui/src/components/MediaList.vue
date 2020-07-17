<template>
    <ul>
        <MediaItem v-for="item in items" v-bind:item="item"/>
    </ul>
</template>

<script>
    import MediaItem from '@/components/MediaItem'

    export default {
        name: 'MediaList',
        components: {
            MediaItem
        },
        data() {
            return {
                items: []
            }
        },
        mounted() {
            fetch('http://flyb1z0n.com/webm_stock/api/files?size=32')
                .then(response => response.json())
                .then(json => this.items = json)
        }

    }
</script>

<style>


</style>
