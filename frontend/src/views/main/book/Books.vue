<template>
    <div>
        <v-app-bar light>
            <v-app-bar-title>
                Daftar Buku
            </v-app-bar-title>
            <v-spacer></v-spacer>
            <v-btn
                v-show="hasAdminAccess"
                color="primary"
                to="/main/book/create"
                >Tambah Buku
            </v-btn>
        </v-app-bar>
        <v-data-table :headers="headers" :items="books">
            <template v-slot:item.actions="{ item }">
                <v-btn
                    text
                    :to="{
                        name: 'main-book-edit',
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
                        name: 'main-book-delete',
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
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IUserProfile } from '@/interfaces';
import { readBooks } from '@/store/book/getters';
import { dispatchGetBook } from '@/store/book/actions';
import { readHasAdminAccess } from '@/store/main/getters';

@Component
export default class Books extends Vue {
    public headers = [
        {
            text: 'Judul Buku',
            sortable: true,
            value: 'title',
            align: 'left',
        },
        {
            text: 'Tahun',
            sortable: true,
            value: 'year',
            align: 'left',
        },
        {
            text: 'Kategori',
            sortable: true,
            value: 'category_desc',
            align: 'left',
        },
        {
            text: 'Penerbit',
            sortable: true,
            value: 'publisher',
            align: 'left',
        },
        {
            text: ' Pengarang',
            sortable: true,
            value: 'author',
            align: 'left',
        },
        {
            text: 'Kode ISBN',
            sortable: true,
            value: 'isbn',
            align: 'left',
        },
        {
            text: 'Jumlah',
            sortable: true,
            value: 'quantity',
            align: 'left',
        },
        {
            text: 'Actions',
            value: 'actions',
            align: 'center',
        },
    ];
    get books() {
        return readBooks(this.$store);
    }

    public async mounted() {
        await dispatchGetBook(this.$store);
    }

    public get hasAdminAccess() {
        return readHasAdminAccess(this.$store);
    }
}
</script>
