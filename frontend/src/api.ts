import axios from 'axios';
import { apiUrl } from '@/env';
import {
    IUserProfile,
    IUserProfileUpdate,
    IUserProfileCreate,
    ICustomer,
    ICustomerUpdate,
    ICustomerCreate,
    IBookCategory,
    IBookCategoryCreate,
    IBookCategoryUpdate,
    IBook,
    IBookCreate,
    IBookUpdate,
    IBookTransactionCreate,
    IBookTransaction,
} from './interfaces';

function authHeaders(token: string) {
    return {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    };
}

export const api = {
    async logInGetToken(username: string, password: string) {
        const params = new URLSearchParams();
        params.append('username', username);
        params.append('password', password);

        return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
    },
    async getMe(token: string) {
        return axios.get<IUserProfile>(
            `${apiUrl}/api/v1/users/me`,
            authHeaders(token),
        );
    },
    async updateMe(token: string, data: IUserProfileUpdate) {
        return axios.put<IUserProfile>(
            `${apiUrl}/api/v1/users/me`,
            data,
            authHeaders(token),
        );
    },
    async getUsers(token: string) {
        return axios.get<IUserProfile[]>(
            `${apiUrl}/api/v1/users/`,
            authHeaders(token),
        );
    },
    async updateUser(token: string, userId: number, data: IUserProfileUpdate) {
        return axios.put(
            `${apiUrl}/api/v1/users/${userId}`,
            data,
            authHeaders(token),
        );
    },
    async createUser(token: string, data: IUserProfileCreate) {
        return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
    },
    async passwordRecovery(email: string) {
        return axios.post(`${apiUrl}/api/v1/password-recovery/${email}`);
    },
    async resetPassword(password: string, token: string) {
        return axios.post(`${apiUrl}/api/v1/reset-password/`, {
            new_password: password,
            token,
        });
    },
    // Customer
    async getCustomers(token: string) {
        return axios.get<ICustomer[]>(
            `${apiUrl}/api/v1/customers/`,
            authHeaders(token),
        );
    },
    async updateCustomer(token: string, id: number, data: ICustomerUpdate) {
        return axios.put(
            `${apiUrl}/api/v1/customers/${id}`,
            data,
            authHeaders(token),
        );
    },
    async createCustomer(token: string, data: ICustomerCreate) {
        return axios.post(
            `${apiUrl}/api/v1/customers/`,
            data,
            authHeaders(token),
        );
    },
    async deleteCustomer(token: string, id: number) {
        return axios.delete(
            `${apiUrl}/api/v1/customers/${id}`,
            authHeaders(token),
        );
    },
    // Book Category
    async getBookCategories(token: string) {
        return axios.get<IBookCategory[]>(
            `${apiUrl}/api/v1/book-categories/`,
            authHeaders(token),
        );
    },
    async updateBookCategories(
        token: string,
        id: number,
        data: IBookCategoryUpdate,
    ) {
        return axios.put(
            `${apiUrl}/api/v1/book-categories/${id}`,
            data,
            authHeaders(token),
        );
    },
    async createBookCategories(token: string, data: IBookCategoryCreate) {
        return axios.post(
            `${apiUrl}/api/v1/book-categories/`,
            data,
            authHeaders(token),
        );
    },
    async deleteBookCategories(token: string, id: number) {
        return axios.delete(
            `${apiUrl}/api/v1/book-categories/${id}`,
            authHeaders(token),
        );
    },

    // Books
    async getBooks(token: string) {
        return axios.get<IBook[]>(
            `${apiUrl}/api/v1/books/`,
            authHeaders(token),
        );
    },
    async updateBooks(
        token: string,
        id: number,
        data: IBookUpdate,
    ) {
        return axios.put(
            `${apiUrl}/api/v1/books/${id}`,
            data,
            authHeaders(token),
        );
    },
    async createBooks(token: string, data: IBookCreate) {
        return axios.post(
            `${apiUrl}/api/v1/books/`,
            data,
            authHeaders(token),
        );
    },
    async deleteBooks(token: string, id: number) {
        return axios.delete(
            `${apiUrl}/api/v1/books/${id}`,
            authHeaders(token),
        );
    },


    //Books Transaction
    async getBookTransactions(token: string) {
        return axios.get<IBookTransaction[]>(
            `${apiUrl}/api/v1/book-transactions/`,
            authHeaders(token),
        );
    },
    async borrowBooks(token: string, data: IBookTransactionCreate) {
        return axios.post(
            `${apiUrl}/api/v1/book-transactions/`,
            data,
            authHeaders(token),
        );
    },
    async returningBooks(
        token: string,
        id: number
    ) {
        return axios.put(
            `${apiUrl}/api/v1/book-transactions-return/${id}`,
            authHeaders(token),
        );
    },
};
