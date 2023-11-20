<template>
    <button @click="logout">Logout</button>
</template>

<script>
import { getToken } from '../utils/auth';

export default {
  methods: {
    logout() {
      this.$axios.post('/logout', {}, {
        headers: {
          Authorization: `Bearer ${getToken()}`
        }
      })
      .then(() => {
        localStorage.removeItem('token');
        this.$emit('loggedOut');
        this.$store.commit('logout');
        this.$router.push('/login');
      })
      .catch(error => {
        console.error(error);
      });
    }
  }
};
</script>
