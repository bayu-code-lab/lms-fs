<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Tambah Buku</div>
            </v-card-title>
            <v-card-text>
                <template>
                    <v-form v-model="valid" ref="form" lazy-validation>
                        <v-text-field
                            label="Judul Buku"
                            v-model="title"
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Tahun"
                            v-model="year"
                            type="number"
                            required
                        ></v-text-field>
                        <v-select
                            :items="categories"
                            label="Kategori"
                            item-text="desc"
                            v-model="categoryId"
                            item-value="id"
                            required
                        ></v-select>
                        <v-text-field
                            label="Penerbit"
                            v-model="publisher"
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Pengarang"
                            v-model="author"
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Kode ISBN"
                            v-model="isbn"
                        ></v-text-field>
                        <v-text-field
                            label="Jumlah Buku"
                            v-model="quantity"
                            type="number"
                            required
                        ></v-text-field>
                    </v-form>
                </template>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancel">Cancel</v-btn>
                <v-btn @click="reset">Reset</v-btn>
                <v-btn @click="submit" :disabled="!valid">
                    Save
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { IBookCreate } from '@/interfaces';
import { dispatchGetBook, dispatchCreateBook } from '@/store/book/actions';
import { readBookCategories } from '@/store/book_category/getters';
import { dispatchGetBookCategory } from '@/store/book_category/actions';

@Component
export default class EditBook extends Vue {
    public valid = true;
    public title: string = '';
    public year: number = 0;
    public categoryId = '';
    public publisher: string = '';
    public author: string = '';
    public isbn: string = '';
    public quantity: number = 0;

    public async mounted() {
        await dispatchGetBook(this.$store);
        await dispatchGetBookCategory(this.$store);
        this.reset();
    }

    public reset() {
        this.title = '';
        this.year = 0;
        this.categoryId = '';
        this.publisher = '';
        this.author = '';
        this.isbn = '';
        this.quantity = 0;
    }

    public cancel() {
        this.$router.back();
    }

    get categories() {
        return readBookCategories(this.$store);
    }

    public async submit() {
        if (await this.$validator.validateAll()) {
            const updatedBook: IBookCreate = {};
            if (this.title) {
                updatedBook.title = this.title;
            }
            if (this.year) {
                updatedBook.year = this.year;
            }
            if (this.categoryId) {
                updatedBook.category_id = Number(this.categoryId);
            }
            if (this.publisher) {
                updatedBook.publisher = this.publisher;
            }
            if (this.author) {
                updatedBook.author = this.author;
            }
            if (this.isbn) {
                updatedBook.isbn = this.isbn;
            }
            if (this.quantity) {
                updatedBook.quantity = Number(this.quantity);
            }
            await dispatchCreateBook(this.$store, updatedBook);
            this.$router.push('/main/book');
        }
    }
}
</script>
