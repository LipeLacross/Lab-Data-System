<template>
  <div>
    <h2>Inserir Dados</h2>
    <form @submit.prevent="submitData">
      <input v-model="dbo" type="number" placeholder="DBO" required />
      <input v-model="dqo" type="number" placeholder="DQO" required />
      <input v-model="ph" type="number" placeholder="pH" required />
      <button type="submit">Enviar</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      dbo: '',
      dqo: '',
      ph: '',
    };
  },
  methods: {
    async submitData() {
      try {
        await axios.post('/analyses', {
          dbo: this.dbo,
          dqo: this.dqo,
          ph: this.ph,
        });
        alert('Dados enviados com sucesso!');
      } catch (error) {
        console.error('Erro ao enviar dados', error);
      }
    },
  },
};
</script>
