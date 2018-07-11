<template>
  <div>
    <div class="order-index-top">
      <div class="order-box">
        <div class="order-text">{{days}}下单笔数</div>
        <div class="order-number">{{orderNumber}}</div>
      </div>
      <div class="order-box">
        <div class="order-text">待付款</div>
        <div class="order-number">{{toPay}}</div>
      </div>
      <div class="order-box">
        <div class="order-text">待发货</div>
        <div class="order-number">{{toSend}}</div>
      </div>
      <div class="order-box">
        <div class="order-text">{{days}}收入</div>
        <div class="order-number number-red">￥{{income}}</div>
      </div>
    </div>
    <div class="order-subTitle">
      <img class="subTitle-img" src="../../assets/images/timeLine.png"/>
      <div class="subTitle-text">流量趋势</div>
    </div>
  </div>
</template>

<script>
  import orderIndex from '../../common/json/orderIndex'
  import orderIndexTop from "../../components/common/order-index-top";
    export default {
      props: ["days"],
      name: "order-index-top",
      data() {
        return {
          orderNumber: '',
          toPay: '',
          toSend: '',
          income: ''
        }
      },
      components: {
        'orderIndexTop': orderIndexTop
      },
      methods: {
        changeTopData(i) {
          this.orderNumber = orderIndex[i].orderNumber;
          this.toPay = orderIndex[i].toPay;
          this.toSend = orderIndex[i].toSend;
          this.income = orderIndex[i].income;
        }
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
      float: left;
      margin-left: 1.5rem;
      .order-text {
        text-align: center;
      }
      .order-number {
        color: @mainColor;
        text-align: center;
        margin-top: 0.2rem;
        font-size: 0.3rem;
      }
      .number-red {
        color: @red;
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
