<template>
    <div>
        <v-toolbar light>
        <v-toolbar-title>
            Manage Customer
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="primary" to="/main/customer/create">Create Customer</v-btn>
        </v-toolbar>
        <v-data-table :headers="headers" :items="customers">
        <template slot="items" slot-scope="props">
            <td>{{ props.item.customer_id }}</td>
            <td>{{ props.item.full_name }}</td>
            <td>{{ props.item.address }}</td>
            <td class="justify-center layout px-0">
                <v-tooltip top>
                    <span>Edit</span>
                    <v-btn slot="activator" flat :to="{name: 'main-customer-edit', params: {id: props.item.id}}">
                    <v-icon>edit</v-icon>
                    </v-btn>
                </v-tooltip>
                <v-tooltip top>
                    <span>Delete</span>
                    <v-btn slot="activator" flat :to="{name: 'main-customer-delete', params: {id: props.item.id}}">
                    <v-icon>delete</v-icon>
                    </v-btn>
                </v-tooltip>
            </td>
        </template>
        </v-data-table>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IUserProfile } from '@/interfaces';
import { readCustomers } from '@/store/customer/getters';
import { dispatchGetCustomer } from '@/store/customer/actions';

@Component
export default class Customers extends Vue {
    public headers = [
        {
        text: 'Customer ID',
        sortable: true,
        value: 'customer_id',
        align: 'left',
        },
        {
        text: 'Full  Name',
        sortable: true,
        value: 'full_name',
        align: 'left',
        },
        {
        text: 'Address',
        sortable: true,
        value: 'address',
        align: 'left',
        },
        {
        text: 'Actions',
        value: 'id',
        align: 'center',
        },
    ];
    get customers() {
        return readCustomers(this.$store);
    }

    public async mounted() {
        await dispatchGetCustomer(this.$store);
    }
}
</script>
