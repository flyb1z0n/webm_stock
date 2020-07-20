<template>
    <ul>
        <modal name="modal-video">
            <video controls autoplay class="media-list-video">
                <source v-bind:src="selectedItem.base_url + selectedItem.path"/>
            </video>
        </modal>

        <MediaItem v-for="item in items" v-bind:item="item" v-on:open-media="openMedia"/>
    </ul>
</template>

<script>
    import MediaItem from '@/components/MediaItem'

    export default {
        name: 'MediaList',
        components: {
            MediaItem
        },
        methods: {
            openMedia: function (item) {
                this.selectedItem = item;
                this.$modal.show('modal-video');
            }
        },
        data() {
            return {
                items: [],
                selectedItem: {}
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


    .media-list-video {
        height: 100%;
        width: 100%;
    }

</style>
