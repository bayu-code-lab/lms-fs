<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Delete Book Category</div>
            </v-card-title>
            <v-card-text>
                <template>
                    <v-form v-model="valid" ref="form" lazy-validation>
                        <v-text-field
                            label="Category Desc"
                            v-model="desc"
                            disabled
                        ></v-text-field>
                    </v-form>
                </template>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancel">Cancel</v-btn>
                <v-btn color="error" @click="submit" :disabled="!valid">
                    Delete
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import {
    dispatchGetBookCategory,
    dispatchDeleteBookCategory,
} from '@/store/book_category/actions';
import { readOneBookCategory } from '@/store/book_category/getters';

@Component
export default class EditBookCategory extends Vue {
    public valid = true;
    public desc: string = '';

    public async mounted() {
        await dispatchGetBookCategory(this.$store);
        if (this.bookCategory) {
            this.desc = this.bookCategory.desc;
        }
    }

    public cancel() {
        this.$router.back();
    }

    public async submit() {
        await dispatchDeleteBookCategory(this.$store, {
            id: this.bookCategory!.id,
        });
        this.$router.push('/main/book-category');
    }

    get bookCategory() {
        return readOneBookCategory(this.$store)(
            +this.$router.currentRoute.params.id,
        );
    }
}
</script>
