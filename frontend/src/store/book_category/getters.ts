import { BookCategoryState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    BookCategories: (state: BookCategoryState) => state.bookCategories,
    OneBookCategory: (state: BookCategoryState) => (id: number) => {
        const filteredBookCategories = state.bookCategories.filter((bookCategory) => bookCategory.id === id);
        if (filteredBookCategories.length > 0) {
            return { ...filteredBookCategories[0] };
        }
    },
};

const { read } = getStoreAccessors<BookCategoryState, State>('');

export const readOneBookCategory = read(getters.OneBookCategory);
export const readBookCategories = read(getters.BookCategories);
