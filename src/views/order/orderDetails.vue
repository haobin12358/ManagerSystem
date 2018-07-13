<template>
  <div class="m-step">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-step-content">
      <div class="m-step-part">
        <step :list="step"></step>
      </div>
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
      this.order = this.$route.query;
      // console.log(this.order)
    },
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  @import "../../common/css/activity";
  .m-step {
    .details-top {
    }
  }
</style>
