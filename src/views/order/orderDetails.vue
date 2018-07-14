<template>
  <div class="m-step">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-step-content">
      <div class="m-step-part">
        <step :list="step"></step>
      </div>
      <div class="details-middle-left">
        <div class="m-step-part">
          <h4>订单详情</h4>
          <div class="order-info-part">
            <div class="left-text-div">
              <div class="left-text">订单编号：</div>
              <div class="left-text">付款方式：</div>
              <div class="left-text" style="margin-left: 0.4rem;">买 家：</div>
              <div class="left-text">配送方式：</div>
              <div class="left-text">收货地址：</div>
              <div class="left-text" style="margin-top: 0.2rem">买家留言：</div>
            </div>
            <div class="left-value-div">
              <div class="left-text">{{order.orderNo}}</div>
              <div class="left-text">{{order.payType}}</div>
              <div class="left-text">{{order.buyer}}</div>
              <div class="left-text">{{order.sendType}}</div>
              <div class="left-text">{{order.buyerAddress}}</div>
              <div class="left-text" style="margin-top: 0.2rem">{{order.memo}}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="details-middle-right">

    </div>
    <div class="details-bottom">

    </div>
  </div>
</template>

<script>
  // 1、待付款，2、待发货，3、已发货，4、已完成，5、已关闭，6、退款中
  import allOrder from "../../common/json/allOrder";
  import pageTitle from '../../components/common/title';
  import step from '../../components/common/step';
  export default {
    name: "orderDetails",
    data() {
      return {
        name: '所有订单 > 订单详情',
        order: '',
        step:[
          {
            name:'买家下单',
            time: '2018-07-12 14:25:20',
            active:true,
            next:true
          },
          {
            name:'买家付款',
            time: '2018-07-12 14:34:21',
            active:true,
            next:true
          },
          {
            name:'商家发货',
            time: '待发货',
            active:false,
            next:false
          },
          {
            name:'交易完成',
            time: '未完成',
            active:false,
            next:false
          }
        ]
      }
    },
    components: {
      'pageTitle': pageTitle,
      'step': step
    },
    methods: {
      freshClick(){
        console.log('fresh');
      }
    },
    created() {
      this.order = this.$route.query.order;
      console.log(this.order)
    },
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  @import "../../common/css/activity";
  .m-step {
    .m-step-content {
      .details-middle-left {
        width: 40%;
        .order-info-part {
          height: 1.5rem;
          .left-text-div {
            width: 20%;
            float: left;
          }
          .left-value-div {
            width: 80%;
            float: right;
          }
          .left-text {
            font-size: 14px;
            color: @greyColor;
            line-height: 0.12rem;
            margin: 0 0 0.1rem 0.2rem;
          }
        }
      }
    }
  }
</style>
