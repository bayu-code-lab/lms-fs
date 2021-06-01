<template>
    <section>
            <v-autocomplete
                v-model="model"
                :items="items"
                :loading="isLoading"
                :search-input.sync="search"
                hide-no-data
                hide-selected
                item-text="desc"
                item-value="id"
                label="Customer"
                placeholder="Start typing to Search"
                append-icon="search"
                required
                return-object
            ></v-autocomplete>
        <v-expand-transition>
            <v-list v-if="model">
                <v-list-item v-for="(field, i) in fields" :key="i">
                    <v-list-item-content>
                        <v-list-item-desc
                            v-text="field.value"
                        ></v-list-item-desc>
                        <v-list-item-subdesc
                            v-text="field.key"
                        ></v-list-item-subdesc>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-expand-transition>
    </section>
</template>
<script>
import { apiUrl } from '@/env';
export default {
    data: () => ({
        descriptionLimit: 60,
        entries: [],
        isLoading: false,
        model: null,
        search: null,
    }),

    computed: {
        fields() {
            if (!this.model) {
                return [];
            }

            return Object.keys(this.model).map((key) => {
                return {
                    key,
                    value: this.model[key] || 'n/a',
                };
            });
        },
        items() {
            return this.entries.map((entry) => {
                const Description =
                    entry.desc.length > this.descriptionLimit
                        ? entry.desc.slice(0, this.descriptionLimit) + '...'
                        : entry.desc;

                return Object.assign({}, entry, { Description });
            });
        },
    },

    emits: ['customer-id-data'],

    watch: {
        model(value) {
            this.$emit('customer-id-data', value['id']);
        },
        search(val) {
            // Items have already been loaded
            if (this.items.length > 0) {
                return;
            }

            // Items have already been requested
            if (this.isLoading) {
                return;
            }

            this.isLoading = true;

            // Lazily load input items
            fetch(`${apiUrl}/api/v1/customers-search`, {
                method: 'get',
                headers: new Headers({
                    'Authorization': 'Bearer ' + localStorage.token,
                    'Content-Type': 'application/json',
                }),
            })
                .then((res) => res.json())
                .then((res) => {
                    const { count, entries } = res;
                    this.count = count;
                    this.entries = entries;
                })
                // .catch((err) => {
                // })
                .finally(() => (this.isLoading = false));
        },
    },
};
</script>
