webpackJsonp([6],{CXuy:function(e,t){},"UKK+":function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});a("v4fL");var o=a("XiPb"),s=a("QGdL"),r=a("P9l9"),i=(a("zL8q"),a("mtWM")),d=a.n(i),m={name:"orderDetails",data:function(){return{name:"所有订单 > 订单详情",order:"",OMid:"",step:[],orderStatus:"",searchWhere:!1,whereList:["2018-07-15 14:25:23 快递已到达杭州萧山分拨中心","2018-07-14 14:25:23 快递已到达杭州分拨中心","2018-07-13 14:25:23 快递已到达分拨中心","2018-07-13 14:25:23 快递已到达杭州萧山分拨中心","2018-07-13 14:25:23 快递已到达杭州萧山分拨中心","2018-07-13 14:25:23 快递已到达杭州萧山分拨中心","2018-07-13 14:25:23 快递已到达杭州萧山分拨中心","2018-07-13 14:25:23 快递已到达杭州萧山分拨中心","2018-07-13 14:25:23 快递已到达杭州萧山分拨中心","2018-07-13 14:25:23 快递已到达杭州萧山分拨中心"],star:0,toSendForm:!1,memoForm:!1,form:{name:"",region:""},memoForms:{name:""},formLabelWidth:"0.6rem"}},components:{pageTitle:o.a,step:s.a},methods:{freshClick:function(){console.log("fresh")},getData:function(e){var t=this,a={token:localStorage.getItem("token"),OMid:e};d.a.get(r.a.get_order_by_LOid,{params:a}).then(function(e){200==e.data.status?(t.order=e.data.data,t.setStep()):t.$message.error(e.data.message)},function(e){t.$message.error(e.data.message)})},toSend:function(){var e=this;if(this.toSendForm=!1,"已支付"==this.order.OMstatus){var t=localStorage.getItem("token"),a={OMid:this.order.OMid,OMstatus:"已发货"};d.a.post(r.a.update_order_status+"?token="+t,a).then(function(t){200==t.data.status?(e.order.OMstatus="已发货",e.orderStatus=e.order.OMstatus,e.setStep(),e.$message({message:t.data.message,type:"success"})):e.$message.error(t.data.message)},function(t){e.$message.error(t.data.message)})}},setStep:function(){"已取消"==this.order.OMstatus?(this.step=[{name:"买家下单",time:this.order.OMtime,active:!0,next:!0},{name:"买家支付",time:"订单已取消",active:!1,next:!1},{name:"商家发货",time:"订单已取消",active:!1,next:!1},{name:"交易完成",time:"未完成",active:!1,next:!1}],this.orderStatus=this.order.OMstatus):"未支付"==this.order.OMstatus?(this.step=[{name:"买家下单",time:this.order.OMtime,active:!0,next:!0},{name:"买家支付",time:"待支付",active:!1,next:!1},{name:"商家发货",time:"待发货",active:!1,next:!1},{name:"交易完成",time:"未完成",active:!1,next:!1}],this.orderStatus=this.order.OMstatus):"支付中"==this.order.OMstatus?(this.step=[{name:"买家下单",time:this.order.OMtime,active:!0,next:!0},{name:"买家支付",time:"支付中",active:!0,next:!0},{name:"商家发货",time:"待发货",active:!1,next:!1},{name:"交易完成",time:"未完成",active:!1,next:!1}],this.orderStatus=this.order.OMstatus):"已支付"==this.order.OMstatus?(this.step=[{name:"买家下单",time:this.order.OMtime,active:!0,next:!0},{name:"买家支付",time:"已支付",active:!0,next:!0},{name:"商家发货",time:"待发货",active:!1,next:!1},{name:"交易完成",time:"未完成",active:!1,next:!1}],this.orderStatus=this.order.OMstatus):"已发货"==this.order.OMstatus?(this.step=[{name:"买家下单",time:this.order.OMtime,active:!0,next:!0},{name:"买家支付",time:"已支付",active:!0,next:!0},{name:"商家发货",time:"已发货",active:!0,next:!0},{name:"交易完成",time:"未完成",active:!1,next:!1}],this.orderStatus=this.order.OMstatus):"已收货"==this.order.OMstatus?(this.step=[{name:"买家下单",time:this.order.OMtime,active:!0,next:!0},{name:"买家支付",time:"已支付",active:!0,next:!0},{name:"买家收货",time:"已收货",active:!0,next:!0},{name:"交易完成",time:"未完成",active:!1,next:!1}],this.orderStatus=this.order.OMstatus):"已完成"==this.order.OMstatus?(this.step=[{name:"买家下单",time:this.order.OMtime,active:!0,next:!0},{name:"买家支付",time:"已支付",active:!0,next:!0},{name:"买家收货",time:"已收货",active:!0,next:!0},{name:"交易完成",time:"已完成",active:!0,next:!0}],this.orderStatus=this.order.OMstatus):"已评价"==this.order.OMstatus?(this.step=[{name:"买家下单",time:this.order.OMtime,active:!0,next:!0},{name:"买家支付",time:"已支付",active:!0,next:!0},{name:"交易完成",time:"已完成",active:!0,next:!0},{name:"填写评价",time:"已评价",active:!0,next:!0}],this.orderStatus=this.order.OMstatus):"退款中"==this.order.OMstatus&&(this.step=[{name:"买家下单",time:this.order.OMtime,active:!0,next:!0},{name:"买家支付",time:"已支付",active:!0,next:!0},{name:"买家收货",time:"已收货",active:!0,next:!0},{name:"退款完成",time:"退款中",active:!1,next:!0}],this.orderStatus=this.order.OMstatus)}},created:function(){this.OMid=this.$route.query.OMid,this.getData(this.OMid)}},l={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"m-step"},[a("page-title",{attrs:{title:e.name},on:{freshClick:e.freshClick}}),e._v(" "),a("div",{staticClass:"m-step-content"},[a("div",{staticClass:"m-step-part"},[a("step",{attrs:{list:e.step}})],1),e._v(" "),a("div",{staticClass:"details-middle-left"},[a("div",{staticClass:"m-step-part"},[a("h4",[e._v("订单详情")]),e._v(" "),a("div",{staticClass:"order-info-part"},[e._m(0),e._v(" "),a("div",{staticClass:"left-value-div"},[a("div",{staticClass:"left-text"},[e._v(e._s(e.order.OMid))]),e._v(" "),a("div",{staticClass:"left-text"},[e._v(e._s(e.order.OMstatus))]),e._v(" "),a("div",{staticClass:"left-text"},[e._v(e._s(e.order.LOname))]),e._v(" "),a("div",{staticClass:"left-text"},[e._v(e._s(e.order.LOtelphone))]),e._v(" "),a("div",{staticClass:"left-text"},[e._v(e._s(e.order.OMlogisticsName))]),e._v(" "),a("div",{staticClass:"left-text"},[e._v(e._s(e.order.LOdetail))]),e._v(" "),a("div",{staticClass:"left-text"},[e._v(e._s(e.order.OMabo))])])])])]),e._v(" "),a("div",{staticClass:"details-middle-right"},[a("div",{staticClass:"m-step-part"},[a("div",{staticClass:"right-top-top"},[e._m(1),e._v(" "),a("div",{staticClass:"right-text"},[a("div",{staticClass:"right-top"},[e._v("订单状态："+e._s(e.orderStatus))])])]),e._v(" "),a("div",{staticClass:"right-middle"},[a("el-dialog",{staticStyle:{padding:"0"},attrs:{title:"收货地址",visible:e.toSendForm},on:{"update:visible":function(t){e.toSendForm=t}}},[a("div",{staticClass:"buyer-info"},[a("div",{staticClass:"buyer-info-title"},[e._v("买家收货信息")]),e._v(" "),a("div",{staticClass:"info-left-text-div"},[a("div",{staticClass:"info-text"},[e._v("订单编号：")]),e._v(" "),a("div",{staticClass:"info-text"},[e._v("联系对象：")]),e._v(" "),a("div",{staticClass:"info-text"},[e._v("联系方式：")]),e._v(" "),a("div",{staticClass:"info-text"},[e._v("收货地址：")]),e._v(" "),a("div",{staticClass:"info-text"},[e._v("下单时间：")]),e._v(" "),a("div",{staticClass:"info-text"},[e._v("备注：")])]),e._v(" "),a("div",{staticClass:"info-right-text-div"},[a("div",{staticClass:"info-text-value"},[e._v(e._s(e.order.OMid))]),e._v(" "),a("div",{staticClass:"info-text-value"},[e._v(e._s(e.order.LOname))]),e._v(" "),a("div",{staticClass:"info-text-value"},[e._v(e._s(e.order.LOtelphone))]),e._v(" "),a("div",{staticClass:"info-text-value"},[e._v(e._s(e.order.LOdetail))]),e._v(" "),a("div",{staticClass:"info-text-value"},[e._v(e._s(e.order.OMtime))]),e._v(" "),a("div",{staticClass:"info-text-value"},[e._v(e._s(e.order.OMabo))])])]),e._v(" "),a("div",{staticClass:"send-info"},[a("el-form",{staticClass:"send-info-form",attrs:{model:e.form}},[a("el-form-item",{attrs:{label:"物流公司:","label-width":e.formLabelWidth}},[a("el-select",{staticStyle:{width:"1.7rem"},attrs:{placeholder:"",size:"small"},model:{value:e.form.region,callback:function(t){e.$set(e.form,"region",t)},expression:"form.region"}},[a("el-option",{attrs:{label:"顺丰速运",value:"顺丰速运"}}),e._v(" "),a("el-option",{attrs:{label:"EMS",value:"EMS"}})],1)],1),e._v(" "),a("el-form-item",{attrs:{label:"快递单号:","label-width":e.formLabelWidth}},[a("el-input",{staticStyle:{width:"1.7rem"},attrs:{"auto-complete":"off",size:"small"},model:{value:e.form.name,callback:function(t){e.$set(e.form,"name",t)},expression:"form.name"}})],1)],1)],1),e._v(" "),a("div",{staticStyle:{"text-align":"center","margin-bottom":"0.2rem"},attrs:{slot:"footer"},slot:"footer"},[a("el-button",{staticClass:"right-button",staticStyle:{"background-color":"#fff",color:"#000"},on:{click:function(t){e.toSendForm=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{staticClass:"right-button",on:{click:e.toSend}},[e._v("确 定")])],1)]),e._v(" "),a("el-dialog",{attrs:{title:"备 注",visible:e.memoForm,width:"4rem"},on:{"update:visible":function(t){e.memoForm=t}}},[a("el-form",{attrs:{model:e.memoForms}},[a("el-form-item",{attrs:{label:"备 注：","label-width":e.formLabelWidth}},[a("el-input",{staticStyle:{width:"90%"},attrs:{"auto-complete":"off",size:"small",type:"textarea",autosize:{minRows:2,maxRows:5}},model:{value:e.memoForms.name,callback:function(t){e.$set(e.memoForms,"name",t)},expression:"memoForms.name"}})],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{staticClass:"right-button",staticStyle:{"background-color":"#fff",color:"#000"},on:{click:function(t){e.memoForm=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{staticClass:"right-button",on:{click:function(t){e.memoForm=!1}}},[e._v("确 定")])],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"物流信息",visible:e.searchWhere,width:"4rem"},on:{"update:visible":function(t){e.searchWhere=t}}},[e._l(e.whereList,function(t){return a("div",{staticClass:"where-list"},[e._v("\n              "+e._s(t)+"\n            ")])}),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{staticClass:"right-button",on:{click:function(t){e.searchWhere=!1}}},[e._v("确 定")])],1)],2),e._v(" "),"已取消"==e.order.OMstatus?a("div",[a("div",{staticStyle:{height:"0.3rem"}},[e._v("用户已取消订单")])]):e._e(),e._v(" "),"未支付"==e.order.OMstatus?a("div",[a("div",{staticStyle:{height:"0.3rem"}},[e._v("等待用户支付")])]):e._e(),e._v(" "),"支付中"==e.order.OMstatus?a("div",[a("div",{staticStyle:{height:"0.3rem"}},[e._v("等待支付款项到账")])]):e._e(),e._v(" "),"已支付"==e.order.OMstatus?a("div",[a("el-button",{staticClass:"right-button",on:{click:function(t){e.toSendForm=!0}}},[e._v("发 货")])],1):e._e(),e._v(" "),"已发货"==e.order.OMstatus?a("div",[a("el-button",{staticClass:"right-button",on:{click:function(t){e.searchWhere=!0}}},[e._v("查看物流进度")])],1):e._e(),e._v(" "),"已收货"==e.order.OMstatus?a("div",[a("div",{staticStyle:{height:"0.3rem"}},[e._v("用户已收货")])]):e._e(),e._v(" "),"已完成"==e.order.OMstatus?a("div",[a("div",{staticStyle:{height:"0.3rem"}},[e._v("该订单已完成")])]):e._e(),e._v(" "),"已评价"==e.order.OMstatus?a("div",[a("div",{staticStyle:{height:"0.3rem"}},[e._v("用户已评价该订单")])]):e._e(),e._v(" "),"退款中"==e.order.OMstatus?a("div",[a("div",{staticStyle:{height:"0.3rem"}},[e._v("该订单正在退款中")])]):e._e()],1),e._v(" "),e._m(2)])]),e._v(" "),a("div",{staticClass:"details-bottom"},[a("div",{staticClass:"bottom-total"},[e._v("总计："+e._s(e.order.OMprice)+"元")]),e._v(" "),a("el-table",{staticClass:"details-table",staticStyle:{width:"100%"},attrs:{data:e.order.order_abo,border:"",stripe:"",size:"mini"}},[a("el-table-column",{attrs:{align:"center",prop:"PBimage",label:"商品图片"},scopedSlots:e._u([{key:"default",fn:function(e){return[a("img",{staticStyle:{width:"0.5rem",height:"0.5rem"},attrs:{src:e.row.PBimage,alt:""}})]}}])}),e._v(" "),a("el-table-column",{attrs:{align:"center",prop:"PRname",label:"商品名称"}}),e._v(" "),a("el-table-column",{attrs:{align:"center",prop:"PBprice",label:"单价"}}),e._v(" "),a("el-table-column",{attrs:{align:"center",prop:"PRnumber",label:"数量"}}),e._v(" "),a("el-table-column",{attrs:{align:"center",prop:"PRinfo",label:"商品简介"}}),e._v(" "),a("el-table-column",{attrs:{align:"center",prop:"PRtype",label:"商品类型"}}),e._v(" "),a("el-table-column",{attrs:{align:"center",prop:"PRbrand",label:"商品分类"}})],1)],1)])],1)},staticRenderFns:[function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"left-text-div"},[a("div",{staticClass:"left-text"},[e._v("订单编号：")]),e._v(" "),a("div",{staticClass:"left-text"},[e._v("订单状态：")]),e._v(" "),a("div",{staticClass:"left-text",staticStyle:{"margin-left":"0.38rem"}},[e._v("买 家：")]),e._v(" "),a("div",{staticClass:"left-text"},[e._v("联系方式：")]),e._v(" "),a("div",{staticClass:"left-text"},[e._v("快递方式：")]),e._v(" "),a("div",{staticClass:"left-text"},[e._v("收货地址：")]),e._v(" "),a("div",{staticClass:"left-text"},[e._v("买家留言：")])])},function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"left-icon"},[t("img",{attrs:{src:a("i7m9"),height:"50"}})])},function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"right-bottom-text"},[t("div",{staticClass:"bottom-title"},[this._v("温馨提示")]),this._v(" "),t("div",{staticClass:"bottom-text"},[this._v("•如果无法发货，请及时与买家联系并说明情况后进行退款；")]),this._v(" "),t("div",{staticClass:"bottom-text"},[this._v("•买家申请退款后，需征得卖家同意后再发货，否则卖家有权拒收货物；")]),this._v(" "),t("div",{staticClass:"bottom-text"},[this._v("•买家付款后超过7天仍未发货，将有权申请平台客服介入发起退款维权。")])])}]};var n=a("VU/8")(m,l,!1,function(e){a("CXuy")},"data-v-1f7522ce",null);t.default=n.exports},i7m9:function(e,t){e.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF8AAABdCAIAAABM5i2pAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAABAFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMDY3IDc5LjE1Nzc0NywgMjAxNS8wMy8zMC0yMzo0MDo0MiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ1dWlkOjVEMjA4OTI0OTNCRkRCMTE5MTRBODU5MEQzMTUwOEM4IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjcwMEI5N0FBODQwQjExRTg4Q0I5OEI0RTZENEM4OUM4IiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjcwMEI5N0E5ODQwQjExRTg4Q0I5OEI0RTZENEM4OUM4IiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIElsbHVzdHJhdG9yIENTNiAoV2luZG93cykiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo2RkU3QTM3QUYwODNFODExOTBDRDlFNUMxQThGQ0YyQyIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo2RUU3QTM3QUYwODNFODExOTBDRDlFNUMxQThGQ0YyQyIvPiA8ZGM6dGl0bGU+IDxyZGY6QWx0PiA8cmRmOmxpIHhtbDpsYW5nPSJ4LWRlZmF1bHQiPuWQjuWPsOeuoeeQhuezu+e7nzA3MDnvvIgy77yJPC9yZGY6bGk+IDwvcmRmOkFsdD4gPC9kYzp0aXRsZT4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7XfMF3AAALAUlEQVR42uxd+VPbWBK2btmyzWEnAYcrnCHkgCFkZ6uyP+xu7W9b+x/vzFZtZsJMSEISmECAzHBjiAHbki3LsrQtMwFb71nyoWcZdl6lUsE2lvS9Pr7u192hTNMM/LFqLLbdFzTNkiyX5Cz8beTzhqqammbqRdMwLt6nYLEcxXO0INLBIC1JTCTChCMUw9xQdExTPzstnpwUT1Ol83OzVGr4GwCxaJTtjXHxOBuLU2ybNpUiqFmmCYhoB3taMmkWi559LU1zt24LiQR3p480TETQMdR8YXu7sLNjFFSCt86yfCIhjowy0ej1QAcMirq5WdjfD5hG26wDqFtwYoqNxToXHZCX/PpaYW8v4JMT5GLx4IMHbFd3h6FjGPmtTXVzowFzS1EMOCMpDF6JEkWa5QIsc/ltYKSMQgE8WimnGLLckBUXBoeC96dpQegIdPTzM2X5Lbhn9ysxDBuPww6zvb1MJFqvhy4zAMvlpVLFk2Nw/+4X4nlp5iF/d8BXdEwz/2k9v7nhrEoUuJj+fiExANC0ylksZnCmHewXDvZdYeL7E9LjJxTH+YAOSL78ekk/TTl53lBIvDcqDAy2eItYXdaODtXPn0FynW8gPP+0FUvUDDp6Oi2/+globq0PgE0RJyYFkG2KImqJ9VQqt77msEkgudKT2aa1rGF0isdJkJpalhLEJDg5JQ6PAGdrm7cqJo+U1VUjp9T6ANjp4PgEcXS0/T15ebkWlwFVDz185JW/aMwiGYa68cnBCIqjY6EHMwTRKUPzFnt5EBnp0WM+cdffkFpPnytvXpcUvBAJwyNwk0TQ0Y6O5NevsNAw0a7I0wUwgZ2QczB1XXm/rB0c4FVsYjI4dd9jdIBuZBdfYm2N5Thn53xJLzgsULH82kfsW6D74si9egNed++Zz8tLr7DQgMMOfzPfadBYMjI+AXuG9Zi51RVgld6gA9Yuu/QzsBsMNOMToZmHpH120wt4Fug7xnWapvzmtZHLeaBZyof3he3fvHIBVW44lcq+/MHhA91//wdEYS1ipB0eABaouQSKGH3+HOhQ87JTTCax0AgDAy1C07ZlmcWZR1jvll9fb16zIFAG44++DjGk9Hg2cH2WMDIC9hFjubc2AaMm0cl9/AU1N8D0wvMLnvBgxo0BtK5WV37qwQzbG0MNkPLunXMITdeiVYXdHfR1aW7eFyrcciaCsnwrz9teLmXShe3thtHJra6ioIJ8cvF44HouWhSlhxiinPu05nAigEEH6AAa9YKcQyzn5XY6Hieg++yBhU4k+Dt9dvXSNPXXzw2gk/+EMeahmUfesj7npA/F8SQkCIgy+hSATi3xsaMDUqOf2VNKXCzO9/UFrv8CDUD9F0CDJS4YdNTPGDELTk+3+zF4jtA3i2PjqNiqv/2KdV5V6BiqqiWP7IJz6xbb3UMEAincZs260GhUfMoPnnRBR9vbxbiq0bHAzVrC8AiFUDZtb8cFHesM08bZJIm7dfuGoQOUDfyXHZ3ksVnUaqJTUpRSNmOHeXDIF+NCOpcmDA6j6QhUueiKmPMIwxG8ODNrv3FxXRAtopFK0QmdkxP7V3T3eBjsdFpswff129H5cmIzu/RlSKafndq91W3fLA4Jrmx/ujt3UOKjZzIYdOBVU9ftvx+/RdY61jYuNMcRV66eXtRzlaqZ8O9vl5BMB/wm290duLkLQgoGOUS2ZXy+opPN2n15tKud55n+2OaeHjSngUNHRtGJ+mhcKPKahX1G20nh7+igOXomHCbOytoCgRM6kmQ3zLpemRH9ik4+32Y+1hGkOSShL5oVtSX0BWCXxdQVdFv0NdXQjr2hQbWR8zhDq5YdbO6H4omLPeW3ZlmF9cg9VKJRRqek4xweG/g/WGgCt1KNynbHMLB0wM+b9l2s0AxG2/eN61h3VoEOTkzQwOKmCogLOlgTgzVGPpoDQgv1SJVo0LX20NSKfqLTHrEyDQw6FZe+kB0G3StDzROnqn4TTkPF1CVVHoXTX9mXPctVqq/+51qvEq6IlxavaDB7yaltYbqBxKUECHGw95//8lN2sjIaGNs1Cxtz6un0jZcdPZNGYu8Ihu+waCwvy21w6j6jg7RZ2HD4KjtoqwUu03yTllnUMDm/ahyuNAvNRaGnFDdpFb+kMNWWvVXZwitHzsXi2mFVibh1wkW4etKqf9jbzW98uui3gh0KTkxiy/y8Rwc5v6PFIFN9tH8VZ6HnM9bpaCZD0ihmzr//d2515bIVDf4BP55//x2ajfPaXRnaEaaeomYUyt2+g6aCCvu75KQmu/gjtkXPUOTM4kui4GjHSVO3s2QOqVGiKzki29tr/5a9PWx+o/UFCuXQvQgAwQfIoYMWU1Ish57fVWUwBOTU3CgUCjX6VVrdvYN9F7tAzCeUFNk6FK5efH8/mtKqQodP3MWU1W1tEFF8tyjXy+EQ9ifaQr0VttqEtuUN+IFBO9LZrHZ06H0Y4Za3JhSmg71HdZaxRpD0uqATKBclo7bZ6nXyekKBayMg6kE8Wfn1j6glFe/h69toJNAI80hxAkQVVt2hp0sYGHSoG4S3BESKPQkdrFkUSDAs3L1bFzqwgpNTOMjXHFqsm1igOOH5p1iA4MXot38mQCLM3If3mOcdn6hVMYB5lYl2oSVf5X7Ld97eLYR83X/9W2jmYSVG8GPX87+QqKoqN9UgQTkI6VDN6j989xqYrvR/vkO7HaVHj4XhkWsZjqfPMy9eoL3ikYU/oWVOTrJzoYrixCT6OtD8Uub65X2AHMivl1BoABcHaAIO51nBsTGrhMd2GatN9BW2TbSDsTHlN0tokQnQF2zXTV3oBCg6PDuHmiu4jLz0czOTzXxaysoHLO227J2bdXM6CwWOFJp+gNHhszOrc98wOh+a3NpHbIcI35+opxTb5aQYyCFauWoFQcfHliZ3NkAAjbqJCYPAT0lP6mptdT9Hl2bnmAimSk5LHmV/WkTzAB1ia8CBYKGBWDy88KzOs9a6Jj2Ag8/88F8sG2Qikcizbzuq6NuiZstv8bEhTcPd1t+/We+UEIhFMz++qFEHxYfn5gmFRQ1nJ2QZbCKaTi/fKBWe+6ahQS8NTJiBICW7WFOVxLGx4NQ05WsRb2F3x8rDYg+aAJrZuUbbPhqbTgSM07I1NXJ6EMFKj2exqQDSC3iG8uF9zfEfTUETaGKyVUmRASCHKRtwE6H7022zRCAp6tam+nmr5rAthgnPLzTX89HMVDTXgXFwQ8LQMOgaLQaJ4gJcBmJLh/w0bFJk4RlK+gmiU0bIyH38xaGT+8JBAOkSh0c81zWQX2vK7O6Oc3YVHAW4i1badVqaVQmUR3m37DoYkZEk8BR8f3/Te3hpXOCK2sE+2hOObkxo6r7V0draeKBWJ3kCNMrKe62+cwvrUCge53piTFcXECV3SmYYICZ6Og1w6Kkv9cwLDZRn6wAV9qTPw5sZueAscisr8CQN/RYtlmeTCwLFcZf1p2ZJN4tWs4Kh5q0T0UZuj+J4EBlheNiriVLezVc2DXV7W93YIDpx2skPjNwLjk94e5Lh8fRpcKtgLMG/Gu0qrAM4LP84OkqisYPMXHfT1JLJws62Rc+IDaMG+yIMDQG9Ile+SxH9/yRAy7TDwyL8OT31apY5mFu+r59PJGxVbNcPnQrmViymUhcDWkq4Dl3He6TBwbHd3VwsxsbilTWhNwQdm95ZU8kVxcgplm/SCgFdv8KLYcHE0jxPlT0aE5KYsOQ6+u4GoXN9Fv0HBA7rfwIMAG/ZRffzUFniAAAAAElFTkSuQmCC"},v4fL:function(e,t){e.exports=[{orderNoText:"订单号：",orderNo:"E25642366453654",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"2",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"2",realPay:"35.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"2",realPay:"35.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"2",realPay:"35.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"2",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453655",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"3",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"3",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453656",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"3",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"3",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]},{orderNoText:"订单号：",orderNo:"E25642366453657",payTypeText:"支付方式：",payType:"微信安全支付-代销",outOrderNoText:"外部订单号：",outOrderNo:"152646462341",payNoText:"支付流水号：",payNo:"152646462341",memo:"-",sendType:"快递配送",buyerAddress:"杭州市萧山区奔竞二路与民和路交叉口西北200米",buyer:"maomao",goods:[{goodsName:"商品一",goodsPrice:"29.00",goodsNumber:"2",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"58.00"},{goodsName:"商品二",goodsPrice:"35.00",goodsNumber:"1",afterSales:"-",buyer:"maomao",orderTime:"2018-07-12 15:32:36",status:"4",realPay:"35.00"}]}]}});
//# sourceMappingURL=6.87812445b5a94dd25825.js.map