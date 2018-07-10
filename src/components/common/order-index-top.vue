<template>
  <div class="order-index-top">
    <div class="order-one">
      <div class="order-text">{{days}}下单笔数</div>
      <div class="order-number">{{orderNumber}}</div>
    </div>
    <div class="order-two">
      <div class="order-text">待付款</div>
      <div class="order-number">{{toPay}}</div>
    </div>
    <div class="order-three">
      <div class="order-text">待发货</div>
      <div class="order-number">{{toSend}}</div>
    </div>
    <div class="order-four">
      <div class="order-text">{{days}}收入</div>
      <div class="order-number-red">￥{{income}}</div>
    </div>
  </div>
</template>

<script>
  import orderIndex from '../../common/json/orderIndex'
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
      methods: {
        changeData(i) {
          console.log(i)
        }
      },
      created() {
        console.log(this.days)
        if(this.days == 'first') {
          this.changeData(1)
        }else if(this.days == 'second') {
          this.changeData(2)
        }else if(this.days == 'third') {
          this.changeData(3)
        }
      }
    }

</script>

<style scoped>

</style>
