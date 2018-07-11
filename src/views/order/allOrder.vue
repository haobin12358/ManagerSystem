<template>
  <div class="all-order">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="all-order-search">
      <div class="order-search-one">
        <div class="search-text-input">
          <div class="search-text" style="margin-left: 0.53rem">订单号：</div>
          <el-input></el-input>
        </div>
        <div class="search-text-input">
          <div class="search-text">维权状态：</div>
          <el-input></el-input>
        </div>
        <div class="search-text-input">
          <div class="search-text">付款方式：</div>
          <el-input></el-input>
        </div>
      </div>
      <div class="order-search-two">
        <div class="search-text-input">
          <div class="search-text">商品名称：</div>
          <el-input></el-input>
        </div>
        <div class="search-text-input">
          <div class="search-text">物流方式：</div>
          <el-input></el-input>
        </div>
        <div class="search-text-input">
          <div class="search-text">订单类型：</div>
          <el-input></el-input>
        </div>
      </div>
      <div class="order-search-three">
        <div class="search-text-input" style="width: 5rem">
          <div class="search-text">下单时间：</div>
          <el-input></el-input>
          <div class="search-text-middle">至</div>
          <el-input></el-input>
        </div>
      </div>
      <div class="search-buttons">
        <el-button class="search-button" size="mini">筛选</el-button>
        <el-button class="search-button" size="mini">批量导出</el-button>
      </div>
    </div>
    <!--<div>
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="全部" name="one">全部</el-tab-pane>
        <el-tab-pane label="待付款" name="two">待付款</el-tab-pane>
        <el-tab-pane label="待发货" name="three">待发货</el-tab-pane>
        <el-tab-pane label="已发货" name="four">已发货</el-tab-pane>
        <el-tab-pane label="已完成" name="five">已完成</el-tab-pane>
        <el-tab-pane label="已关闭" name="six">已关闭</el-tab-pane>
        <el-tab-pane label="退款中" name="seven">退款中</el-tab-pane>
      </el-tabs>
    </div>-->
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  export default {
      data() {
          return {
            name: '所有订单',
            activeName: 'one'
          }
      },
      components: {
        'pageTitle': pageTitle
      },
      methods: {
        freshClick(){
          console.log('fresh');
        },
        handleClick(tab, event) {
          console.log(tab, event);
        }
      },
      created() {

      }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .all-order {
    height: 5rem;
    background-color: @bgMainColor;
    .all-order-search {
      height: 1.35rem;
      padding: 0.2rem 0.3rem 0 0.3rem;
      margin: 0.15rem 0.2rem 0 0.2rem;
      border-radius: 0.1rem;
      background-color: @borderColor;
      .search-buttons {
        float: right;
        margin-right: 1rem;
        .search-button {
          background-color: @btnActiveColor;
          color: @bgMainColor;
          font-size: 0.14rem;
        }
      }
    }
  }
  .search-text-input {
    float: left;
    width: 3.2rem;
    margin-bottom: 0.1rem;
    .search-text {
      float: left;
      margin-left: 0.4rem;
      line-height: 0.32rem;
      font-size: 0.14rem;
    }
    .search-text-middle {
      float: left;
      line-height: 0.32rem;
      margin: 0 0.1rem 0 0.1rem;
    }
    .el-input {
      float: left;
      width: 1.6rem;
    }
  }
</style>
