// Upload.vue // following https://github.com/alessiomaffeis/vue-picture-input-example
<template>
  <div>
    <p>Upload</p>

    <picture-input ref="pictureInput" @change="onChange" width="200" height="200" margin="8" accept="image/jpeg,image/png" size="10"
      :removable="true" :customStrings="{
        upload: '<h1>Bummer!</h1>',
        drag: 'Drag a GIF'
      }">
    </picture-input>
  </div>
</template>

<script>
  import PictureInput from 'vue-picture-input'
  import axios from 'axios'

  export default {
    name: 'app',
    data() {
      return {
      }
    },
    components: {
      PictureInput
    },
    methods: {
      sendUploadToBackend(name, data) {
        const path = 'http://localhost:5000/api/upload'

        axios.post(path, {'name': name, 'data': data})
        console.log('tried code in sendUploadToBackend')
      },

      onChange(image) {
        console.log('New picture selected!')
        if (this.$refs.pictureInput.image) {
          console.log('Picture is loaded.')
          this.sendUploadToBackend(this.$refs.pictureInput.file.name, this.$refs.pictureInput.image)
        } else {
          console.log('FileReader API not supported: use the <form>, Luke!')
        }
      },
    }
  }

</script>
