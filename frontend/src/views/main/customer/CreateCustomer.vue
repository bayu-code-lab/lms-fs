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
                            label="NIK/NISN"
                            v-model="id"
                            :rules="idRules"
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Nama Lengkap"
                            v-model="fullName"
                            :rules="fullNameRules"
                            required
                        ></v-text-field>
                        <v-text-field
                            label="Kelas (Hanya Untuk Murid)"
                            v-model="grade"
                            type="number"
                        ></v-text-field>
                        <v-text-field
                            label="Jurusan (Hanya Untuk Murid)"
                            v-model="major"
                        ></v-text-field>
                        <v-text-field
                            label="Angkatan (Hanya Untuk Murid)"
                            v-model="batchOfYear"
                            type="number"
                        ></v-text-field>
                        <v-text-field
                            label="Address"
                            type="text"
                            v-model="address"
                            :rules="addressRules"
                            required
                        ></v-text-field>
                    </v-form>
                </template>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancel">Keembali</v-btn>
                <v-btn @click="reset">Reset</v-btn>
                <v-btn @click="submit" :disabled="!valid">
                    Simpan
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator';
import { ICustomerCreate } from '@/interfaces';
import {
    dispatchGetCustomer,
    dispatchCreateCustomer,
} from '@/store/customer/actions';
import { readOneCustomer } from '@/store/customer/getters';

@Component
export default class EditCustomer extends Vue {
    public valid = true;
    public id: string = '';
    public idRules = [
            (v) => !!v || 'NIK/NISN wajib  di isi',
            (v) => v.length > 9 || 'NIK/NISN harus lebih dari 9 Karakter',
        ];
    public fullName: string = '';
    public fullNameRules = [
            (v) => !!v || 'Nama lengkap wajib  di isi',
        ];
    public grade: number = 0;
    public major: string = '';
    public batchOfYear: number = 0;
    public address: string = '';
    public addressRules = [
            (v) => !!v || 'Alamat wajib  di isi',
        ];

    public async mounted() {
        await dispatchGetCustomer(this.$store);
        this.reset();
    }

    public reset() {
        this.id = '';
        this.fullName = '';
        this.grade = 0;
        this.major = '';
        this.batchOfYear = 0;
        this.address = '';
    }

    public cancel() {
        this.$router.back();
    }

    public async submit() {
        if (await this.$validator.validateAll()) {
            const updatedCustomer: ICustomerCreate = {};
            if (this.id) {
                updatedCustomer.id = this.id;
            }
            if (this.fullName) {
                updatedCustomer.full_name = this.fullName;
            }
            if (this.grade !== 0) {
                updatedCustomer.grade = this.grade;
            }
            if (this.major) {
                updatedCustomer.major = this.major;
            }
            if (this.batchOfYear !== 0) {
                updatedCustomer.batch_of_year = this.batchOfYear;
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
