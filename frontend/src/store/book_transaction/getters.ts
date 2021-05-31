import { BookTransactionState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    BookTransactions: (state: BookTransactionState) => state.bookTransactions,
    OneBookTransaction: (state: BookTransactionState) => (id: number) => {
        const filteredBookTransactions = state.bookTransactions.filter((bookTransaction) => bookTransaction.id === id);
        if (filteredBookTransactions.length > 0) {
            return { ...filteredBookTransactions[0] };
        }
    },
};

const { read } = getStoreAccessors<BookTransactionState, State>('');

export const readOneBookTransaction = read(getters.OneBookTransaction);
export const readBookTransactions = read(getters.BookTransactions);
