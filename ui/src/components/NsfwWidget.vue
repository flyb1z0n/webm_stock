<template>
  <span class="d-flex">
    <label for="nsfw-switch" class="nsfw_eye_slash_icon">
      <b-icon-eye-slash/>
    </label>
    <b-form-checkbox
        id="nsfw-switch"
        :value.sync="nsfw"
        value="true"
        unchecked-value="false"
        @change="check($event)"
        switch>

    </b-form-checkbox>
    <label for="nsfw-switch" class="nsfw_eye_icon">
       <b-icon-eye/>
    </label>



  </span>

</template>

<script>
import {mapState} from "vuex";

export default {
  name: 'NsfwWidget',

  computed: mapState({
    nsfw: state => state.nsfw,
  }),
  methods: {
    check: function (e) {
      this.$store.dispatch('toggleNSFW');
    }
  }
}
</script>
<style>
.nsfw_eye_slash_icon{
  margin-right: 0.3em
}
.nsfw_eye_icon{
  margin-left: -0.2em
}
</style>
