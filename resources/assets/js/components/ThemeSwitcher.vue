<template>
  <div @click="switchTheme">
    <div v-if="dark" class="flex-center">
      <svg
        width="1em"
        height="1em"
        viewBox="0 0 16 16"
        class="bi bi-sun"
        fill="currentColor"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path d="M3.5 8a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0z" />
        <path
          fill-rule="evenodd"
          d="M8.202.28a.25.25 0 0 0-.404 0l-.91 1.255a.25.25 0 0 1-.334.067L5.232.79a.25.25 0 0 0-.374.155l-.36 1.508a.25.25 0 0 1-.282.19l-1.532-.245a.25.25 0 0 0-.286.286l.244 1.532a.25.25 0 0 1-.189.282l-1.509.36a.25.25 0 0 0-.154.374l.812 1.322a.25.25 0 0 1-.067.333l-1.256.91a.25.25 0 0 0 0 .405l1.256.91a.25.25 0 0 1 .067.334L.79 10.768a.25.25 0 0 0 .154.374l1.51.36a.25.25 0 0 1 .188.282l-.244 1.532a.25.25 0 0 0 .286.286l1.532-.244a.25.25 0 0 1 .282.189l.36 1.508a.25.25 0 0 0 .374.155l1.322-.812a.25.25 0 0 1 .333.067l.91 1.256a.25.25 0 0 0 .405 0l.91-1.256a.25.25 0 0 1 .334-.067l1.322.812a.25.25 0 0 0 .374-.155l.36-1.508a.25.25 0 0 1 .282-.19l1.532.245a.25.25 0 0 0 .286-.286l-.244-1.532a.25.25 0 0 1 .189-.282l1.508-.36a.25.25 0 0 0 .155-.374l-.812-1.322a.25.25 0 0 1 .067-.333l1.256-.91a.25.25 0 0 0 0-.405l-1.256-.91a.25.25 0 0 1-.067-.334l.812-1.322a.25.25 0 0 0-.155-.374l-1.508-.36a.25.25 0 0 1-.19-.282l.245-1.532a.25.25 0 0 0-.286-.286l-1.532.244a.25.25 0 0 1-.282-.189l-.36-1.508a.25.25 0 0 0-.374-.155l-1.322.812a.25.25 0 0 1-.333-.067L8.203.28zM8 2.5a5.5 5.5 0 1 0 0 11 5.5 5.5 0 0 0 0-11z"
        />
      </svg>
    </div>
    <div v-else class="flex-center">
      <svg
        width="1em"
        height="1em"
        viewBox="0 0 16 16"
        class="bi bi-moon"
        fill="currentColor"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill-rule="evenodd"
          d="M14.53 10.53a7 7 0 0 1-9.058-9.058A7.003 7.003 0 0 0 8 15a7.002 7.002 0 0 0 6.53-4.47z"
        />
      </svg>
    </div>
  </div>
</template>

<script>
import { EventBus } from "./EventBus";
export default {
  props: {
    theme: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      dark: false,
    };
  },
  mounted() {
    console.log(EventBus);
    EventBus.$on("theme-default", (def) => {
      console.log("theme-default event", def);
      this.dark = def;
    });
    window
      .matchMedia("(prefers-color-scheme: dark)")
      .addEventListener("change", (e) => {
        this.setTheme(e.matches);
      });
  },

  methods: {
    setTheme(force) {
      console.log(force);
      this.dark = force;
      EventBus.$emit("theme", this.dark);
    },
    switchTheme() {
      axios
        .post("/theme", { mode: this.dark ? "light" : "dark" })
        .then((res) => {
          this.dark = !this.dark;
          EventBus.$emit("theme", this.dark);
        });
    },
  },
};
</script>

<style>
</style>