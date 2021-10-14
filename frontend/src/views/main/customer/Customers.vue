<template>
    <div>
        <v-app-bar light>
            <v-toolbar-title>
                Daftar Data Murid/Guru
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn color="primary" to="/main/customer/create"
                ><v-icon left>add</v-icon>Tambah</v-btn
            >
        </v-app-bar>
        <v-data-table
            :headers="headers"
            :items="customers"
        >
        <template v-slot:item.actions="{ item }">
                <v-btn
                    text
                    :to="{
                        name: 'main-customer-edit',
                        params: { id: item.id },
                    }"
                >
                    <v-icon>
                        edit
                    </v-icon>
                </v-btn>
                <v-btn
                    text
                    :to="{
                        name: 'main-customer-delete',
                        params: { id: item.id },
                    }"
                >
                    <v-icon>
                        delete
                    </v-icon>
                </v-btn>
            </template>
        </v-data-table>
    </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator';
import { readCustomers } from '@/store/customer/getters';
import { dispatchGetCustomer } from '@/store/customer/actions';

@Component
export default class Customers extends Vue {
    public totalCustomers = 0;
    public loading = true;
    public options = {};
    public headers = [
        {
            text: 'NIK/NIS',
            sortable: true,
            value: 'id',
            align: 'left',
        },
        {
            text: 'Nama Lengkap',
            sortable: true,
            value: 'full_name',
            align: 'left',
        },
        {
            text: 'Kelas',
            sortable: true,
            value: 'grade',
            align: 'left',
        },
        {
            text: 'Jurusan',
            sortable: true,
            value: 'major',
            align: 'left',
        },
        {
            text: 'Angkatan',
            sortable: true,
            value: 'batch_of_year',
            align: 'left',
        },
        {
            text: 'Alamat',
            sortable: true,
            value: 'address',
            align: 'left',
        },
        {
            text: 'Actions',
            value: 'actions',
            align: 'center',
        },
    ];


    get customers() {
        return readCustomers(this.$store);
    }

    public async mounted() {
        await dispatchGetCustomer(this.$store);
        this.loading = false;
    }
}
</script>
