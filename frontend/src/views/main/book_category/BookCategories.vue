<template>
    <div>
        <v-toolbar light>
        <v-toolbar-title>
            Book Category
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="primary" to="/main/book-category/create">Create Book Category</v-btn>
        </v-toolbar>
        <v-data-table :headers="headers" :items="bookCategories">
        <template slot="items" slot-scope="props">
            <td>{{ props.item.desc }}</td>
            <td class="justify-center layout px-0">
                <v-tooltip top>
                    <span>Edit</span>
                    <v-btn slot="activator" flat :to="{name: 'main-book-category-edit', params: {id: props.item.id}}">
                    <v-icon>edit</v-icon>
                    </v-btn>
                </v-tooltip>
                <v-tooltip top>
                    <span>Delete</span>
                    <v-btn slot="activator" flat :to="{name: 'main-book-category-delete', params: {id: props.item.id}}">
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
import { readBookCategories } from '@/store/book_category/getters';
import { dispatchGetBookCategory } from '@/store/book_category/actions';

@Component
export default class BookCategories extends Vue {
    public headers = [
        {
        text: 'Category Name',
        sortable: true,
        value: 'desc',
        align: 'left',
        },
        {
        text: 'Actions',
        value: 'id',
        align: 'center',
        },
    ];
    get bookCategories() {
        return readBookCategories(this.$store);
    }

    public async mounted() {
        await dispatchGetBookCategory(this.$store);
    }
}
</script>
