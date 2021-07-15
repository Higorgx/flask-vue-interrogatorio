<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Interrogatório</h1>
        <hr>
        <h4>Você é um suspeito de um assasinato,</h4>
        <h4>responda as perguntas com sinceridade.</h4>
        <br>
        <button
        type="button"
        class="btn btn-primary"
        v-b-modal.book-update-modal
        @click="editBook(book)"
        >Iniciar</button>
      </div>
    </div>
    <b-modal ref="questionsModal"
            id="questions-modal"
            title="Perguntas"
            hide-footer>
          <b-form @submit="onDeleteBook" @reset="onResetDelete" class="w-100">
          <b-form-group id="form-title-edit-group"
                    label="Delete:"
                    label-for="form-title-edit-input">
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Sim</b-button>
          <b-button type="close" variant="danger">Não</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/perguntas';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
