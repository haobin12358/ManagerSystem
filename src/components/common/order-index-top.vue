<template>
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
        changeData(i) {
          console.log(orderIndex[i].orderNumber);
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
    padding: 0.2rem 0 0.25rem 0;
    width: 100%;
    height: 0.7rem;
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
</style>
