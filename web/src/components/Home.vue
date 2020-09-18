<template>
    <div class="row app">
        <div class="col-md-6 offset-3">
            <div class="form-group">
                <input class="form-control" type="text" :placeholder="placeholder" v-model="image_url">
                <br>
                <a class="btn btn-outline-danger" v-if="image_url" href="#" @click="addImage">show image</a>
                <a v-if="showed" style="margin-left: 10px" class="btn btn-outline-danger" href="#"
                   @click="recognizeImage">recognize image</a>
            </div>
        </div>
        <br><br>
        <div class="col-md-12">
            <div v-if="img" class="canvas">
                <img class="image_size" :src="img.src" alt="">
            </div>
        </div>
        <div class="col-md-6 offset-3" style="margin-top: 30px;">
            <div v-if="process">
                <div v-if="data">
                    <ul class="list-group">
                        <li class="list-group-item li-result" v-for="res in data" v-bind:key="res.id">
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
                image_url: null,
                data: null,
                process: false,
                showed: false,
                placeholder: 'Copy Image URL'
            }
        },
        methods: {
            addImage() {
                if (!this.isValidImageAddress()) {
                    this.image_url = null;
                    this.placeholder = 'Not an image address!';
                    return;
                }
                if (this.process) {
                    this.process = false;
                }
                this.img = new Image();
                this.img.src = this.image_url;
                this.image_url = null;
                this.placeholder = 'Image Retrieved! (paste another image)';
                this.showed = true;
            },
            isValidImageAddress() {
                let arr = [ "jpeg", "jpg", "gif", "png" ];
                for(let element of arr) {
                    if(this.image_url.includes(element)) {
                        return true;
                    }
                }
                return false;
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
    .app {
        padding: 100px;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
        background-color: #E3E3E3;
    }

    .canvas {
        height: 300px;
        width: 300px;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
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

    .li-result {
        color: #C60021;
        font-weight: bold;
    }
</style>