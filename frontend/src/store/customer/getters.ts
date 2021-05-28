import { CustomerState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    Customers: (state: CustomerState) => state.customers,
    OneCustomer: (state: CustomerState) => (id: number) => {
        const filteredCustomers = state.customers.filter((customer) => customer.id === id);
        if (filteredCustomers.length > 0) {
            return { ...filteredCustomers[0] };
        }
    },
};

const { read } = getStoreAccessors<CustomerState, State>('');

export const readOneCustomer = read(getters.OneCustomer);
export const readCustomers = read(getters.Customers);
