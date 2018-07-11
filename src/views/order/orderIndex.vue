<template>
  <div class="m-order-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-content">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="昨日" name="one">
          <order-index-top ref="one" :days="days"></order-index-top>
        </el-tab-pane>
        <el-tab-pane label="七日" name="seven">
          <order-index-top ref="seven" :days="days"></order-index-top>
        </el-tab-pane>
        <el-tab-pane label="月度" name="thirty">
          <order-index-top ref="thirty" :days="days"></order-index-top>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import orderIndexTop from "../../components/common/order-index-top";
  export default {
    data() {
      return {
        name: '订单概况',
        activeName: 'seven',
        days: '本周'
      }
    },
    components:{
      'orderIndexTop': orderIndexTop,
      'pageTitle': pageTitle
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      handleClick(tab, event) {
        // console.log(tab.name);
        if(tab.name == 'one') {
          this.days = '昨日';
          this.$refs.one.changeData(0);
        }else if(tab.name == 'seven') {
          this.days = '本周';
          this.$refs.seven.changeData(1);
        }else if(tab.name == 'thirty') {
          this.days = '本月';
          this.$refs.thirty.changeData(2);
        }
      }
    },
    mounted() {
      this.$refs.seven.changeData(1);
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .m-content {
    padding: 0.2rem;
    background-color: @bgMainColor;
  }
</style>

