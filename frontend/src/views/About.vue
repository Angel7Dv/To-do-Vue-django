<template>
  <div class="home">
    <h1 class="title">Vuengo</h1>
  
    <p v-for="task in tasks" v-bind:key="task.id">{{task.id}} {{task.description}} : {{task.status}}</p>     

    <hr>

    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form v-on:submit.prevent="addTask">
          <h2 class="subtitle">Add task</h2>

          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <input class="input" type="text" v-model="description">
            </div>
          </div>

          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
                  <option value="todo">To do</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

  <!-- / las tareas  -->
    <div class="columns iten-center m-6" >
      <div class="column is-6">
        <h2 class="subtitle">To do</h2>

        <div class="todo">
          <div class="card" v-for="task in tasks" v-if="task.status === 'todo'" v-bind:key="task.id">
            <div class="card-content">{{ task.description }}</div>

            <footer class="card-footer">
              <a class="card-footer-item">Done</a>
            </footer>
          </div>
        </div>
      </div>
      <div class="column is-6">
        <h2 class="subtitle">Done</h2>

        <div class="done">
          <div class="card" v-for="task in tasks" v-if="task.status === 'done'" v-bind:key="task.id">
            <div class="card-content">{{ task.description }}</div>

            <footer class="card-footer">
              <a class="card-footer-item" >To do</a>
            </footer>
          </div>
        </div>
      </div>

      <!-- / -->
    </div>
  </div>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000/'
import axios from 'axios'
export default {
  name: 'Home',
  data () {
    return {
      tasks: [],
      description: '',
      status: 'todo'
    }
  },
  mounted () {
    this.getAPITasks()
  },
  methods: {
    getAPITasks() {
      axios({
        method: 'get',
        url: API_URL + 'tasks/',
      }).then(response => this.tasks = response.data)
    },
    
    

  }
}
</script>

<style lang="scss">
.select, select {
  width: 100%;
}
.card {
  margin-bottom: 20px;
}
.done {
  opacity: 0.3;
}
</style>