<template>
    <ul v-infinite-scroll="loadMore" infinite-scroll-disabled="busy" infinite-scroll-distance="10"  class="row justify-content-md-center">
        <modal name="modal-video" v-bind:item="selectedItem" @opened="onModalOpened">
            <video controls autoplay class="media-list-video" ref="video_player"
                   :style="{ backgroundImage: 'url(' + selectedItem.base_url + selectedItem.thumbnail + ')' }"
                   v-on:volumechange="volumeChange">
                <source v-bind:src="selectedItem.base_url + selectedItem.path"/>
            </video>
        </modal>

        <MediaItem v-for="(item, index) in items" v-bind:item="item" v-bind:index="index" v-on:open-media="openMedia" class="col-3 p-1 "/>
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
            onModalOpened: function () {
                //propagate volume
                this.$refs.video_player.volume = this.volume
            },
            volumeChange: function (e) {
                // propagate volume back
                this.volume = this.$refs.video_player.volume
            },
            openMedia: function (index) {
                this.selectedItemIndex = index;
                this.selectedItem = this.items[index];
                console.log("OpenMedia #", index, this.selectedItem)


                this.$modal.show('modal-video')


            },
            loadMore: function () {
                console.log("Loading More | Page: " + this.page + " | Size: " + this.size)

                this.page += 1
                return fetch('http://webm.flyb1z0n.com/api/files?size=' + this.size + "&page=" + this.page)
                    .then(response => response.json())
                    .then(json => json.forEach(i => this.items.push(i)))
            },
            openNextMedia: function () {
                let nextIndex = this.selectedItemIndex + 1;
                if (this.items.length - nextIndex < this.size / 2) {
                    this.loadMore()
                }
                if (nextIndex >= this.items.length) {
                    return;
                }
                this.openMedia(nextIndex);
                this.$refs.video_player.load();

            },
            openPrevMedia: function () {
                let prevIndex = this.selectedItemIndex - 1;

                if (prevIndex < 0) {
                    return
                }
                this.openMedia(prevIndex);
                this.$refs.video_player.load();
            },


            onKeyPress(event) {
                switch (event.key) {
                    case "ArrowUp":
                    case "ArrowLeft":
                        this.openPrevMedia();
                        break;
                    case "ArrowDown":
                    case "ArrowRight":
                        this.openNextMedia();
                        break;
                }
            }


        },
        data() {
            return {
                items: [],
                selectedItemIndex: -1,
                selectedItem: {},
                size: 64,
                page: 0,
                volume: 0.5
            }
        },
        mounted() {
            this.loadMore()
            window.addEventListener("keydown", e => {
                this.onKeyPress(e)
            });
        }

    }
</script>

<style>
    .media-list-video {
        height: 100%;
        width: 100%;
        background-size: cover;
    }

</style>
