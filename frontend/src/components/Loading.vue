<template>
    <v-dialog v-model="loading" persistent width="300">
        <v-card color="primary" dark v-if="isSuccess === false">
            <v-card-text>
                Please stand by
                <v-progress-linear
                    indeterminate
                    color="white"
                    class="mb-0"
                ></v-progress-linear>
            </v-card-text>
        </v-card>
        <v-card color="success" dark v-else>
            <v-card-text>
                {{ loadingMessage }}
                <v-progress-linear
                    indeterminate
                    color="white"
                    class="mb-0"
                ></v-progress-linear>
            </v-card-text>
        </v-card>
    </v-dialog>
</template>
<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';

@Component
export default class AlertBox extends Vue {
    @Prop({ default: false }) loading!: boolean;
    @Prop({ default: false }) isSuccess!: boolean;
    @Prop({ default: '' }) loadingMessage!: string;
}
</script>
