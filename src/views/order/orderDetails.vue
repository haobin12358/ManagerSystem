<template>
  <div class="order-details">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="details-top">
      123
    </div>
    <div class="details-middle-left">

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
  export default {
    name: "orderDetails",
    data() {
      return {
        name: '所有订单 > 订单详情'
      }
    },
    components: {
      'pageTitle': pageTitle
    },
    methods: {
      freshClick(){
        console.log('fresh');
      }
    },
    created() {
      let order = this.$route.query;
      console.log(order)
    },
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .order-details {
    .details-top {

    }
  }
</style>
