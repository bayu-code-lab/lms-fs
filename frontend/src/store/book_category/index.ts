import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { BookCategoryState } from './state';

const defaultState: BookCategoryState = {
  bookCategories: [],
};

export const BookCategoryModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
