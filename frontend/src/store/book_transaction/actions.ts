import { api } from '@/api';
import { ActionContext } from 'vuex';
import { IBookTransactionCreate } from '@/interfaces';
import { State } from '../state';
import { BookTransactionState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { commitSetBookTransactions, commitSetBookTransaction } from './mutations';
import { dispatchCheckApiError } from '../main/actions';
import { commitAddNotification, commitRemoveNotification } from '../main/mutations';

type MainContext = ActionContext<BookTransactionState, State>;

export const actions = {
    
    // async actionUpdateBookTransaction(context: MainContext, payload: { id: number}) {
    //     try {
    //         const loadingNotification = { content: 'saving', showProgress: true };
    //         commitAddNotification(context, loadingNotification);
    //         const response = (await Promise.all([
    //             api.returningBooks(context.rootState.main.token, payload.id),
    //             await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
    //         ]))[0];
    //         commitSetBookTransaction(context, response.data);
    //         commitRemoveNotification(context, loadingNotification);
    //         commitAddNotification(context, { content: 'book has been returned', color: 'success' });
    //     } catch (error) {
    //         await dispatchCheckApiError(context, error);
    //     }
    // },
    async actionGetBookTransactions(context: MainContext) {
        try {
            const response = await api.getBookTransactions(context.rootState.main.token);
            if (response) {
                commitSetBookTransactions(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateBookTransaction(context: MainContext, payload: IBookTransactionCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.borrowBooks(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetBookTransaction(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Book Transaction successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    // async actionDeleteBookCategory(context: MainContext, payload: { id: number}) {
    //     try {
    //         const loadingNotification = { content: 'saving', showProgress: true };
    //         commitAddNotification(context, loadingNotification);
    //         const response = (await Promise.all([
    //             api.deleteBookTransactions(context.rootState.main.token, payload.id),
    //             await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
    //         ]))[0];
    //         commitSetBookCategory(context, response.data);
    //         commitRemoveNotification(context, loadingNotification);
    //         commitAddNotification(context, { content: 'Book Category successfully deleted', color: 'success' });
    //     } catch (error) {
    //         await dispatchCheckApiError(context, error);
    //     }
    // },
};

const { dispatch } = getStoreAccessors<BookTransactionState, State>('');

export const dispatchCreateBookTransaction = dispatch(actions.actionCreateBookTransaction);
export const dispatchGetBookTransaction = dispatch(actions.actionGetBookTransactions);
// export const dispatchUpdateBookTransaction = dispatch(actions.actionUpdateBookTransaction);
// export const dispatchDeleteBookCategory = dispatch(actions.actionDeleteBookCategory);
