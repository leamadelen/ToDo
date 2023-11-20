<template>
<section class="vh-100 bg-image my-0 py-0" style="background-image: 
  url('https://images.unsplash.com/photo-1570301920589-13a3c0beb04b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2067&q=80');">
  <!-- Photo by <a href="https://unsplash.com/pt-br/@luismisanchez?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Luismi Sánchez</a> on <a href="https://unsplash.com/photos/HYRbs2k30IE?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> -->
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-ld-center py-5 h-100">
      <div class="col-xl-10">
        <div class="card rounded-3 text-black">
          <div class="row g-0">
            <div class="col-lg-6">
              <div class="card-body p-md-5 mx-md-4">

                <form @submit.prevent="loginUser">
                  <h2 class="pb-4"> Login to Your Account</h2>

                  <div class="mb-4 d-flex flex-column align-items-start">
                     <label class="form-label">Username</label>
                    <input type="text"  class="form-control" v-model="username" required/>
                   
                  </div>

                  <div class="mb-4 d-flex flex-column align-items-start">
                    <label class="form-label" >Password</label>
                    <input type="password" class="form-control" v-model="password" required/>
                    
                  </div>
                  <div v-if="errorMessage" class="alert alert-danger">
                    {{ errorMessage }}
                  </div>

                  <div class="text-center pt-1 mb-5 pb-1">
                    <button class="btn btn-outline-dark btn-block fa-lg gradient-custom-2 mb-3" type="submit">Log
                      in</button>
                  </div>

                </form>

              </div>
            </div>
            <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
              <div class="text-black px-3 py-4 p-md-5 mx-md-4">
                <h4 class="mb-4">Get your ToDo's done in time</h4>
                <p class="small mb-0">Never doubt doing a ToDo.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import store from '../store';


export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    loginUser() {
      this.$axios.post('/login', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        const token = response.data.access_token;
        localStorage.setItem('token', token);
        this.$store.commit('login');
        store.commit('setUsername', this.username);
        this.$router.push('/dashboard');
      })
      .catch(error => {
        console.error(error);
        if (error.response) {
          this.errorMessage = error.response.data.message;
        } else if (error.request) {
          this.errorMessage = 'Server did not respond. Please try again later.';
        } else {
          this.errorMessage = 'An error occurred. Please try again later.';
        }
      });
    }
  }
};
</script>

<style scoped>
.form-label {
  text-align: left;
}

.text-left {
  text-align: left;
}

.container {
  position: relative;
  min-height: 100vh; 
}

.content {
  padding-bottom: 60px; 
}

section {
  background-color: aqua;
}

.btn {
  background-color: #559c9c5a;
  border-color: #559c9c5a;
}


</style>
