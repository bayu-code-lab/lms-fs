import { IBook } from '@/interfaces';
import { BookState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setBooks(state: BookState, payload: IBook[]) {
        state.books = payload;
    },
    setBook(state: BookState, payload: IBook) {
        const books = state.books.filter((customer: IBook) => customer.id !== payload.id);
        books.push(payload);
        state.books = books;
    },
};

const { commit } = getStoreAccessors<BookState, State>('');

export const commitSetBook = commit(mutations.setBook);
export const commitSetBooks = commit(mutations.setBooks);
