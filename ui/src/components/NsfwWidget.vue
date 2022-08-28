<template>
  <span class="d-flex">
    <label for="nsfw-switch" class="nsfw_eye_slash_icon">
      <b-icon-eye-slash/>
    </label>
    <b-form-checkbox
        id="nsfw-switch"
        v-model="nsfw"
        value="true"
        unchecked-value="false"
        switch>

    </b-form-checkbox>
    <label for="nsfw-switch" class="nsfw_eye_icon">
       <b-icon-eye/>
    </label>



  </span>

</template>

<script>

export default {
  name: 'NsfwWidget',

  computed: {
    nsfw: {
      get() {
        console.log(this.$store.state.nsfw);
        return this.$store.state.nsfw;
      },
      set(value) {
        console.log("set", value);
        this.$store.dispatch('changeNsfw', {value: (value === 'true')});
      }
    }
  },
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
