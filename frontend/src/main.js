import { createApp } from 'vue'
import App from './App.vue'
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import router from "@/router/router";
import axios from "axios";
import VueAxios from "vue-axios";
const app = createApp(App);
app
    .use(router,axios,VueAxios, BootstrapVue3)
    .mount('#app');


