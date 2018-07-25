<template>
  <div>
    <div class="order-index-top">
      <div class="order-box">
        <div class="order-text">待付款</div>
        <div class="order-number">{{orderSituation.paying_count}}</div>
      </div>
      <div class="order-box">
        <div class="order-text">待发货</div>
        <div class="order-number">{{orderSituation.deliver_count}}</div>
      </div>
      <div class="order-box">
        <div class="order-text">已发货</div>
        <div class="order-number">{{orderSituation.received_count}}</div>
      </div>
      <div class="order-box">
        <div class="order-text">退款中</div>
        <div class="order-number">{{orderSituation.refund_count}}</div>
      </div>
    </div>
    <div class="order-subTitle">
      <img class="subTitle-img" src="../../assets/images/timeLine.png"/>
      <div class="subTitle-text">流量趋势</div>
    </div>
  </div>
</template>

<script>
    export default {
      props: ["orderSituation"],
      name: "order-index-top",
      data() {
        return {
          orderNumber: '',
          toPay: '',
          toSend: '',
          income: ''
        }
      },
      methods: {

      }
    }

</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .order-index-top {
    background-color: @sectionBgColor;
    padding: 0.15rem;
    height: 0.7rem;
    border-bottom-left-radius: 0.1rem;
    border-bottom-right-radius: 0.1rem;
    .order-box {
      width: 25%;
      float: left;
      .order-text {
        text-align: center;
      }
      .order-number {
        color: @mainColor;
        text-align: center;
        margin-top: 0.2rem;
        font-size: 40px;
      }
    }
  }
  .order-subTitle {
    height: 0.22rem;
    margin: 0.1rem 0 0.1rem 0;
    padding: 0.15rem;
    border-radius: 0.1rem;
    background-color: @sectionBgColor;
    .subTitle-img {
      float: left;
      width: 0.3rem;
      height: 0.2rem;
      margin-left: 0.1rem;
    }
    .subTitle-text {
      float: left;
      margin-left: 0.2rem;
    }
  }
</style>
