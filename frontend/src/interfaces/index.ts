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
