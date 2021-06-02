<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Hapus Buku</div>
            </v-card-title>
            <v-card-text>
                <template>
                    <v-form v-model="valid" ref="form" lazy-validation>
                        <v-text-field
                            label="Judul Buku"
                            v-model="title"
                            disabled
                        ></v-text-field>
                        <v-text-field
                            label="Tahun"
                            v-model="year"
                            type="number"
                            disabled
                        ></v-text-field>
                        <v-select
                            :items="categories"
                            label="Kategori"
                            item-text="desc"
                            v-model="categoryId"
                            item-value="id"
                            disabled
                        ></v-select>
                        <v-text-field
                            label="Penerbit"
                            v-model="publisher"
                            disabled
                        ></v-text-field>
                        <v-text-field
                            label="Pengarang"
                            v-model="author"
                            disabled
                        ></v-text-field>
                        <v-text-field
                            label="Kode ISBN"
                            v-model="isbn"
                        ></v-text-field>
                        <v-text-field
                            label="Jumlah Buku"
                            v-model="quantity"
                            type="number"
                            disabled
                        ></v-text-field>
                    </v-form>
                </template>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancel">Cancel</v-btn>
                <v-btn @click="submit" :disabled="!valid">
                    Delete
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { dispatchGetBook, dispatchDeleteBook } from '@/store/book/actions';
import { readOneBook } from '@/store/book/getters';
import { readBookCategories } from '@/store/book_category/getters';
import { dispatchGetBookCategory } from '@/store/book_category/actions';

@Component
export default class EditBook extends Vue {
    public valid = true;
    public selectedCategories = {};
    public title: string = '';
    public year: number = 0;
    public publisher: string = '';
    public author: string = '';
    public isbn: string = '';
    public quantity: number = 0;

    public async mounted() {
        await dispatchGetBook(this.$store);
        await dispatchGetBookCategory(this.$store);
        if (this.book) {
            this.title = this.book.title;
            this.year = this.book.year;
            this.publisher = this.book.publisher;
            this.isbn = this.book.isbn;
            this.author = this.book.author;
            this.quantity = Number(this.book.quantity);
            this.selectedCategories =
                this.categories.find(
                    (category) => category.id === this.book?.category_id
                ) || {};
        }
    }
    get categories() {
        return readBookCategories(this.$store);
    }

    public cancel() {
        this.$router.back();
    }

    public async submit() {
        await dispatchDeleteBook(this.$store, {
            id: this.book!.id,
        });
        this.$router.push('/main/book');
    }

    get book() {
        return readOneBook(this.$store)(+this.$router.currentRoute.params.id);
    }
}
</script>
