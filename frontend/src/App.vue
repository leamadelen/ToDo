<template>
  <div id="app">
      <nav class="navbar navbar-expand-lg navbar-light p-5">
      <div class="container-fluid">

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <a class="navbar-brand mt-2 mt-lg-0 ">
        <img
          src="https://lh3.googleusercontent.com/drive-viewer/AFGJ81q76a2Ttq2ly_CIgREmox9ZzoeBMyX_3ptNRxCvB0Kv02axSSxKIYSPgReM2O8gCglUrwkmKiISv5mNi_3xb8dmcMBZdA=s2560"
          height="70"
          alt="Logo DOubt IT"
          loading="lazy"
        />
      </a>

      <ul class="navbar-nav me-auto mb-2 mb-lg-0" v-if="$store.state.isLoggedIn">
        <li class="nav-item">
      <router-link style="text-decoration: none" to="/dashboard" v-if="$store.state.isLoggedIn"> Dashboard &nbsp;</router-link>
        </li>
        <li class="nav-item">
      <router-link style="text-decoration: none" to="/profile" v-if="$store.state.isLoggedIn"> Profile </router-link>
        </li>
      </ul>      

    </div>
      <div class="d-flex align-items-center">
        <p class="mr-3" v-if="$store.state.isLoggedIn">Logged in as <strong>{{profile.username}}</strong></p>

    <div v-if="$store.state.isLoggedIn">
      <a style="padding: 10px;">
        <img
          class="rounded-circle"
          id="profilepicture"
          height="80"
          alt="User profile picture"
          loading="lazy"
          :src="profilePictureURL"
          v-if="profilePictureURL"
        />
      </a>
    </div>

      <span style="display: inline">
      <router-link style="text-decoration: none;" to="/register" v-if="!$store.state.isLoggedIn && isLoginPage" v-slot="{ navigate }" > Don't Have a User? <button type="button" class="btn btn-outline-dark"
        @click="navigate"
        role="link"
      > Register a User </button>
      </router-link>

      <router-link style="text-decoration: none;" to="/login" v-if="!$store.state.isLoggedIn && isRegisterPage" v-slot="{ navigate }" > Already Have a User? <button type="button" class="btn btn-outline-dark"
        @click="navigate"
        role="link"
      > Login Here </button>
      </router-link>   

      <logout-button v-if="$store.state.isLoggedIn" type="button" class="btn btn-dark"></logout-button>
      </span> 
    </div>
  </div>
</nav>

    <router-view />
    <footer class="footer">
      <p> Copyright © Kim & Lea 2023 </p>
    </footer>
  </div>
</template>


<script>
import LogoutButton from './components/LogoutButton.vue';
import { mapState } from 'vuex';
import { getToken } from './utils/auth';


export default {
  data() {
    return {
      errorMessage: '',
      profile: {},
      profilePictureURL: '',
    };
  },
  components: {
  LogoutButton
  },
  computed: {
    ...mapState(['isLoggedIn']),
    ...mapState(['profileUpdated']),
    isLoginPage() {
      return this.$route.path === '/login';
    },
    isRegisterPage() {
      return this.$route.path === '/register';
    }
  },
  methods: {
    handleLogout() {
      this.$store.dispatch('logout');
    },
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
  }
  },
  watch: {
    profileUpdated(value) {
      if (value) {
        this.fetchProfile();
        this.$store.dispatch('setProfileUpdated', false);
      }
    },
    'isLoggedIn': {
      immediate: true,
      handler: function (newValue, oldValue) {
        // Only fetch profile when user has logged in, not when they've logged out
        if (newValue === true && oldValue === false) {
          this.fetchProfile();
        }
      }
    },
  },
  
  mounted() {
    this.fetchProfile();
  },
};
</script>



<style>
@import 'bootstrap/dist/css/bootstrap.css';

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  position: relative;
}

.error-message {
color: red;
}

.navbar {
  margin-bottom: 0px;
  background-color: #f1efef;
  border-bottom-style: solid ;
  border-width: 1px;
  border-color: rgba(120, 119, 119, 0.882);
}

.navbar-brand a {
  height: 40px;
  position: absolute;
  left: 50px;
  top: 30%;
}

#profilepicture {
  border: 2px solid rgb(85, 83, 83);
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}


.footer {
  position: fixed;
  bottom: 0;
  display: flex;
  justify-content: center;
  left: 0;
  align-items: center;
  width: 100%;
  height: 70px; 
  background-color: #f1efef;
  border-top-style: solid ;
  border-width: 1px;
  border-color: rgba(120, 119, 119, 0.882);
}
</style>
