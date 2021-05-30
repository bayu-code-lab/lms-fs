import { api } from '@/api';
import { ActionContext } from 'vuex';
import { IBookCategoryUpdate, IBookCategoryCreate } from '@/interfaces';
import { State } from '../state';
import { BookCategoryState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { commitSetBookCategories, commitSetBookCategory } from './mutations';
import { dispatchCheckApiError } from '../main/actions';
import { commitAddNotification, commitRemoveNotification } from '../main/mutations';

type MainContext = ActionContext<BookCategoryState, State>;

export const actions = {
    async actionGetBookCategories(context: MainContext) {
        try {
            const response = await api.getBookCategories(context.rootState.main.token);
            if (response) {
                commitSetBookCategories(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateBookCategory(context: MainContext, payload: { id: number, book_category: IBookCategoryUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateBookCategories(context.rootState.main.token, payload.id, payload.book_category),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetBookCategory(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Book Category successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateBookCategory(context: MainContext, payload: IBookCategoryCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createBookCategories(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetBookCategory(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Book Category successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionDeleteBookCategory(context: MainContext, payload: { id: number}) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.deleteBookCategories(context.rootState.main.token, payload.id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetBookCategory(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Book Category successfully deleted', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
};

const { dispatch } = getStoreAccessors<BookCategoryState, State>('');

export const dispatchCreateBookCategory = dispatch(actions.actionCreateBookCategory);
export const dispatchGetBookCategory = dispatch(actions.actionGetBookCategories);
export const dispatchUpdateBookCategory = dispatch(actions.actionUpdateBookCategory);
export const dispatchDeleteBookCategory = dispatch(actions.actionDeleteBookCategory);
