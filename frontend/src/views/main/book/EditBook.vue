<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Edit Book</div>
            </v-card-title>
            <v-card-text>
                <template>
                    <v-form v-model="valid" ref="form" lazy-validation>
                        <v-text-field
                            label="Title"
                            v-model="title"
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Description"
                            v-model="desc"
                            required
                        ></v-text-field>
                        <v-select
                            :items="categories"
                            label="Category"
                            item-text="desc"
                            item-value="id"
                            v-model="selectedCategories"
                            required
                        ></v-select>
                        <v-text-field
                            label="Author"
                            v-model="author"
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Quantity"
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
import { Component, Vue, Watch } from 'vue-property-decorator';
import { IBookUpdate } from '@/interfaces';
import {
    dispatchGetBook,
    dispatchUpdateBook,
} from '@/store/book/actions';
import { readOneBook } from '@/store/book/getters';
import { readBookCategories } from '@/store/book_category/getters';
import { dispatchGetBookCategory } from '@/store/book_category/actions';

@Component
export default class EditBook extends Vue {
    public valid = true;
    public selectedCategories = {};
    public categoryId = 0
    public title: string = '';
    public desc: string = '';
    public author: string = '';
    public quantity: number = 0;

    public async mounted() {
        await dispatchGetBook(this.$store);
        await dispatchGetBookCategory(this.$store);
        this.reset();
    }

    get categories() {
        return readBookCategories(this.$store);
    }

    public reset() {
        this.$validator.reset();
        if (this.book) {
            this.title = this.book.title;
            this.desc = this.book.desc;
            this.author = this.book.author;
            this.quantity = Number(this.book.quantity);
            this.selectedCategories = this.categories.find((category) => category.id === this.book?.category_id) || {};
        }
    }

    @Watch('selectedCategories')
    handleCategory(value){
        this.categoryId = value.id
    }

    public cancel() {
        this.$router.back();
    }


    public async submit() {
        if (await this.$validator.validateAll()) {
            const updatedBook: IBookUpdate = {};
            if (this.title) {
                updatedBook.title = this.title;
            }
            if (this.desc) {
                updatedBook.desc = this.desc;
            }
            if (this.selectedCategories) {
                updatedBook.category_id = Number(this.categoryId);
            }
            if (this.author) {
                updatedBook.author = this.author;
            }
            if (this.quantity) {
                updatedBook.quantity = Number(this.quantity);
            }
            await dispatchUpdateBook(this.$store, {
                id: this.book!.id,
                book_: updatedBook,
            });
            this.$router.push('/main/book');
        }
    }

    get book() {
        return readOneBook(this.$store)(
            +this.$router.currentRoute.params.id,
        );
    }
}
</script>
