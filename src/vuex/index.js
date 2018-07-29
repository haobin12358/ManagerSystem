import Vue from 'vue';
import Vuex from 'vuex';
import side from '../common/json/side';


Vue.use(Vuex);

let store= new Vuex.Store({
	state: {
	  side:null,
    role:'',
    route: null,
    now:null,
    number:0,
    isCollapse:false,
    token:'',
    activity:{
      COabo:'',
      COname:'',
      COstatus:'',
      COstart:'',
      COend:'',
      COfilter:0,
      COother:'',
      COdiscount:0,
      COamount:0,
      COtype:'满减',
      COunit:'元',
      COnumber:0,
      COimage:[],
      COotherType:'0',
      COotherContent:[
        '','',''
      ],
      COproduct:'全店商品',
      PRids:[],
      COgenre:'活动'
    },
    discount:{
      COabo:'',
      COname:'',
      COstatus:'',
      COstart:'',
      COend:'',
      COfilter:'',
      COother:'',
      COdiscount:'',
      COamount:'',
      COtype:'',
      COnumber:'',
      COgenre:'优惠券'
    }
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
