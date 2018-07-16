import Vue from 'vue';
import Vuex from 'vuex';


Vue.use(Vuex);

let store= new Vuex.Store({
	state: {
	  side:null,
	    route: {},
	    now:null,
	    number:0,
    isCollapse:false
	},
	mutations: {
	    add(state,route) {
	    	state.now=route.name;
	    	var len=Object.keys(state.route);
	    	if (len.length<5||!!state.route[route.name]) {
    			state.route[route.name]=route.path;
	    	}else{
	    		delete state.route[len[0]]
    			state.route[route.name]=route.path;
	    	}
	    },
	    remove(state,name){
	    	Vue.delete(state.route,name)
	    	// delete state.route[name]


        // this.$store.commit('remove',name)调用此方法
	    }
	}
})


export default store
