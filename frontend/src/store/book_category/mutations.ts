import { IBookCategory } from '@/interfaces';
import { BookCategoryState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setBookCategories(state: BookCategoryState, payload: IBookCategory[]) {
        state.bookCategories = payload;
    },
    setBookCategory(state: BookCategoryState, payload: IBookCategory) {
        const bookCategories = state.bookCategories.filter((customer: IBookCategory) => customer.id !== payload.id);
        bookCategories.push(payload);
        state.bookCategories = bookCategories;
    },
};

const { commit } = getStoreAccessors<BookCategoryState, State>('');

export const commitSetBookCategory = commit(mutations.setBookCategory);
export const commitSetBookCategories = commit(mutations.setBookCategories);
