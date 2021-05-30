import { api } from '@/api';
import { ActionContext } from 'vuex';
import { IBookUpdate, IBookCreate } from '@/interfaces';
import { State } from '../state';
import { BookState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { commitSetBooks, commitSetBook } from './mutations';
import { dispatchCheckApiError } from '../main/actions';
import { commitAddNotification, commitRemoveNotification } from '../main/mutations';

type MainContext = ActionContext<BookState, State>;

export const actions = {
    async actionGetBooks(context: MainContext) {
        try {
            const response = await api.getBooks(context.rootState.main.token);
            if (response) {
                commitSetBooks(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateBook(context: MainContext, payload: { id: number, book_: IBookUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateBooks(context.rootState.main.token, payload.id, payload.book_),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetBook(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Book  successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateBook(context: MainContext, payload: IBookCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createBooks(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetBook(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Book  successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionDeleteBook(context: MainContext, payload: { id: number}) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.deleteBooks(context.rootState.main.token, payload.id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetBook(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Book  successfully deleted', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
};

const { dispatch } = getStoreAccessors<BookState, State>('');

export const dispatchCreateBook = dispatch(actions.actionCreateBook);
export const dispatchGetBook = dispatch(actions.actionGetBooks);
export const dispatchUpdateBook = dispatch(actions.actionUpdateBook);
export const dispatchDeleteBook = dispatch(actions.actionDeleteBook);
