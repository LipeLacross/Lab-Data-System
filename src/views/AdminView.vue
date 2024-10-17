<template>
  <div>
    <h1>Admin Dashboard</h1>
    <station-list />
    <data-form />
  </div>
</template>

<script>
import StationList from '../components/StationList.vue';
import DataForm from '../components/DataForm.vue';

export default {
  components: {
    StationList,
    DataForm,
  },
};
</script>
