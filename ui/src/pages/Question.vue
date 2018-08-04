<template>
  <div>
    <div class="question" v-if="loaded">
      <div class="card">
        <div class="card-content">
          <p class="title">
            {{ question.title }}
          </p>
          <p class="subtitle">
            {{ question.user.username }}
          </p>
        </div>
        <footer class="card-footer">
        </footer>
      </div>
      <div class="box" v-for="(answer, i) in question.answers" :key=i>
        <div class="media">
          <div class="media-content">
            <div class="content">
              <p>
                <strong>{{ answer.user.username }}</strong>
                <br>
                {{ answer.body }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="notFound">
      Question not found!
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        question: null,
        loaded: false,
        notFound: false,
      }
    },
    async created() {
      this.loaded = false

      try {
        const response = await this.axios.get(`question/${this.$route.params.pk}`)
        this.question = response.data
        this.loaded = true

      } catch (error) {
        this.notFound = true
      }
    }
  }
</script>

<style lang="scss" scoped>
  .box, .card {
    margin: 1em 2em;
  }
</style>