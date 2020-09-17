<template>
    <div class="row">
        <div class="col-md-6 offset-3">
            <div class="form-group">
                <input class="form-control" type="text" placeholder="Paste image url" v-model="src">
                <br>
                <a class="btn btn-outline-primary" v-if="src" href="#" @click="addImage">show image</a>
                <a style="margin-left: 10px" class="btn btn-outline-primary" v-if="src" href="#"
                   @click="recognizeImage">recognize image</a>
            </div>
            <div v-if="img">
                <img class="image_size" :src="this.img.src" alt="">
            </div>
            <div v-if="process">
                <div v-if="data">
                    <ul>
                        <li v-for="(value, key) in data" v-bind:key="key">
                            {{key}}: {{ (value * 100).toFixed(1)}} %
                        </li>
                    </ul>
                </div>
                <div v-else>
                    <app-animation></app-animation>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Animations from './helper/Animations';

    export default {
        name: 'Home',
        data() {
            return {
                img: null,
                src: null,
                data: null,
                process: false
            }
        },
        methods: {
            addImage() {
                if(this.process) {
                    this.process = false;
                }
                this.img = new Image();
                this.img.src = this.src;
            },
            recognizeImage() {
                this.process = true;
                this.$http.post('/classify', {
                    url: this.img.src
                }).then(result => {
                    this.data = result.data;
                }).catch(error => {
                    console.log(error)
                })
            }
        },
        components: {
            'app-animation': Animations
        }
    }
</script>

<style>
    .image_size {
        object-fit: contain;
    }
</style>