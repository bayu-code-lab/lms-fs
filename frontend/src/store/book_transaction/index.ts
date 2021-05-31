import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { BookTransactionState } from './state';

const defaultState: BookTransactionState = {
  bookTransactions: [],
};

export const BookTransactionModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
