<template>
  <div class="m-order-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="昨日" name="first">

        </el-tab-pane>
        <el-tab-pane label="七日" name="second">
          <order-index-top :days="days"></order-index-top>
        </el-tab-pane>
        <el-tab-pane label="月度" name="third">

        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import OrderIndexTop from "../../components/common/order-index-top";
  export default {
    data() {
      return {
        name: '订单概况',
        activeName: 'second',
        days: ''
      }
    },
    components:{
      OrderIndexTop,
      pageTitle
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      handleClick(tab, event) {
        console.log(tab.name+1)
        this.days = tab.name
      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  .m-content {
    padding: 0.2rem;
    background: #ffffff;
  }
</style>

