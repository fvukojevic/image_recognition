<template>
    <div class="row">
        <div class="col-md-6 offset-3">
            <div class="form-group">
                <input class="form-control" type="text" placeholder="Paste image url" v-model="src">
                <br>
                <a class="btn btn-outline-primary" v-if="src" href="#" @click="addImage">show image</a>
                <a v-if="showed" style="margin-left: 10px" class="btn btn-outline-primary" href="#"
                   @click="recognizeImage">recognize image</a>
            </div>
        </div>
        <br><br>
        <div class="col-md-12">
            <div v-if="img" class="canvas">
                <img class="image_size" :src="img.src" alt="">
            </div>
            <br><br>
            <div v-if="process">
                <div v-if="data">
                    <ul>
                        <li v-for="res in data" v-bind:key="res.id">
                            {{res[0]}}: {{ (res[1] * 100).toFixed(1)}} %
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
                process: false,
                showed: false,
            }
        },
        methods: {
            addImage() {
                if (this.process) {
                    this.process = false;
                }
                this.img = new Image();
                this.img.src = this.src;
                this.showed = true;
            },
            recognizeImage() {
                this.process = true;
                if (this.data !== null) {
                    this.data = null;
                }
                this.$http.post('/classify', {
                    url: this.img.src
                }).then(result => {
                    let response = [];
                    for (let key in result.data) {
                        response.push([key, result.data[key]])
                    }
                    this.data = response.sort((a, b) => {
                        return b[1] - a[1]
                    });
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
    .canvas {
        height: 300px;
        width: 300px;
        border: 1px solid black;
        display: flex;
        margin: 0 auto;
        text-align: center;
    }

    .image_size {
        height: 100%;
        width: 100%;
        object-fit: contain;
        object-position: center;
    }
</style>