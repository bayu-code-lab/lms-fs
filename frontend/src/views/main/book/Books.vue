<template>
    <div>
        <v-toolbar light>
            <v-toolbar-title>
                Books
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn
                v-show="hasAdminAccess"
                color="primary"
                to="/main/book/create"
                >Create Book
            </v-btn>
        </v-toolbar>
        <v-data-table :headers="headers" :items="books">
            <template slot="items" slot-scope="props">
                <td>{{ props.item.title }}</td>
                <td>{{ props.item.year }}</td>
                <td>{{ props.item.category_desc }}</td>
                <td>{{ props.item.publisher }}</td>
                <td>{{ props.item.author }}</td>
                <td>{{ props.item.isbn }}</td>
                <td>{{ props.item.quantity }}</td>
                <td class="justify-center layout px-0">
                    <v-tooltip v-show="hasAdminAccess" top>
                        <span>Edit</span>
                        <v-btn
                            slot="activator"
                            flat
                            :to="{
                                name: 'main-book-edit',
                                params: { id: props.item.id },
                            }"
                        >
                            <v-icon>edit</v-icon>
                        </v-btn>
                    </v-tooltip>
                    <v-tooltip v-show="hasAdminAccess" top>
                        <span>Delete</span>
                        <v-btn
                            slot="activator"
                            flat
                            :to="{
                                name: 'main-book-delete',
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
            value: 'category_id',
            align: 'left',
        },
        {
            text: 'Penerbit',
            sortable: true,
            value: 'author',
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
            value: 'author',
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
            value: 'id',
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
