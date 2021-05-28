import { mutations } from './mutations';
import { getters } from './getters';
import { actions } from './actions';
import { CustomerState } from './state';

const defaultState: CustomerState = {
  customers: [],
};

export const customerModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
