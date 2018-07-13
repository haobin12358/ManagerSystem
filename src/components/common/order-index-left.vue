<template>
  <div class="order-index-left">
    <div class="order-box">
      <div class="order-text">{{leftDays}}下单笔数</div>
      <div class="order-number">{{oldOrderNumber}}</div>
    </div>
    <div class="order-box">
      <div class="order-text">{{leftDays}}付款笔数</div>
      <div class="order-number">{{oldPay}}</div>
    </div>
  </div>
</template>

<script>
  import orderIndex from '../../common/json/orderIndex'
  // import orderIndexLeft from "../../components/common/order-index-left";
  export default {
    props: ["leftDays"],
    name: "order-index-left",
    data() {
      return {
        oldOrderNumber: '',
        oldPay: ''
      }
    },
    components: {
      // 'orderIndexLeft': orderIndexLeft
    },
    methods: {
      changeLeftData(i) {
        this.oldOrderNumber = orderIndex[i].oldOrderNumber;
        this.oldPay = orderIndex[i].oldPay
      }
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .order-index-left {
    width: 20%;
    float: left;
    height: 2rem;
    border-radius: 0.1rem;
    padding: 0.3rem 0 0.25rem 0;
    background-color: @sectionBgColor;
    .order-box {
      .order-text {
        text-align: center;
      }
      .order-number {
        color: @mainColor;
        text-align: center;
        margin: 0.2rem 0 0.2rem 0;
        font-size: 40px;
      }
    }
  }
</style>
