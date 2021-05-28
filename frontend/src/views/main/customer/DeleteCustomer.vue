<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Create Customer</div>
            </v-card-title>
            <v-card-text>
                <template>
                    <v-form v-model="valid" ref="form" lazy-validation>
                        <v-text-field
                            label="Customer ID"
                            v-model="customerId"
                            disabled
                        ></v-text-field>
                        <v-text-field
                            label="Full Name"
                            v-model="fullName"
                            disabled
                        ></v-text-field>
                        <v-text-field
                            label="Address"
                            type="text"
                            v-model="address"
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
import {
    dispatchGetCustomer,
    dispatchDeleteCustomer,
} from '@/store/customer/actions';
import { readOneCustomer } from '@/store/customer/getters';

@Component
export default class EditUser extends Vue {
    public valid = true;
    public customerId: string = '';
    public fullName: string = '';
    public address: string = '';

    public async mounted() {
        await dispatchGetCustomer(this.$store);
        if (this.customer) {
            this.customerId = this.customer.customer_id;
            this.fullName = this.customer.full_name;
            this.address = this.customer.address;
        }
    }

    public cancel() {
        this.$router.back();
    }

    public async submit() {
        await dispatchDeleteCustomer(this.$store, { id: this.customer!.id });
        this.$router.push('/main/customer');
    }

    get customer() {
        return readOneCustomer(this.$store)(
            +this.$router.currentRoute.params.id,
        );
    }
}
</script>
