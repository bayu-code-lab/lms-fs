import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);

export default new Vuetify({
    dark: false, // it's decide your project
    themes: {
        light: {
            prime: '#df8421',
        },
        dark: {
            prime: '#333',
        },
    },
    icons: {
        iconfont: 'md',
    },
});
