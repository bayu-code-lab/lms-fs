import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';

import { mainModule } from './main';
import { State } from './state';
import { adminModule } from './admin';
import { customerModule } from './customer';
import { BookCategoryModule } from './book_category';
import { BookModule } from './book';
import { BookTransactionModule } from './book_transaction';

Vue.use(Vuex);

const storeOptions: StoreOptions<State> = {
  modules: {
    main: mainModule,
    admin: adminModule,
    customer: customerModule,
    book_category: BookCategoryModule,
    book: BookModule,
    book_transaction: BookTransactionModule,
  },
};

export const store = new Vuex.Store<State>(storeOptions);

export default store;
