<template>
  <div>
    <h2>Estações</h2>
    <ul>
      <li v-for="station in stations" :key="station.id">
        {{ station.name }} - {{ station.location }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      stations: [],
    };
  },
  async created() {
    const response = await axios.get('/stations');
    this.stations = response.data;
  },
};
</script>
