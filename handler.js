Vue.component('pkg-link', {
    props: ['value', 'text'],
    template: '<a href="" class="link" v-on:click="clickLink">{{ value }}{{ text }}</a>',
    methods: {
        clickLink : function(event) {
            event.preventDefault();
            var pkg_name = event.target.text.replace(", ", "");
            fetch('http://localhost:8080/packages/' + pkg_name)
            .then(response => response.json())
            .then(json => {
                app.$data.pkg = json;
                app.$data.mode = 'pkg';
            });
        }
    }
});

Vue.component('pkg-depends', {
    props: ['list'],
    template: `
        <div>
            <span v-for="(package, index) in list">
                <span v-if="index < list.length-1">
                    <pkg-link v-bind:value="package" text=", " />
                </span>
                <span v-if="index === list.length-1">
                    <pkg-link v-bind:value="package" text="" />
                </span>
            </span>
        </div>
    `
});

Vue.component('pkg-div', {
    props: ['pkg'],
    template: `
        <div>
            <a href="" v-on:click="goBack">Back to the list</a>
            <p><b>Package:</b></p>
            <p class="txt">{{ pkg.name }}</p>
            <p><b>Description:</b></p>
            <p class="txt">{{ pkg.description }}</p>
            <p><b>Dependencies:</b></p>
            <div class="txt" v-if="pkg.depends">
                <pkg-depends v-bind:list="pkg.depends"></pkg-depends>
            </div>
            <p><b>Recursive dependencies:</b></p>
            <div class="txt" v-if="pkg.r_depends">
                <pkg-depends v-bind:list="pkg.r_depends"></pkg-depends>
            </div>
        </div>
    `,
    methods: {
        goBack: function(event) {
            event.preventDefault();
            app.$data.mode = 'list';
        }
    }
});

Vue.component('pkg-list', {
    props: ['list'],
    template: `
        <div>
            <div class="list-item" v-for="package in list">
                <pkg-link v-bind:value="package"/>
            </div>  
        </div>
    `
});

const app = new Vue({
    el: '#app',
    data: {
        mode: 'list',
        packages: [],
        pkg: {}
    },
    created() {
        fetch('http://localhost:8080/packages')
        .then(response => response.json())
        .then(json => {
            this.packages = json;
            this.mode = 'list';
        });
    }
});