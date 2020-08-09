<template>
    <ul v-infinite-scroll="loadMore" infinite-scroll-disabled="busy" infinite-scroll-distance="10">
        <modal name="modal-video">
            <video controls autoplay class="media-list-video">
                <source v-bind:src="selectedItem.base_url + selectedItem.path"/>
            </video>
        </modal>

        <MediaItem v-for="(item, index) in items" v-bind:item="item" v-bind:index="index" v-on:open-media="openMedia"/>
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
            openMedia: function (index) {
                this.selectedItemIndex = this.items[index];
                this.selectedItem = this.items[index];
                this.$modal.show('modal-video');
            },
            loadMore: function () {
                this.page += 1
                fetch('http://webm.flyb1z0n.com/api/files?size=' + this.size + "&page=" + this.page)
                    .then(response => response.json())
                    .then(json => json.forEach(i => this.items.push(i)))
            }

        },
        data() {
            return {
                items: [],
                selectedItemIndex: 0,
                selectedItem: {},
                size: 32,
                page: 0
            }
        },
        mounted() {
            this.loadMore()
        }

    }
</script>

<style>
    .media-list-video {
        height: 100%;
        width: 100%;
    }
</style>
