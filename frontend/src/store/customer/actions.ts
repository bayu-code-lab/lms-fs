import { api } from '@/api';
import { ActionContext } from 'vuex';
import { ICustomerCreate, ICustomerUpdate } from '@/interfaces';
import { State } from '../state';
import { CustomerState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { commitSetCustomers, commitSetCustomer } from './mutations';
import { dispatchCheckApiError } from '../main/actions';
import { commitAddNotification, commitRemoveNotification } from '../main/mutations';

type MainContext = ActionContext<CustomerState, State>;

export const actions = {
    async actionGetCustomers(context: MainContext) {
        try {
            const response = await api.getCustomers(context.rootState.main.token);
            if (response) {
                commitSetCustomers(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateCustomer(context: MainContext, payload: { id: number, customer: ICustomerUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateCustomer(context.rootState.main.token, payload.id, payload.customer),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetCustomer(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Customer successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateCustomer(context: MainContext, payload: ICustomerCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createCustomer(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetCustomer(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Customer successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionDeleteCustomer(context: MainContext, payload: { id: number}) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.deleteCustomer(context.rootState.main.token, payload.id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetCustomer(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Customer successfully deleted', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
};

const { dispatch } = getStoreAccessors<CustomerState, State>('');

export const dispatchCreateCustomer = dispatch(actions.actionCreateCustomer);
export const dispatchGetCustomer = dispatch(actions.actionGetCustomers);
export const dispatchUpdateCustomer = dispatch(actions.actionUpdateCustomer);
export const dispatchDeleteCustomer = dispatch(actions.actionDeleteCustomer);
