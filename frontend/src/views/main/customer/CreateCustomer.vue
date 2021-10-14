<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Tambah Data Murid/Guru</div>
            </v-card-title>
            <v-card-text>
                <template>
                    <alert-box
                        :message="message"
                        :messageType="messageType"
                        :triggerAlert="triggerAlert"
                    ></alert-box>
                    <loading
                        :loading="loading"
                        :isSuccess="isSuccess"
                        :loadingMessage="loadingMessage"
                    ></loading>
                    <v-form v-model="valid" ref="form" lazy-validation>
                        <v-text-field
                            label="NIK/NISN"
                            v-model="id"
                            :rules="idRules"
                            required
                            ><v-icon slot="prepend" color="primary"
                                >payment</v-icon
                            ></v-text-field
                        >
                        <v-text-field
                            label="Nama Lengkap"
                            v-model="fullName"
                            :rules="fullNameRules"
                            required
                            ><v-icon slot="prepend" color="primary"
                                >perm_identity</v-icon
                            ></v-text-field
                        >
                        <v-text-field
                            label="Kelas (Hanya Untuk Murid)"
                            v-model="grade"
                            type="number"
                            ><v-icon slot="prepend" color="primary"
                                >gite</v-icon
                            ></v-text-field
                        >
                        <v-text-field
                            label="Jurusan (Hanya Untuk Murid)"
                            v-model="major"
                            ><v-icon slot="prepend" color="primary"
                                >biotech</v-icon
                            ></v-text-field
                        >
                        <v-text-field
                            label="Angkatan (Hanya Untuk Murid)"
                            v-model="batchOfYear"
                            type="number"
                            ><v-icon slot="prepend" color="primary"
                                >calendar_today</v-icon
                            ></v-text-field
                        >
                        <v-text-field
                            label="Alamat"
                            type="text"
                            v-model="address"
                            :rules="addressRules"
                            required
                            ><v-icon slot="prepend" color="primary"
                                >maps_home_work</v-icon
                            ></v-text-field
                        >
                    </v-form>
                </template>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancel"
                    ><v-icon left>arrow_back</v-icon>Kembali</v-btn
                >
                <v-btn color="warning" @click="reset"><v-icon color="white" left>settings_backup_restore</v-icon>Reset</v-btn>
                <v-btn color="primary" @click="submit" :disabled="!valid">
                    <v-icon color="white" left>save</v-icon>Simpan
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script lang="ts">
import axios from 'axios';
import { apiUrl } from '@/env';
import { Component, Vue, Watch } from 'vue-property-decorator';
import { ICustomerCreate } from '@/interfaces';
import {
    dispatchGetCustomer,
    dispatchCreateCustomer,
} from '@/store/customer/actions';
import AlertBox from '@/components/AlertBox.vue';
import Loading from '@/components/Loading.vue';
@Component({
    name: 'helper',
    components: {
        AlertBox,
        Loading,
    },
})
export default class EditCustomer extends Vue {
    public valid = true;
    public loading = false;
    public isSuccess = false;
    public triggerAlert = false;
    public message = '';
    public messageType = {};
    public loadingMessage = 'Data berhasil ditambahkan';
    public id: string = '';
    public fullName: string = '';
    public grade: number = 0;
    public major: string = '';
    public batchOfYear: number = 0;
    public address: string = '';

    //Rules
    public idRules = [
        (v) => !!v || 'NIK/NISN wajib di isi',
        (v) =>
            (v === null ? 0 : v.length) > 9 ||
            'NIK/NISN harus lebih dari 9 Karakter',
        (v) =>
            (!isNaN(parseFloat(v)) && v >= 0 && v <= 9999999999999999) ||
            'Hanya bisa di isi dengan angka dan maximal 16 digit',
    ];
    public fullNameRules = [(v) => !!v || 'Nama lengkap wajib  di isi'];
    public addressRules = [(v) => !!v || 'Alamat wajib  di isi'];

    public async mounted() {
        await dispatchGetCustomer(this.$store);
        this.reset();
    }

    public reset() {
        // this.$refs.form.reset();
    }

    public cancel() {
        this.$router.back();
    }

    public async submit() {
        if (await (this.$refs.form as Vue & { validate: () => boolean }).validate()) {
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
            await this.execApi(updatedCustomer);
        }
    }

    public async execApi(data) {
        this.loading = true;
        axios.defaults.headers.common['Authorization'] =
            'Bearer ' + localStorage.token;
        axios.defaults.headers.common['Content-Type'] = 'application/json';
        await axios.post(`${apiUrl}/api/v1/customers/`, data).then(
            (response) => {
                if (response.status == 200) {
                    setTimeout(() => {
                        this.isSuccess = true;
                        setTimeout(() => {
                            this.$router.push('/main/customer');
                        }, 2000);
                    }, 2000);
                }
            },
            (error) => {
                this.triggerAlert = true;
                this.messageType = { type: 'error' };
                this.message = error.response.data.detail;
                setTimeout(() => {
                    this.loading = false;
                }, 1000);
            }
        );
    }
}
</script>
