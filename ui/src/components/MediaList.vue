<template>
    <ul v-infinite-scroll="loadMore" infinite-scroll-disabled="busy" infinite-scroll-distance="10"
        class="row justify-content-md-center">
        <b-modal id="b-modal-video" size="xl" centered hide-header hide-footer class="mh-100" @shown=onModalOpened >
            <video controls autoplay class="media-list-video" ref="video_player"
                   :style="{ backgroundImage: 'url(' + selectedItem.base_url + selectedItem.thumbnail + ')' }"
                   v-on:volumechange="volumeChange">
                <source v-bind:src="selectedItem.base_url + selectedItem.path"/>±
            </video>
            <div>
                
                            <a :href="'https://2ch.hk/b/res/' + selectedItem.thread_num + '.html#' + selectedItem.post_num" target="_blank" class="float-right">
                            Открыть тред
                              <b-icon-arrow-up-right></b-icon-arrow-up-right>
                            </a>
            </div>
        </b-modal>

        <MediaItem v-for="(item, index) in items" v-bind:item="item" v-bind:index="index" v-bind:key="item.id"
                   v-on:open-media="openMedia" class="col-3 p-1 "/>
    </ul>
</template>

<script>
    import MediaItem from '@/components/MediaItem'
    import { mapState } from 'vuex'

    export default {
        name: 'MediaList',
        components: {
            MediaItem
        },
        computed: mapState({
            items: state => state.items,
            volume: state => state.volume,
            pageSize: state => state.pageSize
        }),
        methods: {
            onModalOpened: function () {
                //propagate volume
                this.$refs.video_player.volume = this.volume
            },
            volumeChange: function (e) {
                this.$store.dispatch('changeVolume', {value: this.$refs.video_player.volume});
            },
            openMedia: function (index) {
                this.isVideoOpen
                this.selectedItemIndex = index;
                this.selectedItem = this.items[index];
                this.$bvModal.show('b-modal-video')
            },
            loadMore: function () {
                this.$store.dispatch('loadItems');
            },
            openNextMedia: function () {
                let nextIndex = this.selectedItemIndex + 1;
                if (this.items.length - nextIndex < this.pageSize / 2) {
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
                selectedItemIndex: -1,
                selectedItem: {}
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
        width: 100%;
        max-height: calc(100vh - 225px);
        background-size: cover;
    }

</style>
