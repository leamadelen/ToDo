<template>

  <section class="vh-100 bg-image" style="background-image: 
  url('https://images.unsplash.com/photo-1570301920589-13a3c0beb04b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2067&q=80');">
  <!-- Photo by <a href="https://unsplash.com/pt-br/@luismisanchez?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Luismi Sánchez</a> on <a href="https://unsplash.com/photos/HYRbs2k30IE?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> -->
  
  <div class="mask d-flex align-items-center h-100 py-5 gradient-custom-3">
    <div class="container h-100">
      <div class="row d-flex justify-content-center align-items-ld-center py-5 h-100">
        <div class="col-12 col-md-9 col-lg-7 col-xl-6">
          <div class="card" style="border-radius: 15px;">
            <div class="card-body p-5">
              <h2 class="text text-center mb-5">Create an Account</h2>

              <form @submit.prevent="registerUser">
                <div class="form-outline mb-4">
                  <label class="form-label" for="form3Example1cg">Username</label>
                  <input type="text" id="username" class="form-control form-control-lg" v-model="username" required />
                  <div v-if="usernameError" class="alert alert-danger">
                     {{ usernameError }}
                   </div>
                </div >

                <div class="form-outline mb-4">
                  <label class="form-label" for="form3Example4cg">Password</label>
                  <input type="password" id="password" class="form-control form-control-lg"  v-model="password" required />
                  <div v-if="passwordError" class="alert alert-danger">
                     {{ passwordError }}
                   </div>
                </div>

                <div v-if="errorMessage" class="alert alert-danger">
                  {{ errorMessage }}
                </div>

                <div class="d-flex justify-content-center">
                  <button type="submit"
                    class="btn btn-success btn-block text-body" >Register</button>
                </div>

              </form>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>


<script>

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
      usernameError: '',
      passwordError: ''
    };
  },
  methods: {
    registerUser() {
      if (!this.validateUsername() || !this.validatePassword()) {
        return;
      }
      this.$axios.post('/register', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        console.log(response.data.message);
        this.$router.push('/login');
      })
      .catch(error => {
        if (error.response) {
          console.log(error.response.data);
          console.log(error.response.status);
          console.log(error.response.headers);
          this.errorMessage = error.response.data.message;
        } else if (error.request) {
          console.log(error.request);
        } else {
          console.log('Error', error.message);
        }
      });
    },
    validateUsername() {
      if (this.username.length < 3) {
        this.usernameError = 'Username must be at least 3 characters.';
        return false;
      }
      this.usernameError = '';
      return true;
    },
    validatePassword() {
      if (!/\d/.test(this.password)) {
        this.passwordError = 'Password must contain at least one number.';
        return false;
      }
      this.passwordError = '';
      return true;
    }
  }
};
</script>

<style scoped>

.btn {
  background-color: #559c9c5a;
  border-color: #559c9c5a;
}

</style>
