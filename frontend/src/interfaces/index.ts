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
    desc: string;
    category_id: number;
    category_desc: string;
    author: string;
    quantity: number;
}

export interface IBookUpdate {
    title?: string;
    desc?: string;
    category_id?: number;
    author?: string;
    quantity?: number;
}

export interface IBookCreate {
    title?: string;
    desc?: string;
    category_id?: number;
    author?: string;
    quantity?: number;
}
