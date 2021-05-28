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
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Full Name"
                            v-model="fullName"
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Address"
                            type="text"
                            v-model="address"
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
import { ICustomerCreate } from '@/interfaces';
import {
    dispatchGetCustomer,
    dispatchCreateCustomer,
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
        this.reset();
    }

    public reset() {
        this.customerId = '';
        this.fullName = '';
        this.address = '';
    }

    public cancel() {
        this.$router.back();
    }

    public async submit() {
        if (await this.$validator.validateAll()) {
            const updatedCustomer: ICustomerCreate = {};
            if (this.customerId) {
                updatedCustomer.customer_id = this.customerId;
            }
            if (this.fullName) {
                updatedCustomer.full_name = this.fullName;
            }
            if (this.address) {
                updatedCustomer.address = this.address;
            }
            await dispatchCreateCustomer(this.$store, updatedCustomer);
            this.$router.push('/main/customer');
        }
    }
}
</script>
