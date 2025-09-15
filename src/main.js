import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import CorpusSection from './components/CorpusSection.vue'

const app = createApp(App)
// app.component('CorpusSection', CorpusSection)
app.mount('#app')
