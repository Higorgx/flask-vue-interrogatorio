<template>
  <div class="container">
    <div class="row">
      <div v-if="this.questStart===false" class="container my-5">
        <h1>Interrogatório</h1>
        <hr>
        <h4>Você é um suspeito de um assasinato,</h4>
        <h4>responda as perguntas com sinceridade.</h4>
        <br>
        <button
        type="button"
        class="btn btn-primary"
        v-on:click.stop.prevent = startQuest
        >Iniciar</button>
      </div>
       <div v-if="this.questStart && this.questFinish == false" class="container my-5">
       <div class="col-8">
                <h1>Questão {{this.index + 1}}</h1>
                <h2 class="text-center mt-5">{{questions[index].question}}</h2>
                <div class="float-right">
                    <button type="button"
                    class="btn btn-success
                    mt-5 mr-3 btn-lg"
                    v-on:click.stop.prevent = getAnswerYes
                    >Sim</button>
                    <button type="button"
                    class="btn btn-danger
                    mt-5 mr-2 btn-lg"
                    v-on:click.stop.prevent = getAnswerNo
                    >Não</button>
                </div>
            </div>
       </div>
    </div>
     <div v-if="this.questFinish" class="container mt-5 text-center">
        <h1>Resultado</h1>
        <h2 class="mt-5">{{result}}</h2>
        <button
        type="button"
        class="btn btn-primary mt-4 btn-lg"
        v-on:click.stop.prevent = resetQuest
        >Reiniciar</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      questStart: false,
      questFinish: false,
      index: 0,
      questions: [],
      questionsId: '',
      result: '',
      answers: [],
      histAnswes: [],
      BookForm: {
        id: 'Null',
        question: '',
        answer: false,
      },
    };
  },
  methods: {
    startQuest() {
      this.questStart = true;
    },
    nextQuest() {
      this.index += 1;
      if (this.index === 5) {
        this.questFinished();
      }
    },
    getAnswerYes() {
      this.answers.push('sim');
      console.log(this.answers);
      this.nextQuest();
    },
    getAnswerNo() {
      this.answers.push('nao');
      console.log(this.answers);
      this.nextQuest();
    },
    questFinished() {
      this.questFinish = true;
      this.questResult();
    },
    resetQuest() {
      this.questStart = false;
      this.questFinish = false;
      this.index = 0;
      for (let i = this.answers.length; i > 0; i -= 1) {
        this.answers.pop();
      }
    },
    getQuestions() {
      const path = 'http://localhost:5000/perguntas';
      axios.get(path)
        .then((res) => {
          this.questions = res.data.questions;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onShowQuestion(questionsId) {
      this.questionsId = questionsId;
      this.$bvModal.show('modal-question');
    },
    onClose() {
      this.$bvModal.show('modal-question');
    },
    questResult() {
      const path = 'http://localhost:5000/result';
      const payload = {
        questions: this.questions,
        answers: this.answers,
      };
      axios.post(path, payload)
        .then((res) => {
          this.result = res.data.result;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getResults() {
      const path = 'http://localhost:5000/result';
      axios.get(path)
        .then((res) => {
          this.histAnswes = res.data.result;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

  },
  created() {
    this.getQuestions();
  },
};
</script>
