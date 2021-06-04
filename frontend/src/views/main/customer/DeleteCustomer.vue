<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Hapus Kostumer</div>
            </v-card-title>
            <v-card-text>
                <template>
                    <v-form v-model="valid" ref="form" lazy-validation>
                        <v-text-field
                            label="NIK/NISN"
                            v-model="id"
                            disabled
                        ></v-text-field>
                        <v-text-field
                            label="Nama Lengkap"
                            v-model="fullName"
                            disabled
                        ></v-text-field>
                        <v-text-field
                            label="Kelas (Hanya Untuk Murid)"
                            v-model="grade"
                            type="number"
                            disabled
                        ></v-text-field>
                        <v-text-field
                            label="Jurusan (Hanya Untuk Murid)"
                            v-model="major"
                            disabled
                        ></v-text-field>
                        <v-text-field
                            label="Angkatan (Hanya Untuk Murid)"
                            v-model="batchOfYear"
                            type="number"
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
                <v-btn @click="cancel">Kembali</v-btn>
                <v-btn @click="submit" :disabled="!valid">
                    Hapus
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
export default class EditCustomer extends Vue {
    public id: string = '';
    public fullName: string = '';
    public grade: number = 0;
    public major: string = '';
    public batchOfYear: number = 0;
    public address: string = '';
    public async mounted() {
        await dispatchGetCustomer(this.$store);
        if (this.customer) {
            this.id = this.customer.id;
            this.fullName = this.customer.full_name;
            this.grade = this.customer.grade;
            this.major = this.customer.major;
            this.batchOfYear = this.customer.batch_of_year;
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
