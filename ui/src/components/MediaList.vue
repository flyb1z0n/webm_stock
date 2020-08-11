<template>
    <ul v-infinite-scroll="loadMore" infinite-scroll-disabled="busy" infinite-scroll-distance="10">
        <modal name="modal-video" v-bind:item="selectedItem">
            <video controls autoplay class="media-list-video" ref="video_player">
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
                this.selectedItemIndex = index;
                this.selectedItem = this.items[index];
                console.log("OpenMedia #",index, this.selectedItem)


                this.$modal.show('modal-video');

            },
            loadMore: function () {
                console.log("Loading More")
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
                page: 0
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
    }
</style>
