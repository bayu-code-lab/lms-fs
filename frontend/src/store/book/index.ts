import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { BookState } from './state';

const defaultState: BookState = {
  books: [],
};

export const BookModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
