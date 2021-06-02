export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface ICustomer {
    id: number;
    customer_id: string;
    full_name: string;
    address: string;
}

export interface ICustomerUpdate {
    customer_id?: string;
    full_name?: string;
    address?: string;
}

export interface ICustomerCreate {
    customer_id?: string;
    full_name?: string;
    address?: string;
}

export interface IBookCategory {
    id: number;
    desc: string;
}

export interface IBookCategoryUpdate {
    desc?: string;
}

export interface IBookCategoryCreate {
    desc?: string;
}

export interface IBook {
    id: number;
    title: string;
    year: number;
    category_id: number;
    category_desc: string;
    publisher: string
    author: string;
    isbn: string
    quantity: number;
}

export interface IBookUpdate {
    title?: string;
    year?: number;
    category_id?: number;
    publisher?: string
    author?: string;
    isbn?: string
    quantity?: number;
}

export interface IBookCreate {
    title?: string;
    year?: number;
    category_id?: number;
    publisher?: string
    author?: string;
    isbn?: string
    quantity?: number;
}

export interface IBookTransaction {
    id: number;
    customer_id: number;
    customer_name: string;
    book_id: number;
    book_title: string;
    year: number;
    publisher: string;
    total: number;
    day: number;
    is_returned: boolean;
    is_late: boolean;
    date_returned: string;
    created_date: string;
}

export interface IBookTransactionData {
    id: number;
    customer_id: number;
    customer_name: string;
    book_id: number;
    book_title: string;
    total: number;
    day: number;
    is_returned: boolean;
    is_late: boolean;
    date_returned: string;
    created_date: string;
}

export interface IBookTransactionEdit {
    id?: number;
    customer_id?: number;
    book_id?: number;
    total?: number;
    day?: number;
}

export interface IBookTransactionCreate {
    customer_id?: number;
    book_id?: number;
    total?: number;
    day?: number;
}
