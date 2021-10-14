<template>
    <v-container fluid>
        <v-card class="ma-3 pa-3">
            <v-card-title primary-title>
                <div class="headline primary--text">Hapus Data Murid/Guru</div>
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
                    <v-form ref="form">
                        <v-text-field
                            label="NIK/NISN"
                            v-model="id"
                            readonly
                            ><v-icon slot="prepend" color="primary"
                                >payment</v-icon
                            ></v-text-field
                        >
                        <v-text-field
                            label="Nama Lengkap"
                            v-model="fullName"
                            readonly
                            ><v-icon slot="prepend" color="primary"
                                >perm_identity</v-icon
                            ></v-text-field
                        >
                        <v-text-field
                            label="Kelas (Hanya Untuk Murid)"
                            v-model="grade"
                            type="number"
                            readonly
                            ><v-icon slot="prepend" color="primary"
                                >gite</v-icon
                            ></v-text-field
                        >
                        <v-text-field
                            label="Jurusan (Hanya Untuk Murid)"
                            v-model="major"
                            readonly
                            ><v-icon slot="prepend" color="primary"
                                >biotech</v-icon
                            ></v-text-field
                        >
                        <v-text-field
                            label="Angkatan (Hanya Untuk Murid)"
                            v-model="batchOfYear"
                            type="number"
                            readonly
                            ><v-icon slot="prepend" color="primary"
                                >calendar_today</v-icon
                            ></v-text-field
                        >
                        <v-text-field
                            label="Alamat"
                            type="text"
                            v-model="address"
                            :rules="addressRules"
                            readonly
                            ><v-icon slot="prepend" color="primary"
                                >maps_home_work</v-icon
                            ></v-text-field
                        >
                    </v-form>
                </template>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancel"><v-icon left>arrow_back</v-icon>Kembali</v-btn>
                <v-btn color="error" v-model="dialog" @click="openDialog">
                    <v-icon color="white" left>delete</v-icon>Hapus
                </v-btn>
                <v-dialog v-model="dialog" persistent max-width="290">
                    <v-card>
                        <v-card-title class="text-h5">
                            Peringatan
                        </v-card-title>
                        <v-card-text
                            >Data ini akan dihapus dari database apakah anda
                            yakin?</v-card-text
                        >
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                                color="green darken-1"
                                text
                                @click="dialog = false"
                            >
                                Tidak
                            </v-btn>
                            <v-btn color="red darken-1" text @click="submit">
                                Ya
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script lang="ts">
import axios from 'axios';
import { apiUrl } from '@/env';
import AlertBox from '@/components/AlertBox.vue';
import Loading from '@/components/Loading.vue';
import { Component, Vue } from 'vue-property-decorator';
import {
    dispatchGetCustomer,
    dispatchDeleteCustomer,
} from '@/store/customer/actions';
import { readOneCustomer } from '@/store/customer/getters';

@Component({
    name: 'helper',
    components: {
        AlertBox,
        Loading,
    },
})
export default class EditCustomer extends Vue {
    public dialog = false;
    public loading = false;
    public isSuccess = false;
    public triggerAlert = false;
    public message = '';
    public messageType = {};
    public loadingMessage = 'Data berhasil dihapus';
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

    public openDialog() {
        this.dialog = true;
    }

    public async submit() {
        this.dialog = false;
        await this.execApi(this.customer!.id);
    }

    public async execApi(id) {
        this.loading = true;
        axios.defaults.headers.common['Authorization'] =
            'Bearer ' + localStorage.token;
        axios.defaults.headers.common['Content-Type'] = 'application/json';
        await axios.delete(`${apiUrl}/api/v1/customers/${id}`).then(
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

    get customer() {
        return readOneCustomer(this.$store)(
            +this.$router.currentRoute.params.id
        );
    }
}
</script>
