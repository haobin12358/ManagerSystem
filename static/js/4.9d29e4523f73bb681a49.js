webpackJsonp([4],{"3D6a":function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=a("XiPb"),r={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",{staticClass:"order-index-top"},[a("div",{staticClass:"order-box"},[a("div",{staticClass:"order-text"},[t._v("待付款")]),t._v(" "),a("div",{staticClass:"order-number"},[t._v(t._s(t.orderSituation.paying_count))])]),t._v(" "),a("div",{staticClass:"order-box"},[a("div",{staticClass:"order-text"},[t._v("待发货")]),t._v(" "),a("div",{staticClass:"order-number"},[t._v(t._s(t.orderSituation.deliver_count))])]),t._v(" "),a("div",{staticClass:"order-box"},[a("div",{staticClass:"order-text"},[t._v("已发货")]),t._v(" "),a("div",{staticClass:"order-number"},[t._v(t._s(t.orderSituation.received_count))])]),t._v(" "),a("div",{staticClass:"order-box"},[a("div",{staticClass:"order-text"},[t._v("退款中")]),t._v(" "),a("div",{staticClass:"order-number"},[t._v(t._s(t.orderSituation.refund_count))])])]),t._v(" "),t._m(0)])},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"order-subTitle"},[e("img",{staticClass:"subTitle-img",attrs:{src:a("7TXO")}}),this._v(" "),e("div",{staticClass:"subTitle-text"},[this._v("流量趋势")])])}]};var o=a("VU/8")({props:["orderSituation"],name:"order-index-top",data:function(){return{orderNumber:"",toPay:"",toSend:"",income:""}},methods:{}},r,!1,function(t){a("wGKC")},"data-v-50779b7a",null).exports,s={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"order-index-left"},[a("div",{staticClass:"order-box"},[a("div",{staticClass:"order-text"},[t._v("下单笔数")]),t._v(" "),a("div",{staticClass:"order-number"},[t._v(t._s(t.orderSituation.ordered_count))])]),t._v(" "),a("div",{staticClass:"order-box"},[a("div",{staticClass:"order-text"},[t._v("收入总额")]),t._v(" "),a("div",{staticClass:"order-number number-red"},[t._v("￥"+t._s(t.orderSituation.omprice))])])])},staticRenderFns:[]};var n=a("VU/8")({props:["orderSituation"],name:"order-index-left",data:function(){return{oldOrderNumber:"",oldPay:""}},methods:{}},s,!1,function(t){a("EpFP")},"data-v-7b8ac116",null).exports,d=a("z1Sx"),l=a("P9l9"),c=(a("zL8q"),a("mtWM")),u=a.n(c),v={data:function(){return{name:"订单概况",activeName:"seven",days:"近七日",leftDays:"近七日",echartsId:"myEcharts",orderSituation:[],option1:{},option7:{},option30:{},lazyStatus:!0}},components:{orderIndexTop:o,orderIndexLeft:n,pageTitle:i.a,myEcharts:d.a},methods:{freshClick:function(){console.log("fresh")},getData:function(t){for(var e=this,a={token:localStorage.getItem("token"),days:t},i=[],r=1;r<31;r++){var o="第"+r+"天";i.push(o)}u.a.get(l.a.get_order_situation,{params:a}).then(function(a){200==a.data.status?(e.orderSituation=a.data.data,1==t?e.option1={title:{text:"昨日数据",x:"center"},tooltip:{trigger:"item",formatter:"{a} <br/>{b} : {c} ({d}%)"},legend:{orient:"vertical",left:"left",data:["未支付","已支付"]},series:[{name:"访问来源",type:"pie",radius:"55%",center:["50%","60%"],color:["#EEB5B3","#A0D1C1"],data:[{value:e.orderSituation.paying_count,name:"未支付"},{value:e.orderSituation.week_paying_list[0],name:"已支付"}],itemStyle:{emphasis:{shadowBlur:10,shadowOffsetX:0,shadowColor:"rgba(0, 0, 0, 0.5)"}}}]}:7==t?e.option7={title:{text:"近七日数据",subtext:"注：下单笔数不包括退单数据"},tooltip:{trigger:"axis"},legend:{data:["下单笔数","付款笔数"]},grid:{left:"3%",right:"4%",bottom:"3%",containLabel:!0},xAxis:{type:"category",boundaryGap:!1,data:["周一","周二","周三","周四","周五","周六","周日"]},yAxis:{type:"value"},series:[{name:"下单笔数",type:"line",smooth:!0,color:"#EEB5B3",data:e.orderSituation.week_payed_list},{name:"付款笔数",type:"line",smooth:!0,color:"#A0D1C1",data:e.orderSituation.week_paying_list}]}:30==t&&(e.option30={title:{text:"近三十日数据",subtext:"注：下单笔数不包括退单数据"},tooltip:{trigger:"axis"},legend:{data:["下单笔数","付款笔数"]},grid:{left:"3%",right:"4%",bottom:"3%",containLabel:!0},xAxis:{type:"category",boundaryGap:!1,data:i},yAxis:{type:"value"},series:[{name:"下单笔数",type:"line",smooth:!0,color:"#EEB5B3",data:e.orderSituation.week_payed_list},{name:"付款笔数",type:"line",smooth:!0,color:"#A0D1C1",data:e.orderSituation.week_paying_list}]})):e.$message.error(a.data.message)},function(t){e.$message.error(t.data.message)})},handleClick:function(t,e){"one"==t.name?(this.days="昨日",this.leftDays="昨日",this.getData(1)):"seven"==t.name?(this.days="七日",this.leftDays="近七日",this.getData(7)):"thirty"==t.name&&(this.days="近三十日",this.leftDays="近三十日",this.getData(30))}},mounted:function(){this.getData(7)}},m={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"m-order-index"},[a("page-title",{attrs:{title:t.name},on:{freshClick:t.freshClick}}),t._v(" "),a("div",{staticClass:"m-content"},[a("el-tabs",{on:{"tab-click":t.handleClick},model:{value:t.activeName,callback:function(e){t.activeName=e},expression:"activeName"}},[a("el-tab-pane",{attrs:{label:"昨日",name:"one",lazy:t.lazyStatus}},[a("order-index-top",{ref:"one",attrs:{orderSituation:t.orderSituation}}),t._v(" "),a("order-index-left",{ref:"leftOne",attrs:{orderSituation:t.orderSituation}}),t._v(" "),a("my-echarts",{staticClass:"my-echarts",attrs:{id:"echartsId1",option:t.option1,width:650,height:250}})],1),t._v(" "),a("el-tab-pane",{attrs:{label:"近七日",name:"seven",lazy:t.lazyStatus}},[a("order-index-top",{ref:"seven",attrs:{orderSituation:t.orderSituation}}),t._v(" "),a("order-index-left",{ref:"leftSeven",attrs:{orderSituation:t.orderSituation}}),t._v(" "),a("my-echarts",{staticClass:"my-echarts",attrs:{id:"echartsId7",option:t.option7,width:650,height:250}})],1),t._v(" "),a("el-tab-pane",{attrs:{label:"近三十日",name:"thirty",lazy:t.lazyStatus}},[a("order-index-top",{ref:"thirty",attrs:{orderSituation:t.orderSituation}}),t._v(" "),a("order-index-left",{ref:"leftThirty",attrs:{orderSituation:t.orderSituation}}),t._v(" "),a("my-echarts",{staticClass:"my-echarts",attrs:{id:"echartsId30",option:t.option30,width:750,height:250}})],1)],1)],1)],1)},staticRenderFns:[]};var b=a("VU/8")(v,m,!1,function(t){a("3EvB")},"data-v-4923c0a1",null);e.default=b.exports},"3EvB":function(t,e){},"7TXO":function(t,e){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADEAAAAgCAIAAAA0dAd1AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAABAFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMDY3IDc5LjE1Nzc0NywgMjAxNS8wMy8zMC0yMzo0MDo0MiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ1dWlkOjVEMjA4OTI0OTNCRkRCMTE5MTRBODU5MEQzMTUwOEM4IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkY0RENDQUMwODQwQTExRThCQ0ZDQUVGNTQ0NUY3QUExIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkY0RENDQUJGODQwQTExRThCQ0ZDQUVGNTQ0NUY3QUExIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIElsbHVzdHJhdG9yIENTNiAoV2luZG93cykiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpENTZBOEFEREVGODNFODExOTBDRDlFNUMxQThGQ0YyQyIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDpENDZBOEFEREVGODNFODExOTBDRDlFNUMxQThGQ0YyQyIvPiA8ZGM6dGl0bGU+IDxyZGY6QWx0PiA8cmRmOmxpIHhtbDpsYW5nPSJ4LWRlZmF1bHQiPuWQjuWPsOeuoeeQhuezu+e7nzA3MDnvvIgy77yJPC9yZGY6bGk+IDwvcmRmOkFsdD4gPC9kYzp0aXRsZT4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz5AQnHBAAADRElEQVR42syY6VPaQBjGk03IBkFRFMWjU23VeoCc9v//WuTwqEen2nYqCvUEh0ru9I0o2VhygDNAhmFCjt3fPnneI9DNZpMaso0dHhRdltXKpXL1ZyiYtNq9Ui4DDaVpTHiSHbQwFeWirP1ttA+i0dHBMGn1GqAo1SoI8+oUHQz2lUlXFLVaUcrnWqNhdw0K9lEnMI1QKlKq6nQRTaNAAPWNCY1PcCurMKvTNYEAhRDqa+JZeIcTSYphbGUKBg2yPrubmYrw2W3KRgsw0wCYYFNvbv4Pt3YiGACTcv5bPju191Pfn51SuZS+nViNP26ayeejeb47Jr35KB0f2cnu/siur6SjQ/KIb3mFz372LX0gzdRFDdaFppDP66IAZDiRcoidzkB3d+LBPqXrJtDiEnyMnY/LtN8Pq20FnSGYl15FF0WhsKM/Pj4vKBTCqQzNel2P9lAXCnkyW7LzC9z6hgX69pZSFGZmxhOTLklCPtcGetE5iNNZmuPcgRoNEdYjy2Y6iEbxZtwheSJXILGYfwXUmskAFUVXC4rFggVoKoI3Yi7Z3LlkirtFu3oJoELuC8zq9MQBSDK5mYkwjm9RbsUDOQGVCtrDgxmrmMfJFHwTswrCTq4j9JPABZ0wBhob4xwLixuTqkr7u1q9bgJxHJ/NtioDPTJimTufAxd3EJjs1AJBnEx7DItOTJom7pUgekkgw9F+AwXils9so5e4bRFAWKn3d+Z69nYtAvv9OJ3xEhA2TAB0sGcBYlmIfBKCxhgQISOQuoqlonp9/XT7vslnrAfzAISx92RmzQW6bowIvToJlM6gsVBHw4Ee5PRGRxYKabUaWS6wVdQuddJ16fArCQR+BFd2BHrGTabAYeQIJBDcjlPpboEsTNLJsVKtEGeQMeVE2LEbYvBWgpmJdhoYQQmyW48nJgPoomwZMZ5wAWpfGYtDrXjVVkMeYsJhqqfNYJJPv8O7hGXE2BYTiXj2JA3Fy/d+sX2A29hkItO9d+7yjzP510/LBJsxZrrrEX0rq1DhDaBPa+zs3Jvadkh65G9YMRud7W0s6ISYycnePGTRiVtbb8sO++zc/JuGezPQc0/na712sSy86wzDXxr/BBgAGiiFFrnJ0EkAAAAASUVORK5CYII="},EpFP:function(t,e){},wGKC:function(t,e){}});
//# sourceMappingURL=4.9d29e4523f73bb681a49.js.map