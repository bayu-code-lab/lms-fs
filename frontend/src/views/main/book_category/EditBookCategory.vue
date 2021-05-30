<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Edit Book Category</div>
            </v-card-title>
            <v-card-text>
                <template>
                    <v-form v-model="valid" ref="form" lazy-validation>
                        <v-text-field
                            label="Category Description"
                            v-model="desc"
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
import { IBookCategoryUpdate } from '@/interfaces';
import {
    dispatchGetBookCategory,
    dispatchUpdateBookCategory,
} from '@/store/book_category/actions';
import { readOneBookCategory } from '@/store/book_category/getters';

@Component
export default class EditBookCategory extends Vue {
    public valid = true;
    public desc: string = '';

    public async mounted() {
        await dispatchGetBookCategory(this.$store);
        this.reset();
    }

    public reset() {
        this.$validator.reset();
        if (this.bookCategory) {
            this.desc = this.bookCategory.desc;
        }
    }

    public cancel() {
        this.$router.back();
    }

    public async submit() {
        if (await this.$validator.validateAll()) {
            const updatedBookCategory: IBookCategoryUpdate = {};
            if (this.desc) {
                updatedBookCategory.desc = this.desc;
            }
            await dispatchUpdateBookCategory(this.$store, {
                id: this.bookCategory!.id,
                book_category: updatedBookCategory,
            });
            this.$router.push('/main/book-category');
        }
    }

    get bookCategory() {
        return readOneBookCategory(this.$store)(
            +this.$router.currentRoute.params.id,
        );
    }
}
</script>
