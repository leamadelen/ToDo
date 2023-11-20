<template>
   <div class="container-fluid">
      <div class="row" style="height: 100vh;">
        <div class="col-md-4" id="colorcategory">
          <div class="d-flex justify-content-center-end">
            <span>
                <h8 class="p-2"> New Category </h8>
                <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#Categorymodal">
                <i class="bi bi-folder-plus" style="font-size: 35px;"></i>
                </button>
            </span>
          </div>

      <div class="modal fade" id="Categorymodal" tabindex="-1" aria-labelledby="ModalCat" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="ModalCat">Create New Category</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <form @submit.prevent="onSubmitCategory">
                <label for="categoryName"> Name </label>
                <input id="categoryName" v-model="categoryName" required>
                <button type="submit" class="btn btn-outline-dark"> Create </button>
              </form>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div v-for="category in categories" :key="category.id" class="col-lg-6">
          <div class="mb-2" id="categoryborder">
            <h4>{{ category.name }}</h4>
      
            <button type="button" class="btn btn-outline-dark" @click="deleteCategory(category.id)">
              <i class="bi bi-trash"></i>
            </button>
            <button type="button" class="btn btn-outline-dark" data-bs-toggle="modal" :data-bs-target="'#updateModal' + category.id">
              <i class="bi bi-pencil-square"></i>
            </button>

            <div class="modal fade" :id="'updateModal' + category.id" tabindex="-1" :aria-labelledby="'updateModalLabel' + category.id" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" :id="'updateModalLabel' + category.id">Update ToDo</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <form @submit.prevent="updateCategory(category)">
                      <label for="updateCategory"> Name </label>
                      <input :id="'updateCategory' + category.id" v-model="category.name" required>
                      <button type="submit" class="btn btn-outline-dark">Update </button>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
    </div>
  </div>
      
  <div class="col-md-8" id="colortodos" style="height: 100vh;">
    <div class="d-flex justify-content-between align-items-center mb-5">
      <span class="d-flex justify-content-center-end mt-2 ">
        <h3 class="justify-content-center px-2">Your ToDo's</h3>
        <button type="button" class="btn btn-success pb-2" data-bs-toggle="modal" data-bs-target="#todoModal">
        New ToDo
        </button>
      </span>

    <div>
      <h6 class="mr-2 inline">Sort by </h6>
      <select v-model="$store.state.sortOrder" @change="sortTodos($event.target.value)">
        <option value="createdAt">Date Added</option>
        <option value="-createdAt">Date Added (Reverse)</option>
        <option value="task">Alphabetical Order (A-Z)</option>
        <option value="-task">Alphabetical Order (Z-A)</option>
        <option value="priority">Priority</option>
        <option value="-priority">Priority (Reverse)</option>
        <option value="due_date">Due Date</option>
        <option value="-due_date">Due Date (Reverse)</option>
        <option value="category">Category</option>
      </select>
    </div>
  </div>

  <div class="modal fade" id="todoModal" tabindex="-1" aria-labelledby="todoModall" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="todoModall">Submit</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        
        <form @submit.prevent="formTodo.id ? updateTodo(formTodo) : addTodo()">
          <div class="modal-body">
            <div class="mb-3">
              <label> Name </label>
              <input type="text" class="form-control" v-model="formTodo.task" placeholder="Taskname" required>
            </div>

            <div class="mb-3">
              <label >Priority</label>
              <select class="form-control" v-model="formTodo.priority" required>
                <option value="" disabled selected>Please select a priority</option>
                <option value="1">!!! (High)</option>
                <option value="2">!! (Medium)</option>
                <option value="3">! (Low)</option>
              </select>
            </div>

            <div class="mb-3">
              <label> Due Date </label>
              <input type="datetime-local" class="form-control" v-model="formTodo.due_date" placeholder="Add due date">
            </div>
            <div class="mb-3">
                <label> Choose Category </label>
                  <select class="form-control" v-model="formTodo.category_id">
                  <option disabled value="">Please select a category</option>
                  <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
                </select>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
        </form>
      </div>
    </div>
  </div>

<div class="d-flex align-items-center">
  <ul style="width: 100%; margin: 0; padding: 0;">
    <li v-for="todo in todos" :key="todo.id" id="todosdisplayed" class="d-flex justify-content-between align-items-center">
      <div>
        <span>
          <input type="checkbox" style="height: 30px; margin-right: 5px;" v-model="todo.completed" @change="updateTodo(todo)" />
          <span style="color: red;">
            {{ convertPriorityToString(todo.priority) }}
          </span>
        </span>
      </div>
      <div>
        <span :style="todo.completed ? { textDecoration: 'line-through', color: 'grey' } : {}">
          {{ todo.task }} &nbsp;
        </span>
        <span v-if="todo.due_date" style="font-style: italic;"> Time left: {{ getTimeLeft(todo.due_date) }} &nbsp;</span>
        <span v-if="todo.category_id" id="categoryupper">
          <i class="bi bi-list-task"> </i>
          {{ categories.find(category => category.id === todo.category_id)?.name || 'No category' }}
        </span>
      </div>
      <div>
        <button @click="editTodo(todo)" data-bs-toggle="modal" data-bs-target="#todoModal" class="btn btn-outline-success btn-sm"><i class="bi bi-pencil"></i></button>
        <button @click="deleteTodo(todo)" class="btn btn-outline-danger btn-sm"><i class="bi bi-trash"></i></button>
      </div>
    </li>
  </ul>
</div>
<div v-if="errorMessage" class="error-message">
  {{ errorMessage }}
</div>
</div>
</div>
</div>
</template>


<script>
import { getToken } from '../utils/auth';
import { mapState } from 'vuex';


export default {
  data() {
    return {
      todos: [],
      formTodo: {},
      categoryName: '',
      categories: [],
      errorMessage: '',
      profile: {},
      profilePictureURL: '',
      isTodoModalOpen: false,
    };
  },
   computed: {
    ...mapState(['isLoggedIn'])
  },
  methods: {
    onSubmitCategory() {
      this.$axios.post('/categories', {
        name: this.categoryName,
      }, {
        headers: {
          Authorization: `Bearer ${getToken()}`
        }
      })
      .then(response => {
        this.categories.push(response.data)
        this.categoryName = ''
      })
      .catch(error => {
        console.error(error)
      })
    },
    fetchCategories() {
      this.$axios.get('/categories', {
        headers: {
          Authorization: `Bearer ${getToken()}`
        }
      })
      .then(response => {
        this.categories = response.data
      })
      .catch(error => {
        console.error(error)
      })
    },
    fetchCategory(categoryId) {
    this.$axios.get(`/categories/${categoryId}`, {
      headers: {
        Authorization: `Bearer ${getToken()}`
      }
    })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.error(error);
    })
  },

  updateCategory(category) {
    this.$axios.put(`/categories/${category.id}`, {
      name: category.name
    }, {
      headers: {
        Authorization: `Bearer ${getToken()}`
      }
    })
    .then(response => {
      console.log(response.data);
      this.fetchCategories();
    })
    .catch(error => {
      console.error(error);
    })
  },

  deleteCategory(categoryId) {
    this.$axios.delete(`/categories/${categoryId}`, {
      headers: {
        Authorization: `Bearer ${getToken()}`
      }
    })
    .then(response => {
      console.log(response.data);
      this.fetchCategories();
    })
    .catch(error => {
      console.error(error);
    })
  },
    getTimeLeft(due_date) {
        const now = new Date();
        const due = new Date(due_date);
        const diffMs = due - now; 

        if (diffMs < 0) {
        return 'Past Due';
        }

        const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24)); // days
        const diffHours = Math.floor((diffMs % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)); // hours
        const diffMinutes = Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60)); // minutes
        const diffSeconds = Math.floor((diffMs % (1000 * 60)) / 1000); // seconds

        return `${diffDays}d ${diffHours}h ${diffMinutes}m ${diffSeconds}s`;
    },
    convertPriorityToString(priority) {
        const priorityMap = {
        1: '!!!',
        2: '!!',
        3: '!',
        };
        return priorityMap[priority] || 'Unknown';
    },
    fetchTodos() {
      const sortOrder = this.$store.state.sortOrder;
      this.$axios.get('/todos', {
        headers: {
          Authorization: `Bearer ${getToken()}`
        },
        params: {
          sort: sortOrder
        }
      })
      .then(response => {
        this.todos = response.data;
      })
      .catch(error => {
        this.errorMessage = error.response ? error.response.data.message : 'Server did not respond. Please try again later.';
        console.error(error);
      });
    },
    sortTodos(sortType) {
      this.$store.commit('setSortOrder', sortType);

      this.fetchTodos();
    },
    addTodo() {
      this.$axios.post('/todos', {
            task: this.formTodo.task,
            priority: parseInt(this.formTodo.priority),
            due_date: this.formTodo.due_date,
            category_id: this.formTodo.category_id
        }, {
        headers: {
          Authorization: `Bearer ${getToken()}`
        }
      })
      .then(() => {
        this.fetchTodos();
        this.formTodo = {};
      })
      .catch(error => {
        this.errorMessage = error.response ? error.response.data.message : 'Server did not respond. Please try again later.';
        console.error(error);
      });
    },
    updateTodo(todo) {
      this.$axios.put(`/todos/${todo.id}`, {
            task: todo.task,
            completed: todo.completed,
            priority: parseInt(todo.priority),
            due_date: todo.due_date,
            category_id: this.formTodo.category_id
       }, {
        headers: {
          Authorization: `Bearer ${getToken()}`
        }
      })
      .then(() => {
        this.fetchTodos();
        this.formTodo = {};
      })
      .catch(error => {
        this.errorMessage = error.response ? error.response.data.message : 'Server did not respond. Please try again later.';
        console.error(error);
      });
    },
    deleteTodo(todo) {
      this.$axios.delete(`/todos/${todo.id}`, {
        headers: {
          Authorization: `Bearer ${getToken()}`
        }
      })
      .then(() => {
        this.fetchTodos();
        if (this.formTodo.id === todo.id) {
          this.formTodo = {};
        }
      })
      .catch(error => {
        this.errorMessage = error.response ? error.response.data.message : 'Server did not respond. Please try again later.';
        console.error(error);
      });
    },
    editTodo(todo) {
      this.formTodo = {...todo};      
    },
    handleLogout() {
      this.$store.dispatch('logout');
    }
  },
  created() {
    this.sortOrder = this.$store.state.sortOrder;
    this.fetchTodos();
    this.fetchCategories();
  },

};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Koulen&display=swap');


.nav-item {
  text-decoration: none;
}

#categoryborder {
  border-radius: 35px;
  background-color: #afc6c786;
  padding: 20px; 
  width: 200px;
  height: 150px; 
}

ul {
  list-style-type: none;
  width: 100%;
  
}

#categoryupper {
  font-family: 'Koulen', sans-serif;
}

#todosdisplayed {
  font-size: 18px;
  border-bottom: 1px solid #a6a6a686;
}

.container {
  position: relative;
  min-height: 100vh; 
}

#colortodos {
    background-color: rgb(250, 250, 250);
}

.content {
  padding-bottom: 60px; 
}

.inline {
    display: inline;
  }

#colorcategory {
  background-color: rgb(200, 216, 215);
}

h4, h8 {
  font-family: 'Koulen', sans-serif;
}

</style>
