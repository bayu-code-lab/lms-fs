<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Create Book Category</div>
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
import { IBookCategoryCreate } from '@/interfaces';
import {
    dispatchGetBookCategory,
    dispatchCreateBookCategory,
} from '@/store/book_category/actions';
import { readOneCustomer } from '@/store/customer/getters';

@Component
export default class EditBookCategory extends Vue {
    public valid = true;
    public desc: string = '';

    public async mounted() {
        await dispatchGetBookCategory(this.$store);
        this.reset();
    }

    public reset() {
        this.desc = '';
    }

    public cancel() {
        this.$router.back();
    }

    public async submit() {
        if (await this.$validator.validateAll()) {
            const updatedBookCategory: IBookCategoryCreate = {};
            if (this.desc) {
                updatedBookCategory.desc = this.desc;
            }
            await dispatchCreateBookCategory(this.$store, updatedBookCategory);
            this.$router.push('/main/book-category');
        }
    }
}
</script>
