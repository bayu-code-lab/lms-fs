<template>
    <v-alert
        v-model="triggerAlert"
        transition="fade-transition"
        dismissible
        v-bind="messageType"
    >
        {{ message }}
    </v-alert>
</template>
<script lang="ts">
import { Component, Vue, Prop, Watch, Emit } from 'vue-property-decorator';

@Component
export default class AlertBox extends Vue {
    public alert: boolean = false;
    @Prop({ default: false }) triggerAlert!: boolean;
    @Prop({ default: '' }) message!: string;
    @Prop({ default: {} }) messageType!: {};
}
</script>
