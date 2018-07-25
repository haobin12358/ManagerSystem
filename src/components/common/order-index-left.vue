<template>
  <div class="order-index-left">
    <div class="order-box">
      <div class="order-text">付款笔数</div>
      <div class="order-number">{{orderSituation.week_paying_count}}</div>
    </div>
    <div class="order-box">
      <div class="order-text">退款笔数</div>
      <div class="order-number">{{orderSituation.week_payed_count}}</div>
    </div>
  </div>
</template>

<script>
  export default {
    props: ["orderSituation"],
    name: "order-index-left",
    data() {
      return {
        oldOrderNumber: '',
        oldPay: ''
      }
    },
    methods: {
      // changeLeftData(i) {
      //   this.oldOrderNumber = orderIndex[i].oldOrderNumber;
      //   this.oldPay = orderIndex[i].oldPay
      // }
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
