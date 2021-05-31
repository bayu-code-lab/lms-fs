import { IBookTransaction } from '@/interfaces';
import { BookTransactionState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setBookTransactions(state: BookTransactionState, payload: IBookTransaction[]) {
        state.bookTransactions = payload;
    },
    setBookTransaction(state: BookTransactionState, payload: IBookTransaction) {
        const bookTransactions = state.bookTransactions.filter((customer: IBookTransaction) => customer.id !== payload.id);
        bookTransactions.push(payload);
        state.bookTransactions = bookTransactions;
    },
};

const { commit } = getStoreAccessors<BookTransactionState, State>('');

export const commitSetBookTransaction = commit(mutations.setBookTransaction);
export const commitSetBookTransactions = commit(mutations.setBookTransactions);
