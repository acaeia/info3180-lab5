<script setup>
import {ref, onMounted} from 'vue'
let movies = ref([])

function fetchMovies() {
    fetch('/api/v1/movies')
        .then(response => response.json())
        .then(data => {
            movies.value = data.movies;
        });
}

onMounted(() => {
    fetchMovies();
});
</script>

<template>
  <div class="container mt-4">
    <h1 class="mb-4">Movies</h1>
    <div class="row row-cols-1 row-cols-md-2 g-4">
      <div class="col-12" v-for="movie in movies" :key="movie.id">
        <div class="card h-100">
          <div class="row g-0">
            <div class="col-md-3">
              <img :src="movie.poster" class="img-fluid rounded-start h-100" alt="Movie Poster" style="height: 250px; object-fit: cover;">
            </div>
            <div class="col-md-9">
              <div class="card-body">
                <h5 class="card-title">{{ movie.title }}</h5>
                <p class="card-text">{{ movie.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>