<template>
    <section class="vh=100 my-0 py-5">
      <div class="container py-5 h-100">
        <div class="row justify-content-center p-4">
          <div class="col-md-8">
            <h3 class="text-center">Change Profile Picture</h3>
            <p>User: <strong>{{ profile.username }}</strong></p>
              <div class="row justify-content-center">
                <img :src="profilePictureURL" v-if="profilePictureURL" class="profile-picture" />
                <input id="textfile" type="file" ref="file" @change="uploadProfilePicture" />
              </div>
          <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      </div>
    </div>
  </div>
  </section>

</template>

<script>
import { getToken } from '../utils/auth';
import { mapState } from 'vuex';

export default {
name: 'ProfileForm',
data() {
  return {
    profile: {},
    profilePictureURL: '',
    errorMessage: ''
  }
},
computed: {
  ...mapState(['isLoggedIn'])
},
methods: {
  fetchProfile() {
    this.$axios.get('/profile', {
      headers: {
        Authorization: `Bearer ${getToken()}`
      }
    })
    .then(response => {
      this.profile = response.data;
      this.profilePictureURL = this.profile.profile_picture ? `http://127.0.0.1:5000/profilepics/${this.profile.profile_picture.split('/').pop()}` : '';
    })
    .catch(error => {
      console.error(error);
    });
  },
  uploadProfilePicture() {
    const file = this.$refs.file.files[0];
    const formData = new FormData();
    formData.append('file', file);
    this.$axios.post('/upload_profile_pic', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Bearer ${getToken()}`
      }
    })
    .then(() => {
      this.fetchProfile();
      this.errorMessage = '';
      this.$store.dispatch('setProfileUpdated', true);
    })
    .catch(error => {
      console.error(error);
      this.errorMessage = error.response ? error.response.data.error : 'Server did not respond. Please try again later.';
    });
  }
},
mounted() {
  this.fetchProfile();
}
}
</script>

<style scoped>

.profile-picture {
max-width: 300px;
max-height: 300px;
border-radius: 50%;
}

input[type='file'] {
  color: rgba(0, 0, 0, 0)
}

section {
  background: linear-gradient(to bottom, #d0dbdf, #94a494);
}

</style>
