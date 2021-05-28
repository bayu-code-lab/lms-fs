import { ICustomer } from '@/interfaces';
import { CustomerState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setCustomers(state: CustomerState, payload: ICustomer[]) {
        state.customers = payload;
    },
    setCustomer(state: CustomerState, payload: ICustomer) {
        const customers = state.customers.filter((customer: ICustomer) => customer.id !== payload.id);
        customers.push(payload);
        state.customers = customers;
    },
};

const { commit } = getStoreAccessors<CustomerState, State>('');

export const commitSetCustomer = commit(mutations.setCustomer);
export const commitSetCustomers = commit(mutations.setCustomers);
