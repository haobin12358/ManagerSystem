<template>
  <div class="m-user-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <div class="m-left">
        <div class="one-part">
          <h3 class="m-title">待办事项</h3>
          <div class="m-scroll">
           <ul>
             <li class="m-label m-red" @click="goPage('待处理')">
               <span>待处理</span>
               <span>{{index.dealing_sum}}</span>
             </li>
             <li class="m-label m-green" @click="goPage('待审批')">
               <span>待审批</span>
               <span>{{index.approvaling_sum}}</span>
             </li>
             <li class="m-label m-blue" @click="goPage('21')">
               <span>待发货</span>
               <span>{{index.deliver_sum}}</span>
             </li>
           </ul>
            <div class="m-activity">
              <h3>订单管理</h3>
              <ul>
                <li v-for="item in orderStatusList">
                  <span>{{item.status}}</span>
                  <span class="m-red" @click="goPage(item.index)">{{item.value}}</span>
                </li>
              </ul>
            </div>
            <div class="m-activity-left">
              <h3>活动管理</h3>
              <ul>
                <li>
                  <span>正在进行的活动：</span>
                  <router-link to="/activity/storeActivity" >
                    <span class="m-red">{{index.active_sum}}</span>
                  </router-link>
                </li>
              </ul>
            </div>
            <div class="m-activity-right">
              <h3>优惠券管理</h3>
              <ul>
                <li>
                  <span>正在发放的优惠券：</span>
                  <router-link to="/activity/discountCoupon" >
                    <span class="m-red">{{index.couponse_sum}}</span>
                  </router-link>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="one-part">
          <h3 class="m-title">实时数据</h3>
          <ul>
            <li class="m-data-li">
              <div class="m-data-top">
                <span class="m-data-icon icon-money"></span>
                <div class="m-data-label">
                  <p>支付金额</p>
                  <p>{{index.today_payed}}</p>
                </div>
              </div>
              <div class="m-data-bottom">
                <p>昨日全天</p>
                <p>{{index.yesterday_payed}}</p>
              </div>
            </li>
            <li class="m-data-li">
              <div class="m-data-top">
                <span class="m-data-icon icon-order"></span>
                <div class="m-data-label">
                  <p>访客数</p>
                  <p>{{index.today_vistor}}</p>
                </div>
              </div>
              <div class="m-data-bottom">
                <p>昨日全天</p>
                <p>{{index.yesterday_vistor}}</p>
              </div>
            </li>
            <li class="m-data-li">
              <div class="m-data-top">
                <span class="m-data-icon icon-pay"></span>
                <div class="m-data-label">
                  <p>支付买家数</p>
                  <p>{{index.today_omprice}}</p>
                </div>
              </div>
              <div class="m-data-bottom">
                <p>昨日全天</p>
                <p>{{index.yesterday_omprice}}</p>
              </div>
            </li>
            <li class="m-data-li">
              <div class="m-data-top">
                <span class="m-data-icon icon-person"></span>
                <div class="m-data-label">
                  <p>支付订单数</p>
                  <p>{{index.today_order}}</p>
                </div>
              </div>
              <div class="m-data-bottom">
                <p>昨日全天</p>
                <p>{{index.yesterday_order}}</p>
              </div>
            </li>
          </ul>
        </div>
      </div>
      <div class="m-right">
        <div class="one-part">
          <h3 class="m-title">店铺周数据</h3>
          <div class="m-store-data">
            <div class="m-store-content">
              <ul>
                <li class="m-store-label icon-green">
                  <div class="m-store-content">
                    <p>周访客人数：</p>
                    <p></p>
                    <p class="m-decline">{{index.visitors_sum}}</p>
                  </div>
                  <div class="m-store-icon-box">
                    <span class="m-store-icon icon-person"></span>
                    <span>访客</span>
                  </div>
                </li>
                <li class="m-store-label icon-red">
                  <div class="m-store-content">
                    <div>
                      <p>下单数</p>
                      <p class="m-decline">{{index.ordered_sum}}</p>
                    </div>
                    <div>
                      <p>下单总金额</p>
                      <p class="m-decline">{{index.ordered_price_sum}}</p>
                    </div>
                  </div>
                  <div class="m-store-icon-box">
                    <span class="m-store-icon icon-make-order"></span>
                    <span>下单</span>
                  </div>
                </li>
                <li class="m-store-label icon-yellow">
                  <div class="m-store-content">
                    <div>
                      <p>支付数</p>
                      <p class="m-decline">{{index.paid_num}}</p>
                    </div>
                    <div>
                      <p>支付总金额</p>
                      <p class="m-decline">{{index.payed_price_sum}}</p>
                    </div>
                    <div>
                      <p>客单价</p>
                      <p class="m-decline">{{index.pct}}</p>
                    </div>
                  </div>
                  <div class="m-store-icon-box">
                    <span class="m-store-icon icon-pay"></span>
                    <span>支付</span>
                  </div>
                </li>
              </ul>
              <span class="m-arrows"></span>
            </div>

            <p class="m-percent">
              <span class="m-percent-content">下单转化率：{{index.vtp*100}}% </span>
              <span class="m-green m-arrow"></span>
              <span class="m-green m-arrow-head"></span>
            </p>
            <p class="m-percent">
              <span class="m-percent-content">支付转化率：{{index.otp*100}}% </span>
              <span class="m-red m-arrow"></span>
              <span class="m-red m-arrow-head"></span>
            </p>
            <p class="m-percent">
              <span class="m-percent-content">下单-支付转化率：{{index.vtp*100}}% </span>
              <span class="m-yellow m-arrow"></span>
              <span class="m-yellow m-arrow-head"></span>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import api from '../../api/api';
  import {Message} from 'element-ui';
  import axios from 'axios';
    export default {
      data() {
          return {
            name:'工作模块管理',
            index: {},
            orderStatusList: [
              { status: '已取消：', index: 0, value: 0 },
              { status: '未支付：', index: 1, value: 1 },
              { status: '支付中：', index: 2, value: 2 },
              { status: '已发货：', index: 4, value: 4 },
              { status: '已完成：', index: 6, value: 6 },
              { status: '已评价：', index: 7, value: 7 },
            ]
          }
      },
      components:{
        pageTitle
      },
      methods: {
        freshClick(){
          console.log('fresh');
        },
        // 获取用户首页
        getData() {
          axios.get(api.get_userIndex+'?token='+localStorage.getItem('token')).then(res => {
            if (res.data.status == 200) {
              this.index = res.data.data
              // console.log(this.index)
              for(let i=0;i<this.orderStatusList.length;i++) {
                this.orderStatusList[i].value = this.index.om_count[this.orderStatusList[i].value*7]
              }
            } else {
              this.$message.error(res.data.message);
            }
          }, error => {
            this.$message.error(error.data.message);
          })
        },
        goPage(page) {
          if(page == '待审批') {
            this.$router.push({path: '/index/adminIndex', query: 0})
          }else {
            this.$router.push({path: '/order/allOrder', query: 0})
          }
        }
      },
      created() {
        this.getData()
      }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
.m-content{
  font-size: 0.14rem;
  margin-top: 0.1rem;
  &:after{
    content: '';
    display: block;
    clear: both;
  }
  .m-left{
    width: 5.4rem;
    .one-part{
      background-color: #fff;
      height: 2.6rem;
      margin-bottom: 0.1rem;
      h3.m-title{
        padding: 0.1rem 0.4rem;
        border-bottom: 1px solid @borderColor;
        margin: 0 0.05rem;
      }
      .m-scroll{
        height: 2.3rem;
        overflow-y:auto ;
        margin-top: 0.1rem;
        padding: 0 0.4rem;
      }
      ul{
        .flex-row(flex-start);
        flex-flow: wrap;
        width: 100%;
        margin: 0 0.05rem;
      }
      .m-label{
        padding: 0.15rem;
        .flex-row(space-between);
        color: #fff;
        background-color: #edb3b1;
        width: 22%;
        margin-right: 2%;
        border-radius: 5px;
        &.m-green{
          background-color: #9fd0bf;
        }
        &.m-blue{
          background-color: #91aeb5;
        }
      }
      .m-activity{
        h3{
          margin: 0.1rem 0 ;
        }
        ul{
          li{
            font-size: 0.12rem;
            color: #999;
            width: 33%;
            margin-bottom: 0.1rem;
            span.m-red{
              color: @red;
              margin-left: 0.1rem;
            }
          }
        }
      }
      .m-activity-left{
        width: 50%;
        float: left;
        h3{
          margin: 0.1rem 0 ;
        }
        ul{
          li{
            font-size: 0.12rem;
            color: #999;
            width: 60%;
            /*margin-bottom: 0.1rem;*/
            span.m-red{
              color: @red;
            }
          }
        }
      }
      .m-activity-right{
        width: 50%;
        float: left;
        h3{
          margin: 0.1rem 0 ;
        }
        ul{
          li{
            font-size: 0.12rem;
            color: #999;
            width: 60%;
            /*margin-bottom: 0.1rem;*/
            span.m-red{
              color: @red;
            }
          }
        }
      }
      .m-data-li{
        width: 34.3%;
        padding: 0.1rem 0.4rem;
        font-size: 0.14rem;
        .m-data-top{
          .flex-row(flex-start);
          .m-data-icon{
            display: block;
            width: 0.47rem;
            height: 0.47rem;
            background: url("../../common/images/icon-data-money.png");
            background-size: 100%  100%;
            margin-right:0.1rem;
            &.icon-order{
              background: url("../../common/images/icon-data-order.png");
              background-size: 100%  100%;
            }
            &.icon-pay{
              background: url("../../common/images/icon-data-pay.png");
              background-size: 100%  100%;
            }
            &.icon-person{
              background: url("../../common/images/icon-data-person.png");
              background-size: 100%  100%;
            }
          }
          .m-data-label{
            line-height: 0.3rem;
          }
        }
        &:nth-child(odd){
          border-right:1px solid @borderColor
        }
        &:nth-child(3){
          border-top: 1px solid @borderColor;
        }
        &:nth-child(4){
          border-top: 1px solid @borderColor;
        }
        .m-data-bottom{
          color: #999;
          font-size: 0.12rem;
          line-height: 0.3rem;
          .flex-row(space-between);
        }
      }
    }
  }
  .m-right{
    width: 5.4rem;
    .one-part{
      background-color: #fff;
      height: 5.3rem;
      margin-bottom: 0.1rem;
      h3.m-title{
        padding: 0.1rem 0.4rem;
        border-bottom: 1px solid @borderColor;
        margin: 0 0.05rem;
      }
      .m-store-data{
        padding: 0.2rem 0.15rem;
        border-bottom: 1px solid @borderColor;
        margin: 0 0.05rem;
        .m-store-content {
          .flex-row(flex-start);
          margin-bottom: 0.2rem;
          ul {
            li.m-store-label {
              width: 3.4rem;
              height: 0.8rem;
              padding: 0 0.24rem;
              background: url("../../common/images/icon-data-green.png");
              background-size: 100% 100%;
              .flex-row(space-between);
              &.icon-red {
                background: url("../../common/images/icon-data-red.png");
                background-size: 100% 100%;
              }
              &.icon-yellow {
                background: url("../../common/images/icon-data-yellow.png");
                background-size: 100% 100%;
              }
              .m-store-content {
                line-height: 0.4rem;
                font-size: 0.12rem;
                p {
                  height: 0.3rem;
                }
                .flex-row(flex-start);
                div {
                  margin-right: 0.2rem;
                }
                .m-decline {
                  color: @red;
                  text-align: center;
                }
              }
              .m-store-icon-box {
                color: #fff;
                .flex-row(flex-start);
                .m-store-icon {
                  display: inline-block;
                  width: 0.32rem;
                  height: 0.32rem;
                  background: url("../../common/images/icon-visitor.png");
                  background-size: 100% 100%;
                  margin-right: 0.1rem;
                  &.icon-make-order {
                    background: url("../../common/images/icon-make-order.png");
                    background-size: 100% 100%;
                  }
                  &.icon-pay {
                    background: url("../../common/images/icon-pay.png");
                    background-size: 100% 100%;
                  }
                }
              }

            }
          }
          span.m-arrows{
            width: 0.6rem;
            height: 2rem;
            display: block;
            background: url("../../common/images/icon-arrow.png");
            background-size: 100% 100%;
          }
        }
        .m-percent{
          font-size: 0.12rem;
          line-height: 0.24rem;
          .flex-row(flex-start);
          .m-percent-content{
            width: 1.5rem;
            margin-left: 0.2rem;
          }
          .m-arrow{
            display: block;
            width: 0.4rem;
            height: 0.02rem;
            background-color:#a9d5c6 ;
            &.m-red{
              background-color:#edb3b1 ;
            }
            &.m-yellow{
              background-color:#fee1bf ;
            }
          }
          .m-arrow-head{
            display: block;
            width: 0;
            border: 0.05rem solid #a9d5c6;
            border-top-color: transparent;
            border-bottom-color: transparent;
            border-right-color: transparent;
            &.m-red{
              border: 0.05rem solid #edb3b1;
              border-top-color: transparent;
              border-bottom-color: transparent;
              border-right-color: transparent;
            }
            &.m-yellow{
              border: 0.05rem solid #fee1bf;
              border-top-color: transparent;
              border-bottom-color: transparent;
              border-right-color: transparent;
            }
          }
        }
      }
    }
  }
}
  /*滚动条样式*/
  .m-scroll::-webkit-scrollbar {/*滚动条整体样式*/
    width: 5px;     /*高宽分别对应横竖滚动条的尺寸*/
    height: 5px;
  }
  .m-scroll::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 5px @scrollColor;
    background: @scrollColor;
  }
  .m-scroll::-webkit-scrollbar-track {/*滚动条里面轨道*/
    -webkit-box-shadow: inset 0 0 5px @scrollBgColor;
    border-radius: 10px;
    background:@scrollBgColor;
  }
</style>
