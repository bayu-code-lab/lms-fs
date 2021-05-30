import { BookState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    Books: (state: BookState) => state.books,
    OneBook: (state: BookState) => (id: number) => {
        const filteredBooks = state.books.filter((book) => book.id === id);
        if (filteredBooks.length > 0) {
            return { ...filteredBooks[0] };
        }
    },
};

const { read } = getStoreAccessors<BookState, State>('');

export const readOneBook = read(getters.OneBook);
export const readBooks = read(getters.Books);
