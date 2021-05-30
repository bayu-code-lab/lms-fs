<template>
    <div>
        <v-toolbar light>
        <v-toolbar-title>
            Books
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="primary" to="/main/book/create">Create Book </v-btn>
        </v-toolbar>
        <v-data-table :headers="headers" :items="books">
        <template slot="items" slot-scope="props">
            <td>{{ props.item.title }}</td>
            <td>{{ props.item.desc }}</td>
            <td>{{ props.item.category_desc }}</td>
            <td>{{ props.item.author }}</td>
            <td>{{ props.item.quantity }}</td>
            <td class="justify-center layout px-0">
                <v-tooltip top>
                    <span>Edit</span>
                    <v-btn slot="activator" flat :to="{name: 'main-book-edit', params: {id: props.item.id}}">
                    <v-icon>edit</v-icon>
                    </v-btn>
                </v-tooltip>
                <v-tooltip top>
                    <span>Delete</span>
                    <v-btn slot="activator" flat :to="{name: 'main-book-delete', params: {id: props.item.id}}">
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

@Component
export default class Books extends Vue {
    public headers = [
        {
        text: 'Title',
        sortable: true,
        value: 'title',
        align: 'left',
        },
        {
        text: 'Description',
        sortable: true,
        value: 'desc',
        align: 'left',
        },
        {
        text: 'Category',
        sortable: true,
        value: 'category_id',
        align: 'left',
        },
        {
        text: ' Author',
        sortable: true,
        value: 'author',
        align: 'left',
        },
        {
        text: ' quantity',
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
}
</script>
