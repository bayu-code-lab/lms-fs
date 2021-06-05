<template>
    <div>
        <v-app-bar light>
            <v-app-bar-title>
                Pengaturan Kostumer
            </v-app-bar-title>
            <v-spacer></v-spacer>
            <v-btn color="primary" to="/main/customer/create"
                >Tambah Kustomer</v-btn
            >
        </v-app-bar>
        <v-data-table
            :headers="headers"
            :items="customers"
            :options="options"
            :server-items-length="totalCustomers"
            :loading="loading"
        >
            <template slot="items" slot-scope="props">
                <td>{{ props.item.id }}</td>
                <td>{{ props.item.full_name }}</td>
                <td>{{ props.item.grade }}</td>
                <td>{{ props.item.major }}</td>
                <td>{{ props.item.batch_of_year }}</td>
                <td>{{ props.item.address }}</td>
                <td class="justify-center layout px-0">
                    <v-tooltip top>
                        <span>Ubah</span>
                        <v-btn
                            slot="activator"
                            flat
                            :to="{
                                name: 'main-customer-edit',
                                params: { id: props.item.id },
                            }"
                        >
                            <v-icon>edit</v-icon>
                        </v-btn>
                    </v-tooltip>
                    <v-tooltip top>
                        <span>Hapus</span>
                        <v-btn
                            slot="activator"
                            flat
                            :to="{
                                name: 'main-customer-delete',
                                params: { id: props.item.id },
                            }"
                        >
                            <v-icon>delete</v-icon>
                        </v-btn>
                    </v-tooltip>
                </td>
            </template>
        </v-data-table>
    </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IUserProfile } from '@/interfaces';
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
            value: 'id',
            align: 'center',
        },
    ];

    @Watch('options', { deep: true })
    public async handler(val) {
        await console.log(val);
        await dispatchGetCustomer(this.$store);
        this.loading = false;
    }
    public optionsHandler(val){
        // await console.log(val);
        this.options = val;
    }

    get customers() {
        return readCustomers(this.$store);
    }

    public async mounted() {
        await dispatchGetCustomer(this.$store);
        this.loading = false;
    }
}
</script>
