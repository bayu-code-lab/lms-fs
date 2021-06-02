<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Peminjaman Buku</div>
            </v-card-title>
            <v-card-text>
                <template>
                    <v-form v-model="valid" ref="form" lazy-validation>
                        <v-container>
                            <customer-auto-complete @customer-id-data="setCustomerId"></customer-auto-complete>
                            <books-auto-complete @book-id-data="setBookId"></books-auto-complete>
                            <v-text-field
                                label="Jumlah Buku"
                                v-model="total"
                                type="number"
                                required
                            ></v-text-field>
                            <v-text-field
                                label="Jumlah Hari"
                                v-model="day"
                                type="day"
                                required
                            ></v-text-field>
                        </v-container>
                    </v-form>
                </template>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="reset">Reset
                    <v-icon right>
                        restore
                    </v-icon>
                </v-btn>
                <v-btn @click="submit" :disabled="!valid">
                    Submit
                    <v-icon right>
                        done
                    </v-icon>
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script lang="ts">
import { IBookTransactionCreate } from '@/interfaces';
import { dispatchCreateBookTransaction } from '@/store/book_transaction/actions';
import { Component, Vue, Watch } from 'vue-property-decorator';
import BooksAutoComplete from './BooksAutoComplete.vue';
import CustomerAutoComplete from './CustomerAutoComplete.vue';

@Component({
    name: 'Books',
    components: {
        BooksAutoComplete,
        CustomerAutoComplete,
    },
})
export default class EditBook extends Vue {
    public valid = true;
    public customerId: number = 0;
    public bookId: number = 0;
    public total: number = 0;
    public day: number = 0;

    public setCustomerId(value) {
        this.customerId = value
    }

    public setBookId(value) {
        this.bookId = value
    }

    // @Watch('bookId')
    // onBookChanged(val: string, oldVal: string) {
    //     console.log(val, oldVal)
    // }

    public reset(){

    }

    public async submit() {
        if (await this.$validator.validateAll()) {
            const updatedBorrow: IBookTransactionCreate = {};
            if (this.customerId) {
                updatedBorrow.customer_id = this.customerId;
            }
            if (this.bookId) {
                updatedBorrow.book_id = this.bookId;
            }
            if (this.total) {
                updatedBorrow.total = this.total;
            }
            if (this.day) {
                updatedBorrow.day = this.day;
            }
            
            await dispatchCreateBookTransaction(this.$store, updatedBorrow);
            this.$router.push('/main/returned/all');
        }
    }
}
</script>
