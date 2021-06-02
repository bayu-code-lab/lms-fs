<template>
    <div>
        <v-alert v-model="alert" type="success">
            Buku berhasil dikembalikan.
        </v-alert>

        <v-card>
            <v-card-title>
                <v-toolbar-title>
                    Pengembalian Buku
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <v-text-field
                    v-model="search"
                    append-icon="search"
                    label="Pencarian"
                    single-line
                    hide-details
                ></v-text-field>
            </v-card-title>
            <v-data-table
                :headers="headers"
                :items="transactions"
                :search="search"
                :rows-per-page-items="rowsPerPageItems"
                :pagination.sync="pagination"
            >
                <template slot="items" slot-scope="props">
                    <td>{{ props.item.customer_name }}</td>
                    <td>{{ props.item.book_title }}</td>
                    <td>{{ props.item.year }}</td>
                    <td>{{ props.item.publisher }}</td>
                    <td style="text-align:center">{{ props.item.total }}</td>
                    <td style="text-align:center">{{ props.item.day }}</td>
                    <td style="text-align:center">
                        <v-icon v-if="props.item.is_late" color="blue"
                            >done</v-icon
                        >
                        <v-icon v-else color="red">clear</v-icon>
                    </td>
                    <td>{{ props.item.created_date }}</td>
                    <td class="justify-center layout px-0">
                        <v-btn
                            slot="activator"
                            class="primary"
                            @click="submitData(props.item.id)"
                        >
                            <span>Kembalikan Buku</span>
                            <v-icon left>assignment_returned</v-icon>
                        </v-btn>
                    </td>
                </template>
            </v-data-table>
        </v-card>
    </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IBookTransaction } from '@/interfaces';
import { readBookTransactions } from '@/store/book_transaction/getters';
import { dispatchGetBookTransaction } from '@/store/book_transaction/actions';
import { apiUrl } from '@/env';

@Component
export default class Books extends Vue {
    public alert = false;
    public rowsPerPageItems = [10, 20, 30, 40];
    public pagination = {
        rowsPerPage: 20,
    };
    public search: string = '';
    public headers = [
        {
            text: 'Nama Peminjam',
            sortable: true,
            value: 'customer_name',
            align: 'left',
        },
        {
            text: 'Judul Buku',
            sortable: true,
            value: 'book_title',
            align: 'left',
        },
        {
            text: 'Tahun',
            sortable: true,
            value: 'year',
            align: 'left',
        },
        {
            text: 'Penerbit',
            sortable: true,
            value: 'publisher',
            align: 'left',
        },
        {
            text: 'Jumlah Buku',
            sortable: true,
            filterable: false,
            value: 'total',
            align: 'center',
        },
        {
            text: 'Lama Dipinjam',
            sortable: true,
            filterable: false,
            value: 'day',
            align: 'center',
        },
        {
            text: 'Terlambat',
            sortable: true,
            filterable: false,
            value: 'is_late',
            align: 'center',
        },
        {
            text: 'Tanggal Peminjaman',
            sortable: true,
            filterable: false,
            value: 'created_date',
            align: 'left',
        },
        {
            text: 'Actions',
            value: 'id',
            align: 'center',
        },
    ];

    get transactions() {
        return readBookTransactions(this.$store);
    }

    public async mounted() {
        await dispatchGetBookTransaction(this.$store);
    }

    public async submitData(value) {
        await fetch(`${apiUrl}/api/v1/book-transactions-return/${value}`, {
            method: 'put',
            headers: new Headers({
                'Authorization': 'Bearer ' + localStorage.token,
                'Content-Type': 'application/json',
            }),
        })
            .then((res) => {
                this.alert = true;
                setTimeout(() => {
                    this.alert = false;
                }, 1000);
            }).finally(async () => await dispatchGetBookTransaction(this.$store));
    }
}
</script>
